import pytest
from infra.config_provider import ConfigProvider
from infra.streaming_validator import StreamingValidator
from infra.mobile_session import MobileSession


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="config/config.json",
        help="Path to the configuration file"
    )
    
@pytest.fixture(scope="session")
def app_config(request):
    """Load configuration data based on command line option."""
    env_path = request.config.getoption("--env")
    return ConfigProvider.load_config(env_path)
    
@pytest.fixture(scope="session")
def streaming_validator(app_config):
    # Retrieve the base_url from the config dictionary
    url = app_config['stream_server']['base_url']
    return StreamingValidator(base_url=url)

@pytest.fixture(scope="function")
def mobile_session(app_config):
    """
    Provides a fresh mobile session for each test.
    Scope is 'function' because we want a fresh app state for every test case.
    """
    # 1. Get mobile config
    mobile_conf = app_config['mobile']
    platform = mobile_conf['platform']
    
    # 2. Start Session
    session = MobileSession(platform, mobile_conf)
    session.launch_app()
    
    yield session
    
    # 3. Teardown
    session.quit()
import pytest
from infra.config_provider import ConfigProvider
from infra.streaming_validator import StreamingValidator


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="config.json",
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
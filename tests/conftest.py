import pytest
import logging
from infra.handlers import ConfigHandler, LoggingHandler
from infra.streaming_validator import StreamingValidator
from infra.mobile_session import MobileSession


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="config/config.json",
        help="Path to the configuration file"
    )

    parser.addoption(
        "--platform",
        action="store",
        choices=["android", "ios"], # Restricts input to these two
        default=None,               # Default to None so we can fallback to config/env vars
        help="Target mobile platform (android or ios)"
    )
    
@pytest.fixture(scope="session")
def app_config(request):
    """Load configuration data based on command line option."""
    env_path = request.config.getoption("--env")
    return ConfigHandler.load_config(env_path)
    
@pytest.fixture(scope="session")
def streaming_validator(app_config):
    # Retrieve the base_url from the config dictionary
    url = app_config['stream_server']['base_url']
    return StreamingValidator(base_url=url)

@pytest.fixture(scope="function")
def mobile_session(request, app_config):
    """
    Provides a fresh mobile session for each test.
    Scope is 'function' because we want a fresh app state for every test case.
    """
    # Try to get platform from CLI argument
    platform = request.config.getoption("--platform")

    mobile_conf = app_config['mobile']
    
    # Fallback to config file if platform not provided via CLI
    if not platform:  
        platform = mobile_conf.get('platform')
    
    # Start Session
    session = MobileSession(platform, mobile_conf)
    session.launch_app()
    
    yield session
    
    # Teardown
    session.quit()

@pytest.fixture(scope="function", autouse=True)
def test_logger(request):
    """
    Automatically sets up file logging for every test.
    Pytest handles the console output automatically via pytest.ini.
    """
    test_name = request.node.name
    logger = logging.getLogger("TEST")
    
    # SETUP: Attach the file handler
    file_handler = LoggingHandler.setup_file_logging(test_name)
    
    logger.info(f"--- STARTING TEST: {test_name} ---")
    
    yield logger
    
    logger.info(f"--- FINISHED TEST: {test_name} ---")
    
    # TEARDOWN: Remove ONLY the file handler we added
    # This leaves Pytest's console handler intact for the next test
    logger.removeHandler(file_handler)
    file_handler.close()
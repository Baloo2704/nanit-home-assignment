import pytest
from infra.pages import WelcomePage

@pytest.mark.mobile
def test_mobile_login_flow(mobile_session):
    """
    Verifies that a user can log in and see the stream.
    Credentials are sourced from config.json via the mobile_session.
    """
    # 1. Retrieve credentials from the session configuration
    # Note: 'mobile_session' fixture already loaded the 'mobile' section of config.json
    username = mobile_session.config.get("username")
    password = mobile_session.config.get("password")
    
    # 2. Start at Welcome Page
    welcome_page = WelcomePage(mobile_session)
    
    # 3. Navigate to Login Page
    login_page = welcome_page.navigate_to_login()
    
    # 4. Verify Login Screen is visible
    assert login_page.is_visible() is True, "Login screen should be visible after clicking 'Log In'"
    
    # 5. Perform Login
    # Fluent API: perform_login returns the next page object (LiveStreamPage)
    stream_page = login_page.perform_login(username, password)
    
    # 6. Verify Stream
    assert stream_page.is_stream_visible() is True, "Live stream container should be found after login"
from infra.pages import WelcomePage


def test_mobile_login_flow(mobile_session):
    # Access app credentials
    user = mobile_session.config["username"]
    pwd = mobile_session.config["password"]

    # 1. Start at Welcome Page
    welcome_page = WelcomePage(mobile_session)
    
    # 2. Navigate to Login
    login_page = welcome_page.navigate_to_login()
    
    # 3. Verify Login Screen
    assert login_page.is_visible() is True
    
    # 4. Perform Login
    stream_page = login_page.perform_login(user, pwd)
    
    # 5. Verify Stream
    assert stream_page.is_stream_visible() is True
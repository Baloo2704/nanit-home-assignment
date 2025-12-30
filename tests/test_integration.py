import pytest
from infra.pages import WelcomePage

@pytest.mark.integration
def test_mobile_and_backend_sync(mobile_session, streaming_validator):
    """
    Stage 3 Requirement:
    1. Mobile: Login → Navigate to stream → Verify visible stream
    2. Backend: Check /health endpoint reports status = "streaming"
    3. Validation: Both layers agree on streaming state
    """
    
    # --- Step 1: Mobile Layer ---
    user = mobile_session.config.get("username")
    pwd = mobile_session.config.get("password")
    
    welcome_page = WelcomePage(mobile_session)
    stream_page = welcome_page.navigate_to_login() \
                              .perform_login(user, pwd)
    
    mobile_is_streaming = stream_page.is_stream_visible()
    
    # --- Step 2: Backend Layer ---
    # Fetch and validate Schema only
    health_model = streaming_validator.validate_health_check()
    
    # --- Step 3: Validation (Agreement) ---
    print(f"\n[Sync Check] Mobile Visible: {mobile_is_streaming} | Backend Status: {health_model.status}")

    # Assertion 1: Mobile is working
    assert mobile_is_streaming is True, "Mobile App does not show the video stream"

    # Assertion 2: Backend is working (Business Logic)
    # This check is now explicitly here in the test, not hidden in the validator
    assert health_model.status == "streaming", \
        f"Backend mismatch! Expected 'streaming', but got '{health_model.status}'"
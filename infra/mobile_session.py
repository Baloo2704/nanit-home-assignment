from infra.base_session import BaseSession

class MobileSession(BaseSession):
    """
    Mock session that simulates Appium behavior.
    Inherits logging and error handling capabilities from BaseSession.
    """
    def __init__(self, platform, config):
        # Initialize Base with a specific name "MOBILE"
        # This triggers BaseSession to create the LoggingHandler and RetryHandler
        super().__init__(name="MOBILE")
        
        self.platform = platform.lower()
        self.config = config
        self.current_screen = None
        self.log_info(f"Session Created for Platform: {self.platform}")

    def launch_app(self):
        self.log_info("Launching Nanit App...")
        self.current_screen = "WelcomeScreen"

    def find_element(self, element_id):
        self.log_info(f"Finding element: {element_id}")
        # If finding elements was flaky, you could wrap this in self.retry_operation()
        return {"id": element_id, "found": True}

    def click(self, element):
        e_id = element.get('id', 'unknown')
        self.log_info(f"Clicking: {e_id}")
        
        # Mock Navigation Logic
        if "login" in e_id and self.current_screen == "WelcomeScreen":
            self.current_screen = "LoginScreen"
            self.log_info("Navigated to: LoginScreen")

    def send_keys(self, element, text):
        e_id = element.get('id', 'unknown')
        # Security: Mask passwords in logs
        masked = "*****" if "password" in e_id else text
        self.log_info(f"Typing '{masked}' into {e_id}")
    
    def quit(self):
        self.log_info("Closing App.")
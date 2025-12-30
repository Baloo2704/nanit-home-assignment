from infra.ui_map import UIMap
from infra.pages.base_page import BasePage
# Import the next page in the flow
from infra.pages.live_stream_page import LiveStreamPage

class LoginPage(BasePage):
    def is_visible(self):
        """
        Verifies the Login Page is visible by checking for the email input.
        """
        element = self._find(UIMap.EMAIL_INPUT)
        return element.get('found', False)

    def perform_login(self, username, password):
        self._type(UIMap.EMAIL_INPUT, username)
        self._type(UIMap.PASSWORD_INPUT, password)
        self._click(UIMap.TERMS_CHECKBOX)
        self._click(UIMap.LOGIN_SUBMIT_BUTTON)
        
        # Return the next page object
        return LiveStreamPage(self.session)
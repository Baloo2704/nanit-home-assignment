from infra.ui_map import UIMap
from infra.pages.base_page import BasePage
from infra.pages.login_page import LoginPage

class WelcomePage(BasePage):
    def navigate_to_login(self):
        """Clicks the login button on the welcome screen."""
        self._click(UIMap.LOGIN_BUTTON_WELCOME)
        return LoginPage(self.session)
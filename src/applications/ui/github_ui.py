from src.applications.ui.pages.login_page import LoginPage
# from src.applications.ui.pages.signup_page import SignUPPage
from src.applications.ui.base_app import BaseApp

class GitHubUI(BaseApp):

    def __init__(self, browser) -> None:

        super().__init__(browser)

        self.login_page = LoginPage(self)
       # self.signup_page = SignUpPage(self)

    def try_login(self, username: str, password: str):
        #return self.login_page.try_login(self.username, self.password)
        return self.login_page.try_login(username, password)

    def logout(self):
        # TODO self.login_page.logout()
        self.wait_and_click(locator, timer)

    def create_user(self):
        pass

    def close(self):
        self.close_browser()
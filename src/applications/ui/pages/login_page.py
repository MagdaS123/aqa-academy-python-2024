from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class LoginPage:
    
    # URL of the page
    URL = 'https://github.com/login'

    # Elements of the page
    LOGIN_FLD = '//*[@id="login_field"]'
    PASSWORD_FLD = '//*[@id="password"]'
    SIGNIN_BTN = '//*[@id="login"]/div[4]/form/div/input[13]'
    ERROR_INO = '//*[@id="js-flash-container"]/div/div/div'

    def __init__(self, app) -> None:
        self.app = app # app = GitHubUI
    
    # user methods

    def try_login(self, username: str, password: str):
        # TODO self.app.browser
        login = self.app.browser.find_element(By.XPATH, self.LOGIN_FLD)
        login.send_keys(username)
        passwordField = self.app.browser.find_element(By.XPATH, self.PASSWORD_FLD)
        passwordField.send_keys(password)
        button = self.app.browser.find_element(By.XPATH, self.SIGNIN_BTN)
        button.click()
        
        return True

    def navigate_to(self):
        self.app.navigate_to(self.URL)

    # check functions

    def check_wrong_creds_message(self):
        # TODO
        # find error message
        # check if message is equal to "BLA" text
        errorField = self.app.browser.find_element(By.XPATH, self.ERROR_INO)
        print(f"errorField is {errorField}")

        return errorField != None

    def check_documentation_link(self):
        pass
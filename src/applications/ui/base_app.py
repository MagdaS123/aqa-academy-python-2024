from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BaseApp:

    def __init__(self, browser) -> None:
        self.browser = browser

    def navigate_to(self, url):
        self.browser.get(url)

    def wait_and_click(self, locator, timeout=20):
        # read what is implicit and explisit waiters
        self.browser.implicity.wait(timeout)
        elem = self.browser.find_element(By.XPATH, locator)
        elem.click()

        return True
    
    def enter_text(self, locator, text):
        elem = self.browser.find_element(By.XPATH, locator)
        elem.clear()
        elem.send_keys(text)

        if elem.text != text:
            raise RuntimeError(f"Text {text} is not entered to {locator} element")
        
        elem.send_keys(Keys.RETURN)

        return True
    
    def close_browser(self):
        self.browser.close()
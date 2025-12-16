from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config


class LoginPage:

    #login variables to use
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_BANNER = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(Config.BASE_URL)

    def login(self, username, password=None):
        self.driver.find_element(*self.USERNAME_INPUT).clear()
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

        if password is not None:
            self.driver.find_element(*self.PASSWORD_INPUT).clear()
            self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_error_visible(self):
        try:
            el = self.wait.until(EC.visibility_of_element_located(self.ERROR_BANNER))
            return el.is_displayed()
        except Exception:
            return False

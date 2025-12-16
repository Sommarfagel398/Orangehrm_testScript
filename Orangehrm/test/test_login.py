import pytest

from config import Config
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.mark.skipif(Config.LANG != "en", reason="only vlaid for English Text")
class TestLogin:
    def test_login_page_loads(self, driver):
        login_page = LoginPage(driver)
        login_page.open()

        assert driver.find_element(*LoginPage.USERNAME_INPUT)
        assert driver.find_element(*LoginPage.PASSWORD_INPUT)
        assert driver.find_element(*LoginPage.LOGIN_BUTTON)

    def test_login_with_invalid_credentials(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("InvalidUser", "WrongPass123")

        assert login_page.is_error_visible()

    def test_login_with_invalid_user(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("InvalidUser", "admin123")

        assert login_page.is_error_visible()

    def test_login_with_invalid_pass(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "")

        assert login_page.is_error_visible()

    def test_login_with_empty_credentials(self,driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("","")

        assert login_page.is_error_visible()

    def test_login_with_wrong_user(self,driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin1","admin123")

        assert login_page.is_error_visible()

    def test_login_with_wrong_pass(self,driver):
        login_page  = LoginPage(driver)
        login_page.open()
        login_page.login("Admin","admin456")

        assert login_page.is_error_visible()


    def test_link_text(self,driver):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


        link = driver.find_element(By.LINK_TEXT, 'OrangeHRM, Inc')
        link.click()

        driver.switch_to.window(driver.window_handles[-1])

        assert 'https://www.orangehrm.com/' in driver.current_url


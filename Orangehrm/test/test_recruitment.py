import time
import re
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config
from pages.login_page import LoginPage
from pages.recruitment import Recruit


#this is for dropdown in selecting any option"

def select_any_option_from_open_dropdown(driver, wait):
    """Assumes dropdown is already clicked; selects the first non-empty option."""
    options = wait.until(
        EC.visibility_of_all_elements_located(
            (By.XPATH, "//div[@role='listbox']//span")
        )
    )
    assert options, "No options in dropdown"

    for opt in options:
        text = opt.text.strip()
        if text:
            opt.click()
            return text

    raise AssertionError("All dropdown options are empty")


@pytest.mark.skipif(Config.LANG != "en", reason="Only valid for English UI texts")
class TestRecruitment:

#This part is for testing tabs

    def test_candidate_tab(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")

        recruit = Recruit(driver)
        recruit.candidate_tab()
        assert "/recruitment/viewCandidates" in driver.current_url
        time.sleep(5)

    def test_vacancy_tab(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewJobVacancy")

        recruit = Recruit(driver)
        recruit.vacancy_tab()
        assert "/recruitment/viewJobVacancy" in driver.current_url
        time.sleep(1)

#this is for candidate forms testing

    def test_candidate_vacancy_fill_any(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")

        recruit = Recruit(driver)
        wait = WebDriverWait(driver, 10)

        # open vacancy dropdown using page object
        recruit.candidate_vac()

        selected_text = select_any_option_from_open_dropdown(driver, wait)

        selected_value = driver.find_element(
            By.XPATH,
            "//label[text()='Vacancy']/ancestor::div[contains(@class,'oxd-grid-item')]"
            "//div[contains(@class,'oxd-select-text-input')]"
        )
        assert selected_text in selected_value.text

    def test_candidate_job_title_fill_any(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")

        recruit = Recruit(driver)
        wait = WebDriverWait(driver, 10)

        recruit.job_titles()
        selected_text = select_any_option_from_open_dropdown(driver, wait)

        selected_value = driver.find_element(
            By.XPATH,
            "//label[text()='Job Title']/ancestor::div[contains(@class,'oxd-grid-item')]"
            "//div[contains(@class,'oxd-select-text-input')]"
        )
        assert selected_text in selected_value.text

    def test_candidate_hiring_fill_any(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")

        recruit = Recruit(driver)
        wait = WebDriverWait(driver, 10)

        recruit.hired()
        selected_text = select_any_option_from_open_dropdown(driver, wait)

        selected_value = driver.find_element(
            By.XPATH,
            "//label[text()='Hiring Manager']/ancestor::div[contains(@class,'oxd-grid-item')]"
            "//div[contains(@class,'oxd-select-text-input')]"
        )
        assert selected_text in selected_value.text

    def test_candidate_status_fill_any(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")

        recruit = Recruit(driver)
        wait = WebDriverWait(driver, 10)

        recruit.can_status()
        selected_text = select_any_option_from_open_dropdown(driver, wait)

        selected_value = driver.find_element(
            By.XPATH,
            "//label[text()='Status']/ancestor::div[contains(@class,'oxd-grid-item')]"
            "//div[contains(@class,'oxd-select-text-input')]"
        )
        assert selected_text in selected_value.text

    def test_candidate_search_button_any_vacancy(self, driver):
        """Select any vacancy, then search; assert that search completed (rows OR 'No Records Found')."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")

        recruit = Recruit(driver)
        wait = WebDriverWait(driver, 15)  # a bit more time

        # open vacancy dropdown and pick any option
        recruit.candidate_vac()
        select_any_option_from_open_dropdown(driver, wait)

        # click Search
        recruit.can_search()

        # wait for table body to be visible (this appears even if there are no rows)
        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'oxd-table-body')]")
            )
        )

        # either some rows OR 'No Records Found' is fine
        results = driver.find_elements(
            By.XPATH, "//div[contains(@class,'oxd-table-card')]"
        )
        no_records = driver.find_elements(
            By.XPATH, "//span[normalize-space()='No Records Found']"
        )
        assert results or no_records

    def test_candidate_reset_button_any_vacancy(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")

        recruit = Recruit(driver)
        wait = WebDriverWait(driver, 10)

        # set a vacancy
        recruit.candidate_vac()
        selected_text = select_any_option_from_open_dropdown(driver, wait)

        selected_value = driver.find_element(
            By.XPATH,
            "//label[text()='Vacancy']/ancestor::div[contains(@class,'oxd-grid-item')]"
            "//div[contains(@class,'oxd-select-text-input')]"
        )
        assert selected_text in selected_value.text

        # reset
        recruit.can_reset()
        time.sleep(1)

        reset_value = driver.find_element(
            By.XPATH,
            "//label[text()='Vacancy']/ancestor::div[contains(@class,'oxd-grid-item')]"
            "//div[contains(@class,'oxd-select-text-input')]"
        )
        assert "-- Select --" in reset_value.text

# This is for Vacancies labels

    def test_vacancies_vacancy_fill_any(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewJobVacancy")

        wait = WebDriverWait(driver, 10)
        #locates vacancy icon
        vacancy_icon = driver.find_element(
            By.XPATH,
            "//label[text()='Vacancy']/ancestor::div[contains(@class,'oxd-grid-item')]"
            "//div[contains(@class,'oxd-select-text--after')]"
        )
        vacancy_icon.click()
        #select any option from dropdown that selects non-empty option and returns next
        selected_text = select_any_option_from_open_dropdown(driver, wait)


        selected_value = driver.find_element(
            By.XPATH,
            "//label[text()='Vacancy']/ancestor::div[contains(@class,'oxd-grid-item')]"
            "//div[contains(@class,'oxd-select-text-input')]"
        )
        #verifies if the selected value is displayed
        assert selected_text in selected_value.text

    def test_vacancies_hiring_fill_any(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewJobVacancy")

        wait = WebDriverWait(driver, 10)

        hiring_icon = driver.find_element(
            By.XPATH,
            "//label[text()='Hiring Manager']/ancestor::div[contains(@class,'oxd-grid-item')]"
            "//div[contains(@class,'oxd-select-text--after')]"
        )
        hiring_icon.click()

        selected_text = select_any_option_from_open_dropdown(driver, wait)

        selected_value = driver.find_element(
            By.XPATH,
            "//label[text()='Hiring Manager']/ancestor::div[contains(@class,'oxd-grid-item')]"
            "//div[contains(@class,'oxd-select-text-input')]"
        )
        assert selected_text in selected_value.text

    def test_vacancies_search_button_any_vacancy(self, driver):
        """Select any vacancy on Vacancies, then search; assert that search completed."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewJobVacancy")

        wait = WebDriverWait(driver, 15)

        # open vacancy dropdown and pick any option
        vacancy_icon = driver.find_element(
            By.XPATH,
            "//label[text()='Vacancy']/ancestor::div[contains(@class,'oxd-grid-item')]"
            "//div[contains(@class,'oxd-select-text--after')]"
        )
        vacancy_icon.click()
        select_any_option_from_open_dropdown(driver, wait)

        # click Search
        search_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
            )
        )
        search_btn.click()

        # Wait for results table to be visible
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@role='table']")
            )
        )

        # Check for result rows OR "No Records Found" message
        result_rows = driver.find_elements(
            By.XPATH,
            '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div'
        )
        no_records_msg = driver.find_elements(
            By.XPATH,
            "//span[contains(text(), 'No Records Found')]"
        )

        assert result_rows or no_records_msg, "Search completed but no results or 'No Records Found' message displayed"

    def test_vacancies_reset_button(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewJobVacancy")

        wait = WebDriverWait(driver, 10)

        # set a vacancy - click dropdown icon
        vacancy_icon = driver.find_element(
            By.XPATH,
            "//label[text()='Vacancy']/ancestor::div[contains(@class,'oxd-grid-item')]"
            "//div[contains(@class,'oxd-select-text--after')]"
        )
        vacancy_icon.click()
        selected_text = select_any_option_from_open_dropdown(driver, wait)

        selected_value = driver.find_element(
            By.XPATH,
            "//label[text()='Vacancy']/ancestor::div[contains(@class,'oxd-grid-item')]"
            "//div[contains(@class,'oxd-select-text-input')]"
        )
        assert selected_text in selected_value.text

        # reset
        reset_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Reset']")
        reset_btn.click()
        time.sleep(1)

        reset_value = driver.find_element(
            By.XPATH,
            "//label[text()='Vacancy']/ancestor::div[contains(@class,'oxd-grid-item')]"
            "//div[contains(@class,'oxd-select-text-input')]"
        )
        assert "-- Select --" in reset_value.text


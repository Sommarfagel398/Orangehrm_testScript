from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Recruit:
    url = "/web/index.php/recruitment/viewCandidates"

    # variables used for testing
    candidates = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')
    vacancies = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]')

    # Candidate filter form
    job_title = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i')
    vacancy = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i')
    hiring = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]/i')
    status = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i')
    name = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[1]/div/div[2]/div/div/input')
    date_application = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[3]/div/div[2]/div/div/i')
    method_application = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[3]/div/div/div/div[2]/div/div/div[2]/i')
    search = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[2]')
    reset = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[1]')
    add_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
    records = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # navigation
    def open(self, base_url):
        self.driver.get(base_url + self.url)

    # header
    def candidate_tab(self):
        header = self.wait.until(EC.element_to_be_clickable(self.candidates))
        header.click()
        return True

    def vacancy_tab(self):
        header = self.wait.until(EC.element_to_be_clickable(self.vacancies))
        header.click()
        return True

    # Candidate filter form (click/visibility)
    def job_titles(self):
        job = self.wait.until(EC.element_to_be_clickable(self.job_title))
        job.click()
        return True

    def candidate_vac(self):
        vacant = self.wait.until(EC.element_to_be_clickable(self.vacancy))
        vacant.click()
        return True

    def hired(self):
        hiring = self.wait.until(EC.element_to_be_clickable(self.hiring))
        hiring.click()
        return True

    def can_status(self):
        status = self.wait.until(EC.element_to_be_clickable(self.status))
        status.click()
        return True

    def can_name(self):
        name = self.wait.until(EC.visibility_of_element_located(self.name))
        return name.is_displayed()

    def date(self):
        date_applicant = self.wait.until(EC.element_to_be_clickable(self.date_application))
        date_applicant.click()
        return True

    def can_method(self):
        method_applicant = self.wait.until(EC.element_to_be_clickable(self.method_application))
        method_applicant.click()
        return True

    def can_search(self):
        candidate_search = self.wait.until(EC.element_to_be_clickable(self.search))
        candidate_search.click()
        return True

    def can_reset(self):
        reset_button = self.wait.until(EC.element_to_be_clickable(self.reset))
        reset_button.click()
        return True

    def button_add(self):
        add_button = self.wait.until(EC.element_to_be_clickable(self.add_button))
        add_button.click()
        return True

    def cand_record(self):
        records = self.wait.until(EC.visibility_of_element_located(self.records))
        return records.is_displayed()



    def get_record_count(self):
        """Get the number of candidate records displayed"""
        count_text = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(text(),'Records Found')]")
        )).text
        # Extract number from "(66) Records Found"
        import re
        match = re.search(r'\((\d+)\)', count_text)
        return int(match.group(1)) if match else 0

    def select_job_title_option(self, option_text):
        """Select an option from Job Title dropdown"""
        self.wait.until(EC.element_to_be_clickable(self.job_title)).click()
        option = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[@role='listbox']//span[contains(text(),'{option_text}')]")
        ))
        option.click()

    def select_vacancy_option(self, option_text):
        """Select an option from Vacancy dropdown"""
        self.wait.until(EC.element_to_be_clickable(self.vacancy)).click()
        option = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[@role='listbox']//span[contains(text(),'{option_text}')]")
        ))
        option.click()

# Orangehrm_testScript
OrangeHRM Test Automation Framework
Project structure
pages/
login_page.py – Page Object for the login screen (open page, submit credentials, error banner helper).

recruitment.py – Page Object for the Recruitment module (Candidates tab, Vacancies tab, dropdowns, search/reset buttons).

test/
test_login.py – Login tests (valid/invalid credentials, link navigation).

test_recruitment.py – Recruitment form tests (Candidates and Vacancies: inputs, selections, dropdown interactions, search/reset functionality).

config/
config.py – Global settings such as BASE_URL and LANG.

helpers/
dropdown_helper.py – Reusable helper function select_any_option_from_open_dropdown() for dropdown selection logic.

reports/
assets/ – Static files (if needed for reports).

*.html – Pytest HTML reports generated per run.

conftest.py
Shared Pytest fixtures and hooks (WebDriver setup/teardown, HTML reporting, screenshots on failure).

Prerequisites
Python 3.8+ installed.

Google Chrome installed.

ChromeDriver compatible with your Chrome version and on your PATH (or configured via webdriver-manager / local path).

Recommended: Create and activate a virtual environment for the project.

Install dependencies (example):
bash
pip install -r requirements.txt
Typical requirements.txt:
text
selenium
pytest
pytest-html
Running the tests
From the project root (where conftest.py lives), run:

bash
pytest
Pytest will:

Start a fresh Chrome browser for each test using the driver fixture (maximized with implicit waits).

Generate an HTML report under reports/ with a timestamped filename like orangehrm_report_YYYYMMDD_HHMMSS.html and embed screenshots for failed tests via pytest-html extras.

To run only login or recruitment tests:
bash
pytest test/test_login.py
pytest test/test_recruitment.py
Use -k to filter by test name pattern:
bash
pytest -k "vacancy or invalid_credentials"
Test coverage
Current high-level coverage:
Login page
Page load and presence of username, password, and login button.

Multiple invalid credential combinations (empty fields, wrong user, wrong password) and verification of the error banner.

External "OrangeHRM, Inc" link navigation to the marketing site.

Recruitment Module
Tab Navigation:

Candidates tab navigation and URL verification.

Vacancies tab navigation and URL verification.

Candidates Page Testing:

Vacancy dropdown selection (fill any option and verify).

Job Title dropdown selection (fill any option and verify).

Hiring Manager dropdown selection (fill any option and verify).

Status dropdown selection (fill any option and verify).

Search button functionality with results or "No Records Found" validation.

Reset button functionality (clears dropdown to "-- Select --").

Vacancies Page Testing:

Vacancy dropdown selection (fill any option and verify).

Hiring Manager dropdown selection (fill any option and verify).

Search button functionality with results or "No Records Found" validation.

How to extend
Add new pages to pages/ as Page Objects, following the existing LoginPage and Recruit patterns.

Create corresponding tests in test/ that use the shared driver fixture and methods from your Page Objects.

Update config.Config with additional settings (e.g., alternative base URLs, credentials, timeouts, language settings) as the framework grows.

Add reusable helpers to helpers/ for common operations like dropdown selection, date pickers, file uploads, etc.

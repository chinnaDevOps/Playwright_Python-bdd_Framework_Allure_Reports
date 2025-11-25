**Playwright + pytest-bdd Framework with Allure Reports**
**Overview**

This framework uses: Playwright (via Python) for browser automation pytest bdd for BDD style tests (Given-When-Then) Allure for rich HTML test reporting Page Object Model (POM) for maintainable test architecture Screenshots captured for each test step, visible in the Allure report

**Prerequisites**
NodeJs latest version
Java(for allure reports)
Python 3.8+ 

**Playwright pytest Installation process** (both Windows, Macbook)

create folder(in your system) --> cd <folder>

python -m venv venv

venv\Scripts\activate (to activate the virtual env)

pip install pytest-playwright

playwright install

pip install allure-pytest

pip install pytest-bdd

pip install pytest-xdist (for parallel execution)

pip install pytest-html (for python htmle report - this is optional)

pip install -r requirements.txt

**Clone the repository**

git clone https://github.com/chinnaDevOps/Pyhton_Playwright_Farmowrk_Allure_Reports.git

cd Pyhton_Playwright_Farmowrk_Allure_Reports

**Running Tests** **through terminal**

pytest --alluredir=reports/allure-results; allure generate reports/allure-results -o reports/allure-report --clean

****in case of if you want run different env's like (QA, Prod, Dev, UAT) from terminal ****

pytest --env=qa --my-browser=chrome --alluredir=reports/allure-results; allure generate reports/allure-results -o reports/allure-report --clean

**How It Works**

Tests are defined in Gherkin (.feature) files under tests/features/.

Step definitions map those Gherkin steps to Python functions under tests/steps/.

Page Objects (under pages/) encapsulate UI interactions.

The conftest.py fixture sets up Playwright browser/page.

Hook logic captures screenshots after each pytest-bdd step and attaches them into the Allure results.

After test execution, Allure is used to generate a human-readable HTML report including those screenshots.

**Customising / Extending**

To add a new page object: create a Python class in pages/, inheriting from a base page if you have one.

To add a new feature test: add a .feature file, then create matching step definitions.

To modify browser settings (launch headless vs headed, browser type, viewport): update the fixture in conftest.py.

To update report output location: change --alluredir and -o paths accordingly.

To integrate into CI (e.g., GitHub Actions, Jenkins): you can add a pipeline that installs dependencies, runs tests, generates Allure report, and publishes it as artifact or on GitHub Pages.

**Troubleshooting**

If Playwright browsers are not installed, you may get errors about missing browsers — run playwright install.

If screenshot attachments are missing: check that the hook pytest_bdd_after_step is capturing the page fixture correctly.

If Allure CLI is not installed: install the Allure command‐line tool (see Allure docs).

If using Windows: paths may need to be adjusted (backslashes, scripts folder).








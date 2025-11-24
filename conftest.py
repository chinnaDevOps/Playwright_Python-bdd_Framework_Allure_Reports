import os

import pytest
from playwright.sync_api import sync_playwright
import allure
import shutil
from utilities.environment_loader import load_environment


# --------------------------------------------------------------------
# CLI OPTIONS
# --------------------------------------------------------------------
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa",
                     help="Environment: qa | staging | prod")
    parser.addoption("--my-browser", action="store", default="chromium",
                     help="Browser: chromium | firefox | webkit")


# --------------------------------------------------------------------
# ENV FIXTURES
# --------------------------------------------------------------------
@pytest.fixture(scope="session")
def env_config(pytestconfig):
    """Load environment.json and return the selected environment settings."""
    env_data = load_environment()
    selected_env = pytestconfig.getoption("--env") or env_data["env"]
    return env_data[selected_env]


@pytest.fixture(scope="session")
def base_url(env_config):
    return env_config["base_url"]


@pytest.fixture(scope="session")
def credentials(env_config):
    """Optional: username, password (if needed later)."""
    return {
        "username": env_config["username"],
        "password": env_config["password"]
    }


# --------------------------------------------------------------------
# BROWSER FIXTURE (dynamic)
# --------------------------------------------------------------------
@pytest.fixture(scope="session")
def browser_instance(pytestconfig):
    value = pytestconfig.getoption("--my-browser")
    print("🔥 BROWSER CLI VALUE RECEIVED =", value)
    browser_name = pytestconfig.getoption("--my-browser").lower()

    with sync_playwright() as playwright:
        if browser_name == "chrome":
            browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
        elif browser_name == "firefox":
            print("------Inside the fire fox browser--------------")
            browser = playwright.firefox.launch(headless=False)
        elif browser_name == "webkit":
            browser = playwright.webkit.launch(headless=False)
        else:
            raise ValueError(
                f" Invalid browser: {browser_name}. Must be chromium | firefox | webkit"
            )

        yield browser
        browser.close()


# --------------------------------------------------------------------
# PAGE FIXTURE
# --------------------------------------------------------------------
@pytest.fixture(scope="function")
def page(browser_instance):
    context = browser_instance.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()


# --------------------------------------------------------------------
# ALLURE SCREENSHOT AFTER EACH STEP
# --------------------------------------------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    outcome = yield
    allure.attach(
        request.getfixturevalue("page").screenshot(),
        name=f"Step - {step.name}",
        attachment_type=allure.attachment_type.PNG
    )
REPORT_DIR = "reports/allure-results"

def pytest_sessionstart(session):
    """Clean allure results before running tests."""
    if os.path.exists(REPORT_DIR):
        shutil.rmtree(REPORT_DIR)
    os.makedirs(REPORT_DIR, exist_ok=True)
    print(f"✨ Cleaned Allure report folder: {REPORT_DIR}")
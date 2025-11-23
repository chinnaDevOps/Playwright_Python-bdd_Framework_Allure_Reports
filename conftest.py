import pytest
from playwright.sync_api import sync_playwright
import allure


def pytest_adoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="QA",
        help="Environment to run tests on: QA / UAT / DEV / PROD"
    )

@pytest.fixture(scope="session")
def browser_instance():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser_instance):
    context = browser_instance.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()


# 📸 Screenshot after EVERY step (Serenity-style)
@pytest.hookimpl(hookwrapper=True)
def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    outcome = yield
    allure.attach(
        request.getfixturevalue("page").screenshot(),
        name=f"Step - {step.name}",
        attachment_type=allure.attachment_type.PNG
    )

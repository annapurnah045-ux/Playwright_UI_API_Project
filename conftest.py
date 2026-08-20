import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="broswer selection")

@pytest.fixture(scope="session")
def userData_set(request):
    return request.param

@pytest.fixture
def browserInstance(playwright, request):
    browserName = request.config.getoption("browser_name")
    if browserName == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browserName == "firefox":
        browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()


from playwright.sync_api import sync_playwright
from playwright.sync_api import Page

# Method 1 : Using sync_api in each function and defining browser,page
def test_playwright_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://google.com")
        print(page.title())
        browser.close()

# Method 2 : Using playwright as a global fixture via plugin pytest-playwright
def test_playwright_test1(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://google.com")
    print(page.title())
    browser.close()

# Method 3 : Using page object as fixture from Page class and calling browser directly from page object
def test_playwright_test2(page:Page):
    page.goto("https://google.com")
    print(page.title())




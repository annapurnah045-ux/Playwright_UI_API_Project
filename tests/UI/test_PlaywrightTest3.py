from playwright.sync_api import Playwright
import time

def test_firefox_browser(playwright:Playwright):
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    print(page.title())
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    # page.get_by_label("Password:").fill("Learning")
    page.get_by_role("combobox").select_option("consult")
    page.locator("#terms").click()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    #expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)
    print("Test completed successfully!!")
    browser.close()

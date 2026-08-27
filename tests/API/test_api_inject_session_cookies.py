from playwright.sync_api import Playwright, expect
from utils.API_Utils import API_Utils
import time

def test_api_inject_session_cookies(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com")
    # api_utils=API_Utils()
    # token = api_utils.get_token(playwright)
    # page.add_init_script(f""" localStorage.setItem('token','{token}') """)
    # page.goto("https://rahulshettyacademy.com/client")
    # page.get_by_role("button", name="ORDERS").click()
    # expect(page.get_by_text("Your Orders")).to_be_visible()
    # time.sleep(3)
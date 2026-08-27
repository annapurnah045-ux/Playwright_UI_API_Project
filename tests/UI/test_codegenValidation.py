import re
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page


def test_playwright_test1(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://google.com")
    print(page.title())
    print("Disabled Codegen test temporarily")
    browser.close()

# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()

    # page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    # page.get_by_role("textbox", name="email@example.com").click()
    # page.get_by_role("textbox", name="email@example.com").fill("")
    # page.get_by_text("Register here").click()
    # page.get_by_role("textbox", name="First Name").click()
    # page.get_by_role("textbox", name="First Name").fill("Avvi")
    # page.get_by_role("textbox", name="Last Name").click()
    # page.get_by_role("textbox", name="Last Name").fill("H")
    # page.get_by_role("textbox", name="email@example.com").click()
    # page.get_by_role("textbox", name="email@example.com").fill("abc@gmail.com")
    # page.get_by_role("textbox", name="enter your number").dblclick()
    # page.get_by_role("combobox").select_option("3: Engineer")
    # page.get_by_role("radio", name="Female").check()
    # page.get_by_role("textbox", name="Passsword").click()
    # page.get_by_role("textbox", name="Passsword").fill("123@Qwer")
    # page.get_by_role("textbox", name="Confirm Password").click()
    # page.get_by_role("textbox", name="Confirm Password").fill("123@Qwer")
    # page.get_by_role("checkbox").check()
    # page.get_by_role("button", name="Register").click()
    # page.get_by_role("textbox", name="enter your number").click()
    # page.get_by_role("textbox", name="enter your number").fill("7019851743")
    # page.get_by_role("button", name="Register").click()
    # page.get_by_role("button", name="Register").click()
    # page.get_by_role("textbox", name="Last Name").dblclick()
    # page.get_by_role("textbox", name="Last Name").press("ArrowRight")
    # page.get_by_role("textbox", name="Last Name").fill("Holur")
    # page.get_by_role("button", name="Register").click()
    # page.get_by_role("button", name="Register").click()
    # page.get_by_role("textbox", name="email@example.com").dblclick()
    # page.get_by_role("textbox", name="email@example.com").press("ArrowLeft")
    # page.get_by_role("textbox", name="email@example.com").press("ArrowLeft")
    # page.get_by_role("textbox", name="email@example.com").press("ArrowLeft")
    # page.get_by_role("textbox", name="email@example.com").press("ArrowLeft")
    # page.get_by_role("textbox", name="email@example.com").press("ArrowLeft")
    # page.get_by_role("textbox", name="email@example.com").press("ArrowLeft")
    # page.get_by_role("textbox", name="email@example.com").press("ArrowLeft")
    # page.get_by_role("textbox", name="email@example.com").press("ArrowRight")
    # page.get_by_role("textbox", name="email@example.com").press("ArrowRight")
    # page.get_by_role("textbox", name="email@example.com").fill("naanu0@gmail.com")
    # page.get_by_role("button", name="Register").click()
    # page.get_by_role("button", name="Login").click()
    # page.get_by_role("textbox", name="email@example.com").click()
    # page.get_by_role("textbox", name="email@example.com").fill("anus4640@gmail.com")
    # page.get_by_role("textbox", name="enter your passsword").click()
    # page.get_by_role("textbox", name="enter your passsword").fill("123@Qwer")
    # page.get_by_role("button", name="Login").click()
    # page.locator("#sidebar").get_by_text("electronics").click()
    # page.locator("#sidebar").get_by_text("electronics").click()
    # page.get_by_role("checkbox").nth(1).check()
    # page.get_by_role("button", name=" Add To Cart").nth(2).click()
    # page.get_by_role("button", name="   Cart").click()
    # page.get_by_role("button", name="Checkout❯").click()
    # page.get_by_role("textbox", name="Select Country").click()
    # page.get_by_role("textbox", name="Select Country").fill("india")
    # page.get_by_role("button", name=" India").click()
    # page.get_by_text("Place Order").click()
    # with page.expect_download() as download_info:
    #     page.get_by_role("button", name="Click To Download Order").click()
    # download = download_info.value
    #
    # # ---------------------
    # context.close()
    # browser.close()


# with sync_playwright() as playwright:
#     run(playwright)

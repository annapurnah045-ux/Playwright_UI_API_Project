from playwright.sync_api import Page
import time

def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6a7191d585b8849b492a2eb5")

def test_api_intercept_request(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details/*", intercept_request)
    page.get_by_role("textbox", name="email@example.com").fill("anus4640@gmail.com")
    page.get_by_role("textbox", name="enter your passsword").fill("123@Qwer")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)
    time.sleep(3)



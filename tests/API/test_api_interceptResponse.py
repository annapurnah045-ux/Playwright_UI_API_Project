from playwright.sync_api import Page
import time

fake_order_payload = {"data":[],"message":"No Orders"}
def intercept_response(route):
    route.fulfill(json=fake_order_payload)

def test_api_intercept_response(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_role("textbox", name="email@example.com").fill("anus4640@gmail.com")
    page.get_by_role("textbox", name="enter your passsword").fill("123@Qwer")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    message= page.locator(".mt-4").text_content()
    time.sleep(3)
    print(message)



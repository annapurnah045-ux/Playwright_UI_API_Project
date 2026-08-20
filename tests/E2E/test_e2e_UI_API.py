
from playwright.sync_api import Playwright, expect
from utils.API_Utils import API_Utils

def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Create Order via API
    api_utils = API_Utils()
    order_id = api_utils.create_order(playwright)

    # Login to application in UI
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("textbox", name="email@example.com").fill("anus4640@gmail.com")
    page.get_by_role("textbox", name="enter your passsword").fill("123@Qwer")
    page.get_by_role("button", name="Login").click()

    # Check orders history for order placed via API call
    page.get_by_role("button", name="ORDERS").click()
    #page.locator("tbody tr th[scope='row']").filter(has_text=order_id)
    page.locator("tr").filter(has_text=order_id).get_by_role("button", name="View").click()
    expect(page.locator("body")).to_contain_text("Thank you for Shopping With Us")
    context.close

    # ids = page.locator("tbody tr th[scope='row']")
    # for i in range(ids.count()):
    #     current_order_id = ids.nth(i).text_content().strip()
    #     if current_order_id == order_id:
    #         print(current_order_id)
    #         print("Order found!!")
    #         row = page.locator("tr").filter(has_text=current_order_id)
    #         row.get_by_role("button",name = "View").click()
    #         expect(page.locator("body")).to_contain_text("Thank you for Shopping With Us")
    #         break
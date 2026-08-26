import json
from pathlib import Path

import pytest
from playwright.sync_api import Playwright
from pages.Login import Login
from utils.API_Utils import API_Utils
from utils.logger import get_logger

creds_path = Path(__file__).parent.parent.parent / "data" / "credentials.json"
with open(creds_path) as f:
    userdata = json.load(f)
    print(userdata)
    userData_list = userdata["userCredentials"]


logger = get_logger(__name__)

# url_path = Path(__file__).parent / "data" / "URLs.json"
# with open(url_path) as f:
#     url = json.load(f)
#     print(url)
#     baseURL = url["baseURL"]


@pytest.mark.parametrize("userData_set",userData_list)
def test_e2e_web_api(playwright:Playwright, userData_set, browserInstance, base_url):
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()

    logger.info("Starting E2E test for web and API integration")

    # Create Order via API
    api_utils = API_Utils()
    order_id = api_utils.create_order(playwright,userData_set)

    login = Login(browserInstance)
    dashboard = login.get_login(userData_set,base_url)
    ordersPage = dashboard.navigate_to_orders()
    order = ordersPage.get_order(order_id)
    order.view_order_details()

    logger.info("Order details viewed successfully for order ID: {}".format(order_id))

    # Login to application in UI
    # Check orders history for order placed via API call
    #page.locator("tbody tr th[scope='row']").filter(has_text=order_id)
   

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
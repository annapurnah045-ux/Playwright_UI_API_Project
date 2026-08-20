from playwright.sync_api import Playwright
import json
from pathlib import Path
import pytest

login_payload = { "userEmail" : "anus4640@gmail.com", "userPassword": "123@Qwer"}
create_order_payload = {"orders":[{"country":"India","productOrderedId":"6960ea76c941646b7a8b3dd5"}]}

class API_Utils:

    # creds_path = Path(__file__).parent.parent / "data" / "credentials.json"
    # with open(creds_path) as f:
    #     userdata = json.load(f)
    #     print(userdata)
    #     userData_list = userdata["userCredentials"]


    def get_token(self,playwright : Playwright,userData_set):
        request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = request_context.post("/api/ecom/auth/login", data=userData_set)
        if not response.ok:
            print(f"Auth failed: {response.status} - {response.text()}")
        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]

    def create_order(self, playwright : Playwright,userData_set):
        token = self.get_token(playwright,userData_set)
        request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = request_context.post("/api/ecom/order/create-order",
                                        headers = {"Authorization" : token, "content-type" : "application/json"},
                                        data = create_order_payload)
        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["orders"][0]

from playwright.sync_api import expect


class OrderDetails:

    def __init__(self, page):
        self.page = page

    def view_order_details(self):
        expect(self.page.locator("body")).to_contain_text("Thank you for Shopping With Us")
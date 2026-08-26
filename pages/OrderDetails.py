from playwright.sync_api import expect

from utils.logger import get_logger


class OrderDetails:

    def __init__(self, page):
        self.page = page
        self.logger = get_logger(__name__)

    def view_order_details(self):
        self.logger.info("Viewing order details")
        expect(self.page.locator("body")).to_contain_text("Thank you for Shopping With Us")
        self.logger.info("Order details viewed successfully")
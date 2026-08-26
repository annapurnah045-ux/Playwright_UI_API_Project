from pages.OrdersPage import OrdersPage
from utils.logger import get_logger


class Dashboard:

    def __init__(self, page):
        self.page = page
        self.logger = get_logger(__name__)

    def navigate_to_orders(self):
        self.logger.info("Navigating to Orders page")
        self.page.get_by_role("button", name="ORDERS").click()
        self.logger.info("Navigation to Orders page successful")
        return OrdersPage(self.page)



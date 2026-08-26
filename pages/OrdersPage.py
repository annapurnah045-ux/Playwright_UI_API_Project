from pages.OrderDetails import OrderDetails
from utils.logger import get_logger


class OrdersPage:

    def __init__(self, page):
        self.page = page
        self.logger = get_logger(__name__)

    def get_order(self,order_id):
        self.logger.info("Fetching order details for order ID: {}".format(order_id))
        self.page.locator("tr").filter(has_text=order_id).get_by_role("button", name="View").click()
        self.logger.info("Order details fetched successfully for order ID: {}".format(order_id))
        return OrderDetails(self.page)



from pages.OrderDetails import OrderDetails

class OrdersPage:

    def __init__(self, page):
        self.page = page

    def get_order(self,order_id):
        self.page.locator("tr").filter(has_text=order_id).get_by_role("button", name="View").click()
        return OrderDetails(self.page)



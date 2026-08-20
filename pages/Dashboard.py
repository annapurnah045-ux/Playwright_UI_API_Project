from pages.OrdersPage import OrdersPage

class Dashboard:

    def __init__(self, page):
        self.page = page

    def navigate_to_orders(self):
        self.page.get_by_role("button", name="ORDERS").click()
        return OrdersPage(self.page)



from pages.Dashboard import Dashboard
from utils.logger import get_logger


class Login:

    def __init__(self, page):
        self.page = page
        self.logger = get_logger(__name__)

    def get_login(self,userData_set,baseURL):
        self.logger.info("Navigating to login page: {}".format(baseURL))
        self.page.goto(baseURL)
        #page.goto("https://rahulshettyacademy.com/client")
        self.page.get_by_role("textbox", name="email@example.com").fill(userData_set["userEmail"])
        self.page.get_by_role("textbox", name="enter your passsword").fill(userData_set["userPassword"])
        self.page.get_by_role("button", name="Login").click()
        self.logger.info("Login successful for user: {}".format(userData_set["userEmail"]))
        return Dashboard(self.page)
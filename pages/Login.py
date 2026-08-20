from pages.Dashboard import Dashboard

class Login:

    def __init__(self, page):
        self.page = page

    def get_login(self,userData_set,baseURL):
        self.page.goto(baseURL)
        #page.goto("https://rahulshettyacademy.com/client")
        self.page.get_by_role("textbox", name="email@example.com").fill(userData_set["userEmail"])
        self.page.get_by_role("textbox", name="enter your passsword").fill(userData_set["userPassword"])
        self.page.get_by_role("button", name="Login").click()
        return Dashboard(self.page)
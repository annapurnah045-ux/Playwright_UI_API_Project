
from playwright.sync_api import Page
from playwright.sync_api import expect
import time

def test_addItemsToCart(page:Page):
     page.goto("https://rahulshettyacademy.com/loginpagePractise/")
     print(page.title())
     page.get_by_label("Username:").fill("rahulshettyacademy")
     page.get_by_label("Password:").fill("Learning@830$3mK2")
     page.get_by_role("combobox").select_option("consult")
     page.locator("#terms").click()
     page.get_by_role("link",name="terms and conditions").click()
     page.get_by_role("button", name="Sign In").click()
     iphone_product = page.locator("app-card").filter(has_text="iphone X")
     iphone_product.get_by_role("button").click()
     SamsungProduct = page.locator("app-card").filter(has_text="Samsung Note 8")
     SamsungProduct.get_by_role("button", name="Add ").click()
     page.get_by_text("Checkout").click()
     expect(page.locator(".media-body")).to_have_count(2)
     time.sleep(5)


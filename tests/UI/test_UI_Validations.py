from playwright.sync_api import Page
from playwright.sync_api import expect
import time


def test_UI_Validations(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    # Alerts
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()
    time.sleep(3)

    # Hidden/Visible
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_placeholder("Hide/Show Example").fill("Test")
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    # Mouse Hover
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()

    # FrameHandles
    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role("link",name="All Access plan").click()
    expect(page_frame.locator("body")).to_contain_text("Happy Subscibers!")

    # Iterate through table
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    header = page.locator("th")
    priceColdIndex = 0
    for i in range(header.count()):
        if header.nth(i).text_content().strip() == "Price":
            priceColdIndex = i
            break
    price = page.locator("tr").filter(has_text="Rice").locator("td").nth(priceColdIndex)
    print(f"Price of rice : {price}")
    expect(price).to_have_text("37")
    #assert price.strip == "37"

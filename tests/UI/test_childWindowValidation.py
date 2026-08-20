from playwright.sync_api import Page

def test_childWindowValidation(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as popupInfo:
        page.locator(".blinkingText").first.click()
        childPage = popupInfo.value
        text = childPage.locator(".im-para").nth(1).text_content()
        print(text)
        words=text.split("at")
        email = words[1].strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"


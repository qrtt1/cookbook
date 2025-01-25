import pytest
from playwright.sync_api import sync_playwright

headless = True
# headless = False


@pytest.fixture
def browser():
    global headless
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page(no_viewport=True)
    yield page
    page.close()

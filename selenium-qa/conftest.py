import os, pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1366,768")
    if os.getenv("CI"):  # friendlier for pipelines
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
    d = webdriver.Chrome(options=opts)
    try:
        yield d
    finally:
        d.quit()

class HomePage:
    URL = "https://example.com"
    TITLE = "Example Domain"

    def __init__(self, driver):
        self.d = driver

    def open(self):
        self.d.get(self.URL)

    def title(self):
        return self.d.title

from pages.home_page import HomePage

def test_title_matches(driver):
    page = HomePage(driver)
    page.open()
    assert page.TITLE in page.title()

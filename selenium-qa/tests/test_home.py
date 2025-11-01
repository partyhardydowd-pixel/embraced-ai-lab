from pages.home_page import HomePage


def test_title_matches(driver):
    page = HomePage(driver)
    page.open()
    assert page.TITLE in page.title()

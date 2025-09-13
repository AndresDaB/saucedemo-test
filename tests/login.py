from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_login_valid_user(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    assert "inventory" in driver.current_url, "Login failed"

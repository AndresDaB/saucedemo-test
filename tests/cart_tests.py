from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_add_product_to_cart(driver):
    # Login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Add product
    products_page = ProductsPage(driver)
    products_page.add_backpack_to_cart()
    products_page.back_to_products()

    # Verify cart count
    count = products_page.get_cart_count()
    assert count == "1", f"Expected 1 item in cart, but got {count}"

def test_product_by_price(driver):
    # Login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    products = products_page.get_all_products()

    found = False
    for product in products:
        name = product.find_element_by_class_name("inventory_item_name").text.strip()
        price = product.find_element_by_class_name("inventory_item_price").text.strip()
        if price == "$7.99":
            found = True
            assert name == "Sauce Labs Onesie" or name == "Sauce Labs Bike Light"
            break

    assert found, "No product found with price $7.99"

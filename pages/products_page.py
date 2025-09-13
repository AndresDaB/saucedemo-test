from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        backpack = self.driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
        backpack.click()
        add_button = self.driver.find_element(By.XPATH, '//button[contains(text(), "Add to cart")]')
        add_button.click()

    def back_to_products(self):
        self.driver.find_element(By.ID, "back-to-products").click()

    def get_cart_count(self):
        cart_badge = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        return cart_badge.text.strip()

    def get_all_products(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item")

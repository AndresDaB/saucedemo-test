from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        user_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        user_input.send_keys(username)

        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys(password)

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.product_register_page import ProductRegisterPage
from pages.login_page import LoginPage
import time

class TestProductRegister(unittest.TestCase):

    def setUp(self):
        self.__driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.__driver.implicitly_wait(15)
        self.__driver.maximize_window()
        self.__driver.get("https://practicesoftwaretesting.com/auth/login")

        self.__login_page = LoginPage(self.__driver)
        self.__product_register_page = ProductRegisterPage(self.__driver)

    def tearDown(self):
        self.__driver.quit()

    def test_01_register_product_ok(self):
        # Arrange
        email_admin = "admin@practicesoftwaretesting.com"
        password_admin = "welcome01"

        product_name = f"Laptop Gamer X{int(time.time())}"  # único
        description = f"Descripcion del producto {product_name}"
        stock = 75
        price = 150.50
        brand = "ForgeFlex Tools"
        category = "Other"
        image = "Hammer"

        # Act
        self.__login_page.login(email_admin, password_admin)
        self.__login_page.display_menu()
        self.__login_page.click_menu_products()
        self.__product_register_page.click_add_product()

        self.__product_register_page.enter_name(product_name)
        self.__product_register_page.enter_description(description)
        self.__product_register_page.enter_stock(stock)
        self.__product_register_page.enter_price(price)
        self.__product_register_page.select_brand(brand)
        self.__product_register_page.select_category(category)
        self.__product_register_page.select_image(image)
        self.__product_register_page.click_save()

        # Assert
        success_element = self.__product_register_page.get_success_element()
        self.assertTrue(success_element.is_displayed())

        

    def test_02_register_product_error(self):
        # Arrange
        email_admin = "admin@practicesoftwaretesting.com"
        password_admin = "welcome01"

        product_name = f"Laptop Gamer X{int(time.time())}"  # único
        description = f"Descripcion del producto {product_name}"
        stock = -75
        price = -150.50
        brand = "ForgeFlex Tools"
        category = "Other"
        image = "Hammer"

        # Act
        self.__login_page.login(email_admin, password_admin)
        self.__login_page.display_menu()
        self.__login_page.click_menu_products()
        self.__product_register_page.click_add_product()

        self.__product_register_page.enter_name(product_name)
        self.__product_register_page.enter_description(description)
        self.__product_register_page.enter_stock(stock)
        self.__product_register_page.enter_price(price)
        self.__product_register_page.select_brand(brand)
        self.__product_register_page.select_category(category)
        self.__product_register_page.select_image(image)
        self.__product_register_page.click_save()

        # Assert
        danger_element = self.__product_register_page.get_danger_element()
        #self.assertIn("Product saved!", success_message)
        self.assertTrue(danger_element.is_displayed())

if __name__ == "__main__":
    unittest.main()
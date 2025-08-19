import unittest
from selenium import webdriver
from pages.product_register_page import ProductRegisterPage
from pages.login_page import LoginPage
import time

class Test(unittest.TestCase):

    def setUp(self):
        self.__driver = webdriver.Chrome()
        self.__driver.get("https://practicesoftwaretesting.com/auth/login")
        self.__login_page = LoginPage(self.__driver)
        self.__product_register_page = ProductRegisterPage(self.__driver)

    def tearDown(self):
        self.__driver.quit()
    
    def test_register_user_ok(self):
        # Arrange
        email_admin = "admin@practicesoftwaretesting.com"
        password_admin = "welcome01"

        first_name = "Franz"
        last_name = "Muraña"
        date_of_birth = "01-01-1990"
        street = "Calle Azurduy"
        postal_code = "12345"
        city = "Sucre"
        state = "Chuquisaca"
        country = "Bolivia (Plurinational State of)"
        phone = "60328827"
        email = "xavie2@gmail.com"
        enabled = True
        failed_login_attempts = 3
        password = "M43str1a4*"

        # Act
        self.__login_page.login(email_admin, password_admin)
        self.__login_page.display_menu()
        self.__login_page.click_menu_users()
        self.__login_page.click_link_add_user()

        self.__product_register_page.enter_first_name(first_name)
        self.__product_register_page.enter_last_name(last_name)
        self.__product_register_page.enter_date_of_birth(date_of_birth)        
        self.__product_register_page.enter_street(street)
        self.__product_register_page.enter_postal_code(postal_code)
        self.__product_register_page.enter_city(city)
        self.__product_register_page.enter_state(state)
        self.__product_register_page.enter_country(country)
        self.__product_register_page.enter_phone(phone)
        self.__product_register_page.enter_email(email)
        if enabled:
            self.__product_register_page.check_enabled()
        self.__product_register_page.enter_failed_login_attempts(failed_login_attempts)
        self.__product_register_page.enter_password(password)
        self.__product_register_page.click_button_save()

        time.sleep(100)

        # Assert
        
        
if __name__ == '__main__':
    unittest.main()
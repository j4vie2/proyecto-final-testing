import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.user_register_page import UserRegisterPage
from pages.login_page import LoginPage
import time

class Test(unittest.TestCase):

    def setUp(self):
        self.__driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.__driver.implicitly_wait(15)

        self.__driver.get("https://practicesoftwaretesting.com/auth/login")
        self.__login_page = LoginPage(self.__driver)
        self.__user_register_page = UserRegisterPage(self.__driver)

    def tearDown(self):
        self.__driver.quit()
    
    def test_01_register_user_ok(self):
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

        self.__user_register_page.enter_first_name(first_name)
        self.__user_register_page.enter_last_name(last_name)
        self.__user_register_page.enter_date_of_birth(date_of_birth)        
        self.__user_register_page.enter_street(street)
        self.__user_register_page.enter_postal_code(postal_code)
        self.__user_register_page.enter_city(city)
        self.__user_register_page.enter_state(state)
        self.__user_register_page.enter_country(country)
        self.__user_register_page.enter_phone(phone)
        self.__user_register_page.enter_email(email)
        if enabled:
            self.__user_register_page.check_enabled()
        self.__user_register_page.enter_failed_login_attempts(failed_login_attempts)
        self.__user_register_page.enter_password(password)
        self.__user_register_page.click_button_save()

        # Assert
        result = self.__user_register_page.get_message_ok()
        self.assertTrue(result)
    
    def test_02_register_user_email_exists(self):
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
        expected_message_ko = "A customer with this email address already exists."

        # Act
        self.__login_page.login(email_admin, password_admin)
        self.__login_page.display_menu()
        self.__login_page.click_menu_users()
        self.__login_page.click_link_add_user()

        self.__user_register_page.enter_first_name(first_name)
        self.__user_register_page.enter_last_name(last_name)
        self.__user_register_page.enter_date_of_birth(date_of_birth)        
        self.__user_register_page.enter_street(street)
        self.__user_register_page.enter_postal_code(postal_code)
        self.__user_register_page.enter_city(city)
        self.__user_register_page.enter_state(state)
        self.__user_register_page.enter_country(country)
        self.__user_register_page.enter_phone(phone)
        self.__user_register_page.enter_email(email)
        if enabled:
            self.__user_register_page.check_enabled()
        self.__user_register_page.enter_failed_login_attempts(failed_login_attempts)
        self.__user_register_page.enter_password(password)
        self.__user_register_page.click_button_save()

        # Assert
        result = self.__user_register_page.get_message_ko()
        self.assertIn(expected_message_ko, result)
    
if __name__ == '__main__':
    unittest.main()
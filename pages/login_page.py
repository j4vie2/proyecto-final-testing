from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.__driver = driver
        self.__email = (By.ID, "email")
        self.__password = (By.ID, "password")
        self.__button_login = (By.XPATH, "//input[@type='submit']")

    def login(self, email, password):
        email_field = self.__driver.find_element(*self.__email)
        password_field = self.__driver.find_element(*self.__password)
        submit_button = self.__driver.find_element(*self.__button_login)
        
        email_field.clear()
        email_field.send_keys(email)
        password_field.clear()
        password_field.send_keys(password)
        
        submit_button.click()

    def display_menu(self):
        menu_dropdown = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, "menu"))
        )
        menu_dropdown.click()

    def click_menu_users(self):
        users_option = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Users"))
        )
        users_option.click()

    def click_link_add_user(self):
        add_user_link = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Add User"))
        )
        add_user_link.click()

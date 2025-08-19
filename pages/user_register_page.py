from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserRegisterPage:
    def __init__(self, driver):
        self.__driver = driver
        self.__first_name = (By.ID, "firstname")
        self.__last_name = (By.ID, "lastname")
        self.__date_of_birth = (By.ID, "dob")
        self.__street = (By.ID, "street")
        self.__postal_code = (By.ID, "postal_code")
        self.__city = (By.ID, "city")
        self.__state = (By.ID, "state")
        self.__country = (By.ID, "country")
        self.__phone = (By.ID, "phone")
        self.__email = (By.ID, "email")
        self.__enabled = (By.ID, "enabled")
        self.__failed_login_attempts = (By.ID, "failed_login_attempts")
        self.__password = (By.ID, "password")
        self.__button_save = (By.CSS_SELECTOR, "button[type='submit']")

    def enter_first_name(self, first_name):
        first_name_field = self.__driver.find_element(*self.__first_name)
        first_name_field.clear()
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name):
        last_name_field = self.__driver.find_element(*self.__last_name)
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    def enter_date_of_birth(self, date_of_birth):
        date_of_birth_field = self.__driver.find_element(*self.__date_of_birth)
        date_of_birth_field.clear()
        date_of_birth_field.send_keys(date_of_birth)

    def enter_street(self, street):
        street_field = self.__driver.find_element(*self.__street)
        street_field.clear()
        street_field.send_keys(street)
    
    def enter_postal_code(self, postal_code):
        postal_code_field = self.__driver.find_element(*self.__postal_code)
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)

    def enter_city(self, city):
        city_field = self.__driver.find_element(*self.__city)
        city_field.clear()
        city_field.send_keys(city)

    def enter_state(self, state):
        state_field = self.__driver.find_element(*self.__state)
        state_field.clear()
        state_field.send_keys(state)

    def enter_country(self, country):
        country_field = self.__driver.find_element(*self.__country)
        country_field.click()
        opcion = self.__driver.find_element(By.XPATH, f"//option[text()='{country}']")
        opcion.click()

    def enter_phone(self, phone):
        phone_field = self.__driver.find_element(*self.__phone)
        phone_field.clear()
        phone_field.send_keys(phone)

    def enter_email(self, email):
        email_field = self.__driver.find_element(*self.__email)
        email_field.clear()
        email_field.send_keys(email)

    def check_enabled(self):
        enabled_checkbox = self.__driver.find_element(*self.__enabled)
        if not enabled_checkbox.is_selected():
            enabled_checkbox.click()

    def enter_failed_login_attempts(self, attempts):
        attempts_field = self.__driver.find_element(*self.__failed_login_attempts)
        attempts_field.clear()
        attempts_field.send_keys(str(attempts))

    def enter_password(self, password):
        password_field = self.__driver.find_element(*self.__password)
        password_field.clear()
        password_field.send_keys(password)

    def click_button_save(self):
        save_button = self.__driver.find_element(*self.__button_save)
        save_button.click()

    def get_message_ok(self):
        message_element = WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'alert-success') and contains(text(), 'User saved!')]"))
        )
        return message_element.is_displayed()

    def get_message_ko(self):
        message_element = WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'alert-danger')]"))
        )
        
        return message_element.text
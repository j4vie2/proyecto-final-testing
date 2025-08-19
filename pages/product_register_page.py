from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class ProductRegisterPage:
    def __init__(self, driver):
        self.__driver = driver
        # Locators
        self.__button_add_product = (By.CSS_SELECTOR, '[data-test="product-add"]')
        self.__name = (By.CSS_SELECTOR, '[data-test="name"]')
        self.__description = (By.CSS_SELECTOR, '[data-test="description"]')
        self.__stock = (By.CSS_SELECTOR, '[data-test="stock"]')
        self.__price = (By.CSS_SELECTOR, '[data-test="price"]')
        self.__brand = (By.CSS_SELECTOR, '[data-test="brand-id"]')
        self.__category = (By.CSS_SELECTOR, '[data-test="category-id"]')
        self.__image = (By.CSS_SELECTOR, '[data-test="product-image-id"]')
        self.__button_save = (By.CSS_SELECTOR, '[data-test="product-submit"]')
        self.__success_alert = (By.CSS_SELECTOR, 'div.alert-success')
        self.__danger_alert = (By.CSS_SELECTOR, 'div.alert-danger')

    def click_add_product(self):
        self.__driver.find_element(*self.__button_add_product).click()

    def enter_name(self, product_name):
        name_field = WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located(self.__name)
        )
        name_field.clear()
        name_field.send_keys(product_name)

    def enter_description(self, description):
        field = self.__driver.find_element(*self.__description)
        field.clear()
        field.send_keys(description)

    def enter_stock(self, stock):
        field = self.__driver.find_element(*self.__stock)
        field.clear()
        field.send_keys(str(stock))

    def enter_price(self, price):
        field = self.__driver.find_element(*self.__price)
        field.clear()
        field.send_keys(str(price))

    def select_brand(self, brand_text):
        Select(self.__driver.find_element(*self.__brand)).select_by_visible_text(brand_text)

    def select_category(self, category_text):
        Select(self.__driver.find_element(*self.__category)).select_by_visible_text(category_text)

    def select_image(self, image_text):
        Select(self.__driver.find_element(*self.__image)).select_by_visible_text(image_text)

    def click_save(self):
        self.__driver.find_element(*self.__button_save).click()

    def get_success_element(self):
        element = WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located(self.__success_alert)
        )
        return element

    def get_danger_element(self):
        element = WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located(self.__danger_alert)
        )
        return element

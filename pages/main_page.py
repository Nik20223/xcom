from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
class Main_page(Base):
    url = 'https://www.xcom-shop.ru/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    login_window = "//div[@onclick='_popup.login()']"
    user_name = "//input[@id='auth_l']"
    password = "//input[@id='auth_p']"
    city_button = "//span[@class='site_header__city_selector_text']"
    city_window = "//input[@name = 'search_city']"
    login_button = "//input[@id = 'submitLogin']"
    catalog_button = "//div[contains(@class,'button_clear white_on_transparent')]"
    assesories_button = "(//a[@data-url='kompyuternye_komplektyyuschie']//span)[2]"




    # Getters

    def get_login_window(self):
        return driver.find_element(By.XPATH, self.assesories_button)
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))
    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))
    def get_city_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_button)))
    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))
    def get_asessories_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.assesories_button)))
    def get_city_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_window)))


    # Actions

    def login_window_click(self):
        return get_login_window().click()
    def city_button_click(self):
        return get_city_button().click()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
class Login_page(Base):
    url = 'https://supereyes.ru/login/?login=yes&backurl=%2F'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    # login_window = "(//a[@role='button'])[1]"
    user_name = "(//table[@class='bx-auth-table']//input)[1]"
    password = "(//table[@class='bx-auth-table']//input)[2]"
    login_button = "//td[@class='authorize-submit-cell']//input[1]"
    # city_window = "//input[@name = 'search_city']"
    # login_button = "//input[@id = 'submitLogin']"
    # catalog_button = "//div[contains(@class,'button_clear white_on_transparent')]"
    # assesories_button = "(//a[@data-url='kompyuternye_komplektyyuschie']//span)[2]"




    # Getters

    def get_login_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_window)))
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))
    # def get_password(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_password(self):
        return self.driver.find_element(By.XPATH, self.password)
    # def get_city_button(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_button)))
    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
    # def get_catalog_button(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))
    # def get_asessories_button(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.assesories_button)))
    # def get_city_window(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_window)))


    # Actions

    def login_click(self):
        self.get_login_button().click()
    def user_name_send(self):
        self.get_user_name().send_keys('niktih')
    # def password_window(self):
    #     self.get_password().click()
    def password_send(self):
        self.get_password().send_keys('nikita'+'qa')
    # Methods

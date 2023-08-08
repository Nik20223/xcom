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
    login_window = "(//div[@class='profile_block__login'])[2]"
    user_name = "//input[@id='auth_l']"
    password = "//input[@id='auth_p']"
    city_button = ""
    login_button = ""
    catalog_button = ""
    assesories_button = ""




    # Getters

    def get_login_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_window)))



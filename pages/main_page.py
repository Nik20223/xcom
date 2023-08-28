from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
class Main_page(Base):
    url = 'https://supereyes.ru/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    login_window = "//a[@href='/login/?login=yes&backurl=%2F']"





    # Getters


    def get_login_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_window)))

    # Actions
    ### Open login window ###
    def login_window_click(self):
        self.get_login_window().click()
        print(("Click login window"))


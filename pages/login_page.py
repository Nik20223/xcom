from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
myname = "Никита"
class Login_page(Base):
    url = 'https://supereyes.ru/login/?login=yes&backurl=%2F'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    user_name = "(//table[@class='bx-auth-table']//input)[1]"
    password = "(//table[@class='bx-auth-table']//input)[2]"
    login_button = "//td[@class='authorize-submit-cell']//input[1]"
    login_name = "(//a[@href='/personal/'])[1]"



    # Getters

    def get_login_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_window)))
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return self.driver.find_element(By.XPATH, self.password)

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_login_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_name)))

    # Actions

    def login_click(self):
        self.get_login_button().click()
    def user_name_send(self):
        self.get_user_name().send_keys('niktih')

    def password_send(self):
        self.get_password().send_keys('nikita'+'qa')
    # Methods

    def get_login_name_text(self):
        self.assert_word(self.get_login_name(), myname)

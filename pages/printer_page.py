from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Printer_page(Base):
    url = 'https://supereyes.ru/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    # login_window = "(//a[@role='button'])[1]"
    # user_name = "(//div[@class='input-material__input-wrapper']//input)[2]"
    # password = "(//input[@class='input-material__input-user-agent input-material__input'])[2]"
    # city_button = "//span[@class='site_header__city_selector_text']"
    # city_window = "//input[@name = 'search_city']"
    # login_button = "//input[@id = 'submitLogin']"
    # catalog_button = "//div[contains(@class,'button_clear white_on_transparent')]"
    printers_and_chpu_button = "//a[@href='/catalog/stanki_s_chpu_i_3d_printery/']"
    printer_3d_button = "//li[@id='bx_1847241719_283']"
    printer_basket = "//a[@id='bx_3966226736_16497_c80764dfaf26ca80162484593ec7c29b_buy_link']"




    # Getters

    def get_printers_href(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.printers_and_chpu_button)))
    def get_printer_href(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.printer_3d_button)))
    def get_printer_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.printer_basket)))
    # # def get_password(self):
    # #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))
    #
    # def get_password(self):
    #     return self.driver.find_element(By.XPATH, self.password)
    # def get_city_button(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_button)))
    # def get_login_button(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
    # def get_catalog_button(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))
    # def get_asessories_button(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.assesories_button)))
    # def get_city_window(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_window)))
    #

    # Actions
    # action = ActionChains(Base)

    def printers_click(self):
        self.get_printers_href().click()
    # def user_name_send(self):
    #     self.get_user_name().send_keys('sdfsdf@tih.ru')
    def printer_click(self):
        self.get_printer_href().click()
    # def password_send(self):
    #     self.get_password().send_keys('nikita'+'qa')
    # def printer_basket_click(self):
    #     self.get_printer_href().click()
    # def printers_chpu_insight(self):
    #     self.action.move_to_element(self.get_printers_href())
    # #
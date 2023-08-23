import time

from selenium.webdriver import ActionChains, Keys
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

    printers_and_chpu_button = "//a[@href='/catalog/stanki_s_chpu_i_3d_printery/']"
    printer_3d_button = "//li[@id='bx_1847241719_283']"
    printer_basket = "//div[@id='bx_3966226736_16497_c80764dfaf26ca80162484593ec7c29b_basket_actions']"
    sort_button = "//a[@href='/catalog/3d_printery/?sort=low&order=asc']"
    continue_button = "//span[@class='btn btn-default btn-buy btn-sm'][2]"
    checkout_button = "//a[@class='checkout']"
    fio_window = "//input[@name='ORDER_PROP_1']"
    mail_window = "//input[@name='ORDER_PROP_2']"
    phone_window = "//input[@name='ORDER_PROP_3']"
    address_window = "//textarea[@name='ORDER_PROP_7']"




    # Getters

    def get_printers_href(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.printers_and_chpu_button)))
    def get_printer_href(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.printer_3d_button)))
    def get_printer_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.printer_basket)))
    def get_sort_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_button)))
    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))
    def get_ckeckout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))
    def get_fio_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.fio_window)))
    def get_mail_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mail_window)))
    def get_phone_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_window)))
    def get_address_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address_window)))


    # Actions


    def printers_click(self):
        self.get_printers_href().click()

    def printer_click(self):
        self.get_printer_href().click()

    def printer_basket_click(self):
        self.get_printer_basket().click()

    def sort_click(self):
        self.get_sort_button().click()

    def continue_click(self):
        self.get_continue_button().click()
    def checkout_click(self):
        self.get_ckeckout_button().click()

    def fio_send(self):
        self.get_fio_window().clear()
        self.get_fio_window().send_keys('Турапин Никита Владимирович')
    def mail_send(self):
        self.get_mail_window().clear()
        self.get_mail_window().send_keys('555@tih.ru')
        self.get_mail_window().send_keys(Keys.RETURN)
    def phone_send(self):
        self.get_phone_window().clear()
        self.get_phone_window().send_keys('8')
        self.get_phone_window().send_keys('8')
        self.get_phone_window().send_keys('6')
        self.get_phone_window().send_keys('1')
        self.get_phone_window().send_keys('9')
        self.get_phone_window().send_keys('6')
        self.get_phone_window().send_keys('7')
        self.get_phone_window().send_keys('4')
        self.get_phone_window().send_keys('4')
        self.get_phone_window().send_keys('4')
        self.get_phone_window().send_keys('3')
        self.get_phone_window().send_keys(Keys.RETURN)
    def address_send(self):
        self.get_address_window().clear()
        self.get_address_window().send_keys('Тихорецк Мичурина 14')
        time.sleep(1)
        self.get_address_window().send_keys(Keys.RETURN)

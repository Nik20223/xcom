from selenium import webdriver
from pages.main_page import Main_page
from pages.login_page import Login_page
from pages.printer_page import Printer_page
import pytest

driver = webdriver.Chrome()
base_url = 'https://supereyes.ru/'
driver.get(base_url)
driver.maximize_window()
print("Open main page")
@pytest.fixture()
def set_up():
    print("My first test")
def test_1(set_up):
    tool = Main_page(driver)
    tool.login_window_click()
    tool = Login_page(driver)
    tool.login_click()
    tool.get_login_name_text()
    tool = Printer_page(driver)
    tool.printers_click()
    tool.printer_click()
    tool.sort_click()
    tool.printer_basket_click()
    tool.checkout_click()
    tool.fio_send()
    tool.mail_send()
    tool.phone_send()
    tool.address_send()
    tool.screenshot()








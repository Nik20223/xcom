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
    tool = Printer_page(driver)
    tool.printer_choose()
    tool.checkout_click()
    tool.data_send()
    tool.screenshot()








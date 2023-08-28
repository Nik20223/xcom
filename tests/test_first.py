from selenium import webdriver
from pages.main_page import Main_page
from pages.login_page import Login_page
from pages.printer_page import Printer_page
import pytest
driver = webdriver.Chrome()
base_url = 'https://supereyes.ru/'
driver.get(base_url)
driver.maximize_window()

@pytest.fixture()
def set_up():
    print("superyes.ru")

def test_smoke_testing(set_up):
    mp = Main_page(driver)
    mp.login_window_click()
    lp = Login_page(driver)
    lp.login_click()
    pp = Printer_page(driver)
    pp.printer_choose()
    pp.checkout_click()
    pp.data_send()
    pp.screenshot()
    pp = Printer_page(driver)

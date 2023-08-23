from selenium import webdriver
from pages.main_page import Main_page
from pages.login_page import Login_page
from pages.printer_page import Printer_page
from selenium.webdriver.chrome.service import Service
import pytest


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(executable_path='/home/user/PycharmProjects/xcom/utilities/chromedriver')
driver = webdriver.Chrome(options=options, service=service)
base_url = 'https://supereyes.ru/'
driver.get(base_url)
driver.maximize_window()
@pytest.fixture()
def set_up():
    print("Open browser")
def test_1(set_up):
    tool = Main_page(driver)
    print("Open main page")
    tool.login_window_click()
    print(("Click login window"))
def test_2(set_up):
    tool = Login_page(driver)
    tool.user_name_send()
    print("Send username")
    tool.password_send()
    print("Send password")
    tool.login_click()
    print("Click login button")
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






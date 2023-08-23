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
    print("My first test")
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
    tool.get_login_name_text()
def test_3(set_up):
    tool = Printer_page(driver)
    tool.printers_click()
    print("Printers and chpu click")
    tool.printer_click()
    print("3d printers click")
    tool.sort_click()
    print("Sort by low price click")
    tool.printer_basket_click()
    print("Add printer to basket")
    tool.checkout_click()
    print("Chekout click")
    tool.fio_send()
    print("Send fio")
    tool.mail_send()
    print("Send mail")
    tool.phone_send()
    print("Send phone number")
    tool.address_send()
    print("Select address")
    tool.screenshot()
    print("Make screenshot")

# driver.quit()





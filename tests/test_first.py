import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import Main_page
from pages.login_page import Login_page
from pages.printer_page import Printer_page
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(executable_path='/home/user/PycharmProjects/xcom/utilities/chromedriver')
driver = webdriver.Chrome(options=options, service=service)
base_url = 'https://supereyes.ru/'

driver.get(base_url)
driver.maximize_window()
tool = Main_page(driver)
tool.login_window_click()
tool = Login_page(driver)
tool.user_name_send()
tool.password_send()
# print("login click")
tool.login_click()
# print("login send")
tool = Printer_page(driver)
tool.printers_click()
# time.sleep(2)
tool.printer_click()
# time.sleep(2)
# tool.printer_basket_click()
# tool.printers_chpu_insight()
# tool.password_window()
# print("Click password")
# tool.password_send()
# time.sleep(3)
# print("Send password")






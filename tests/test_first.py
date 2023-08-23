from selenium import webdriver
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
tool.login_click()
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






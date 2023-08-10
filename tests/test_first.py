from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import Main_page
from selenium.webdriver.chrome.service import Service
class Test_first():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service(executable_path='/home/user/PycharmProjects/xcom/utilities/chromedriver')
    driver = webdriver.Chrome(options=options, service=service)
    base_url = 'https:\\xcom-shop.ru'
    driver.set_window_size(1920, 1080)
    driver.get(base_url)
    # driver.maximize_window()

test_open_login = Main_page(driver)
test_open_login.login_window_click()

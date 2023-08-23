from datetime import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Assertation OK")

    def screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        driver.savescreenshot('/home/user/PycharmProjects/xcom/screenshot' + name_screenshot)
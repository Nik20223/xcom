from datetime import datetime

class Base():
    def __init__(self, driver):
        self.driver = driver

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Assertation OK")

    def screenshot(self):
        now_date = datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot('/screenshots/' + name_screenshot)

from selenium import webdriver
from selenium.webdriver.common.by import By

class InvalidUserLoginError:

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    url = 'http://demostore.supersqa.com/my-account/'
    invalid_email = 'abcfdfd@gmail.com'
    expected_msg = 'Unknown email address. Check again or try your username.'

    def __init__(self):
        self.driver
        self.driver.implicitly_wait(10)

    def go_to_my_account(self):
        self.driver.get(self.url)

    def input_email(self):
        field = self.driver.find_element(By.ID, 'username')
        field.send_keys(self.invalid_email)

    def input_password(self):
        field = self.driver.find_element(By.ID, 'password')
        field.send_keys('abcdefge')

    def click_login(self):
        self.driver.find_element(By.NAME, 'login').click()

    def verify_error_msg(self):
        error_element = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/ul')
        displayed_error = error_element.text
        assert displayed_error == self.expected_msg, "The displayed error is not expected."
        print("PASS")

    def main(self):
        self.go_to_my_account()
        self.input_email()
        self.input_password()
        self.click_login()
        self.verify_error_msg()
        self.driver.quit()


if __name__ == '__main__':                          # pake 'main' supaya kalo mau jalanin script, harus jalanin filenya. kalo di import doang gaakan jalan

    obj = InvalidUserLoginError()
    obj.main()





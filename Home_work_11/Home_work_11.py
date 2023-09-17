from selenium import webdriver
from selenium.webdriver.common.by import By
import requests


class TestRegistration:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.session = requests.session()

    def sign_up_new_user(self):
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
        signup_button = self.driver.find_element(By.XPATH, "//button[text() ='Sign up']")
        signup_button.click()
        name_field = self.driver.find_element(By.ID, "signupName")
        last_name_field = self.driver.find_element(By.ID, "signupLastName")
        email_field = self.driver.find_element(By.ID, "signupEmail")
        password_field = self.driver.find_element(By.ID, "signupPassword")
        repeat_password_field = self.driver.find_element(By.ID, "signupRepeatPassword")
        confirm_sign_up_button = self.driver.find_element(By.XPATH, "//button[text() = 'Register']")

        #######
        name_field.send_keys("James")
        last_name_field.send_keys("Bond")
        email_field.send_keys("holawider@hdjs.com")
        password_field.send_keys("somePs45")
        repeat_password_field.send_keys("somePs45")
        confirm_sign_up_button.click()

    def test_successful_message(self):
        self.sign_up_new_user()
        expected_message = "You don’t have any cars in your garage"
        actual_message_element = self.driver.find_element(By.XPATH,
                                                          "//p[text() = 'You don’t have any cars in your garage']")
        actual_message = actual_message_element.text
        assert actual_message == expected_message

    def teardown_class(self):
        user_credentials = [
            ("holawider@hdjs.com", "somePs45", False)
        ]

        login_url = "https://qauto2.forstudy.space/api/auth/signin"
        self.session.post(url=login_url, json=user_credentials)
        self.driver.implicitly_wait(2)

        delete_url = "https://qauto2.forstudy.space/api/users"
        self.session.delete(url=delete_url)
        self.session.close()
        self.driver.quit()


a = 0

# def find_element(self, by, value):
#     return self.driver.find_element(by, value)
#
# def click_element(self, element):
#     element.click()
#
# def send_keys_to_element(self, element, text):
#     element.send_keys(text)

# signup_button = driver.find_element(By.XPATH, "//button[text() ='Sign up']")
# signup_button.click()
# name_field = driver.find_element(By.ID, "signupName")
# name_field.send_keys("Roger")
# last_name_field = driver.find_element(By.ID, "signupLastName")
# last_name_field.send_keys("Winston")
# email_field = driver.find_element(By.ID, "signupEmail")
# email_field.send_keys("roger@hdjs.com")
# password_field = driver.find_element(By.ID, "signupPassword")
# password_field.send_keys("somePass55")
# repeat_password_field = driver.find_element(By.ID, "signupRepeatPassword")
# repeat_password_field.send_keys("somePass55")
# confirm_sign_up_button = driver.find_element(By.XPATH, "//button[text() = 'Register']")
# confirm_sign_up_button.click()
# driver = webdriver.Chrome()
# driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
# signup_button = driver.find_element(By.XPATH, "//button[text() ='Sign up']")
# signup_button.click()
# name_field = driver.find_element(By.ID, "signupName")
# name_field.send_keys("Roger")
# last_name_field = driver.find_element(By.ID, "signupLastName")
# last_name_field.send_keys("Winston")
# email_field = driver.find_element(By.ID, "signupEmail")
# email_field.send_keys("roger@hdjs.com")
# password_field = driver.find_element(By.ID, "signupPassword")
# password_field.send_keys("somePass55")
# repeat_password_field = driver.find_element(By.ID, "signupRepeatPassword")
# repeat_password_field.send_keys("somePass55")
# confirm_sign_up_button = driver.find_element(By.XPATH, "//button[text() = 'Register']")
# confirm_sign_up_button.click()

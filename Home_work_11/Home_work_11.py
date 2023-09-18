from selenium import webdriver
from selenium.webdriver.common.by import By
import requests


class TestRegistration:
    email = "holarider@hdjs.com"
    password = "somePs45"

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
        email_field.send_keys(self.email)
        password_field.send_keys(self.password)
        repeat_password_field.send_keys(self.password)
        confirm_sign_up_button.click()

    def test_successful_message(self):
        self.sign_up_new_user()
        expected_message = "You don’t have any cars in your garage"
        actual_message_element = self.driver.find_element(By.XPATH,
                                                          "//p[text() = 'You don’t have any cars in your garage']")
        actual_message = actual_message_element.text
        assert actual_message == expected_message

    def teardown_class(self):
        sign_in_dict = {
            "email": self.email,
            "password": self.password,
            "rememberMe": False
        }

        login_url = "https://qauto2.forstudy.space/api/auth/signin"
        self.session.post(url=login_url, json=sign_in_dict)

        delete_url = "https://qauto2.forstudy.space/api/users"
        self.session.delete(url=delete_url)
        self.session.close()
        self.driver.quit()


a = 0

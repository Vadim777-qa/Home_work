from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

from Facade.registration_facade import RegistrationFacade


class TestBase:

    def setup_method(self):
        self._driver = webdriver.Chrome()
        self._session = requests.session()
        self._registration_facade = RegistrationFacade(self._driver)

        self._driver.implicitly_wait(2)
        self._driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")


class TestRegistration(TestBase):
    email = "hoearidfder@hdjs.com"
    password = "somePs45"

    def test_successful_message(self):
        self._registration_facade.sign_up_new_user("Bobster", "Monster", self.email, self.password, self.password)
        assert self._registration_facade.check_if_user_logged_in()

    def teardown_method(self):
        sign_in_dict = {
            "email": self.email,
            "password": self.password,
            "rememberMe": False
        }

        login_url = "https://qauto2.forstudy.space/api/auth/signin"
        self._session.post(url=login_url, json=sign_in_dict)

        delete_url = "https://qauto2.forstudy.space/api/users"
        self._session.delete(url=delete_url)
        self._session.close()
        self._driver.quit()


a = 0

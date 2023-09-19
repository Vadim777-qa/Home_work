from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegistrationForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.name_field = lambda: self.driver.find_element(By.ID, "signupName")
        self.last_name_field = lambda: self.driver.find_element(By.ID, "signupLastName")
        self.email_field = lambda: self.driver.find_element(By.ID, "signupEmail")
        self.password_field = lambda: self.driver.find_element(By.ID, "signupPassword")
        self.repeat_password_field = lambda: self.driver.find_element(By.ID, "signupRepeatPassword")
        self.confirm_sign_up_button = lambda: self.driver.find_element(By.XPATH, "//button[text() = 'Register']")

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class EmptyGaragePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.empty_garage_message = lambda: self.driver.find_elements(By.XPATH, "//p[text() = 'You don’t have any cars in your garage']")

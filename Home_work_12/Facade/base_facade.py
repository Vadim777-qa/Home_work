from pages.empty_garage_page import EmptyGaragePage
from pages.main_page import MainPage
from pages.registration_form_page import RegistrationForm


class BaseFacade:

    def __init__(self, driver):
        self._driver = driver
        self._main_page = MainPage(self._driver)
        self._registration_form_page = RegistrationForm(self._driver)
        self._empty_garage_page = EmptyGaragePage(self._driver)


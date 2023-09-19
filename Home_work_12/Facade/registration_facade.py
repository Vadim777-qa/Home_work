from Facade.base_facade import BaseFacade


class RegistrationFacade(BaseFacade):

    def __init__(self, driver):
        super().__init__(driver)

    def sign_up_new_user(self, name, last_name, email, password, repeat_password):
        self._main_page.sign_up_button().click()
        self._registration_form_page.name_field().send_keys(name)
        self._registration_form_page.last_name_field().send_keys(last_name)
        self._registration_form_page.email_field().send_keys(email)
        self._registration_form_page.password_field().send_keys(password)
        self._registration_form_page.repeat_password_field().send_keys(repeat_password)
        self._registration_form_page.confirm_sign_up_button().click()

    def check_if_user_logged_in(self):
        return len(self._empty_garage_page.empty_garage_message()) > 0
        # expected_message = "You don’t have any cars in your garage"
        # return expected_message == self._empty_garage_page.empty_garage_message()

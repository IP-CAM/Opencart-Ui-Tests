from locators import Login
from .BasePage import BasePage


class AdminLogin(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.path = "/admin"

    def open(self, url):
        self.driver.get(url + self.path)


    def input_username(self, text):
        self._clear_element_(Login.user_name_field)
        self._input(Login.user_name_field, value=text)


    def input_password(self, password):
        self._clear_element_(Login.password_field)
        self._input(Login.password_field, value=password)


    def submit_login(self):
        self._click(Login.login_button)

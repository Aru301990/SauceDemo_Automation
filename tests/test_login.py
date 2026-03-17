from conftest import setup
from pages.login_page import LoginPage

class Test_Login:
    def test_valid_login(self,setup):
        """Test valid login functionality."""
        login = LoginPage(setup)
        login.Login()
        assert setup.current_url == "https://www.saucedemo.com/inventory.html"

    
    def test_invalid_login(self, setup):
        login = LoginPage(setup)
        login.Login()
        error= login.get_error_message()
        assert error == "Epic sadface: Username and password do not match any user in this service"


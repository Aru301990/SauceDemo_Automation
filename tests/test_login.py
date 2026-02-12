from pages.login_page import LoginPage

class Test_Login:
    def test_valid_login(self,setup):
        """Test valid login functionality."""
        login = LoginPage(setup)
        login.Login()
        assert setup.current_url == "https://www.saucedemo.com/"

    
        
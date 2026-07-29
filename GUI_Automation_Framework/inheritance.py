class BaseTest:
    def open_browser(self):
        print("Browser Opened")
    
    def login(self):
        print("Login successful!")

    def close_browser(self):
        print("Browser closed")

class LoginTest(BaseTest):
    def test_login(self):
        print("Executing login test")

class CheckoutTest(BaseTest):
    def test_checkout(self):
        print("Executing checkout testcase")



login = LoginTest()
checkout = CheckoutTest()

login.open_browser()
login.login()
login.test_login()
login.close_browser()
 
checkout.open_browser()
checkout.login()
checkout.test_checkout()
checkout.close_browser()
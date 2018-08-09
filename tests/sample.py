from library.page_models.heroku_app.forgotten_password import HerokuForgottenPasswordPage
from library.page_models.heroku_app.navigation import HerokuNavigation
from library.selenium_driver import SeleniumDriver
from library.tools import Tools


class TestHerokuPages():


    def test_heroku_forgotten_password_page(self):

        # data
        user_email = "hello@hello.com"

        # init web driver
        web_driver = SeleniumDriver.fetch_chrome_webdriver()

        # navigation
        HerokuNavigation.navigate_to_forgotten_password(web_driver)

        #password recovery
        HerokuForgottenPasswordPage.submit_email_for_forgotten_password(web_driver, user_email)

        #verify
        HerokuForgottenPasswordPage.verify_email_forgotten(web_driver)


        SeleniumDriver.close_web_driver(web_driver)

if __name__ == "__main__":
    TestHerokuPages().test_heroku_forgotten_password_page()
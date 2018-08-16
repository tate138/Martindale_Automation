from library.selenium_actions import *
from library.tools import Tools
from library.selenium_driver import SeleniumDriver

class HerokuNavigation:

    @staticmethod
    def navigate_to_forgotten_password(web_driver):

        # nav to login
        web_driver.get("http://www.google.com")

        Tools.sleep(3)



####
#  Run
####


if __name__ == "__main__":
    HerokuNavigation.navigate_to_forgotten_password(SeleniumDriver.fetch_chrome_webdriver())

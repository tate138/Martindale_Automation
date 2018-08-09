from library.page_data.martindale_app.martindale_data import HerokuPageData
from library.selenium_actions import SeleniumActions
from library.tools import Tools


class HerokuNavigation:

    @staticmethod
    def navigate_to_forgotten_password(web_driver):

        # nav to login
        web_driver.get(HerokuPageData.URL_MAIN_PAGE)

        Tools.sleep(3)

        # act to nav to landing
        link_forgotten_password = SeleniumActions.fetch_web_element(web_driver, HerokuPageData.LINK_MAIN_PAGE_FORGOT_PASSWORD)
        SeleniumActions.click_element(web_driver, link_forgotten_password)

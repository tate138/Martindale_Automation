from library.page_data.martindale_app.martindale_data import MartindalePageData
from library.selenium_actions import SeleniumActions
from library.tools import Tools

import sys

class MartindaleLogin:

    @staticmethod
    def login_to_app(web_driver):

        try:
            # Login
            login_username = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MARTINDALE_LOGIN_USERNAME)
            SeleniumActions.write_to_element(web_driver, login_username, MartindalePageData.MARTINDALE_LOGIN_EMAIL)

            login_password = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MARTINDALE_LOGIN_PASSWORD)
            SeleniumActions.write_to_element(web_driver, login_password, MartindalePageData.MARTINDALE_LOGIN_PASS)

            button_login = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MARTINDALE_LOGIN_BUTTON)
            SeleniumActions.click_element(web_driver, button_login)

            Tools.sleep(2)

            click_pages_tab = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.PAGES_TAB_BUTTON)
            SeleniumActions.click_element(web_driver, click_pages_tab)

            Tools.sleep(2)

            if MartindalePageData.MARTINDALE_URL == "http://my.stg-martindalenolo.com/0004973/site/editor/cms":
                click_automation_edit = \
                    SeleniumActions.fetch_web_element(web_driver, MartindalePageData.AUTOMATION_PAGE_EDIT_BUTTON)
                SeleniumActions.click_element(web_driver, click_automation_edit)
            else:
                click_automation_edit = \
                    SeleniumActions.fetch_web_element(web_driver, MartindalePageData.AUTOMATION_PAGE_EDIT_BUTTON_TWO)
                SeleniumActions.click_element(web_driver, click_automation_edit)

            Tools.sleep(4)

            web_driver.close()
            web_driver.switch_to_window(web_driver.window_handles[0])

        except:
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


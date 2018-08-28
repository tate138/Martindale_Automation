from library.selenium_driver import SeleniumDriver
from library.page_data.martindale_app.martindale_data import MartindalePageData
from tests.test_model.web_data_model import WebDataModel
from testrail.testrail_api_glados import client, APIClient
from library.selenium_actions import *

import sys


class TestRailStatus:
    PASS = 1
    FAIL = 5


class CommonSetup:
    web_data_model = WebDataModel()

    # Test Rail Data
    client = APIClient(MartindalePageData.TEST_RAIL_URL)
    client.user = MartindalePageData.AUTOMATION_USER
    client.password = MartindalePageData.AUTOMATION_PW
    current_test_run_id = MartindalePageData.AUTOMATION_TEST_RUN_ID

    # Denotes module being ran
    selected_module = ""


    def fetch_webdriver(self):
        return self.web_data_model.get_web_driver()

    def close_webdriver(self):
        SeleniumDriver.close_web_driver(self.web_data_model.get_web_driver())

    def failure_message(self, test_case_number, error):
        Tools.log(test_case_number + " Not Tested")
        Tools.log("<p>Error: %s</p>" % error)

    def report_test_rail(self, test_case_number, status_id, comment):
        client.send_post('add_result_for_case/' + CommonSetup.current_test_run_id + '/' + test_case_number + '',
                         {'status_id': status_id, 'comment': comment})
        if status_id == TestRailStatus.PASS:
            Tools.log(test_case_number + " Passed")
        elif status_id == TestRailStatus.FAIL:
            Tools.log(test_case_number + " Failed")


    def common_test_teardown(self):
        try:
            web_driver = self.fetch_webdriver()

            if SeleniumActions.check_element_exists(web_driver, "//*[@id=\"se__body\"]/div[6]"):
                martindale_overlay = SeleniumActions.find_by_xpath(web_driver, MartindalePageData.MARTINDALE_OVERLAY)
                SeleniumActions.click_element(web_driver, martindale_overlay)

            try:
                web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))
            except:
                click_module = SeleniumActions.find_by_xpath(web_driver, MartindalePageData.MODULE)
                SeleniumActions.click_element(web_driver, click_module)

            Tools.sleep(2)

            delete_module_button = SeleniumActions.find_by_xpath(web_driver, MartindalePageData.DELETE_MODULE_BUTTON)
            SeleniumActions.click_element(web_driver, delete_module_button)

            Tools.sleep(2)

            if SeleniumActions.check_element_exists(web_driver,
                                                    "//*[@id=\"ple_column-0\"]/div/button/span[1]/svg/g/circle"):
                delete_module_remove_button_one = \
                    SeleniumActions.find_by_xpath(web_driver, MartindalePageData.DELETE_MODULE_REMOVE_BUTTON)
                SeleniumActions.click_element(web_driver, delete_module_remove_button_one)
            elif SeleniumActions.check_element_exists(web_driver, "/html/body/div[7]/div/form/div[3]/button[2]"):
                delete_module_remove_button_two = \
                    SeleniumActions.find_by_xpath(web_driver, MartindalePageData.DELETE_MODULE_REMOVE_BUTTON_TWO)
                SeleniumActions.click_element(web_driver, delete_module_remove_button_two)
            else:
                Tools.log("Error: Can't find the Remove button.")

            Tools.sleep(2)

            web_driver.close()

        except:
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)

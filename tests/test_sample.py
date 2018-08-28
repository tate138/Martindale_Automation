from library.page_models.martindale.martindale_module_setup import MartindaleModuleSetup
from library.page_models.martindale.martindale_login import MartindaleLogin
from library.page_models.martindale.martindale_navigation import MartindaleNavigation
from library.selenium_actions import *
from library.tools import Tools
from library.page_data.martindale_app.martindale_data import MartindalePageData
from tests.test_setup.common_setup import CommonSetup, TestRailStatus

import pytest
import sys


####
#  Call To Action Module Test
####

'''
python -m pytest "Documents/IB/Martindale Automation/tests/test_call_to_action.py" -s
'''


class TestCallToActionModuleSample(CommonSetup):

    ####
    # Suite Setup and Teardown
    ####

    @pytest.fixture(autouse=True, scope='module')
    def set_up_class(self):

        '''
        Will be run once first before any test
        '''

        web_driver = self.fetch_webdriver()

        Tools.log("Executing CTA module tests...")

        MartindaleNavigation.navigate_to_home_page(web_driver)
        MartindaleLogin.login_to_app(web_driver)
        CommonSetup.selected_module = "cta"

        MartindaleModuleSetup.module_open(web_driver)

    def teardown_class(self):

        '''
        Will be run once when all tests are complete
        '''

        Tools.log("CTA module test run complete.")

    ####
    # Case Setup and Teardown
    ####

    def case_setup(self):

        '''
        Methods that will be run to setup individual cases
        called in test as
        self.case_setup()
        '''
        global mod
        mod = TestRailStatus.PASS


    def case_teardown(self):

        '''
        Methods that will be run to cleanup individual cases
        called in test as
        self.case_teardown()
        '''

        self.common_test_teardown()


    ####
    # Test Case Setup and Teardown
    ####


    def test_c18521173(self):

        test_case_number = "18521173"

        web_driver = self.fetch_webdriver()

        try:
            click_cta_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE)
            SeleniumActions.click_element(web_driver, click_cta_module)

            Tools.sleep(3)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_MODULE_EDIT_BUTTON)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            element_path = MartindalePageData.CTA_MODULE_HEADER
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)
            cta_text = SeleniumActions.read_web_element_text(web_element)

            try:
                assert(cta_text == "CALL TO ACTION(CTA)")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            Tools.log("C18521173 Not Tested")
            e = sys.exc_info()[0]
            Tools.log("<p>Error: %s</p>" % e)



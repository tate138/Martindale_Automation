from library.page_models.martindale.martindale_module_setup import MartindaleModuleSetup
from library.page_models.martindale.martindale_login import MartindaleLogin
from library.page_models.martindale.martindale_navigation import MartindaleNavigation
from library.selenium_actions import *
from library.tools import Tools
from library.page_data.martindale_app.martindale_data import MartindalePageData
from tests.test_setup.common_setup import CommonSetup
from tests.test_model.web_data_model import WebDataModel

import pytest
import sys


####
#  Sample Module Test
####

'''
python -m pytest tests/test_banner_module.py -s
'''

class TestBannerModule(CommonSetup):

    web_data_model = WebDataModel()

    ####
    # Suite Setup and Teardown
    ####

    @pytest.fixture(autouse=True, scope='module')
    def set_up_class(self):
        '''Will be run once first before any test
        '''
        web_driver = self.fetch_webdriver()

        Tools.log("Test Suite Started")

        MartindaleNavigation.navigate_to_home_page(web_driver)
        MartindaleLogin.login_to_app(web_driver)
        MartindaleModuleSetup.cta_module_edit(web_driver)

    # will run at end of all tests
    def teardown_class(self):
        '''Will be run once when all tests are complete
        '''
        Tools.log("Test Suite Completed")
        # cannot use common setup methods, because the class is already dealloc

    ####
    # Case Setup and Teardown
    ####

    def case_setup(self):
        '''Methods that will be run to setup individual cases
        called in test as
        self.case_setup()
        '''


    def case_teardown(self):
        '''Methods that will be run to cleanup individual cases
        called in test as
        self.case_teardown()
        '''
        web_driver = self.fetch_webdriver()
        web_element = SeleniumActions.find_by_xpath(web_driver, MartindalePageData.MARTINDALE_OVERLAY)
        SeleniumActions.click_element(web_driver, web_element)

        Tools.sleep(2)

        web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

        web_element = SeleniumActions.find_by_xpath(web_driver, MartindalePageData.DELETE_MODULE_BUTTON)
        SeleniumActions.click_element(web_driver, web_element)

        Tools.sleep(2)

        web_element = SeleniumActions.find_by_xpath(web_driver, MartindalePageData.DELETE_MODULE_REMOVE_BUTTON_TWO)
        SeleniumActions.click_element(web_driver, web_element)

        Tools.sleep(2)

        web_driver.close()


    ####
    # Test Case Setup and Teardown
    ####


    def test_case_one(self):

        ####
        # Execute Test Case C18521173
        ####

        try:
            web_driver = self.fetch_webdriver()

            click_cta_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_MODULE)
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
                assert (cta_text == "CALL TO ACTION(CTA)")
                print("C18521173 Passed")
                result = CommonSetup.client.send_post(
                    'add_result_for_case/' + CommonSetup.current_test_run_id + '/18521173',
                    {'status_id': 1, 'comment': ''}
                )
            except AssertionError, e:
                print("C18521173 Failed")
                result = CommonSetup.client.send_post(
                    'add_result_for_case/' + CommonSetup.current_test_run_id + '/18521173',
                    {'status_id': 5, 'comment': ''}
                )
                print("<p>Error: %s</p>" % e)

        except:
            print("C18521173 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)



    def test_case_two(self):

        ####
        # Execute Test Case C18521175
        ####

        web_driver = self.fetch_webdriver()

        try:
            write_cta_title = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_MODULE_TITLE)
            SeleniumActions.clearTextField(web_driver, write_cta_title)
            SeleniumActions.write_to_element(web_driver, write_cta_title, "Automated Title")

            write_cta_caption = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_MODULE_CAPTION)
            SeleniumActions.clearTextField(web_driver, write_cta_caption)
            SeleniumActions.write_to_element(web_driver, write_cta_caption, "Automated Caption")

            click_done_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_MODULE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

            Tools.sleep(4)

            element_path = MartindalePageData.CTA_MODULE_TITLE_DISPLAY
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)
            cta_title_text = SeleniumActions.read_web_element_text(web_element)

            element_path = MartindalePageData.CTA_MODULE_CAPTION_DISPLAY
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)
            cta_caption_text = SeleniumActions.read_web_element_text(web_element)

            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_MODULE_EDIT_BUTTON)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            write_cta_title = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_MODULE_TITLE)
            SeleniumActions.clearTextField(web_driver, write_cta_title)
            SeleniumActions.write_to_element(web_driver, write_cta_title, "Test Title")

            write_cta_caption = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_MODULE_CAPTION)
            SeleniumActions.clearTextField(web_driver, write_cta_caption)
            SeleniumActions.write_to_element(web_driver, write_cta_caption, "Test Caption")

            click_done_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_MODULE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

            Tools.sleep(4)

            TestBannerModule().case_teardown()

            try:
                assert (cta_title_text == "Automated Title" and cta_caption_text == "Automated Caption")
                print("C18521175 Passed")
                result = CommonSetup.client.send_post(
                    'add_result_for_case/' + CommonSetup.current_test_run_id + '/18521175',
                    {'status_id': 1, 'comment': ''}
                )
            except AssertionError, e:
                print("C18521175 Failed")
                result = CommonSetup.client.send_post(
                    'add_result_for_case/' + CommonSetup.current_test_run_id + '/18521175',
                    {'status_id': 5, 'comment': ''}
                )
                print("<p>Error: %s</p>" % e)


        except:
            print("C18521175 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


if __name__ == "__main__":
    TestBannerModule().set_up_class()
    TestBannerModule().test_case_one()
    TestBannerModule().test_case_two()
    TestBannerModule().teardown_class()
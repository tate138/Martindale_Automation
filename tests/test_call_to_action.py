from library.page_models.martindale.martindale_module_setup import MartindaleModuleSetup
from library.page_models.martindale.martindale_login import MartindaleLogin
from library.page_models.martindale.martindale_navigation import MartindaleNavigation
from library.selenium_actions import *
from library.tools import Tools
from library.page_data.martindale_app.cta_module_data import CtaModuleData
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


class TestCallToActionModule(CommonSetup):

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
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.IFRAME_EDIT_BUTTON)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            element_path = CtaModuleData.CTA_MODULE_HEADER
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


    def test_c18521175(self):

        test_case_number = "18521175"

        web_driver = self.fetch_webdriver()

        try:
            write_cta_title = \
                SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_MODULE_TITLE)
            SeleniumActions.clearTextField(web_driver, write_cta_title)
            SeleniumActions.write_to_element(web_driver, write_cta_title, "Automated Title")

            write_cta_caption = \
                SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_MODULE_CAPTION)
            SeleniumActions.clearTextField(web_driver, write_cta_caption)
            SeleniumActions.write_to_element(web_driver, write_cta_caption, "Automated Caption")

            click_done_button = \
                SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_MODULE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

            Tools.sleep(4)

            element_path = CtaModuleData.CTA_MODULE_TITLE_DISPLAY
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)
            cta_title_text = SeleniumActions.read_web_element_text(web_element)

            element_path = CtaModuleData.CTA_MODULE_CAPTION_DISPLAY
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)
            cta_caption_text = SeleniumActions.read_web_element_text(web_element)

            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.IFRAME_EDIT_BUTTON)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            write_cta_title = \
                SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_MODULE_TITLE)
            SeleniumActions.clearTextField(web_driver, write_cta_title)
            SeleniumActions.write_to_element(web_driver, write_cta_title, "Test Title")

            write_cta_caption = \
                SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_MODULE_CAPTION)
            SeleniumActions.clearTextField(web_driver, write_cta_caption)
            SeleniumActions.write_to_element(web_driver, write_cta_caption, "Test Caption")

            click_done_button = \
                SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_MODULE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

            Tools.sleep(4)

            try:
                assert(cta_title_text == "Automated Title" and cta_caption_text == "Automated Caption")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521175 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521178(self):

        test_case_number = "18521178"

        web_driver = self.fetch_webdriver()

        try:
            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.IFRAME_EDIT_BUTTON)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            # CTA Button One

            element_path = CtaModuleData.CTA_MODULE_BUTTON_ONE_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "0")

            Tools.sleep(1)

            element_path = CtaModuleData.CTA_MODULE_LINK_PAGE_ONE_DROP_DOWN
            link_page_one_drop_down = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, link_page_one_drop_down))
                test_one = "Passed"
            except AssertionError:
                test_one = "Failed"
                print("<p>Error: %s</p>")

            element_path = CtaModuleData.CTA_MODULE_BUTTON_ONE_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "1")

            Tools.sleep(1)

            element_path = CtaModuleData.CTA_MODULE_EXTERNAL_URL_ONE
            url_one = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, url_one))
                test_two = "Passed"
            except AssertionError:
                test_two = "Failed"
                print("<p>Error: %s</p>")

            element_path = CtaModuleData.CTA_MODULE_BUTTON_ONE_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "2")

            Tools.sleep(1)

            element_path = CtaModuleData.CTA_MODULE_PHONE_NUMBER_ONE
            phone_number = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, phone_number))
                test_three = "Passed"
            except AssertionError:
                test_three = "Failed"
                print("<p>Error: %s</p>")

            element_path = CtaModuleData.CTA_MODULE_BUTTON_ONE_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "3")

            Tools.sleep(1)

            try:
                assert(SeleniumActions.element_is_not_visible(link_page_one_drop_down) and
                       SeleniumActions.element_is_not_visible(url_one) and
                       SeleniumActions.element_is_not_visible(phone_number))
                test_four = "Passed"
            except AssertionError:
                test_four = "Failed"
                print("<p>Error: %s</p>")


            # CTA Button Two

            element_path = CtaModuleData.CTA_MODULE_TWO_BUTTON_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "0")

            Tools.sleep(1)

            element_path = CtaModuleData.CTA_MODULE_LINK_PAGE_TWO_DROP_DOWN
            link_page_two_drop_down = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, link_page_two_drop_down))
                test_five = "Passed"
            except AssertionError:
                test_five = "Failed"
                print("<p>Error: %s</p>")

            element_path = CtaModuleData.CTA_MODULE_TWO_BUTTON_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "1")

            Tools.sleep(1)

            element_path = CtaModuleData.CTA_MODULE_EXTERNAL_URL_TWO
            url_two = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, url_two))
                test_six = "Passed"
            except AssertionError:
                test_six = "Failed"
                print("<p>Error: %s</p>")

            element_path = CtaModuleData.CTA_MODULE_TWO_BUTTON_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "2")

            Tools.sleep(1)

            element_path = CtaModuleData.CTA_MODULE_PHONE_NUMBER_TWO
            phone_number_two = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, phone_number_two))
                test_seven = "Passed"
            except AssertionError:
                test_seven = "Failed"
                print("<p>Error: %s</p>")

            element_path = CtaModuleData.CTA_MODULE_TWO_BUTTON_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "3")

            Tools.sleep(1)

            try:
                assert(SeleniumActions.element_is_not_visible(link_page_two_drop_down) and
                       SeleniumActions.element_is_not_visible(url_two) and
                       SeleniumActions.element_is_not_visible(phone_number_two))
                test_eight = "Passed"
            except AssertionError:
                test_eight = "Failed"
                print("<p>Error: %s</p>")

            if test_one == "Passed" and test_two == "Passed" and test_three == "Passed" and test_four == "Passed" and \
                    test_five == "Passed" and test_six == "Passed" and test_seven == "Passed" and test_eight == "Passed":
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            else:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521178 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521180(self):

        test_case_number = "18521180"

        web_driver = self.fetch_webdriver()

        try:
            # CTA Button One

            element_path = CtaModuleData.CTA_MODULE_ONE_LINK_APPEARANCE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "1")

            Tools.sleep(1)

            element_path = CtaModuleData.CTA_MODULE_BUTTON_TEXT_BOX_ONE
            button_text_box_one = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, button_text_box_one))
                test_one = "Passed"
            except AssertionError:
                test_one = "Failed"
                print("<p>Error: %s</p>")

            element_path = CtaModuleData.CTA_MODULE_ONE_LINK_APPEARANCE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "2")

            Tools.sleep(1)

            element_path = CtaModuleData.CTA_MODULE_SELECT_ICON_ONE
            select_icon_one = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, select_icon_one))
                test_two = "Passed"
            except AssertionError:
                test_two = "Failed"
                print("<p>Error: %s</p>")

            element_path = CtaModuleData.CTA_MODULE_ONE_LINK_APPEARANCE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "3")

            Tools.sleep(1)

            element_path = CtaModuleData.CTA_MODULE_BUTTON_TEXT_BOX_ONE
            link_text_one = SeleniumActions.find_by_xpath(web_driver, element_path)

            element_path = CtaModuleData.CTA_MODULE_SELECT_ICON_ONE
            select_icon_one = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, link_text_one)
                       and SeleniumActions.element_is_visible(web_driver, select_icon_one))
                test_three = "Passed"
            except AssertionError:
                test_three = "Failed"
                print("<p>Error: %s</p>")

            element_path = CtaModuleData.CTA_MODULE_ONE_LINK_APPEARANCE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "0")

            Tools.sleep(1)

            element_path = CtaModuleData.CTA_MODULE_BUTTON_TEXT_BOX_ONE
            link_text_one = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, link_text_one))
                test_four = "Passed"
            except AssertionError:
                test_four = "Failed"
                print("<p>Error: %s</p>")

            # CTA Button Two

            element_path = CtaModuleData.CTA_MODULE_TWO_LINK_APPEARANCE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "1")

            Tools.sleep(1)

            element_path = CtaModuleData.CTA_MODULE_BUTTON_TEXT_BOX_TWO
            button_text_box_two = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, button_text_box_two))
                test_five = "Passed"
            except AssertionError:
                test_five = "Failed"
                print("<p>Error: %s</p>")

            element_path = CtaModuleData.CTA_MODULE_TWO_LINK_APPEARANCE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "2")

            Tools.sleep(1)

            element_path = CtaModuleData.CTA_MODULE_SELECT_ICON_TWO
            select_icon_two = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, select_icon_two))
                test_six = "Passed"
            except AssertionError:
                test_six = "Failed"
                print("<p>Error: %s</p>")

            element_path = CtaModuleData.CTA_MODULE_TWO_LINK_APPEARANCE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "3")

            Tools.sleep(2)

            element_path = CtaModuleData.CTA_MODULE_BUTTON_TEXT_BOX_TWO
            button_text_box_two = SeleniumActions.find_by_xpath(web_driver, element_path)

            element_path = CtaModuleData.CTA_MODULE_SELECT_ICON_TWO
            select_icon_two = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, button_text_box_two)
                       and SeleniumActions.element_is_visible(web_driver, select_icon_two))
                test_seven = "Passed"
            except AssertionError:
                test_seven = "Failed"
                print("<p>Error: %s</p>")

            element_path = CtaModuleData.CTA_MODULE_TWO_LINK_APPEARANCE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "0")

            Tools.sleep(1)

            element_path = CtaModuleData.CTA_MODULE_LINK_TEXT_BOX_TWO
            link_text_two = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, link_text_two))
                test_eight = "Passed"
            except AssertionError:
                test_eight = "Failed"
                print("<p>Error: %s</p>")

            if test_one == "Passed" and test_two == "Passed" and test_three == "Passed" and test_four == "Passed" and \
                    test_five == "Passed" and test_six == "Passed" and test_seven == "Passed" and test_eight == "Passed":
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            else:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521180 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521174(self):

        test_case_number = "18521174"

        web_driver = self.fetch_webdriver()

        try:
            write_link_text_two = \
                SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_MODULE_LINK_TEXT_BOX_TWO)
            SeleniumActions.clearTextField(web_driver, write_link_text_two)
            SeleniumActions.write_to_element(web_driver, write_link_text_two, "Legalize Ferrets")

            click_settings_tab = SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            cta_settings_button_one = \
                SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_SETTINGS_SHOW_BUTTON_ONE)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, cta_settings_button_one))
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521174 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521182(self):

        test_case_number = "18521182"

        web_driver = self.fetch_webdriver()

        try:
            # Link One

            click_cta_settings_button_one = \
                SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_SETTINGS_SHOW_BUTTON_ONE)
            SeleniumActions.click_element(web_driver, click_cta_settings_button_one)

            click_done_button = \
                SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_MODULE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

            Tools.sleep(5)

            element_path = CtaModuleData.CTA_MODULE_LINK_DISPLAY
            link_display_one = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, link_display_one))
                test_one = "Passed"
            except AssertionError:
                test_one = "Failed"
                print("<p>Error: %s</p>")

            # Link Two

            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.IFRAME_EDIT_BUTTON)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            click_settings_tab = SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            click_cta_settings_button_one = \
                SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_SETTINGS_SHOW_BUTTON_ONE)
            SeleniumActions.click_element(web_driver, click_cta_settings_button_one)

            click_cta_settings_button_two = \
                SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_SETTINGS_SHOW_BUTTON_TWO)
            SeleniumActions.click_element(web_driver, click_cta_settings_button_two)

            click_done_button = \
                SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_MODULE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

            Tools.sleep(5)

            element_path = CtaModuleData.CTA_MODULE_LINK_DISPLAY
            link_display_one = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, link_display_one))
                test_two = "Passed"
            except AssertionError:
                test_two = "Failed"
                print("<p>Error: %s</p>")

            if test_one == "Passed" and test_two == "Passed":
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            else:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521182 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521230(self):

        test_case_number = "18521230"

        web_driver = self.fetch_webdriver()

        try:
            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.IFRAME_EDIT_BUTTON)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            click_settings_tab = SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            click_cta_settings_button_two = \
                SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_SETTINGS_SHOW_BUTTON_TWO)
            SeleniumActions.click_element(web_driver, click_cta_settings_button_two)

            click_content_tab = SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_CONTENT_TAB)
            SeleniumActions.click_element(web_driver, click_content_tab)

            element_path = CtaModuleData.CTA_MODULE_TWO_LINK_APPEARANCE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except AssertionError:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521230 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521191(self):

        test_case_number = "18521191"

        web_driver = self.fetch_webdriver()

        try:

            click_settings_tab = SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            click_show_title = SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_SETTINGS_SHOW_TITLE)
            SeleniumActions.click_element(web_driver, click_show_title)

            click_done_button = \
                SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_MODULE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

            Tools.sleep(5)

            try:
                assert(SeleniumActions.check_element_exists(web_driver, "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div/div/h3"))
                test_one = "Failed"
            except:
                test_one = "Passed"

            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.IFRAME_EDIT_BUTTON)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            click_settings_tab = SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            click_show_title = SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_SETTINGS_SHOW_TITLE)
            SeleniumActions.click_element(web_driver, click_show_title)

            click_done_button = \
                SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_MODULE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

            Tools.sleep(5)

            try:
                assert(SeleniumActions.check_element_exists(web_driver, "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div/div/h3"))
                test_two = "Passed"
            except:
                test_two = "Failed"

            if test_one == "Passed" and test_two == "Passed":
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            else:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521191 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521192(self):

        test_case_number = "18521192"

        web_driver = self.fetch_webdriver()

        try:

            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.IFRAME_EDIT_BUTTON)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            click_settings_tab = SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            click_show_title = SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_SETTINGS_SHOW_CAPTION)
            SeleniumActions.click_element(web_driver, click_show_title)

            click_done_button = \
                SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_MODULE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

            Tools.sleep(5)

            try:
                assert(SeleniumActions.check_element_exists(web_driver, "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div/div/h4"))
                test_one = "Failed"
            except:
                test_one = "Passed"

            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.IFRAME_EDIT_BUTTON)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            click_settings_tab = SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            click_show_title = SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_SETTINGS_SHOW_CAPTION)
            SeleniumActions.click_element(web_driver, click_show_title)

            click_done_button = \
                SeleniumActions.fetch_web_element(web_driver, CtaModuleData.CTA_MODULE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

            Tools.sleep(5)

            try:
                assert(SeleniumActions.check_element_exists(web_driver, "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div/div/h3"))
                test_two = "Passed"
            except:
                test_two = "Failed"

            if test_one == "Passed" and test_two == "Passed":
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            else:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

            self.case_teardown()

        except:
            print("C18521192 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)

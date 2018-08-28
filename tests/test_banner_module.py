from library.page_models.martindale.martindale_module_setup import MartindaleModuleSetup
from library.page_models.martindale.martindale_login import MartindaleLogin
from library.page_models.martindale.martindale_navigation import MartindaleNavigation
from library.selenium_actions import *
from library.tools import Tools
from library.page_data.martindale_app.banner_module_data import BannerModuleData
from library.page_data.martindale_app.martindale_data import MartindalePageData
from tests.test_setup.common_setup import CommonSetup, TestRailStatus

import pytest
import sys

####
#  Banner Module Test
####

'''
python -m pytest "Documents/IB/Martindale Automation/tests/test_banner_module.py" -s
'''


class TestBannerModule(CommonSetup):

    ####
    # Suite Setup and Teardown
    ####

    @pytest.fixture(autouse=True, scope='module')
    def set_up_class(self):

        '''
        Will be run once first before any test
        '''

        web_driver = self.fetch_webdriver()

        Tools.log("Executing Banner module tests...")

        MartindaleNavigation.navigate_to_home_page(web_driver)
        MartindaleLogin.login_to_app(web_driver)
        CommonSetup.selected_module = "banner"
        MartindaleModuleSetup.module_open(web_driver)

    # will run at end of all tests
    def teardown_class(self):

        '''
        Will be run once when all tests are complete
        '''

        Tools.log("Banner module test run complete.")


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


    def test_c18513007(self):

        test_case_number = "18513007"

        web_driver = self.fetch_webdriver()

        try:
            click_banner_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE)
            SeleniumActions.click_element(web_driver, click_banner_module)

            Tools.sleep(2)

            click_banner_name = \
                SeleniumActions.fetch_web_element(web_driver, BannerModuleData.BANNER_MODULE_HEADER)
            SeleniumActions.click_element(web_driver, click_banner_name)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.IFRAME_EDIT_BUTTON)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            element_path = BannerModuleData.GALLERY_BANNER_TITLE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            banner_text = SeleniumActions.read_web_element_text(web_element)

            try:
                assert(banner_text == "BANNER MODULE")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18513007 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18513008(self):

        test_case_number = "18513008"

        web_driver = self.fetch_webdriver()

        try:
            click_settings_tab = \
                SeleniumActions.fetch_web_element(web_driver, BannerModuleData.BANNER_MODULE_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            element_path = BannerModuleData.BANNER_MODULE_SETTINGS_ELEMENT_VISIBILITY
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            element_visibility_text = SeleniumActions.read_web_element_text(web_element)

            click_layout_tab = \
                SeleniumActions.fetch_web_element(web_driver, BannerModuleData.BANNER_MODULE_LAYOUT_TAB)
            SeleniumActions.click_element(web_driver, click_layout_tab)

            element_path = BannerModuleData.BANNER_MODULE_LAYOUT_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            layout_type_text = SeleniumActions.read_web_element_text(web_element)

            click_content_tab = \
                SeleniumActions.fetch_web_element(web_driver, BannerModuleData.BANNER_MODULE_CONTENT_TAB)
            SeleniumActions.click_element(web_driver, click_content_tab)

            element_path = BannerModuleData.BANNER_MODULE_CONENT_MANAGE_CONTENT
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            manage_content_text = SeleniumActions.read_web_element_text(web_element)

            try:
                assert(element_visibility_text == "ELEMENT VISIBILITY"
                       and layout_type_text == "LAYOUT TYPE"
                       and manage_content_text == "Manage Content")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18513008 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521018(self):

        test_case_number = "18521018"

        web_driver = self.fetch_webdriver()

        try:
            click_add_banner = \
                SeleniumActions.fetch_web_element(web_driver, BannerModuleData.BANNER_MODULE_CONTENT_ADD_BANNER_BUTTON)
            SeleniumActions.click_element(web_driver, click_add_banner)

            Tools.sleep(5)

            element_path = BannerModuleData.BANNER_MODULE_CONTENT_ADD_BANNER
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            add_banner_text = SeleniumActions.read_web_element_text(web_element)

            try:
                assert(add_banner_text == "ADD BANNER")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521018 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521037(self):

        test_case_number = "18521037"

        web_driver = self.fetch_webdriver()

        try:
            # CTA Button 1
            element_path = BannerModuleData.BANNER_MODULE_CONTENT_ADD_LINK_APPEARANCE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "0")

            link_text = SeleniumActions.read_select_text(web_element)

            SeleniumActions.select_by_index(web_element, "1")

            button_text = SeleniumActions.read_select_text(web_element)

            SeleniumActions.select_by_index(web_element, "2")

            icon_only = SeleniumActions.read_select_text(web_element)

            SeleniumActions.select_by_index(web_element, "3")

            icon_and_button = SeleniumActions.read_select_text(web_element)

            # CTA Button 2
            element_path = BannerModuleData.BANNER_MODULE_CONTENT_ADD_LINK_APPEARANCE_TWO
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            Tools.sleep(2)

            SeleniumActions.select_by_index(web_element, "0")

            link_text_two = SeleniumActions.read_select_text(web_element)

            SeleniumActions.select_by_index(web_element, "1")

            button_text_two = SeleniumActions.read_select_text(web_element)

            SeleniumActions.select_by_index(web_element, "2")

            icon_only_two = SeleniumActions.read_select_text(web_element)

            SeleniumActions.select_by_index(web_element, "3")

            icon_and_button_two = SeleniumActions.read_select_text(web_element)

            try:
                assert(link_text == "Text Link" and button_text == "Text Button" and icon_only == "Icon Only"
                       and icon_and_button == "Icon & Text Button" and link_text_two == "Text Link"
                       and button_text_two == "Text Button" and icon_only_two == "Icon Only"
                       and icon_and_button_two == "Icon & Text Button")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521037 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521024(self):

        test_case_number = "18521024"

        web_driver = self.fetch_webdriver()

        try:
            # CTA Button 1
            element_path = BannerModuleData.BANNER_MODULE_CONTENT_ADD_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            Tools.sleep(2)

            SeleniumActions.select_by_index(web_element, "0")

            my_pages = SeleniumActions.read_select_text(web_element)

            SeleniumActions.select_by_index(web_element, "1")

            external_link = SeleniumActions.read_select_text(web_element)

            SeleniumActions.select_by_index(web_element, "2")

            no_link = SeleniumActions.read_select_text(web_element)

            # CTA Button 2
            element_path = BannerModuleData.BANNER_MODULE_CONTENT_ADD_LINK_TYPE_TWO
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            Tools.sleep(2)

            SeleniumActions.select_by_index(web_element, "0")

            my_pages_two = SeleniumActions.read_select_text(web_element)

            SeleniumActions.select_by_index(web_element, "1")

            external_link_two = SeleniumActions.read_select_text(web_element)

            SeleniumActions.select_by_index(web_element, "2")

            no_link_two = SeleniumActions.read_select_text(web_element)

            try:
                assert(my_pages == "My Pages" and external_link == "External Link" and no_link == "No Link"
                       and my_pages_two == "My Pages" and external_link_two == "External Link"
                       and no_link_two == "No Link")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521024 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521040(self):

        test_case_number = "18521040"

        web_driver = self.fetch_webdriver()

        try:
            # CTA Button 1
            element_path = BannerModuleData.BANNER_MODULE_CONTENT_ADD_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "0")

            Tools.sleep(2)

            element_path = BannerModuleData.BANNER_MODULE_CONTENT_ADD_LINK_PAGE_LABEL
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            link_page_element = SeleniumActions.read_web_element_text(web_element)

            # CTA Button 2
            element_path = BannerModuleData.BANNER_MODULE_CONTENT_ADD_LINK_TYPE_TWO
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "0")

            Tools.sleep(2)

            element_path = BannerModuleData.BANNER_MODULE_CONTENT_ADD_LINK_PAGE_LABEL_TWO
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            link_page_element_two = SeleniumActions.read_web_element_text(web_element)

            try:
                assert(link_page_element == "Link Page *" and link_page_element_two == "Link Page *")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521040 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521041(self):

        test_case_number = "18521041"

        web_driver = self.fetch_webdriver()

        try:
            # CTA Button 1
            element_path = BannerModuleData.BANNER_MODULE_CONTENT_ADD_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "1")

            Tools.sleep(2)

            element_path = BannerModuleData.BANNER_MODULE_CONTENT_ADD_LINK_PAGE_URL_LABEL
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            link_page_element = SeleniumActions.read_web_element_text(web_element)

            # CTA Button 2
            element_path = BannerModuleData.BANNER_MODULE_CONTENT_ADD_LINK_TYPE_TWO
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "1")

            Tools.sleep(2)

            element_path = BannerModuleData.BANNER_MODULE_CONTENT_ADD_LINK_PAGE_URL_LABEL_TWO
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            link_page_element_two = SeleniumActions.read_web_element_text(web_element)

            try:
                assert(link_page_element == "URL *" and link_page_element_two == "URL *")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521041 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521042(self):

        test_case_number = "18521042"

        web_driver = self.fetch_webdriver()

        try:
            click_save_button = \
                SeleniumActions.fetch_web_element(web_driver, BannerModuleData.ADD_BANNER_SAVE_BUTTON)
            SeleniumActions.click_element(web_driver, click_save_button)

            element_path = BannerModuleData.BANNER_TITLE_ERROR
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            banner_title_error = SeleniumActions.read_web_element_text(web_element)

            element_path = BannerModuleData.BANNER_CAPTION_ERROR
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            banner_caption_error = SeleniumActions.read_web_element_text(web_element)

            banner_title = SeleniumActions.fetch_web_element(web_driver, BannerModuleData.BANNER_TITLE)
            SeleniumActions.write_to_element \
                (web_driver, banner_title, "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ012")

            banner_caption = SeleniumActions.fetch_web_element(web_driver, BannerModuleData.BANNER_CAPTION)
            SeleniumActions.write_to_element \
                (web_driver, banner_caption, "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ012ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ012")

            click_save_button = \
                SeleniumActions.fetch_web_element(web_driver, BannerModuleData.ADD_BANNER_SAVE_BUTTON)
            SeleniumActions.click_element(web_driver, click_save_button)

            element_path = BannerModuleData.BANNER_TITLE_ERROR
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            banner_title_error_two = SeleniumActions.read_web_element_text(web_element)

            element_path = BannerModuleData.BANNER_CAPTION_ERROR
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            banner_caption_error_two = SeleniumActions.read_web_element_text(web_element)

            try:
                assert(banner_title_error == "This field is required."
                       and banner_caption_error == "This field is required."
                       and banner_title_error_two == "Please enter no more than 100 characters."
                       and banner_caption_error_two == "Please enter no more than 200 characters.")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521042 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521043(self):

        test_case_number = "18521043"

        web_driver = self.fetch_webdriver()

        try:
            banner_title = SeleniumActions.fetch_web_element(web_driver, BannerModuleData.BANNER_TITLE)
            SeleniumActions.clearTextField(web_driver, banner_title)
            SeleniumActions.write_to_element(web_driver, banner_title, "Automated")

            banner_caption = SeleniumActions.fetch_web_element(web_driver, BannerModuleData.BANNER_CAPTION)
            SeleniumActions.clearTextField(web_driver, banner_caption)
            SeleniumActions.write_to_element(web_driver, banner_caption, "Test")

            click_save_button = \
                SeleniumActions.fetch_web_element(web_driver, BannerModuleData.ADD_BANNER_SAVE_BUTTON)
            SeleniumActions.click_element(web_driver, click_save_button)
            Tools.sleep(4)

            web_element = SeleniumActions.find_by_xpath(web_driver, "//*[contains(@id, 'item_item-')]")
            new_banner_test = SeleniumActions.read_web_element_text(web_element)

            try:
                assert(new_banner_test == "Title: Automated\nTest")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521043 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521045(self):

        test_case_number = "18521045"

        web_driver = self.fetch_webdriver()

        try:
            web_element = SeleniumActions.find_by_xpath(web_driver, "//*[contains(@id, 'edit_item-')]")
            SeleniumActions.click_element(web_driver, web_element)

            Tools.sleep(3)

            banner_title = SeleniumActions.fetch_web_element(web_driver, BannerModuleData.BANNER_TITLE)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, banner_title))
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521045 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521044(self):

        test_case_number = "18521044"

        web_driver = self.fetch_webdriver()

        try:
            web_element = SeleniumActions.find_by_xpath(web_driver, BannerModuleData.ADD_BANNER_CANCEL_BUTTON)
            SeleniumActions.click_element(web_driver, web_element)

            Tools.sleep(3)

            element_path = BannerModuleData.GALLERY_BANNER_TITLE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521044 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521046(self):

        test_case_number = "18521046"

        web_driver = self.fetch_webdriver()

        try:
            web_element = SeleniumActions.find_by_xpath(web_driver, "//*[contains(@id, 'delete_item-')]")
            SeleniumActions.click_element(web_driver, web_element)

            Tools.sleep(2)

            web_element = SeleniumActions.find_by_xpath(web_driver, BannerModuleData.DELETE_BANNER_CONFIRMATION)
            SeleniumActions.element_is_visible(web_driver, web_element)

            web_element = SeleniumActions.find_by_xpath(web_driver, BannerModuleData.DELETE_BANNER_CANCEL_BUTTON)
            SeleniumActions.click_element(web_driver, web_element)

            Tools.sleep(2)

            web_element = SeleniumActions.find_by_xpath(web_driver, "//*[contains(@id, 'item_item-')]")
            SeleniumActions.element_is_visible(web_driver, web_element)

            web_element = SeleniumActions.find_by_xpath(web_driver, "//*[contains(@id, 'delete_item-')]")
            SeleniumActions.click_element(web_driver, web_element)

            Tools.sleep(2)

            web_element = SeleniumActions.find_by_xpath(web_driver, BannerModuleData.DELETE_BANNER_OK_BUTTON)
            SeleniumActions.click_element(web_driver, web_element)

            Tools.sleep(4)

            web_element = SeleniumActions.find_by_xpath(web_driver, "//*[contains(@id, 'item_item-')]")
            new_banner_test = SeleniumActions.read_web_element_text(web_element)

            try:
                assert(new_banner_test == "Title: Title\nCaption")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

            self.case_teardown()

        except:
            print("C18521230 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


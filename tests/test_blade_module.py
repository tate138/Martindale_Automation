from library.page_models.martindale.martindale_module_setup import MartindaleModuleSetup
from library.page_models.martindale.martindale_login import MartindaleLogin
from library.page_models.martindale.martindale_navigation import MartindaleNavigation
from library.selenium_actions import *
from library.tools import Tools
from library.page_data.martindale_app.blade_module_data import BladeModuleData
from library.page_data.martindale_app.martindale_data import MartindalePageData
from tests.test_setup.common_setup import CommonSetup, TestRailStatus

import pytest
import sys

####
#  Blade Module Test
####

'''
python -m pytest "Documents/IB/Martindale Automation/tests/test_blade_module.py" -s
'''

class TestBladeModule(CommonSetup):

    ####
    # Suite Setup and Teardown
    ####

    @pytest.fixture(autouse=True, scope='module')
    def set_up_class(self):

        '''
        Will be run once first before any test
        '''

        web_driver = self.fetch_webdriver()

        Tools.log("Executing Blade module tests...")

        MartindaleNavigation.navigate_to_home_page(web_driver)
        MartindaleLogin.login_to_app(web_driver)
        CommonSetup.selected_module = "blade"
        MartindaleModuleSetup.module_open(web_driver)

    # will run at end of all tests
    def teardown_class(self):

        '''
        Will be run once when all tests are complete
        '''
        Tools.log("Blade module test run complete.")


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

    def test_c18527973(self):

        test_case_number = "18527973"

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
            element_path = BladeModuleData.BLADE_TITLE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            blade_text = SeleniumActions.read_web_element_text(web_element)

            try:
                assert(blade_text == "BLADE MODULE")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18527973 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18527974(self):

        test_case_number = "18527974"

        web_driver = self.fetch_webdriver()

        try:
            click_settings_tab = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            Tools.sleep(2)

            element_path = BladeModuleData.BLADE_SETTINGS_ELEMENT_VISIBILITY
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            settings_element_visibility = SeleniumActions.read_web_element_text(web_element)

            element_path = BladeModuleData.BLADE_SETTINGS_SETTINGS
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            settings_settings = SeleniumActions.read_web_element_text(web_element)

            element_path = BladeModuleData.BLADE_SETTINGS_MODULE_VISIBILITY
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            settings_module_visibility = SeleniumActions.read_web_element_text(web_element)

            try:
                assert(settings_element_visibility == "ELEMENT VISIBILITY"
                       and settings_settings == "BLADE SETTINGS"
                       and settings_module_visibility == "MODULE VISIBILITY")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

            test_case_number = "18527997"

            try:
                assert(settings_element_visibility == "ELEMENT VISIBILITY"
                       and settings_settings == "BLADE SETTINGS"
                       and settings_module_visibility == "MODULE VISIBILITY")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18527974 Not Tested")
            print("C18527997 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18527975(self):

        test_case_number = "18527975"

        web_driver = self.fetch_webdriver()

        try:
            click_content_tab = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_TAB)
            SeleniumActions.click_element(web_driver, click_content_tab)

            Tools.sleep(2)

            write_new_title = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_TITLE)
            SeleniumActions.clearTextField(web_driver, write_new_title)
            SeleniumActions.write_to_element \
                (web_driver, write_new_title, "Blade")

            write_new_caption = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_CAPTION)
            SeleniumActions.clearTextField(web_driver, write_new_caption)
            SeleniumActions.write_to_element \
                (web_driver, write_new_caption, "Runner")

            write_new_alt_text = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_ALT_TEXT)
            SeleniumActions.clearTextField(web_driver, write_new_alt_text)
            SeleniumActions.write_to_element \
                (web_driver, write_new_alt_text, "alt")

            write_new_image_title = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_IMAGE_TITLE)
            SeleniumActions.clearTextField(web_driver, write_new_image_title)
            SeleniumActions.write_to_element \
                (web_driver, write_new_image_title, "image")

            write_new_cta_one_link_text = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_CTA_ONE_LINK_TEXT)
            SeleniumActions.clearTextField(web_driver, write_new_cta_one_link_text)
            SeleniumActions.write_to_element \
                (web_driver, write_new_cta_one_link_text, "CTA One")

            write_new_cta_two_link_text = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_CTA_TWO_LINK_TEXT)
            SeleniumActions.clearTextField(web_driver, write_new_cta_two_link_text)
            SeleniumActions.write_to_element \
                (web_driver, write_new_cta_two_link_text, "CTA Two")

            click_done_button = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            Tools.sleep(5)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

            element_path = BladeModuleData.BLADE_IFRAME_TITLE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            blade_iframe_title = SeleniumActions.read_web_element_text(web_element)

            element_path = BladeModuleData.BLADE_IFRAME_CAPTION
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            blade_iframe_caption = SeleniumActions.read_web_element_text(web_element)

            try:
                assert(blade_iframe_title == "Blade" and blade_iframe_caption == "Runner")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18527975 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18678388(self):

        test_case_number = "18678388"

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

            click_settings_tab = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            click_show_banner_title = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_SHOW_BLADE_TITLE)
            SeleniumActions.click_element(web_driver, click_show_banner_title)

            click_done_button = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            Tools.sleep(5)
            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

            try:
                assert(SeleniumActions.check_element_exists(web_driver, "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div/div[1]/div[1]/h3"))
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

            click_settings_tab = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            click_show_banner_title = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_SHOW_BLADE_TITLE)
            SeleniumActions.click_element(web_driver, click_show_banner_title)

            click_done_button = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            Tools.sleep(5)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

            Tools.sleep(2)

            web_element = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_IFRAME_TITLE)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                test_two = "Passed"
            except:
                test_two = "Failed"

            if test_one == "Passed" and test_two == "Passed":
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            else:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18678388 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18678389(self):

        test_case_number = "18678389"

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

            click_settings_tab = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            click_show_banner_title = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_SHOW_BLADE_TITLE)
            SeleniumActions.click_element(web_driver, click_show_banner_title)

            click_show_banner_caption = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_SHOW_BLADE_CAPTION)
            SeleniumActions.click_element(web_driver, click_show_banner_caption)

            click_done_button = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            Tools.sleep(5)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

            try:
                assert(SeleniumActions.check_element_exists(web_driver, "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div/div[1]/div[1]/h4"))
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

            click_settings_tab = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            click_show_banner_title = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_SHOW_BLADE_TITLE)
            SeleniumActions.click_element(web_driver, click_show_banner_title)

            click_show_banner_caption = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_SHOW_BLADE_CAPTION)
            SeleniumActions.click_element(web_driver, click_show_banner_caption)

            click_done_button = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            Tools.sleep(5)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

            Tools.sleep(2)

            web_element = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_IFRAME_CAPTION)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                test_two = "Passed"
            except:
                test_two = "Failed"

            if test_one == "Passed" and test_two == "Passed":
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            else:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18678389 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)

    def test_c18678390(self):

        test_case_number = "18678390"

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

            click_settings_tab = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            click_show_banner_caption = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_SHOW_BLADE_CAPTION)
            SeleniumActions.click_element(web_driver, click_show_banner_caption)

            click_show_read_more = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_SHOW_READ_MORE)
            SeleniumActions.click_element(web_driver, click_show_read_more)

            click_done_button = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            Tools.sleep(5)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

            if SeleniumActions.check_element_exists \
                        (web_driver, "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div/div[1]/div[2]/a"):
                blade_title_existence = "true"
            else:
                blade_title_existence = "false"

            try:
                assert(blade_title_existence == "false")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18678390 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18678391(self):

        test_case_number = "18678391"

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

            click_settings_tab = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)
            click_show_read_more = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_SHOW_READ_MORE)
            SeleniumActions.click_element(web_driver, click_show_read_more)

            click_show_cta_button_one = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_SHOW_CTA_ONE)
            SeleniumActions.click_element(web_driver, click_show_cta_button_one)
            click_done_button = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            Tools.sleep(5)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

            element_path = BladeModuleData.BLADE_IFRAME_CTA_BUTTON_TWO
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)
            read_cta_button = SeleniumActions.read_web_element_text(web_element)

            try:
                assert(read_cta_button == "CTA TWO")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18678391 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18678392(self):

        test_case_number = "18678392"

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

            click_settings_tab = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            click_show_cta_button_one = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_SHOW_CTA_ONE)
            SeleniumActions.click_element(web_driver, click_show_cta_button_one)

            click_show_cta_button_two = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_SHOW_CTA_TWO)
            SeleniumActions.click_element(web_driver, click_show_cta_button_two)

            click_done_button = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            Tools.sleep(5)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

            element_path = BladeModuleData.BLADE_IFRAME_CTA_BUTTON_TWO
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)
            read_cta_button = SeleniumActions.read_web_element_text(web_element)

            try:
                assert(read_cta_button == "CTA ONE")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18678392 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18678385(self):

        test_case_number = "18678385"

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

            click_settings_tab = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            click_show_cta_button_two = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_SHOW_CTA_TWO)
            SeleniumActions.click_element(web_driver, click_show_cta_button_two)

            web_element = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_SHOW_BLADE_TITLE)

            click_element_visibility = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_ELEMENT_VISIBILITY)
            SeleniumActions.click_element(web_driver, click_element_visibility)

            Tools.sleep(1)

            SeleniumActions.element_is_not_visible(web_element)

            click_element_visibility = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_ELEMENT_VISIBILITY)
            SeleniumActions.click_element(web_driver, click_element_visibility)

            Tools.sleep(1)

            web_element = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_SHOW_BLADE_TITLE)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18678385 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18678386(self):

        test_case_number = "18678386"

        web_driver = self.fetch_webdriver()

        try:
            web_element = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_SWAP_MEDIA_TEXT)

            click_blade_settings = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_SETTINGS)
            SeleniumActions.click_element(web_driver, click_blade_settings)

            Tools.sleep(1)

            SeleniumActions.element_is_not_visible(web_element)

            click_blade_settings = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_SETTINGS)
            SeleniumActions.click_element(web_driver, click_blade_settings)

            Tools.sleep(1)

            web_element = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_SWAP_MEDIA_TEXT)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18678386 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18678387(self):

        test_case_number = "18678387"

        web_driver = self.fetch_webdriver()

        try:
            web_element = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_DESKTOP_MODULE)

            click_module_visibility = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_MODULE_VISIBILITY)
            SeleniumActions.click_element(web_driver, click_module_visibility)

            Tools.sleep(1)

            SeleniumActions.element_is_not_visible(web_element)

            click_module_visibility = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_MODULE_VISIBILITY)
            SeleniumActions.click_element(web_driver, click_module_visibility)

            Tools.sleep(1)

            web_element = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_DESKTOP_MODULE)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18678387 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18678393(self):

        test_case_number = "18678393"

        web_driver = self.fetch_webdriver()

        try:
            click_swap_setting = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_SWAP_MEDIA_TEXT)
            SeleniumActions.click_element(web_driver, click_swap_setting)

            click_done_button = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            Tools.sleep(5)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))
            web_element = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_IFRAME_IMAGE_LEFT)

            SeleniumActions.element_is_visible(web_driver, web_element)

            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.IFRAME_EDIT_BUTTON)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            click_settings_tab = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            click_swap_setting = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_SETTINGS_SWAP_MEDIA_TEXT)
            SeleniumActions.click_element(web_driver, click_swap_setting)

            click_done_button = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            Tools.sleep(5)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))
            web_element = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_IFRAME_IMAGE_RIGHT)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18678393 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18527976(self):

        test_case_number = "18527976"

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
            web_element = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_TITLE)

            click_module_info = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_MODULE_INFORMATION)
            SeleniumActions.click_element(web_driver, click_module_info)

            SeleniumActions.element_is_not_visible(web_element)

            click_module_info = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_MODULE_INFORMATION)
            SeleniumActions.click_element(web_driver, click_module_info)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18527976 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18527977(self):

        test_case_number = "18527977"

        web_driver = self.fetch_webdriver()

        try:
            web_element = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_SELECT_FROM_GALLERY)

            click_module_info = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_MANAGE_CONTENT)
            SeleniumActions.click_element(web_driver, click_module_info)

            Tools.sleep(2)

            try:
                SeleniumActions.element_is_not_visible(web_element)
                test_one = "Passed"
            except:
                test_one = "Failed"

            click_module_info = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_MANAGE_CONTENT)
            SeleniumActions.click_element(web_driver, click_module_info)

            Tools.sleep(2)

            try:
                SeleniumActions.element_is_not_visible(web_element)
                test_two = "Passed"
            except:
                test_two = "Failed"

            if test_one == "Passed" and test_two == "Passed":
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            else:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')


        except:
            print("C18527977 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18527978(self):

        test_case_number = "18527978"

        web_driver = self.fetch_webdriver()

        try:
            web_element = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_CTA_ONE_LINK_TEXT)

            click_module_info = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_MANAGE_CTA_BUTTONS)
            SeleniumActions.click_element(web_driver, click_module_info)

            SeleniumActions.element_is_not_visible(web_element)

            click_module_info = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_MANAGE_CTA_BUTTONS)
            SeleniumActions.click_element(web_driver, click_module_info)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18527978 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18527998(self):

        test_case_number = "18527998"

        web_driver = self.fetch_webdriver()

        try:
            #CTA Button One
            element_path = BladeModuleData.BLADE_CONTENT_CTA_ONE_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "0")

            link_page_text = SeleniumActions.read_select_text(web_element)
            link_page = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_CTA_ONE_LINK_PAGE)
            SeleniumActions.element_is_visible(web_driver, web_element)

            SeleniumActions.select_by_index(web_element, "1")

            url_text = SeleniumActions.read_select_text(web_element)
            url_text_box = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_CTA_ONE_URL)
            SeleniumActions.element_is_visible(web_driver, web_element)

            SeleniumActions.select_by_index(web_element, "2")

            no_link = SeleniumActions.read_select_text(web_element)

            SeleniumActions.element_is_not_visible(link_page)
            SeleniumActions.element_is_not_visible(url_text_box)

            #CTA Button Two
            element_path = BladeModuleData.BLADE_CONTENT_CTA_TWO_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "0")

            link_page_text_two = SeleniumActions.read_select_text(web_element)
            link_page = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_CTA_TWO_LINK_PAGE)
            SeleniumActions.element_is_visible(web_driver, web_element)

            SeleniumActions.select_by_index(web_element, "1")

            url_text_two = SeleniumActions.read_select_text(web_element)
            url_text_box = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_CTA_TWO_URL)
            SeleniumActions.element_is_visible(web_driver, web_element)

            SeleniumActions.select_by_index(web_element, "2")

            no_link_two = SeleniumActions.read_select_text(web_element)

            SeleniumActions.element_is_not_visible(link_page)
            SeleniumActions.element_is_not_visible(url_text_box)

            try:
                assert(link_page_text == "My Pages"
                       and url_text == "External Link" and no_link == "No Link" and link_page_text_two == "My Pages"
                       and url_text_two == "External Link" and no_link_two == "No Link")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

            test_case_number = "18527999"

            try:
                assert(link_page_text == "My Pages"
                       and url_text == "External Link" and no_link == "No Link" and link_page_text_two == "My Pages"
                       and url_text_two == "External Link" and no_link_two == "No Link")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18527999 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18527993(self):

        test_case_number = "18527993"

        web_driver = self.fetch_webdriver()

        try:
            # CTA Button One
            element_path = BladeModuleData.BLADE_CONTENT_CTA_ONE_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "1")
            Tools.sleep(2)

            url_text_clear = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_CTA_ONE_URL)
            SeleniumActions.write_to_element(web_driver, url_text_clear, "blackvinyl45")

            click_done_button = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            url_error_msg = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_CTA_ONE_URL_ERROR)
            url_one_error_text = SeleniumActions.read_web_element_text(url_error_msg)

            if url_one_error_text == "Please enter a valid URL.":
                test_one = "Passed"
            else:
                test_one = "Failed"

            url_text_clear = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_CTA_ONE_URL)
            SeleniumActions.clearTextField(web_driver, url_text_clear)
            SeleniumActions.write_to_element(web_driver, url_text_clear, "blackvinyl45.com")

            click_done_button = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            url_error_msg = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_CTA_ONE_URL_ERROR)
            url_one_error_text = SeleniumActions.read_web_element_text(url_error_msg)

            if url_one_error_text == "Please enter a valid URL.":
                test_two = "Passed"
            else:
                test_two = "Failed"

            url_text_clear = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_CTA_ONE_URL)
            SeleniumActions.clearTextField(web_driver, url_text_clear)
            SeleniumActions.write_to_element(web_driver, url_text_clear, "http://www.blackvinyl45.com")

            url_error_msg = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_CTA_ONE_URL_ERROR)

            if SeleniumActions.element_is_visible(web_driver, url_error_msg):
                test_three = "Failed"
            else:
                test_three = "Passed"

            # CTA Button Two
            element_path = BladeModuleData.BLADE_CONTENT_CTA_TWO_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "1")
            Tools.sleep(2)

            url_text_clear = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_CTA_TWO_URL)
            SeleniumActions.write_to_element(web_driver, url_text_clear, "blackvinyl45")

            click_done_button = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            url_error_msg = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_CTA_TWO_URL_ERROR)
            url_one_error_text = SeleniumActions.read_web_element_text(url_error_msg)

            if url_one_error_text == "Please enter a valid URL.":
                test_four = "Passed"
            else:
                test_four = "Failed"

            url_text_clear = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_CTA_TWO_URL)
            SeleniumActions.clearTextField(web_driver, url_text_clear)
            SeleniumActions.write_to_element(web_driver, url_text_clear, "blackvinyl45.com")

            url_error_msg = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_CTA_TWO_URL_ERROR)
            url_one_error_text = SeleniumActions.read_web_element_text(url_error_msg)

            if url_one_error_text == "Please enter a valid URL.":
                test_five = "Passed"
            else:
                test_five = "Failed"

            url_text_clear = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_CTA_TWO_URL)
            SeleniumActions.clearTextField(web_driver, url_text_clear)
            SeleniumActions.write_to_element(web_driver, url_text_clear, "http://www.blackvinyl45.com")

            click_done_button = SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            url_error_msg = \
                SeleniumActions.fetch_web_element(web_driver, BladeModuleData.BLADE_CONTENT_CTA_TWO_URL_ERROR)

            if SeleniumActions.element_is_visible(web_driver, url_error_msg):
                test_six = "Failed"
            else:
                test_six = "Passed"

            try:
                assert(test_one == "Passed" and test_two == "Passed" and test_three == "Passed"
                       and test_four == "Passed" and test_five == "Passed" and test_six == "Passed")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

            self.case_teardown()

        except:
            print("C18527993 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)
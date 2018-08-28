from library.page_models.martindale.martindale_module_setup import MartindaleModuleSetup
from library.page_models.martindale.martindale_login import MartindaleLogin
from library.page_models.martindale.martindale_navigation import MartindaleNavigation
from library.selenium_actions import *
from library.tools import Tools
from library.page_data.martindale_app.featured_blocks_data import FeaturedBlocksData
from library.page_data.martindale_app.martindale_data import MartindalePageData
from tests.test_setup.common_setup import CommonSetup, TestRailStatus

import pytest
import sys

####
#  Featured Blocks Module Test
####

'''
python -m pytest "Documents/IB/Martindale Automation/tests/test_featured_blocks.py" -s
'''

class TestFeaturedBlocksModule(CommonSetup):

    ####
    # Suite Setup and Teardown
    ####

    @pytest.fixture(autouse=True, scope='module')
    def set_up_class(self):

        '''
        Will be run once first before any test
        '''

        web_driver = self.fetch_webdriver()

        Tools.log("Executing Featured Blocks module tests...")

        MartindaleNavigation.navigate_to_home_page(web_driver)
        MartindaleLogin.login_to_app(web_driver)
        CommonSetup.selected_module = "featured"
        MartindaleModuleSetup.module_open(web_driver)

    # will run at end of all tests
    def teardown_class(self):

        '''
        Will be run once when all tests are complete
        '''
        Tools.log("Featured Blocks module test run complete.")


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

    def test_c18521219(self):

        test_case_number = "18521219"

        web_driver = self.fetch_webdriver()

        try:
            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.IFRAME_EDIT_BUTTON_TWO)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            element_path = FeaturedBlocksData.FEATURED_BLOCKS_MODULE_HEADER
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            blade_text = SeleniumActions.read_web_element_text(web_element)

            try:
                assert(blade_text == "FEATURED BLOCKS MODULE")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521219 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521222(self):

        test_case_number = "18521222"

        web_driver = self.fetch_webdriver()

        try:
            click_settings_tab = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            Tools.sleep(1)

            web_element = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_SETTINGS_SHOW_TITLE)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521222 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18527231(self):

        test_case_number = "18527231"

        web_driver = self.fetch_webdriver()

        try:
            click_layout_tab = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_LAYOUT_TAB)
            SeleniumActions.click_element(web_driver, click_layout_tab)

            Tools.sleep(1)

            web_element = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_LAYOUT_LABEL)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18527231 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521229(self):

        test_case_number = "18521229"

        web_driver = self.fetch_webdriver()

        try:
            click_content_tab = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_CONTENT_TAB)
            SeleniumActions.click_element(web_driver, click_content_tab)

            Tools.sleep(1)

            web_element = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_CONTENT_TITLE)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521229 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521228(self):

        test_case_number = "18521228"

        web_driver = self.fetch_webdriver()

        try:
            # Module Information
            click_module_info = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_MODULE_INFORMATION)
            SeleniumActions.click_element(web_driver, click_module_info)

            Tools.sleep(1)

            web_element = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_CONTENT_TITLE)

            try:
                assert(SeleniumActions.element_is_not_visible(web_element))
                test_one = "Passed"
            except AssertionError:
                test_one = "Failed"

            SeleniumActions.click_element(web_driver, click_module_info)

            Tools.sleep(2)

            web_element = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_CONTENT_TITLE)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                test_two = "Passed"
            except AssertionError:
                test_two = "Failed"

            # Manage Content
            click_manage_content = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_MANAGE_CONTENT)
            SeleniumActions.click_element(web_driver, click_manage_content)

            Tools.sleep(1)

            web_element = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_CONTENT_ADD_CONTENT)

            try:
                assert(SeleniumActions.element_is_not_visible(web_element))
                test_three = "Passed"
            except AssertionError:
                test_three = "Failed"

            SeleniumActions.click_element(web_driver, click_manage_content)

            Tools.sleep(2)

            web_element = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_CONTENT_ADD_CONTENT)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                test_four = "Passed"
            except AssertionError:
                test_four = "Failed"

            if test_one == "Passed" and test_two == "Passed" and test_three == "Passed" and test_four == "Passed":
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            else:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521228 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521223(self):

        test_case_number = "18521223"

        web_driver = self.fetch_webdriver()

        try:
            click_add_content = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_CONTENT_ADD_CONTENT)
            SeleniumActions.click_element(web_driver, click_add_content)

            Tools.sleep(1)

            web_element = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_CONTENT_BLOCK_TITLE)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521223 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18527150(self):

        test_case_number = "18527150"

        web_driver = self.fetch_webdriver()

        try:
            click_csncel_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_CONTENT_CANCEL_BUTTON)
            SeleniumActions.click_element(web_driver, click_csncel_button)

            Tools.sleep(3)

            web_element = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_MODULE_INFORMATION)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18527150 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521225(self):

        test_case_number = "18521225"

        web_driver = self.fetch_webdriver()

        try:
            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_EDIT_BUTTON)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(1)

            web_element = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_CONTENT_BLOCK_TITLE)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521225 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521224(self):

        test_case_number = "18521224"

        web_driver = self.fetch_webdriver()

        try:
            click_csncel_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_CONTENT_CANCEL_BUTTON)
            SeleniumActions.click_element(web_driver, click_csncel_button)

            Tools.sleep(3)

            click_delete_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_DELETE_BUTTON)
            SeleniumActions.click_element(web_driver, click_delete_button)

            Tools.sleep(1)

            delete_modal = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.DELETE_FEATURED_BLOCKS_MODAL)
            featured_blocks_delete_modal = SeleniumActions.read_web_element_text(delete_modal)

            try:
                assert(featured_blocks_delete_modal == "Are you sure you want to remove this link?")
                test_one = "Passed"
            except AssertionError:
                test_one = "Failed"

            click_csncel_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.DELETE_FEATURED_BLOCKS_MODAL_CANCEL_BUTTON)
            SeleniumActions.click_element(web_driver, click_csncel_button)

            Tools.sleep(1)

            featured_block = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCK)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, featured_block))
                test_two = "Passed"
            except AssertionError:
                test_two = "Failed"

            click_delete_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_DELETE_BUTTON)
            SeleniumActions.click_element(web_driver, click_delete_button)

            Tools.sleep(1)
            click_modal_ok = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.DELETE_FEATURED_BLOCKS_MODAL_OK_BUTTON)
            SeleniumActions.click_element(web_driver, click_modal_ok)

            Tools.sleep(2)

            try:
                assert(SeleniumActions.check_element_exists(web_driver,
                    "//*[contains(@id, 'link_link-')]/div[2]/div/div[2]/div[1]"))
                test_three = "Failed"
            except AssertionError:
                test_three = "Passed"

            if test_one == "Passed" and test_two == "Passed" and test_three == "Passed":
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            else:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521224 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18527155(self):

        test_case_number = "18527155"

        web_driver = self.fetch_webdriver()

        try:
            click_add_content = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_CONTENT_ADD_CONTENT)
            SeleniumActions.click_element(web_driver, click_add_content)

            Tools.sleep(3)

            click_select_gallery = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_CONTENT_SELECT_FROM_GALLERY)
            SeleniumActions.click_element(web_driver, click_select_gallery)

            Tools.sleep(3)

            click_gallery_image = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_CONTENT_SELECT_GALLERY_IMAGE)
            SeleniumActions.click_element(web_driver, click_gallery_image)

            element_path = FeaturedBlocksData.ADD_CONTENT_SELECT_GALLERY_IMAGE_TEXT
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)
            image_text = SeleniumActions.read_web_element_text(web_element)

            click_insert_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_CONTENT_SELECT_GALLERY_INSERT_BUTTON)
            SeleniumActions.click_element(web_driver, click_insert_button)

            Tools.sleep(2)

            element_path = FeaturedBlocksData.ADD_CONTENT_IMAGE_CONTAINER
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)
            SeleniumActions.move_to_element(web_driver, web_element)

            element_path = FeaturedBlocksData.ADD_CONTENT_IMAGE_TEXT
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)
            added_image_text = SeleniumActions.read_web_element_text(web_element)

            try:
                assert("/" + image_text == added_image_text)
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18527155 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18527161(self):

        test_case_number = "18527161"

        web_driver = self.fetch_webdriver()

        try:
            element_path = FeaturedBlocksData.ADD_CONTENT_IMAGE_CONTAINER
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)
            SeleniumActions.move_to_element(web_driver, web_element)

            click_replace_image = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_CONTENT_REPLACE_BUTTON)
            SeleniumActions.click_element(web_driver, click_replace_image)

            Tools.sleep(3)

            gallery_image = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_CONTENT_SELECT_GALLERY_IMAGE)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, gallery_image))
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18527161 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)

    def test_c18527151(self):

        test_case_number = "18527151"

        web_driver = self.fetch_webdriver()

        try:
            click_cancel_image = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_CONTENT_SELECT_GALLERY_CANCEL_BUTTON)
            SeleniumActions.click_element(web_driver, click_cancel_image)

            Tools.sleep(3)

            element_path = FeaturedBlocksData.FEATURED_BLOCK_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "1")

            Tools.sleep(2)

            link_drop_down = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCK_LINK_DROP_DOWN)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, link_drop_down))
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18527151 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18527152(self):

        test_case_number = "18527152"

        web_driver = self.fetch_webdriver()

        try:
            element_path = FeaturedBlocksData.FEATURED_BLOCK_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "2")

            Tools.sleep(2)

            link_drop_down = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCK_EXTERNAL_LINK)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, link_drop_down))
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18527152 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18527172(self):

        test_case_number = "18527172"

        web_driver = self.fetch_webdriver()

        try:
            click_select_gallery = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_CONTENT_SELECT_FROM_GALLERY)
            SeleniumActions.click_element(web_driver, click_select_gallery)

            Tools.sleep(3)

            click_gallery_image = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_CONTENT_SELECT_GALLERY_IMAGE)
            SeleniumActions.click_element(web_driver, click_gallery_image)

            click_insert_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_CONTENT_SELECT_GALLERY_INSERT_BUTTON)
            SeleniumActions.click_element(web_driver, click_insert_button)

            Tools.sleep(2)

            write_block_title = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_CONTENT_BLOCK_TITLE)
            SeleniumActions.write_to_element(web_driver, write_block_title, "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ012")

            click_save_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_CONTENT_SAVE_BUTTON)
            SeleniumActions.click_element(web_driver, click_save_button)
            Tools.sleep(2)

            element_path = FeaturedBlocksData.ADD_BLOCK_TITLE_ERROR
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            block_title_error = SeleniumActions.read_web_element_text(web_element)

            write_block_description = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_BLOCK_DESCRIPTION)
            SeleniumActions.write_to_element(web_driver, write_block_description, "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ012ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ012ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ012")

            click_save_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_CONTENT_SAVE_BUTTON_TWO)
            SeleniumActions.click_element(web_driver, click_save_button)

            element_path = FeaturedBlocksData.ADD_BLOCK_DESCRIPTION_ERROR
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            block_description_error = SeleniumActions.read_web_element_text(web_element)

            try:
                assert(block_title_error == "Please enter no more than 100 characters."
                       and block_description_error == "Please enter no more than 300 characters.")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18527172 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18527153(self):

        test_case_number = "18527153"

        web_driver = self.fetch_webdriver()

        try:
            write_block_title = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_CONTENT_BLOCK_TITLE)
            SeleniumActions.clearTextField(web_driver, write_block_title)
            SeleniumActions.write_to_element(web_driver, write_block_title, "Automated")

            write_block_description = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_BLOCK_DESCRIPTION)
            SeleniumActions.clearTextField(web_driver, write_block_description)
            SeleniumActions.write_to_element(web_driver, write_block_description, "This is an automated test.")

            write_link_box_text = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_BLOCK_LINK_TEXT_BOX)
            SeleniumActions.clearTextField(web_driver, write_link_box_text)
            SeleniumActions.write_to_element(web_driver, write_link_box_text, "Black Vinyl 45")

            write_external_link_text = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCK_EXTERNAL_LINK)
            SeleniumActions.clearTextField(web_driver, write_external_link_text)
            SeleniumActions.write_to_element(web_driver, write_external_link_text, "http://www.blackvinyl45.com")

            write_block_alt_text = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_ALT_TEXT)
            SeleniumActions.clearTextField(web_driver, write_block_alt_text)
            SeleniumActions.write_to_element(web_driver, write_block_alt_text, "alt")

            click_save_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_CONTENT_SAVE_BUTTON_TWO)
            SeleniumActions.click_element(web_driver, click_save_button)

            Tools.sleep(4)

            saved_image = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCK_IMAGE)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, saved_image))
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18527153 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18527162(self):

        test_case_number = "18527162"

        web_driver = self.fetch_webdriver()

        try:
            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_EDIT_BUTTON)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(1)

            click_modal_no = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.DELETE_FEATURED_BLOCKS_MODAL_CANCEL_BUTTON)
            SeleniumActions.click_element(web_driver, click_modal_no)

            Tools.sleep(1)

            write_block_title = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_CONTENT_BLOCK_TITLE)
            SeleniumActions.clearTextField(web_driver, write_block_title)
            SeleniumActions.write_to_element(web_driver, write_block_title, "Automated")

            write_block_description = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_BLOCK_DESCRIPTION)
            SeleniumActions.clearTextField(web_driver, write_block_description)
            SeleniumActions.write_to_element(web_driver, write_block_description, "This is an automated test.")

            element_path = FeaturedBlocksData.ADD_BLOCK_LINK_APPEARANCE_DROP_DOWN
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            select = Select(web_element)
            select.select_by_index("1")

            Tools.sleep(2)

            link_text = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_BLOCK_LINK_TEXT_LABEL)
            read_link_text = SeleniumActions.read_web_element_text(link_text)

            try:
                assert(read_link_text == "Link text*")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18527162 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18527163(self):

        test_case_number = "18527163"

        web_driver = self.fetch_webdriver()

        try:
            element_path = FeaturedBlocksData.ADD_BLOCK_LINK_APPEARANCE_DROP_DOWN
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            select = Select(web_element)
            select.select_by_index("2")

            Tools.sleep(2)

            link_text = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_BLOCK_BUTTON_TEXT_LABEL)
            read_link_text = SeleniumActions.read_web_element_text(link_text)

            try:
                assert(read_link_text == "Button text*")
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18527163 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521234(self):

        test_case_number = "18521234"

        web_driver = self.fetch_webdriver()

        try:
            element_path = FeaturedBlocksData.ADD_BLOCK_LINK_APPEARANCE_DROP_DOWN
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            SeleniumActions.select_by_index(web_element, "0")

            click_save_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_CONTENT_SAVE_BUTTON)
            SeleniumActions.click_element(web_driver, click_save_button)

            Tools.sleep(3)

            click_done_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURE_BLOCK_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))
            Tools.sleep(4)

            web_element = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_BLOCK_TITLE)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                test_one = "Passed"
            except AssertionError:
                test_one = "Failed"

            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.IFRAME_EDIT_BUTTON_TWO)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            click_settings_tab = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            Tools.sleep(1)

            click_show_title = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_SETTINGS_SHOW_BLOCK_TITLE)
            SeleniumActions.click_element(web_driver, click_show_title)
            click_done_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURE_BLOCK_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            Tools.sleep(4)
            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

            try:
                assert(SeleniumActions.check_element_exists(web_driver,
                                                            "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div/ul/li/div/a/span[2]"))
                test_two = "Failed"
            except AssertionError:
                test_two = "Passed"

            if test_one == "Passed" and test_two == "Passed":
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            else:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18527232 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18527232(self):

        test_case_number = "18527232"

        web_driver = self.fetch_webdriver()

        try:
            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.IFRAME_EDIT_BUTTON_TWO)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            click_settings_tab = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            Tools.sleep(1)

            click_show_title = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_SETTINGS_SHOW_BLOCK_TITLE)
            SeleniumActions.click_element(web_driver, click_show_title)

            click_layout_tab = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_LAYOUT_TAB)
            SeleniumActions.click_element(web_driver, click_layout_tab)

            Tools.sleep(1)

            element_path = FeaturedBlocksData.FEATURED_BLOCKS_LAYOUT_OVERLAY
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)
            SeleniumActions.move_to_element(web_driver, web_element)

            click_layout_tab = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_CHANGE_LAYOUT_BUTTON)
            SeleniumActions.click_element(web_driver, click_layout_tab)

            Tools.sleep(1)

            click_layout = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_LAYOUT_ONE)
            SeleniumActions.click_element(web_driver, click_layout)

            click_done_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURE_BLOCK_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))
            Tools.sleep(4)

            element_path = FeaturedBlocksData.FEATURED_BLOCKS_LAYOUT
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            except:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18527232 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521231(self):

        test_case_number = "18521231"

        web_driver = self.fetch_webdriver()

        try:
            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.IFRAME_EDIT_BUTTON_TWO)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            write_block_title = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_CONTENT_TITLE)
            SeleniumActions.clearTextField(web_driver, write_block_title)
            SeleniumActions.write_to_element(web_driver, write_block_title, "Automated Title")

            write_block_caption = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_CAPTION)
            SeleniumActions.clearTextField(web_driver, write_block_caption)
            SeleniumActions.write_to_element(web_driver, write_block_caption, "Automated Caption")

            click_done_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURE_BLOCK_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))
            Tools.sleep(4)

            element_path = FeaturedBlocksData.FEATURED_BLOCKS_TITLE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                test_one = "Passed"
            except AssertionError:
                test_one = "Failed"

            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.IFRAME_EDIT_BUTTON_TWO)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            click_settings_tab = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            Tools.sleep(1)

            click_show_title = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_SETTINGS_SHOW_TITLE)
            SeleniumActions.click_element(web_driver, click_show_title)

            click_done_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURE_BLOCK_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))
            Tools.sleep(4)

            try:
                assert(SeleniumActions.check_element_exists(web_driver, "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div[1]/h2"))
                test_two = "Failed"
            except AssertionError:
                test_two = "Passed"

            if test_one == "Passed" and test_two == "Passed":
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            else:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521231 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521232(self):

        test_case_number = "18521232"

        web_driver = self.fetch_webdriver()

        try:
            element_path = FeaturedBlocksData.FEATURED_BLOCKS_CAPTION_DISPLAY
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                test_one = "Passed"
            except AssertionError:
                test_one = "Failed"

            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.IFRAME_EDIT_BUTTON_TWO)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            click_settings_tab = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            Tools.sleep(1)

            click_show_title = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_SETTINGS_SHOW_TITLE)
            SeleniumActions.click_element(web_driver, click_show_title)

            click_show_caption = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_SETTINGS_SHOW_CAPTION)
            SeleniumActions.click_element(web_driver, click_show_caption)

            click_done_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURE_BLOCK_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))
            Tools.sleep(4)

            element_path = FeaturedBlocksData.FEATURED_BLOCKS_TITLE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.check_element_exists(web_driver, "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div[1]/h3"))
                test_two = "Failed"
            except AssertionError:
                test_two = "Passed"

            if test_one == "Passed" and test_two == "Passed":
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            else:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521232 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18521235(self):

        test_case_number = "18521235"

        web_driver = self.fetch_webdriver()

        try:
            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.IFRAME_EDIT_BUTTON_TWO)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            click_settings_tab = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            Tools.sleep(1)

            click_show_caption = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_SETTINGS_SHOW_CAPTION)
            SeleniumActions.click_element(web_driver, click_show_caption)

            click_show_description = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_SETTINGS_SHOW_BLOCK_DESCRIPTION)
            SeleniumActions.click_element(web_driver, click_show_description)

            click_done_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURE_BLOCK_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))
            Tools.sleep(4)

            element_path = FeaturedBlocksData.FEATURED_BLOCKS_DESCRIPTION
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)
            element_text = SeleniumActions.read_web_element_text(web_element)

            try:
                assert(element_text == "LEARN MORE")
                test_one = "Passed"
            except AssertionError:
                test_one = "Failed"

            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.IFRAME_EDIT_BUTTON_TWO)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            click_settings_tab = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            Tools.sleep(1)

            click_show_description = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_SETTINGS_SHOW_BLOCK_DESCRIPTION)
            SeleniumActions.click_element(web_driver, click_show_description)

            click_done_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURE_BLOCK_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))
            Tools.sleep(4)

            element_path = FeaturedBlocksData.FEATURED_BLOCKS_DESCRIPTION
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            try:
                assert(SeleniumActions.element_is_visible(web_driver, web_element))
                test_two = "Passed"
            except AssertionError:
                test_two = "Failed"

            if test_one == "Passed" and test_two == "Passed":
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            else:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

        except:
            print("C18521235 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


    def test_c18527148(self):

        test_case_number = "18527148"

        web_driver = self.fetch_webdriver()

        try:
            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.IFRAME_EDIT_BUTTON_TWO)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            click_layout_tab = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_LAYOUT_TAB)
            SeleniumActions.click_element(web_driver, click_layout_tab)

            Tools.sleep(1)

            element_path = FeaturedBlocksData.FEATURED_BLOCKS_LAYOUT_OVERLAY
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)
            SeleniumActions.move_to_element(web_driver, web_element)

            change_layout_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_CHANGE_LAYOUT_BUTTON)
            SeleniumActions.click_element(web_driver, change_layout_button)

            Tools.sleep(1)

            click_layout = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_LAYOUT_TWO)
            SeleniumActions.click_element(web_driver, click_layout)

            click_content_tab = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_CONTENT_TAB)
            SeleniumActions.click_element(web_driver, click_content_tab)

            Tools.sleep(1)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_EDIT_BUTTON)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(4)

            element_path = FeaturedBlocksData.DELETE_FEATURED_BLOCKS_MODAL
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            modal_text = SeleniumActions.read_web_element_text(web_element)

            try:
                assert(modal_text == "You're about to navigate out of the featured blocks settings")
                test_one = "Passed"
            except AssertionError:
                test_one = "Failed"

            click_yes_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_SAVE_CHANGES_YES_BUTTON)
            SeleniumActions.click_element(web_driver, click_yes_button)

            Tools.sleep(2)

            click_cancel_button = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.ADD_CONTENT_CANCEL_BUTTON)
            SeleniumActions.click_element(web_driver, click_cancel_button)

            Tools.sleep(2)

            click_layout_tab = \
                SeleniumActions.fetch_web_element(web_driver, FeaturedBlocksData.FEATURED_BLOCKS_LAYOUT_TAB)
            SeleniumActions.click_element(web_driver, click_layout_tab)

            Tools.sleep(2)

            element_path = FeaturedBlocksData.FEATURED_BLOCKS_LAYOUT_LABEL
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            layout_label_text = SeleniumActions.read_web_element_text(web_element)

            try:
                assert(layout_label_text == "Fly-Up A")
                test_two = "Passed"
            except AssertionError:
                test_two = "Failed"

            if test_one == "Passed" and test_two == "Passed":
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().PASS, '')
            else:
                CommonSetup.report_test_rail(self, test_case_number, TestRailStatus().FAIL, '')

            self.case_teardown()

        except:
            print("C18527148 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)



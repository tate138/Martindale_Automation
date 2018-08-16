from library.page_data.martindale_app.martindale_data import MartindalePageData
from library.page_models.martindale.martindale_module_setup import MartindaleModuleSetup
from library.page_models.martindale.martindale_login import MartindaleLogin
from library.page_models.martindale.martindale_navigation import MartindaleNavigation
from library.selenium_actions import *
from library.tools import Tools
from tests.test_setup.common_setup import CommonSetup

import sys


####
#  Call to Action Module Test
####

class CallToAction(CommonSetup):

    def test_call_to_action(self):

        try:
            # Setup
            web_driver = self.fetch_webdriver()

            MartindaleNavigation.navigate_to_home_page(web_driver)
            MartindaleLogin.login_to_app(web_driver)
            MartindaleModuleSetup.cta_module_edit(web_driver)

        except:
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)

        print("Executing CTA module tests...")

        ####
        # Execute Test Case C18521173
        ####

        try:

            Tools.sleep(5)

            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_MODULE_EDIT_BUTTON)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            element_path = MartindalePageData.CTA_MODULE_HEADER
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            cta_text = SeleniumActions.read_web_element_text(web_element)

            if cta_text == "CALL TO ACTION(CTA)":
                print("C18521173 Passed")
                result = CommonSetup.client.send_post(
                    'add_result_for_case/' + CommonSetup.current_test_run_id + '/18521173',
                    {'status_id': 1, 'comment': ''}
                )
            else:
                print("C18521173 Failed")
                result = CommonSetup.client.send_post(
                    'add_result_for_case/' + CommonSetup.current_test_run_id + '/18521173',
                    {'status_id': 5, 'comment': ''}
                )

        except:
            print("C18521173 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


        ####
        # Execute Test Case C18521175
        ####

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

            if cta_title_text == "Automated Title" and cta_caption_text == "Automated Caption":
                print("C18521175 Passed")
                result = CommonSetup.client.send_post(
                    'add_result_for_case/' + CommonSetup.current_test_run_id + '/18521175',
                    {'status_id': 1, 'comment': ''}
                )
            else:
                print("C18521175 Failed")
                result = CommonSetup.client.send_post(
                    'add_result_for_case/' + CommonSetup.current_test_run_id + '/18521175',
                    {'status_id': 5, 'comment': ''}
                )

        except:
            print("C18521175 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


        ####
        # Execute Test Case C18521178
        ####

        try:
            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_MODULE_EDIT_BUTTON)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            # CTA Button One

            element_path = MartindalePageData.CTA_MODULE_BUTTON_ONE_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            select = Select(web_element)
            select.select_by_index("0")

            Tools.sleep(1)

            element_path = MartindalePageData.CTA_MODULE_LINK_PAGE_ONE_DROP_DOWN
            link_page_one_drop_down = SeleniumActions.find_by_xpath(web_driver, element_path)

            if SeleniumActions.element_is_visible(web_driver, link_page_one_drop_down):
                test_one = "Passed"
            else:
                test_one = "Failed"

            element_path = MartindalePageData.CTA_MODULE_BUTTON_ONE_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            select = Select(web_element)
            select.select_by_index("1")

            Tools.sleep(1)

            element_path = MartindalePageData.CTA_MODULE_EXTERNAL_URL_ONE
            url_one = SeleniumActions.find_by_xpath(web_driver, element_path)

            if SeleniumActions.element_is_visible(web_driver, url_one):
                test_two = "Passed"
            else:
                test_two = "Failed"

            element_path = MartindalePageData.CTA_MODULE_BUTTON_ONE_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            select = Select(web_element)
            select.select_by_index("2")

            Tools.sleep(1)

            element_path = MartindalePageData.CTA_MODULE_PHONE_NUMBER_ONE
            phone_number = SeleniumActions.find_by_xpath(web_driver, element_path)

            if SeleniumActions.element_is_visible(web_driver, phone_number):
                test_three = "Passed"
            else:
                test_three = "Failed"

            element_path = MartindalePageData.CTA_MODULE_BUTTON_ONE_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            select = Select(web_element)
            select.select_by_index("3")

            Tools.sleep(1)

            if SeleniumActions.element_is_visible(web_driver, link_page_one_drop_down) and \
                    SeleniumActions.element_is_visible(web_driver, url_one) and \
                    SeleniumActions.element_is_visible(web_driver, phone_number):
                test_four = "Failed"
            else:
                test_four = "Passed"

            # CTA Button Two

            element_path = MartindalePageData.CTA_MODULE_TWO_BUTTON_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            select = Select(web_element)
            select.select_by_index("0")

            Tools.sleep(1)

            element_path = MartindalePageData.CTA_MODULE_LINK_PAGE_TWO_DROP_DOWN
            link_page_two_drop_down = SeleniumActions.find_by_xpath(web_driver, element_path)

            if SeleniumActions.element_is_visible(web_driver, link_page_two_drop_down):
                test_five = "Passed"
            else:
                test_five = "Failed"

            element_path = MartindalePageData.CTA_MODULE_TWO_BUTTON_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            select = Select(web_element)
            select.select_by_index("1")

            Tools.sleep(1)

            element_path = MartindalePageData.CTA_MODULE_EXTERNAL_URL_TWO
            url_two = SeleniumActions.find_by_xpath(web_driver, element_path)

            if SeleniumActions.element_is_visible(web_driver, url_two):
                test_six = "Passed"
            else:
                test_six = "Failed"

            element_path = MartindalePageData.CTA_MODULE_TWO_BUTTON_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            select = Select(web_element)
            select.select_by_index("2")

            Tools.sleep(1)

            element_path = MartindalePageData.CTA_MODULE_PHONE_NUMBER_TWO
            phone_number_two = SeleniumActions.find_by_xpath(web_driver, element_path)

            if SeleniumActions.element_is_visible(web_driver, phone_number_two):
                test_seven = "Passed"
            else:
                test_seven = "Failed"

            element_path = MartindalePageData.CTA_MODULE_TWO_BUTTON_LINK_TYPE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            select = Select(web_element)
            select.select_by_index("3")

            Tools.sleep(1)

            if SeleniumActions.element_is_visible(web_driver, link_page_two_drop_down) and \
                    SeleniumActions.element_is_visible(web_driver, url_two) and \
                    SeleniumActions.element_is_visible(web_driver, phone_number_two):
                test_eight = "Failed"
            else:
                test_eight = "Passed"

            if test_one == "Passed" and test_two == "Passed" and test_three == "Passed" and test_four == "Passed" and \
                    test_five == "Passed" and test_six == "Passed" and test_seven == "Passed" and test_eight == "Passed":
                print("C18521178 Passed")
                result = CommonSetup.client.send_post(
                    'add_result_for_case/' + CommonSetup.current_test_run_id + '/18521178',
                    {'status_id': 1, 'comment': ''}
                )
            else:
                print("C18521178 Failed")
                result = CommonSetup.client.send_post(
                    'add_result_for_case/' + CommonSetup.current_test_run_id + '/18521178',
                    {'status_id': 5, 'comment': ''}
                )

        except:
            print("C18521178 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


        ####
        # Execute Test Case C18521180
        ####

        try:

            # CTA Button One

            element_path = MartindalePageData.CTA_MODULE_ONE_LINK_APPEARANCE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            select = Select(web_element)
            select.select_by_index("1")

            Tools.sleep(1)

            element_path = MartindalePageData.CTA_MODULE_BUTTON_TEXT_BOX_ONE
            button_text_box_one = SeleniumActions.find_by_xpath(web_driver, element_path)

            if SeleniumActions.element_is_visible(web_driver, button_text_box_one):
                test_one = "Passed"
            else:
                test_one = "Failed"

            element_path = MartindalePageData.CTA_MODULE_ONE_LINK_APPEARANCE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            select = Select(web_element)
            select.select_by_index("2")

            Tools.sleep(1)

            element_path = MartindalePageData.CTA_MODULE_SELECT_ICON_ONE
            select_icon_one = SeleniumActions.find_by_xpath(web_driver, element_path)

            if SeleniumActions.element_is_visible(web_driver, select_icon_one):
                test_two = "Passed"
            else:
                test_two = "Failed"

            element_path = MartindalePageData.CTA_MODULE_ONE_LINK_APPEARANCE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            select = Select(web_element)
            select.select_by_index("3")

            Tools.sleep(1)

            element_path = MartindalePageData.CTA_MODULE_BUTTON_TEXT_BOX_ONE
            link_text_one = SeleniumActions.find_by_xpath(web_driver, element_path)

            element_path = MartindalePageData.CTA_MODULE_SELECT_ICON_ONE
            select_icon_one = SeleniumActions.find_by_xpath(web_driver, element_path)

            if SeleniumActions.element_is_visible(web_driver, link_text_one) \
                    and SeleniumActions.element_is_visible(web_driver, select_icon_one):
                test_three = "Passed"
            else:
                test_three = "Failed"

            element_path = MartindalePageData.CTA_MODULE_ONE_LINK_APPEARANCE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            select = Select(web_element)
            select.select_by_index("0")

            Tools.sleep(1)


            element_path = MartindalePageData.CTA_MODULE_BUTTON_TEXT_BOX_ONE
            link_text_one = SeleniumActions.find_by_xpath(web_driver, element_path)

            if SeleniumActions.element_is_visible(web_driver, link_text_one):
                test_four = "Passed"
            else:
                test_four = "Failed"

            # CTA Button Two

            element_path = MartindalePageData.CTA_MODULE_TWO_LINK_APPEARANCE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            select = Select(web_element)
            select.select_by_index("1")

            Tools.sleep(1)

            element_path = MartindalePageData.CTA_MODULE_BUTTON_TEXT_BOX_TWO
            button_text_box_two = SeleniumActions.find_by_xpath(web_driver, element_path)

            if SeleniumActions.element_is_visible(web_driver, button_text_box_two):
                test_five = "Passed"
            else:
                test_five = "Failed"

            element_path = MartindalePageData.CTA_MODULE_TWO_LINK_APPEARANCE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            select = Select(web_element)
            select.select_by_index("2")

            Tools.sleep(1)

            element_path = MartindalePageData.CTA_MODULE_SELECT_ICON_TWO
            select_icon_two = SeleniumActions.find_by_xpath(web_driver, element_path)

            if SeleniumActions.element_is_visible(web_driver, select_icon_two):
                test_six = "Passed"
            else:
                test_six = "Failed"

            element_path = MartindalePageData.CTA_MODULE_TWO_LINK_APPEARANCE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            select = Select(web_element)
            select.select_by_index("3")

            Tools.sleep(2)

            element_path = MartindalePageData.CTA_MODULE_BUTTON_TEXT_BOX_TWO
            button_text_box_two = SeleniumActions.find_by_xpath(web_driver, element_path)

            element_path = MartindalePageData.CTA_MODULE_SELECT_ICON_TWO
            select_icon_two = SeleniumActions.find_by_xpath(web_driver, element_path)

            if SeleniumActions.element_is_visible(web_driver, button_text_box_two) \
                    and SeleniumActions.element_is_visible(web_driver, select_icon_two):
                test_seven = "Passed"
            else:
                test_seven = "Failed"

            element_path = MartindalePageData.CTA_MODULE_TWO_LINK_APPEARANCE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            select = Select(web_element)
            select.select_by_index("0")

            Tools.sleep(1)

            element_path = MartindalePageData.CTA_MODULE_LINK_TEXT_BOX_TWO
            link_text_two = SeleniumActions.find_by_xpath(web_driver, element_path)

            if SeleniumActions.element_is_visible(web_driver, link_text_two):
                test_eight = "Passed"
            else:
                test_eight = "Failed"

            if test_one == "Passed" and test_two == "Passed" and test_three == "Passed" and test_four == "Passed" and \
                    test_five == "Passed" and test_six == "Passed" and test_seven == "Passed" and test_eight == "Passed":
                print("C18521180 Passed")
                result = CommonSetup.client.send_post(
                    'add_result_for_case/' + CommonSetup.current_test_run_id + '/18521180',
                    {'status_id': 1, 'comment': ''}
                )
            else:
                print("C18521180 Failed")
                result = CommonSetup.client.send_post(
                    'add_result_for_case/' + CommonSetup.current_test_run_id + '/18521180',
                    {'status_id': 5, 'comment': ''}
                )

        except:
            print("C18521180 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


        ####
        # Execute Test Case C18521174
        ####

        try:
            write_link_text_two = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_MODULE_LINK_TEXT_BOX_TWO)
            SeleniumActions.clearTextField(web_driver, write_link_text_two)
            SeleniumActions.write_to_element(web_driver, write_link_text_two, "Legalize Ferrets")

            click_settings_tab = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            cta_settings_button_one = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_SETTINGS_SHOW_BUTTON_ONE)

            if SeleniumActions.element_is_visible(web_driver, cta_settings_button_one):
                print("C18521174 Passed")
                result = CommonSetup.client.send_post(
                    'add_result_for_case/' + CommonSetup.current_test_run_id + '/18521174',
                    {'status_id': 1, 'comment': ''}
                )
            else:
                print("C18521174 Failed")
                result = CommonSetup.client.send_post(
                    'add_result_for_case/' + CommonSetup.current_test_run_id + '/18521174',
                    {'status_id': 5, 'comment': ''}
                )

        except:
            print("C18521174 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


        ####
        # Execute Test Case C18521182
        ####

        try:

            # Link One

            click_cta_settings_button_one = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_SETTINGS_SHOW_BUTTON_ONE)
            SeleniumActions.click_element(web_driver, click_cta_settings_button_one)

            click_done_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_MODULE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

            Tools.sleep(5)

            element_path = MartindalePageData.CTA_MODULE_LINK_DISPLAY
            link_display_one = SeleniumActions.find_by_xpath(web_driver, element_path)

            if SeleniumActions.element_is_visible(web_driver, link_display_one):
                test_one = "Passed"
            else:
                test_one = "Failed"

            # Link Two

            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_MODULE_EDIT_BUTTON)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            click_settings_tab = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            click_cta_settings_button_one = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_SETTINGS_SHOW_BUTTON_ONE)
            SeleniumActions.click_element(web_driver, click_cta_settings_button_one)

            click_cta_settings_button_two = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_SETTINGS_SHOW_BUTTON_TWO)
            SeleniumActions.click_element(web_driver, click_cta_settings_button_two)

            click_done_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_MODULE_DONE_BUTTON)
            SeleniumActions.click_element(web_driver, click_done_button)

            web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

            Tools.sleep(5)

            element_path = MartindalePageData.CTA_MODULE_LINK_DISPLAY
            link_display_one = SeleniumActions.find_by_xpath(web_driver, element_path)

            if SeleniumActions.element_is_visible(web_driver, link_display_one):
                test_two = "Passed"
            else:
                test_two = "Failed"

            if test_one == "Passed" and test_two == "Passed":
                print("C18521182 Passed")
                result = CommonSetup.client.send_post(
                    'add_result_for_case/' + CommonSetup.current_test_run_id + '/18521182',
                    {'status_id': 1, 'comment': ''}
                )
            else:
                print("C18521182 Failed")
                result = CommonSetup.client.send_post(
                    'add_result_for_case/' + CommonSetup.current_test_run_id + '/18521182',
                    {'status_id': 5, 'comment': ''}
                )

        except:
            print("C18521182 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)


        ####
        # Execute Test Case C18521230
        ####

        try:
            click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_MODULE)
            SeleniumActions.click_element(web_driver, click_blade_module)

            Tools.sleep(2)

            click_edit_button = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_MODULE_EDIT_BUTTON)
            SeleniumActions.click_element(web_driver, click_edit_button)

            Tools.sleep(5)

            web_driver.switch_to.default_content()

            click_settings_tab = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_SETTINGS_TAB)
            SeleniumActions.click_element(web_driver, click_settings_tab)

            click_cta_settings_button_two = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_SETTINGS_SHOW_BUTTON_TWO)
            SeleniumActions.click_element(web_driver, click_cta_settings_button_two)

            click_content_tab = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_CONTENT_TAB)
            SeleniumActions.click_element(web_driver, click_content_tab)

            element_path = MartindalePageData.CTA_MODULE_TWO_LINK_APPEARANCE
            web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

            if SeleniumActions.element_is_visible(web_driver, web_element):
                print("C18521230 Passed")
                result = CommonSetup.client.send_post(
                    'add_result_for_case/' + CommonSetup.current_test_run_id + '/18521230',
                    {'status_id': 1, 'comment': ''}
                )
            else:
                print("C18521230 Failed")
                result = CommonSetup.client.send_post(
                    'add_result_for_case/' + CommonSetup.current_test_run_id + '/18521230',
                    {'status_id': 5, 'comment': ''}
                )

        except:
            print("C18521230 Not Tested")
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)













        ####
        # Clean up
        ####
        try:
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
            print("CTA module test run complete.")


        except:
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)










####
#  Run
####


if __name__ == "__main__":
    CallToAction().test_call_to_action()
from library.selenium_actions import *
from library.tools import Tools
from library.selenium_driver import SeleniumDriver
from library.page_data.martindale_app.martindale_data import MartindalePageData
from testrail.testrail import *

import sys


####
#  Banner Module Test
####


def test_suite():

    try:
        # Setup Test Rail
        client = APIClient(MartindalePageData.TEST_RAIL_URL)
        client.user = MartindalePageData.AUTOMATION_USER
        client.password = MartindalePageData.AUTOMATION_PW
        current_test_run_id = MartindalePageData.AUTOMATION_TEST_RUN_ID

        # Setup Driver
        web_driver = SeleniumDriver.fetch_chrome_webdriver()
        web_driver.get(MartindalePageData.MARTINDALE_URL)
        Tools.sleep(3)

        # Login
        login_username = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MARTINDALE_LOGIN_USERNAME)
        SeleniumActions.write_to_element \
            (web_driver, login_username, MartindalePageData.MARTINDALE_LOGIN_EMAIL)

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

        web_driver.switch_to_window(web_driver.window_handles[1])

    except:
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    print("Executing Banner module tests...")


    ####
    # Execute Test Case C18513007
    ####

    try:
        web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

        add_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_MODULE_BUTTON)
        SeleniumActions.click_element(web_driver, add_module)

        select_banner_module = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_MODULE_BUTTON)
        SeleniumActions.click_element(web_driver, select_banner_module)

        click_banner_radio = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.SAVED_BANNER_RADIO_BUTTON)
        SeleniumActions.click_element(web_driver, click_banner_radio)

        element_path = MartindalePageData.MODULE_NAME_DROP_DOWN
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        Tools.sleep(2)

        select = Select(web_element)
        select.select_by_index("1")

        click_submit_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE_SUBMIT_BUTTON)
        SeleniumActions.click_element(web_driver, click_submit_button)

        Tools.sleep(5)

        click_banner_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_MODULE)
        SeleniumActions.click_element(web_driver, click_banner_module)

        Tools.sleep(2)

        click_banner_name = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_MODULE_HEADER)
        SeleniumActions.click_element(web_driver, click_banner_name)

        Tools.sleep(2)

        click_edit_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_MODULE_EDIT_BUTTON)
        SeleniumActions.click_element(web_driver, click_edit_button)

        Tools.sleep(5)

        web_driver.switch_to.default_content()

        element_path = MartindalePageData.GALLERY_BANNER_TITLE
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        banner_text = SeleniumActions.read_web_element_text(web_element)

        if banner_text == "BANNER MODULE":
            print("C18513007 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18513007',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18513007 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18513007',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18513007 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18513008
    ####

    try:
        click_settings_tab = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_MODULE_SETTINGS_TAB)
        SeleniumActions.click_element(web_driver, click_settings_tab)

        element_path = MartindalePageData.BANNER_MODULE_SETTINGS_ELEMENT_VISIBILITY
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        element_visibility_text = SeleniumActions.read_web_element_text(web_element)

        click_layout_tab = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_MODULE_LAYOUT_TAB)
        SeleniumActions.click_element(web_driver, click_layout_tab)

        element_path = MartindalePageData.BANNER_MODULE_LAYOUT_TYPE
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        layout_type_text = SeleniumActions.read_web_element_text(web_element)

        click_content_tab = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_MODULE_CONTENT_TAB)
        SeleniumActions.click_element(web_driver, click_content_tab)

        element_path = MartindalePageData.BANNER_MODULE_CONENT_MANAGE_CONTENT
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        manage_content_text = SeleniumActions.read_web_element_text(web_element)

        if element_visibility_text == "ELEMENT VISIBILITY" \
                and layout_type_text == "LAYOUT TYPE" \
                and manage_content_text == "Manage Content":
            print("C18513008 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18513008',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18513008 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18513008',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18513008 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18521018
    ####

    try:
        click_add_banner = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_MODULE_CONTENT_ADD_BANNER_BUTTON)
        SeleniumActions.click_element(web_driver, click_add_banner)

        Tools.sleep(5)

        element_path = MartindalePageData.BANNER_MODULE_CONTENT_ADD_BANNER
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        add_banner_text = SeleniumActions.read_web_element_text(web_element)

        if add_banner_text == "ADD BANNER":
            print("C18521018 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521018',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18521018 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521018',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18521018 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18521037
    ####

    try:
        # CTA Button 1
        element_path = MartindalePageData.BANNER_MODULE_CONTENT_ADD_LINK_APPEARANCE
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        Tools.sleep(2)

        select = Select(web_element)
        select.select_by_index("0")

        link_text = SeleniumActions.read_select_text(web_element)

        select = Select(web_element)
        select.select_by_index("1")

        button_text = SeleniumActions.read_select_text(web_element)

        select = Select(web_element)
        select.select_by_index("2")

        icon_only = SeleniumActions.read_select_text(web_element)

        select = Select(web_element)
        select.select_by_index("3")

        icon_and_button = SeleniumActions.read_select_text(web_element)

        # CTA Button 2
        element_path = MartindalePageData.BANNER_MODULE_CONTENT_ADD_LINK_APPEARANCE_TWO
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        Tools.sleep(2)

        select = Select(web_element)
        select.select_by_index("0")

        link_text_two = SeleniumActions.read_select_text(web_element)

        select = Select(web_element)
        select.select_by_index("1")

        button_text_two = SeleniumActions.read_select_text(web_element)

        select = Select(web_element)
        select.select_by_index("2")

        icon_only_two = SeleniumActions.read_select_text(web_element)

        select = Select(web_element)
        select.select_by_index("3")

        icon_and_button_two = SeleniumActions.read_select_text(web_element)


        if link_text == "Text Link" and button_text == "Text Button" and icon_only == "Icon Only" \
                and icon_and_button == "Icon & Text Button" and link_text_two == "Text Link" and button_text_two \
                == "Text Button" and icon_only_two == "Icon Only" and icon_and_button_two == "Icon & Text Button":
            print("C18521037 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521037',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18521037 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521037',
                {'status_id': 5, 'comment': ''}
            )

        Tools.sleep(2)

    except:
        print("C18521037 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18521024
    ####

    try:
        # CTA Button 1
        element_path = MartindalePageData.BANNER_MODULE_CONTENT_ADD_LINK_TYPE
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        Tools.sleep(2)

        select = Select(web_element)
        select.select_by_index("0")

        my_pages = SeleniumActions.read_select_text(web_element)

        select = Select(web_element)
        select.select_by_index("1")

        external_link = SeleniumActions.read_select_text(web_element)

        select = Select(web_element)
        select.select_by_index("2")

        no_link = SeleniumActions.read_select_text(web_element)

        # CTA Button 2
        element_path = MartindalePageData.BANNER_MODULE_CONTENT_ADD_LINK_TYPE_TWO
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        Tools.sleep(2)

        select = Select(web_element)
        select.select_by_index("0")

        my_pages_two = SeleniumActions.read_select_text(web_element)

        select = Select(web_element)
        select.select_by_index("1")

        external_link_two = SeleniumActions.read_select_text(web_element)

        select = Select(web_element)
        select.select_by_index("2")

        no_link_two = SeleniumActions.read_select_text(web_element)

        if my_pages == "My Pages" and external_link == "External Link" and no_link == "No Link" and my_pages_two \
                == "My Pages" and external_link_two == "External Link" and no_link_two == "No Link":
            print("C18521024 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521024',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18521024 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521024',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18521024 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18521040
    ####

    try:
        # CTA Button 1
        element_path = MartindalePageData.BANNER_MODULE_CONTENT_ADD_LINK_TYPE
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        select = Select(web_element)
        select.select_by_index("0")

        Tools.sleep(2)

        element_path = MartindalePageData.BANNER_MODULE_CONTENT_ADD_LINK_PAGE_LABEL
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        link_page_element = SeleniumActions.read_web_element_text(web_element)

        # CTA Button 2
        element_path = MartindalePageData.BANNER_MODULE_CONTENT_ADD_LINK_TYPE_TWO
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        select = Select(web_element)
        select.select_by_index("0")

        Tools.sleep(2)

        element_path = MartindalePageData.BANNER_MODULE_CONTENT_ADD_LINK_PAGE_LABEL_TWO
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        link_page_element_two = SeleniumActions.read_web_element_text(web_element)

        if link_page_element == "Link Page *" and link_page_element_two == "Link Page *":
            print("C18521040 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521040',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18521040 Failed")
            print("Actual Results: " + web_element)
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521040',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18521040 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18521041
    ####

    try:
        # CTA Button 1
        element_path = MartindalePageData.BANNER_MODULE_CONTENT_ADD_LINK_TYPE
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        select = Select(web_element)
        select.select_by_index("1")

        Tools.sleep(2)

        element_path = MartindalePageData.BANNER_MODULE_CONTENT_ADD_LINK_PAGE_URL_LABEL
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        link_page_element = SeleniumActions.read_web_element_text(web_element)

        # CTA Button 2
        element_path = MartindalePageData.BANNER_MODULE_CONTENT_ADD_LINK_TYPE_TWO
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        select = Select(web_element)
        select.select_by_index("1")

        Tools.sleep(2)

        element_path = MartindalePageData.BANNER_MODULE_CONTENT_ADD_LINK_PAGE_URL_LABEL_TWO
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        link_page_element_two = SeleniumActions.read_web_element_text(web_element)

        if link_page_element == "URL *" and link_page_element_two == "URL *":
            print("C18521041 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521041',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18521041 Failed")
            print("Actual Results: " + web_element)
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521041',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18521041 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18521026
    ####

    try:
        # CTA Button 1
        cta_url_test = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_URL_TEXT)
        SeleniumActions.write_to_element(web_driver, cta_url_test, "http://www.blackvinyl45.com")

        # CTA Button 2
        cta_url_test_two = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_URL_TEXT_TWO)
        SeleniumActions.write_to_element(web_driver, cta_url_test_two, "http://www.legalizeferrets.org")

        # This test case needs work; no xpath available for the error text.  This is a bug: SMBWMGR-7136
        print("C18521026 Failed")
        result = client.send_post(
            'add_result_for_case/' + current_test_run_id + '/18521026',
            {'status_id': 5, 'comment': 'SMBWMGR-7136'}
        )

        # CTA Button 2

        #if link_page_element == "URL *" and link_page_element_two == "URL *":
        #    print("C18521026 Passed")
        #    result = client.send_post(
        #        'add_result_for_case/' + current_test_run_id + '/18521026',
        #        {'status_id': 1, 'comment': ''}
        #    )
        #else:
        #    print("C18521026 Failed")
        #    print("Actual Results: " + web_element)
        #    result = client.send_post(
        #        'add_result_for_case/' + current_test_run_id + '/18521026',
        #        {'status_id': 5, 'comment': ''}
        #    )

    except:
        print("C18521026 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18521042
    ####

    try:
        click_save_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_BANNER_SAVE_BUTTON)
        SeleniumActions.click_element(web_driver, click_save_button)

        element_path = MartindalePageData.BANNER_TITLE_ERROR
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        banner_title_error = SeleniumActions.read_web_element_text(web_element)

        element_path = MartindalePageData.BANNER_CAPTION_ERROR
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        banner_caption_error = SeleniumActions.read_web_element_text(web_element)

        banner_title = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_TITLE)
        SeleniumActions.write_to_element \
            (web_driver, banner_title, "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ012")

        banner_caption = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_CAPTION)
        SeleniumActions.write_to_element \
            (web_driver, banner_caption, "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ012ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ012")

        click_save_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_BANNER_SAVE_BUTTON)
        SeleniumActions.click_element(web_driver, click_save_button)

        element_path = MartindalePageData.BANNER_TITLE_ERROR
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        banner_title_error_two = SeleniumActions.read_web_element_text(web_element)

        element_path = MartindalePageData.BANNER_CAPTION_ERROR
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        banner_caption_error_two = SeleniumActions.read_web_element_text(web_element)

        if banner_title_error == "This field is required." and banner_caption_error == "This field is required." and \
                banner_title_error_two == "Please enter no more than 100 characters." and \
                banner_caption_error_two == "Please enter no more than 200 characters.":
            print("C18521042 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521042',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18521042 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521042',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18521042 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18521043
    ####

    try:
        banner_title = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_TITLE)
        SeleniumActions.clearTextField(web_driver, banner_title)
        SeleniumActions.write_to_element(web_driver, banner_title, "Automated")

        banner_caption = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_CAPTION)
        SeleniumActions.clearTextField(web_driver, banner_caption)
        SeleniumActions.write_to_element(web_driver, banner_caption, "Test")

        click_save_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_BANNER_SAVE_BUTTON)
        SeleniumActions.click_element(web_driver, click_save_button)
        Tools.sleep(4)

        web_element = SeleniumActions.find_by_xpath(web_driver, "//*[contains(@id, 'item_item-')]")
        new_banner_test = SeleniumActions.read_web_element_text(web_element)

        if new_banner_test == "Title: Automated\nTest":
            print("C18521043 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521043',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18521043 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521043',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18521043 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18521045
    ####

    try:
        web_element = SeleniumActions.find_by_xpath(web_driver, "//*[contains(@id, 'edit_item-')]")
        SeleniumActions.click_element(web_driver, web_element)

        Tools.sleep(3)

        banner_title = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_TITLE)

        if SeleniumActions.element_is_visible(web_driver, banner_title):
            print("C18521045 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521045',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18521045 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521045',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18521045 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18521044
    ####

    try:
        web_element = SeleniumActions.find_by_xpath(web_driver, MartindalePageData.ADD_BANNER_CANCEL_BUTTON)
        SeleniumActions.click_element(web_driver, web_element)

        Tools.sleep(3)

        element_path = MartindalePageData.GALLERY_BANNER_TITLE
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        if SeleniumActions.element_is_visible(web_driver, web_element):
            print("C18521044 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521044',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18521044 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521044',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18521044 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18521046
    ####

    try:
        web_element = SeleniumActions.find_by_xpath(web_driver, "//*[contains(@id, 'delete_item-')]")
        SeleniumActions.click_element(web_driver, web_element)

        Tools.sleep(2)

        web_element = SeleniumActions.find_by_xpath(web_driver, MartindalePageData.DELETE_BANNER_CONFIRMATION)
        SeleniumActions.element_is_visible(web_driver, web_element)

        web_element = SeleniumActions.find_by_xpath(web_driver, MartindalePageData.DELETE_BANNER_CANCEL_BUTTON)
        SeleniumActions.click_element(web_driver, web_element)

        Tools.sleep(2)

        web_element = SeleniumActions.find_by_xpath(web_driver, "//*[contains(@id, 'item_item-')]")
        SeleniumActions.element_is_visible(web_driver, web_element)

        web_element = SeleniumActions.find_by_xpath(web_driver, "//*[contains(@id, 'delete_item-')]")
        SeleniumActions.click_element(web_driver, web_element)

        Tools.sleep(2)

        web_element = SeleniumActions.find_by_xpath(web_driver, MartindalePageData.DELETE_BANNER_OK_BUTTON)
        SeleniumActions.click_element(web_driver, web_element)

        Tools.sleep(4)

        web_element = SeleniumActions.find_by_xpath(web_driver, "//*[contains(@id, 'item_item-')]")
        new_banner_test = SeleniumActions.read_web_element_text(web_element)

        if new_banner_test == "Title: Title\nCaption":
            print("C18521046 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521046',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18521046 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521046',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18521046 Not Tested")
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

        Tools.sleep(4)

        web_driver.close()
        print("Banner module test run complete.")

    except:
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


####
#  Run
####


if __name__ == "__main__":
    test_suite()

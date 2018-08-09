from library.selenium_actions import *
from library.tools import Tools
from library.selenium_driver import SeleniumDriver
from library.page_data.martindale_app.martindale_data import MartindalePageData
from testrail.testrail import *

import sys


####
#  blade Module Test
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

        web_driver.switch_to_window(web_driver.window_handles[1])

    except:
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)

    print("Executing Featured Blocks module tests...")


    ####
    # Execute Test Case C18521219
    ####

    try:
        web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))
        add_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_MODULE_BUTTON)
        SeleniumActions.click_element(web_driver, add_module)

        select_featured_block_module = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_MODULE_BUTTON)
        SeleniumActions.click_element(web_driver, select_featured_block_module)

        click_featured_block_radio = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.SAVED_FEATURED_BLOCK_RADIO_BUTTON)
        SeleniumActions.click_element(web_driver, click_featured_block_radio)

        Tools.sleep(2)

        element_path = MartindalePageData.MODULE_NAME_DROP_DOWN
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        Tools.sleep(2)

        select = Select(web_element)
        select.select_by_index("2")

        click_submit_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE_SUBMIT_BUTTON)
        SeleniumActions.click_element(web_driver, click_submit_button)

        Tools.sleep(5)

        click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_MODULE)
        SeleniumActions.click_element(web_driver, click_blade_module)

        Tools.sleep(2)

        click_edit_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_MODULE_EDIT_BUTTON)
        SeleniumActions.click_element(web_driver, click_edit_button)

        Tools.sleep(5)

        web_driver.switch_to.default_content()
        element_path = MartindalePageData.FEATURED_BLOCKS_MODULE_HEADER
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        blade_text = SeleniumActions.read_web_element_text(web_element)

        if blade_text == "FEATURED BLOCKS MODULE":
            print("C18521219 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521219',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18521219 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521219',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18521219 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18521222
    ####

    try:
        click_settings_tab = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_SETTINGS_TAB)
        SeleniumActions.click_element(web_driver, click_settings_tab)

        Tools.sleep(1)

        web_element = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_SETTINGS_SHOW_TITLE)

        if SeleniumActions.element_is_visible(web_driver, web_element):
            print("C18521222 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521222',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18521222 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521222',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18521222 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18527231
    ####

    try:
        click_layout_tab = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATUREDE_BLOCKS_LAYOUT_TAB)
        SeleniumActions.click_element(web_driver, click_layout_tab)

        Tools.sleep(1)

        web_element = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_LAYOUT_LABEL)

        if SeleniumActions.element_is_visible(web_driver, web_element):
            print("C18527231 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527231',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18527231 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527231',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18527231 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18521229
    ####

    try:
        click_content_tab = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_CONTENT_TAB)
        SeleniumActions.click_element(web_driver, click_content_tab)

        Tools.sleep(1)

        web_element = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_CONTENT_TITLE)

        if SeleniumActions.element_is_visible(web_driver, web_element):
            print("C18521229 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521229',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18521229 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521229',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18521229 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18521228
    ####

    try:
        # Module Information
        click_module_info = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_MODULE_INFORMATION)
        SeleniumActions.click_element(web_driver, click_module_info)

        Tools.sleep(1)

        web_element = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_CONTENT_TITLE)

        if SeleniumActions.element_is_visible(web_driver, web_element):
            test_one = "Failed"
        else:
            test_one = "Passed"

        SeleniumActions.click_element(web_driver, click_module_info)

        Tools.sleep(2)

        web_element = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_CONTENT_TITLE)

        if SeleniumActions.element_is_visible(web_driver, web_element):
            test_two = "Passed"
        else:
            test_two = "Failed"

        # Manage Content
        click_manage_content = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_MANAGE_CONTENT)
        SeleniumActions.click_element(web_driver, click_manage_content)

        Tools.sleep(1)

        web_element = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_CONTENT_ADD_CONTENT)

        if SeleniumActions.element_is_visible(web_driver, web_element):
            test_three = "Failed"
        else:
            test_three = "Passed"

        SeleniumActions.click_element(web_driver, click_manage_content)

        Tools.sleep(2)

        web_element = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_CONTENT_ADD_CONTENT)

        if SeleniumActions.element_is_visible(web_driver, web_element):
            test_four = "Passed"
        else:
            test_four = "Failed"

        if test_one == "Passed" and test_two == "Passed" and test_three == "Passed" and test_four == "Passed":
            print("C18521228 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521228',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18521228 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521228',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18521228 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18521223
    ####

    try:
        click_add_content = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_CONTENT_ADD_CONTENT)
        SeleniumActions.click_element(web_driver, click_add_content)

        Tools.sleep(1)

        web_element = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_CONTENT_BLOCK_TITLE)

        if SeleniumActions.element_is_visible(web_driver, web_element):
            print("C18521223 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521223',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18521223 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521223',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18521223 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18527150
    ####

    try:
        click_csncel_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_CONTENT_CANCEL_BUTTON)
        SeleniumActions.click_element(web_driver, click_csncel_button)

        Tools.sleep(3)

        web_element = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_MODULE_INFORMATION)

        if SeleniumActions.element_is_visible(web_driver, web_element):
            print("C18527150 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527150',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18527150 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527150',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18527150 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18521225
    ####

    try:
        click_edit_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_EDIT_BUTTON)
        SeleniumActions.click_element(web_driver, click_edit_button)

        Tools.sleep(1)

        web_element = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_CONTENT_BLOCK_TITLE)

        if SeleniumActions.element_is_visible(web_driver, web_element):
            print("C18521225 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521225',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18521225 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521225',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18521225 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18521224
    ####
    try:
        click_csncel_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_CONTENT_CANCEL_BUTTON)
        SeleniumActions.click_element(web_driver, click_csncel_button)

        Tools.sleep(3)

        click_delete_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_DELETE_BUTTON)
        SeleniumActions.click_element(web_driver, click_delete_button)

        Tools.sleep(1)

        delete_modal = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.DELETE_FEATURED_BLOCKS_MODAL)
        featured_blocks_delete_modal = SeleniumActions.read_web_element_text(delete_modal)

        click_csncel_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.DELETE_FEATURED_BLOCKS_MODAL_CANCEL_BUTTON)
        SeleniumActions.click_element(web_driver, click_csncel_button)

        Tools.sleep(1)

        featured_block = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCK)


        if SeleniumActions.element_is_visible(web_driver, featured_block):
            test_one == "Passed"
        else:
            test_one == "Failed"

        click_delete_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_DELETE_BUTTON)
        SeleniumActions.click_element(web_driver, click_delete_button)

        Tools.sleep(1)
        click_modal_ok = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.DELETE_FEATURED_BLOCKS_MODAL_OK_BUTTON)
        SeleniumActions.click_element(web_driver, click_modal_ok)

        Tools.sleep(2)

        if SeleniumActions.check_element_exists(web_driver, "//*[contains(@id, 'link_link-')]/div[2]/div/div[2]/div[1]"):
            test_two == "Failed"
        else:
            test_two == "Passed"

        if featured_blocks_delete_modal == "Are you sure you want to remove this link?" and test_one == "Passed" and \
                test_two == "Passed":
            print("C18521224 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521224',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18521224 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18521224',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18521224 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18527155
    ####
    try:
        click_add_content = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_CONTENT_ADD_CONTENT)
        SeleniumActions.click_element(web_driver, click_add_content)

        Tools.sleep(3)

        click_select_gallery = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_CONTENT_SELECT_FROM_GALLERY)
        SeleniumActions.click_element(web_driver, click_select_gallery)

        Tools.sleep(3)

        click_gallery_image = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_CONTENT_SELECT_GALLERY_IMAGE)
        SeleniumActions.click_element(web_driver, click_gallery_image)

        element_path = MartindalePageData.ADD_CONTENT_SELECT_GALLERY_IMAGE_TEXT
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)
        image_text = SeleniumActions.read_web_element_text(web_element)

        click_insert_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_CONTENT_SELECT_GALLERY_INSERT_BUTTON)
        SeleniumActions.click_element(web_driver, click_insert_button)

        Tools.sleep(2)

        element_path = MartindalePageData.ADD_CONTENT_IMAGE_CONTAINER
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)
        SeleniumActions.move_to_element(web_driver, web_element)

        element_path = MartindalePageData.ADD_CONTENT_IMAGE_TEXT
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)
        added_image_text = SeleniumActions.read_web_element_text(web_element)

        if "/" + image_text == added_image_text:
            print("C18527155 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527155',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18527155 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527155',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18527155 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18527161
    ####
    try:
        element_path = MartindalePageData.ADD_CONTENT_IMAGE_CONTAINER
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)
        SeleniumActions.move_to_element(web_driver, web_element)

        click_replace_image = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_CONTENT_REPLACE_BUTTON)
        SeleniumActions.click_element(web_driver, click_replace_image)

        Tools.sleep(3)

        gallery_image = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_CONTENT_SELECT_GALLERY_IMAGE)

        if SeleniumActions.element_is_visible(web_driver, gallery_image):
            print("C18527161 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527161',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18527161 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527161',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18527161 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18527151
    ####
    try:
        click_cancel_image = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_CONTENT_SELECT_GALLERY_CANCEL_BUTTON)
        SeleniumActions.click_element(web_driver, click_cancel_image)

        Tools.sleep(3)

        element_path = MartindalePageData.FEATURED_BLOCK_LINK_TYPE
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        select = Select(web_element)
        select.select_by_index("1")

        Tools.sleep(2)

        link_drop_down = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCK_LINK_DROP_DOWN)

        if SeleniumActions.element_is_visible(web_driver, link_drop_down):
            print("C18527151 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527151',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18527151 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527151',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18527151 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18527152
    ####
    try:
        element_path = MartindalePageData.FEATURED_BLOCK_LINK_TYPE
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        select = Select(web_element)
        select.select_by_index("2")

        Tools.sleep(2)

        link_drop_down = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCK_EXTERNAL_LINK)

        if SeleniumActions.element_is_visible(web_driver, link_drop_down):
            print("C18527152 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527152',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18527152 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527152',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18527152 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18527172
    ####
    try:
        click_select_gallery = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_CONTENT_SELECT_FROM_GALLERY)
        SeleniumActions.click_element(web_driver, click_select_gallery)

        Tools.sleep(3)

        click_gallery_image = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_CONTENT_SELECT_GALLERY_IMAGE)
        SeleniumActions.click_element(web_driver, click_gallery_image)

        click_insert_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_CONTENT_SELECT_GALLERY_INSERT_BUTTON)
        SeleniumActions.click_element(web_driver, click_insert_button)

        Tools.sleep(2)

        write_block_title = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_CONTENT_BLOCK_TITLE)
        SeleniumActions.write_to_element(web_driver, write_block_title, "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ012")

        click_save_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_CONTENT_SAVE_BUTTON)
        SeleniumActions.click_element(web_driver, click_save_button)
        Tools.sleep(2)

        element_path = MartindalePageData.ADD_BLOCK_TITLE_ERROR
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        block_title_error = SeleniumActions.read_web_element_text(web_element)

        write_block_description = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_BLOCK_DESCRIPTION)
        SeleniumActions.write_to_element(web_driver, write_block_description, "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ012ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ012ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ012")

        click_save_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_CONTENT_SAVE_BUTTON_TWO)
        SeleniumActions.click_element(web_driver, click_save_button)

        element_path = MartindalePageData.ADD_BLOCK_DESCRIPTION_ERROR
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        block_description_error = SeleniumActions.read_web_element_text(web_element)

        if block_title_error == "Please enter no more than 100 characters." and block_description_error == \
                "Please enter no more than 300 characters.":
            print("C18527172 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527172',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18527172 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527172',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18527172 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)




    Tools.sleep(4526)



    ####
    # Execute Test Case C18527153
    ####
    try:
        write_block_title = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_CONTENT_BLOCK_TITLE)
        SeleniumActions.clearTextField(web_driver, write_block_title)
        SeleniumActions.write_to_element(web_driver, write_block_title, "Automated")

        write_block_description = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_BLOCK_DESCRIPTION)
        SeleniumActions.clearTextField(web_driver, write_block_description)
        SeleniumActions.write_to_element(web_driver, write_block_description, "This is an automated test.")

        write_external_link_text = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCK_EXTERNAL_LINK)
        SeleniumActions.write_to_element(web_driver, write_external_link_text, "http://www.blackvinyl45.com")

        write_block_alt_text = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_ALT_TEXT)
        SeleniumActions.write_to_element(web_driver, write_block_alt_text, "alt")

        click_save_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_CONTENT_SAVE_BUTTON_TWO)
        SeleniumActions.click_element(web_driver, click_save_button)

        Tools.sleep(3)

        saved_image = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCK_IMAGE)

        if SeleniumActions.element_is_visible(web_driver, saved_image):
            print("C18527153 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527153',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18527153 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527153',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18527153 Not Tested")
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
        print("Featured Blocks module test run complete.")


    except:
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


####
#  Run
####


if __name__ == "__main__":
    test_suite()

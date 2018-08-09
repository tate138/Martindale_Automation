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


    print("Executing Blade module tests...")


####
# Execute Test Case C18527973
####

    try:
        web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

        add_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_MODULE_BUTTON)
        SeleniumActions.click_element(web_driver, add_module)

        select_blade_module = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_MODULE_BUTTON)
        SeleniumActions.click_element(web_driver, select_blade_module)

        click_blade_radio = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.SAVED_BLADE_RADIO_BUTTON)
        SeleniumActions.click_element(web_driver, click_blade_radio)

        Tools.sleep(2)

        element_path = MartindalePageData.MODULE_NAME_DROP_DOWN
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        Tools.sleep(2)

        select = Select(web_element)
        select.select_by_index("1")

        click_submit_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE_SUBMIT_BUTTON)
        SeleniumActions.click_element(web_driver, click_submit_button)

        Tools.sleep(5)

        click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_MODULE)
        SeleniumActions.click_element(web_driver, click_blade_module)

        Tools.sleep(2)

        click_edit_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_MODULE_EDIT_BUTTON)
        SeleniumActions.click_element(web_driver, click_edit_button)

        Tools.sleep(5)

        web_driver.switch_to.default_content()
        element_path = MartindalePageData.BLADE_TITLE
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        blade_text = SeleniumActions.read_web_element_text(web_element)

        if blade_text == "BLADE MODULE":
            print("C18527973 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527973',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18527973 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527973',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18527973 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18527974 and C18527997
    ####

    try:
        click_settings_tab = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_TAB)
        SeleniumActions.click_element(web_driver, click_settings_tab)

        Tools.sleep(2)

        element_path = MartindalePageData.BLADE_SETTINGS_ELEMENT_VISIBILITY
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        settings_element_visibility = SeleniumActions.read_web_element_text(web_element)

        element_path = MartindalePageData.BLADE_SETTINGS_SETTINGS
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        settings_settings = SeleniumActions.read_web_element_text(web_element)

        element_path = MartindalePageData.BLADE_SETTINGS_MODULE_VISIBILITY
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        settings_module_visibility = SeleniumActions.read_web_element_text(web_element)

        if settings_element_visibility == "ELEMENT VISIBILITY" and settings_settings == "BLADE SETTINGS" and \
                settings_module_visibility == "MODULE VISIBILITY":
            print("C18527974 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527974',
                {'status_id': 1, 'comment': ''}
            )
            print("C18527997 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527997',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18527974 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527974',
                {'status_id': 5, 'comment': ''}
            )
            print("C18527997 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527997',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18527997 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18527975
    ####

    try:
        click_content_tab = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_TAB)
        SeleniumActions.click_element(web_driver, click_content_tab)

        Tools.sleep(2)

        write_new_title = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_TITLE)
        SeleniumActions.clearTextField(web_driver, write_new_title)
        SeleniumActions.write_to_element \
            (web_driver, write_new_title, "Blade")

        write_new_caption = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_CAPTION)
        SeleniumActions.clearTextField(web_driver, write_new_caption)
        SeleniumActions.write_to_element \
            (web_driver, write_new_caption, "Runner")

        write_new_alt_text = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_ALT_TEXT)
        SeleniumActions.clearTextField(web_driver, write_new_alt_text)
        SeleniumActions.write_to_element \
            (web_driver, write_new_alt_text, "alt")

        write_new_image_title = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_IMAGE_TITLE)
        SeleniumActions.clearTextField(web_driver, write_new_image_title)
        SeleniumActions.write_to_element \
            (web_driver, write_new_image_title, "image")

        write_new_cta_one_link_text = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_CTA_ONE_LINK_TEXT)
        SeleniumActions.clearTextField(web_driver, write_new_cta_one_link_text)
        SeleniumActions.write_to_element \
            (web_driver, write_new_cta_one_link_text, "CTA One")

        write_new_cta_two_link_text = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_CTA_TWO_LINK_TEXT)
        SeleniumActions.clearTextField(web_driver, write_new_cta_two_link_text)
        SeleniumActions.write_to_element \
            (web_driver, write_new_cta_two_link_text, "CTA Two")

        click_done_button = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_DONE_BUTTON)
        SeleniumActions.click_element(web_driver, click_done_button)

        Tools.sleep(5)

        web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

        element_path = MartindalePageData.BLADE_IFRAME_TITLE
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        blade_iframe_title = SeleniumActions.read_web_element_text(web_element)

        element_path = MartindalePageData.BLADE_IFRAME_CAPTION
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        blade_iframe_caption = SeleniumActions.read_web_element_text(web_element)

        if blade_iframe_title == "Blade" and blade_iframe_caption == "Runner":
            print("C18527975 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527975',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18527975 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527975',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18527975 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18678388
    ####

    try:
        click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_MODULE)
        SeleniumActions.click_element(web_driver, click_blade_module)

        Tools.sleep(2)

        click_edit_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_MODULE_EDIT_BUTTON)
        SeleniumActions.click_element(web_driver, click_edit_button)

        Tools.sleep(5)

        web_driver.switch_to.default_content()

        click_settings_tab = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_TAB)
        SeleniumActions.click_element(web_driver, click_settings_tab)

        click_show_banner_title = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_SHOW_BLADE_TITLE)
        SeleniumActions.click_element(web_driver, click_show_banner_title)

        click_done_button = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_DONE_BUTTON)
        SeleniumActions.click_element(web_driver, click_done_button)

        Tools.sleep(5)

        web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

        if SeleniumActions.check_element_exists(web_driver, "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div/div[1]/div[1]/h3"):
            blade_title_existence = "true"
        else:
            blade_title_existence = "false"

        if blade_title_existence == "false":
            print("C18678388 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18678388',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18678388 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18678388',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18678388 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18678389
    ####

    try:
        click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_MODULE)
        SeleniumActions.click_element(web_driver, click_blade_module)

        Tools.sleep(2)

        click_edit_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_MODULE_EDIT_BUTTON)
        SeleniumActions.click_element(web_driver, click_edit_button)

        Tools.sleep(5)

        web_driver.switch_to.default_content()

        click_settings_tab = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_TAB)
        SeleniumActions.click_element(web_driver, click_settings_tab)

        click_show_banner_title = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_SHOW_BLADE_TITLE)
        SeleniumActions.click_element(web_driver, click_show_banner_title)

        click_show_banner_caption = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_SHOW_BLADE_CAPTION)
        SeleniumActions.click_element(web_driver, click_show_banner_caption)

        click_done_button = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_DONE_BUTTON)
        SeleniumActions.click_element(web_driver, click_done_button)

        Tools.sleep(5)

        web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

        if SeleniumActions.check_element_exists(web_driver, "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div/div[1]/div[1]/h4"):
            blade_title_existence = "true"
        else:
            blade_title_existence = "false"

        if blade_title_existence == "false":
            print("C18678389 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18678389',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18678389 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18678389',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18678389 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18678390
    ####

    try:
        click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_MODULE)
        SeleniumActions.click_element(web_driver, click_blade_module)

        Tools.sleep(2)

        click_edit_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_MODULE_EDIT_BUTTON)
        SeleniumActions.click_element(web_driver, click_edit_button)

        Tools.sleep(5)

        web_driver.switch_to.default_content()

        click_settings_tab = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_TAB)
        SeleniumActions.click_element(web_driver, click_settings_tab)

        click_show_banner_caption = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_SHOW_BLADE_CAPTION)
        SeleniumActions.click_element(web_driver, click_show_banner_caption)

        click_show_read_more = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_SHOW_READ_MORE)
        SeleniumActions.click_element(web_driver, click_show_read_more)

        click_done_button = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_DONE_BUTTON)
        SeleniumActions.click_element(web_driver, click_done_button)

        Tools.sleep(5)

        web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

        if SeleniumActions.check_element_exists \
                    (web_driver, "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div/div[1]/div[2]/a"):
            blade_title_existence = "true"
        else:
            blade_title_existence = "false"

        if blade_title_existence == "false":
            print("C18678390 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18678390',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18678390 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18678390',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18678390 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18678391
    ####

    try:
        click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_MODULE)
        SeleniumActions.click_element(web_driver, click_blade_module)

        Tools.sleep(2)

        click_edit_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_MODULE_EDIT_BUTTON)
        SeleniumActions.click_element(web_driver, click_edit_button)

        Tools.sleep(5)
        web_driver.switch_to.default_content()

        click_settings_tab = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_TAB)
        SeleniumActions.click_element(web_driver, click_settings_tab)
        click_show_read_more = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_SHOW_READ_MORE)
        SeleniumActions.click_element(web_driver, click_show_read_more)

        click_show_cta_button_one = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_SHOW_CTA_ONE)
        SeleniumActions.click_element(web_driver, click_show_cta_button_one)
        click_done_button = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_DONE_BUTTON)
        SeleniumActions.click_element(web_driver, click_done_button)

        Tools.sleep(5)

        web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

        element_path = MartindalePageData.BLADE_IFRAME_CTA_BUTTON_TWO
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)
        read_cta_button = SeleniumActions.read_web_element_text(web_element)

        if read_cta_button == "CTA TWO":
            print("C18678391 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18678391',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18678391 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18678391',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18678391 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18678392
    ####

    try:
        click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_MODULE)
        SeleniumActions.click_element(web_driver, click_blade_module)

        Tools.sleep(2)

        click_edit_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_MODULE_EDIT_BUTTON)
        SeleniumActions.click_element(web_driver, click_edit_button)

        Tools.sleep(5)

        web_driver.switch_to.default_content()

        click_settings_tab = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_TAB)
        SeleniumActions.click_element(web_driver, click_settings_tab)

        click_show_cta_button_one = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_SHOW_CTA_ONE)
        SeleniumActions.click_element(web_driver, click_show_cta_button_one)

        click_show_cta_button_two = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_SHOW_CTA_TWO)
        SeleniumActions.click_element(web_driver, click_show_cta_button_two)

        click_done_button = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_DONE_BUTTON)
        SeleniumActions.click_element(web_driver, click_done_button)

        Tools.sleep(5)

        web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

        element_path = MartindalePageData.BLADE_IFRAME_CTA_BUTTON_TWO
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)
        read_cta_button = SeleniumActions.read_web_element_text(web_element)

        if read_cta_button == "CTA ONE":
            print("C18678392 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18678392',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18678392 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18678392',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18678392 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18678385
    ####

    try:
        click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_MODULE)
        SeleniumActions.click_element(web_driver, click_blade_module)

        Tools.sleep(2)

        click_edit_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_MODULE_EDIT_BUTTON)
        SeleniumActions.click_element(web_driver, click_edit_button)

        Tools.sleep(5)

        web_driver.switch_to.default_content()

        click_settings_tab = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_TAB)
        SeleniumActions.click_element(web_driver, click_settings_tab)

        click_show_cta_button_two = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_SHOW_CTA_TWO)
        SeleniumActions.click_element(web_driver, click_show_cta_button_two)

        web_element = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_SHOW_BLADE_TITLE)

        click_element_visibility = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_ELEMENT_VISIBILITY)
        SeleniumActions.click_element(web_driver, click_element_visibility)

        Tools.sleep(1)

        SeleniumActions.element_is_not_visible(web_element)

        click_element_visibility = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_ELEMENT_VISIBILITY)
        SeleniumActions.click_element(web_driver, click_element_visibility)

        Tools.sleep(1)

        web_element = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_SHOW_BLADE_TITLE)

        if SeleniumActions.element_is_visible(web_driver, web_element):
            print("C18678385 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18678385',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18678385 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18678385',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18678385 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18678386
    ####

    try:
        web_element = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_SWAP_MEDIA_TEXT)

        click_blade_settings = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_SETTINGS)
        SeleniumActions.click_element(web_driver, click_blade_settings)

        Tools.sleep(1)

        SeleniumActions.element_is_not_visible(web_element)

        click_blade_settings = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_SETTINGS)
        SeleniumActions.click_element(web_driver, click_blade_settings)

        Tools.sleep(1)

        web_element = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_SWAP_MEDIA_TEXT)

        if SeleniumActions.element_is_visible(web_driver, web_element):
            print("C18678386 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18678386',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18678386 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18678386',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18678386 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18678387
    ####

    try:
        web_element = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_DESKTOP_MODULE)

        click_module_visibility = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_MODULE_VISIBILITY)
        SeleniumActions.click_element(web_driver, click_module_visibility)

        Tools.sleep(1)

        SeleniumActions.element_is_not_visible(web_element)

        click_module_visibility = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_MODULE_VISIBILITY)
        SeleniumActions.click_element(web_driver, click_module_visibility)

        Tools.sleep(1)

        web_element = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_DESKTOP_MODULE)

        if SeleniumActions.element_is_visible(web_driver, web_element):
            print("C18678387 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18678387',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18678387 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18678387',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18678387 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18678393
    ####

    try:
        click_swap_setting = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_SWAP_MEDIA_TEXT)
        SeleniumActions.click_element(web_driver, click_swap_setting)

        click_done_button = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_DONE_BUTTON)
        SeleniumActions.click_element(web_driver, click_done_button)

        Tools.sleep(5)

        web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))
        web_element = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_IFRAME_IMAGE_LEFT)

        SeleniumActions.element_is_visible(web_driver, web_element)

        click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_MODULE)
        SeleniumActions.click_element(web_driver, click_blade_module)

        Tools.sleep(2)

        click_edit_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_MODULE_EDIT_BUTTON)
        SeleniumActions.click_element(web_driver, click_edit_button)

        Tools.sleep(5)

        web_driver.switch_to.default_content()

        click_settings_tab = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_TAB)
        SeleniumActions.click_element(web_driver, click_settings_tab)

        click_swap_setting = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_SETTINGS_SWAP_MEDIA_TEXT)
        SeleniumActions.click_element(web_driver, click_swap_setting)

        click_done_button = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_DONE_BUTTON)
        SeleniumActions.click_element(web_driver, click_done_button)

        Tools.sleep(5)

        web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))
        web_element = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_IFRAME_IMAGE_RIGHT)

        if SeleniumActions.element_is_visible(web_driver, web_element):
            print("C18678393 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18678393',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18678393 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18678393',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18678393 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18527976
    ####

    try:
        click_blade_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_MODULE)
        SeleniumActions.click_element(web_driver, click_blade_module)

        Tools.sleep(2)

        click_edit_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_MODULE_EDIT_BUTTON)
        SeleniumActions.click_element(web_driver, click_edit_button)

        Tools.sleep(5)

        web_driver.switch_to.default_content()
        web_element = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_TITLE)

        click_module_info = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_MODULE_INFORMATION)
        SeleniumActions.click_element(web_driver, click_module_info)

        SeleniumActions.element_is_not_visible(web_element)

        click_module_info = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_MODULE_INFORMATION)
        SeleniumActions.click_element(web_driver, click_module_info)


        if SeleniumActions.element_is_visible(web_driver, web_element):
            print("C18527976 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527976',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18527976 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527976',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18527976 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18527977
    ####

    try:
        web_element = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_SELECT_FROM_GALLERY)

        click_module_info = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_MANAGE_CONTENT)
        SeleniumActions.click_element(web_driver, click_module_info)

        Tools.sleep(2)
        SeleniumActions.element_is_not_visible(web_element)

        click_module_info = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_MANAGE_CONTENT)
        SeleniumActions.click_element(web_driver, click_module_info)

        Tools.sleep(2)

        if SeleniumActions.element_is_visible(web_driver, web_element):
            print("C18527977 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527977',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18527977 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527977',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18527977 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18527978
    ####

    try:
        web_element = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_CTA_ONE_LINK_TEXT)

        click_module_info = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_MANAGE_CTA_BUTTONS)
        SeleniumActions.click_element(web_driver, click_module_info)

        SeleniumActions.element_is_not_visible(web_element)

        click_module_info = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_MANAGE_CTA_BUTTONS)
        SeleniumActions.click_element(web_driver, click_module_info)

        if SeleniumActions.element_is_visible(web_driver, web_element):
            print("C18527978 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527978',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18527978 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527978',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18527978 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18527998
    ####

    try:
        #CTA Button One
        element_path = MartindalePageData.BLADE_CONTENT_CTA_ONE_LINK_TYPE
        cta_one_link_type = SeleniumActions.find_by_xpath(web_driver, element_path)

        select = Select(cta_one_link_type)
        select.select_by_index("0")

        link_page_text = SeleniumActions.read_select_text(cta_one_link_type)
        link_page = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_CTA_ONE_LINK_PAGE)
        SeleniumActions.element_is_visible(web_driver, web_element)

        select = Select(cta_one_link_type)
        select.select_by_index("1")

        url_text = SeleniumActions.read_select_text(cta_one_link_type)
        url_text_box = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_CTA_ONE_URL)
        SeleniumActions.element_is_visible(web_driver, web_element)

        select = Select(cta_one_link_type)
        select.select_by_index("2")

        no_link = SeleniumActions.read_select_text(cta_one_link_type)

        SeleniumActions.element_is_not_visible(link_page)
        SeleniumActions.element_is_not_visible(url_text_box)

        #CTA Button Two
        element_path = MartindalePageData.BLADE_CONTENT_CTA_TWO_LINK_TYPE
        cta_two_link_type = SeleniumActions.find_by_xpath(web_driver, element_path)

        select = Select(cta_two_link_type)
        select.select_by_index("0")

        link_page_text_two = SeleniumActions.read_select_text(cta_two_link_type)
        link_page = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_CTA_TWO_LINK_PAGE)
        SeleniumActions.element_is_visible(web_driver, web_element)

        select = Select(cta_two_link_type)
        select.select_by_index("1")

        url_text_two = SeleniumActions.read_select_text(cta_two_link_type)
        url_text_box = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_CTA_TWO_URL)
        SeleniumActions.element_is_visible(web_driver, web_element)

        select = Select(cta_two_link_type)
        select.select_by_index("2")

        no_link_two = SeleniumActions.read_select_text(cta_two_link_type)

        SeleniumActions.element_is_not_visible(link_page)
        SeleniumActions.element_is_not_visible(url_text_box)

        if link_page_text == "My Pages" and url_text == "External Link" and no_link == "No Link" and link_page_text_two \
                == "My Pages" and url_text_two == "External Link" and no_link_two == "No Link":
            print("C18527998 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527998',
                {'status_id': 1, 'comment': ''}
            )
            print("C18527999 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527999',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18527998 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527998',
                {'status_id': 5, 'comment': ''}
            )
            print("C18527999 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527999',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18527999 Not Tested")
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


    ####
    # Execute Test Case C18527993
    ####

    try:
        # CTA Button One
        element_path = MartindalePageData.BLADE_CONTENT_CTA_ONE_LINK_TYPE
        cta_one_link_type = SeleniumActions.find_by_xpath(web_driver, element_path)

        select = Select(cta_one_link_type)
        select.select_by_index("1")
        Tools.sleep(2)

        url_text_clear = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_CTA_ONE_URL)
        SeleniumActions.write_to_element(web_driver, url_text_clear, "blackvinyl45")

        click_done_button = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_DONE_BUTTON)
        SeleniumActions.click_element(web_driver, click_done_button)

        url_error_msg = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_CTA_ONE_URL_ERROR)
        url_one_error_text = SeleniumActions.read_web_element_text(url_error_msg)

        if url_one_error_text == "Please enter a valid URL.":
            test_one = "Passed"
        else:
            test_one = "Failed"

        url_text_clear = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_CTA_ONE_URL)
        SeleniumActions.clearTextField(web_driver, url_text_clear)
        SeleniumActions.write_to_element(web_driver, url_text_clear, "blackvinyl45.com")

        click_done_button = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_DONE_BUTTON)
        SeleniumActions.click_element(web_driver, click_done_button)

        url_error_msg = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_CTA_ONE_URL_ERROR)
        url_one_error_text = SeleniumActions.read_web_element_text(url_error_msg)

        if url_one_error_text == "Please enter a valid URL.":
            test_two = "Passed"
        else:
            test_two = "Failed"

        url_text_clear = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_CTA_ONE_URL)
        SeleniumActions.clearTextField(web_driver, url_text_clear)
        SeleniumActions.write_to_element(web_driver, url_text_clear, "http://www.blackvinyl45.com")

        url_error_msg = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_CTA_ONE_URL_ERROR)

        if SeleniumActions.element_is_visible(web_driver, url_error_msg):
            test_three = "Failed"
        else:
            test_three = "Passed"

        # CTA Button Two
        element_path = MartindalePageData.BLADE_CONTENT_CTA_TWO_LINK_TYPE
        cta_one_link_type = SeleniumActions.find_by_xpath(web_driver, element_path)

        select = Select(cta_one_link_type)
        select.select_by_index("1")
        Tools.sleep(2)

        url_text_clear = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_CTA_TWO_URL)
        SeleniumActions.write_to_element(web_driver, url_text_clear, "blackvinyl45")

        click_done_button = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_DONE_BUTTON)
        SeleniumActions.click_element(web_driver, click_done_button)

        url_error_msg = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_CTA_TWO_URL_ERROR)
        url_one_error_text = SeleniumActions.read_web_element_text(url_error_msg)

        if url_one_error_text == "Please enter a valid URL.":
            test_four = "Passed"
        else:
            test_four = "Failed"

        url_text_clear = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_CTA_TWO_URL)
        SeleniumActions.clearTextField(web_driver, url_text_clear)
        SeleniumActions.write_to_element(web_driver, url_text_clear, "blackvinyl45.com")

        url_error_msg = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_CTA_TWO_URL_ERROR)
        url_one_error_text = SeleniumActions.read_web_element_text(url_error_msg)

        if url_one_error_text == "Please enter a valid URL.":
            test_five = "Passed"
        else:
            test_five = "Failed"

        url_text_clear = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_CTA_TWO_URL)
        SeleniumActions.clearTextField(web_driver, url_text_clear)
        SeleniumActions.write_to_element(web_driver, url_text_clear, "http://www.blackvinyl45.com")

        click_done_button = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_DONE_BUTTON)
        SeleniumActions.click_element(web_driver, click_done_button)

        url_error_msg = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_CONTENT_CTA_TWO_URL_ERROR)

        if SeleniumActions.element_is_visible(web_driver, url_error_msg):
            test_six = "Failed"
        else:
            test_six = "Passed"

        if test_one == "Passed" and test_two == "Passed" and test_three == "Passed" and test_four == "Passed" \
                and test_five == "Passed" and test_six == "Passed":
            print("C18527993 Passed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527993',
                {'status_id': 1, 'comment': ''}
            )
        else:
            print("C18527993 Failed")
            result = client.send_post(
                'add_result_for_case/' + current_test_run_id + '/18527993',
                {'status_id': 5, 'comment': ''}
            )

    except:
        print("C18527993 Not Tested")
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
        print("Blade module test run complete.")


    except:
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


####
#  Run
####


if __name__ == "__main__":
    test_suite()

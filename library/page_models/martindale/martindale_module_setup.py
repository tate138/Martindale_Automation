from library.page_data.martindale_app.martindale_data import MartindalePageData
from library.selenium_actions import SeleniumActions
from library.tools import Tools

from tests.test_setup.common_setup import CommonSetup


class MartindaleModuleSetup:

    @staticmethod
    def module_open(web_driver):
        web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))

        add_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_MODULE_BUTTON)
        SeleniumActions.click_element(web_driver, add_module)

        # Select module button
        if CommonSetup.selected_module == "banner":
            select_banner_module = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_MODULE_BUTTON)
            SeleniumActions.click_element(web_driver, select_banner_module)
        elif CommonSetup.selected_module == "blade":
            select_blade_module = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BLADE_MODULE_BUTTON)
            SeleniumActions.click_element(web_driver, select_blade_module)
        elif CommonSetup.selected_module == "cta":
            select_cta_module = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_MODULE_BUTTON)
            SeleniumActions.click_element(web_driver, select_cta_module)
        elif CommonSetup.selected_module == "featured":
            select_featured_block_module = \
                SeleniumActions.fetch_web_element(web_driver, MartindalePageData.FEATURED_BLOCKS_MODULE_BUTTON)
            SeleniumActions.click_element(web_driver, select_featured_block_module)
        else:
            print("Error: Module not found.")

        click_module_radio = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.SAVED_MODULE_RADIO_BUTTON)
        SeleniumActions.click_element(web_driver, click_module_radio)

        element_path = MartindalePageData.MODULE_NAME_DROP_DOWN
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        Tools.sleep(2)

        SeleniumActions.select_by_text(web_element, "automation_only")

        click_submit_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE_SUBMIT_BUTTON)
        SeleniumActions.click_element(web_driver, click_submit_button)

        Tools.sleep(5)


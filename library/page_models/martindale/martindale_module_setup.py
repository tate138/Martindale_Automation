from library.page_data.martindale_app.martindale_data import MartindalePageData
from library.selenium_actions import SeleniumActions
from library.tools import Tools


class MartindaleModuleSetup:

    @staticmethod
    def banner_module_edit(web_driver):
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

        SeleniumActions.select_by_index(web_element, "1")

        click_submit_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE_SUBMIT_BUTTON)
        SeleniumActions.click_element(web_driver, click_submit_button)

        Tools.sleep(5)

        click_banner_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.BANNER_MODULE)
        SeleniumActions.click_element(web_driver, click_banner_module)

        Tools.sleep(2)


    @staticmethod
    def cta_module_edit(web_driver):
        web_driver.switch_to.frame(web_driver.find_element_by_xpath(MartindalePageData.MARTINDALE_IFRAME))
        add_module = SeleniumActions.fetch_web_element(web_driver, MartindalePageData.ADD_MODULE_BUTTON)
        SeleniumActions.click_element(web_driver, add_module)

        select_featured_block_module = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.CTA_MODULE_BUTTON)
        SeleniumActions.click_element(web_driver, select_featured_block_module)

        click_featured_block_radio = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.SAVED_FEATURED_BLOCK_RADIO_BUTTON)
        SeleniumActions.click_element(web_driver, click_featured_block_radio)

        Tools.sleep(2)

        element_path = MartindalePageData.MODULE_NAME_DROP_DOWN
        web_element = SeleniumActions.find_by_xpath(web_driver, element_path)

        Tools.sleep(2)

        SeleniumActions.select_by_index(web_element, "1")

        click_submit_button = \
            SeleniumActions.fetch_web_element(web_driver, MartindalePageData.MODULE_SUBMIT_BUTTON)
        SeleniumActions.click_element(web_driver, click_submit_button)

        Tools.sleep(5)

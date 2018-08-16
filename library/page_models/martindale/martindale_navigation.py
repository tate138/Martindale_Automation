from library.page_data.martindale_app.martindale_data import MartindalePageData
from library.tools import Tools


class MartindaleNavigation():

    @staticmethod
    def navigate_to_home_page(web_driver):
        web_driver.get(MartindalePageData.MARTINDALE_URL)
        Tools.sleep(3)

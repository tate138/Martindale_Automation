class MartindalePageData:

####
# GENERAL SETTINGS
####
    # URLs
    # Staging
    MARTINDALE_URL = "http://my.stg-martindalenolo.com/0004973/site/editor/cms"
    #Production
    #MARTINDALE_URL = "http://my.martindalenolo.com/0022415/site/editor/cms"
    MARTINDALE_STAGING_URL_FRAME_ONLY = "http://my.stg-martindalenolo.com/0004973/"
    MARTINDALE_AUTOMATION_URL = "http://my.stg-martindalenolo.com/0004973/automation"

    # Login Data
    MARTINDALE_LOGIN_USERNAME = "//*[@id=\"username\"]"
    MARTINDALE_LOGIN_PASSWORD = "//*[@id=\"password\"]"
    # Staging
    MARTINDALE_LOGIN_EMAIL = "tate.johnson@internetbrands.com"
    #Production
    #MARTINDALE_LOGIN_EMAIL = "tjohnson@internetbrands.com"
    MARTINDALE_LOGIN_PRODUCTION_EMAIL = "tjohnson@internetbrands.com"
    MARTINDALE_LOGIN_BUTTON = "//*[@id=\"login-form\"]/div[2]/form/div[3]/button"

    # Test Rail Data
    TEST_RAIL_URL = "https://testrail.internetbrands.com/testrail/"
    AUTOMATION_USER = "qatest@internetbrands.com"
    AUTOMATION_PW = "909SepulvedaApiUser"
    AUTOMATION_TEST_RUN_ID = "66901"

####
# PAGES TAB
####

    PAGES_TAB_BUTTON = "//*[@id=\"se__body\"]/div[2]/ul/li[2]/a"
    AUTOMATION_PAGE_EDIT_BUTTON = "//*[@id=\"tblPages\"]/tbody/tr[4]/td[6]/a[2]/i"
    AUTOMATION_PAGE_EDIT_BUTTON_TWO = "//*[@id=\"tblPages\"]/tbody/tr[2]/td[6]/a[2]/i"

####
# Iframe
####

    MARTINDALE_IFRAME = "//*[@id=\"myframe\"]"
    MARTINDALE_OVERLAY = "//*[@id=\"se__body\"]/div[6]"
    ADD_MODULE_BUTTON = "//*[@id=\"ple_column-0\"]/div/button"
    DELETE_MODULE_BUTTON = "//*[@id=\"ple_column-0\"]/div[2]/button/i"
    DELETE_MODULE_REMOVE_BUTTON = "//*[@id=\"ple_column-0\"]/div/button/span[1]/svg/g/circle"
    DELETE_MODULE_REMOVE_BUTTON_TWO = "/html/body/div[7]/div/form/div[3]/button[2]"
    IFRAME_EDIT_BUTTON = \
        "/html/body/div[6]/div[2]"
    IFRAME_EDIT_BUTTON_TWO = \
        "/html/body/div[6]/div[2]/button/i"
    MODULE = \
        "//*[@id=\"ple_column-0\"]/div[3]/div/div/div"



####
# MODULE GALLERY
####
    BANNER_MODULE_BUTTON = \
        "//*[@id=\"ple_column-0-modal-gallery\"]/div/form/div[2]/div/section[1]/button"
    BLADE_MODULE_BUTTON = \
        "//*[@id=\"ple_column-0-modal-gallery\"]/div/form/div[2]/div/section[2]/button"
    CTA_MODULE_BUTTON = \
        "//*[@id=\"ple_column-0-modal-gallery\"]/div/form/div[2]/div/section[5]/button"
    FEATURED_BLOCKS_MODULE_BUTTON = \
        "//*[@id=\"ple_column-0-modal-gallery\"]/div/form/div[2]/div/section[7]/button"

    SAVED_MODULE_RADIO_BUTTON = \
        "//*[@id=\"ple_column-0-modal-gallery\"]/div/form/div[2]/div[2]/fieldset/div[3]/label/span"
    MODULE_NAME_DROP_DOWN = \
        "//*[@id=\"alias-picker-component-0-existing-alias\"]"
    MODULE_SUBMIT_BUTTON = \
        "//*[@id=\"ple_column-0-modal-gallery\"]/div/form/div[3]/button"

    # Section
    CLOSE_NEW_SECTION_BUTTON = "//*[@id=\"ple-drawer-add-section-0\"]/form/button"




































































    MARTINDALE_LOGIN_PASS = "P@1n1nth3@55"






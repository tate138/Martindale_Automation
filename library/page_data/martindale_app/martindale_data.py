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
    AUTOMATION_TEST_RUN_ID = "67594" # "66901"

####
# Pages Tab
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

    MODULE_NAME_DROP_DOWN = \
        "//*[@id=\"alias-picker-component-0-existing-alias\"]"
    MODULE_SUBMIT_BUTTON = \
        "//*[@id=\"ple_column-0-modal-gallery\"]/div/form/div[3]/button"

    # Section
    CLOSE_NEW_SECTION_BUTTON = "//*[@id=\"ple-drawer-add-section-0\"]/form/button"

####
# BANNER MODULE
####

    BANNER_MODULE = \
        "//*[@id=\"skrollr-body\"]/div/div[2]/div/div/div/ul/li[2]"
    BANNER_MODULE_HEADER = \
        "//*[@id=\"ple_column-0\"]/div[2]"
    BANNER_MODULE_EDIT_BUTTON = \
        "/html/body/div[6]/div[2]"
    CREATE_BANNER_RADIO_BUTTON = \
        "//*[@id=\"ple_column-0-modal-gallery\"]/div/form/div[2]/div[2]/fieldset/div[1]/label"
    SAVED_BANNER_RADIO_BUTTON = \
        "//*[@id=\"ple_column-0-modal-gallery\"]/div/form/div[2]/div[2]/fieldset/div[3]/label"
    CREATE_BANNER_MODULE_NAME_TEXT = \
        "//*[@id=\"alias-picker-component-0-new-alias\"]"

    GALLERY_BANNER_TITLE = \
        "//*[@id=\"BannerSettings-Smb__Banner__Widgets__BannerSettings___automation_only-settings\"]/div/h4"

    BANNER_MODULE_CONTENT_TAB = \
        "//*[@id=\"BannerSettings-Smb__Banner__Widgets__BannerSettings___automation_only-settings\"]/form/div[1]/div/ul/li[1]/a"
    BANNER_MODULE_CONENT_MANAGE_CONTENT = \
        "//*[@id=\"BannerSettings-Smb__Banner__Widgets__BannerSettings___automation_only-tab-content\"]/div/div[1]"
    BANNER_MODULE_CONTENT_ADD_BANNER_BUTTON = \
        "//*[@id=\"addItem\"]"
    BANNER_LIST_ITEM_ONE = \
        "/html/body/ul/li[1]/div[2]/form/div[1]/div/div[1]/div/div[4]/ul[1]/li[1]/div/div[3]/div[1]/div[1]/span"
    BANNER_UNSAVED_CHANGES_MODAL = \
        "//*[@id=\"se__body\"]/div[8]/div[2]/p[1]"

    BANNER_MODULE_CONTENT_ADD_BANNER = \
        "//*[@id=\"BannerSettings-Smb__Banner__Widgets__BannerSettings___automation_only-settings-item\"]/div/h4"
    BANNER_TITLE = \
        "//*[@id=\"title\"]"
    BANNER_TITLE_ERROR = \
        "//*[@id=\"title-error\"]"
    BANNER_CAPTION = \
        "//*[@id=\"caption\"]"
    BANNER_CAPTION_ERROR = \
        "//*[@id=\"caption-error\"]"
    BANNER_MODULE_CONTENT_ADD_LINK_APPEARANCE = \
        "//*[@id=\"cta1_buttonStyle\"]"
    BANNER_MODULE_CONTENT_ADD_LINK_APPEARANCE_TWO = \
        "//*[@id=\"cta2_buttonStyle\"]"
    BANNER_MODULE_CONTENT_ADD_LINK_TYPE = \
        "//*[@id=\"cta1_linkType\"]"
    BANNER_MODULE_CONTENT_ADD_LINK_TYPE_TWO = \
        "//*[@id=\"cta2_linkType\"]"
    BANNER_MODULE_CONTENT_ADD_LINK_PAGE_LABEL = \
        "//*[@id=\"BannerSettings-Smb__Banner__Widgets__BannerSettings___automation_only-settings-item\"]/form/div[1]/div/ul[1]/div[2]/div[6]/label"
    BANNER_MODULE_CONTENT_ADD_LINK_PAGE_LABEL_TWO = \
        "//*[@id=\"BannerSettings-Smb__Banner__Widgets__BannerSettings___automation_only-settings-item\"]/form/div[1]/div/ul[2]/div[2]/div[6]/label"
    BANNER_MODULE_CONTENT_ADD_LINK_PAGE_URL_LABEL = \
        "//*[@id=\"BannerSettings-Smb__Banner__Widgets__BannerSettings___automation_only-settings-item\"]/form/div[1]/div/ul[1]/div[2]/div[7]/label"
    BANNER_MODULE_CONTENT_ADD_LINK_PAGE_URL_LABEL_TWO = \
        "//*[@id=\"BannerSettings-Smb__Banner__Widgets__BannerSettings___automation_only-settings-item\"]/form/div[1]/div/ul[2]/div[2]/div[7]/label"
    CTA_URL_TEXT = \
        "//*[@id=\"cta1_linkUrl\"]"
    CTA_URL_TEXT_TWO = \
        "//*[@id=\"cta2_linkUrl\"]"
    ADD_BANNER_SAVE_BUTTON = \
        "//*[@id=\"BannerSettings-Smb__Banner__Widgets__BannerSettings___automation_only-settings-item\"]/form/div[2]/button[2]"
    ADD_BANNER_CANCEL_BUTTON = \
        "//*[@id=\"cancel-item\"]"
    DELETE_BANNER_CONFIRMATION = \
        "//*[@id=\"se__body\"]/div[8]/div[2]/h2"
    DELETE_BANNER_CANCEL_BUTTON = \
        "//*[@id=\"se__body\"]/div[8]/div[2]/p[2]/button[1]"
    DELETE_BANNER_OK_BUTTON = \
        "//*[@id=\"se__body\"]/div[8]/div[2]/p[2]/button[2]"

    BANNER_MODULE_SETTINGS_TAB = \
        "//*[@id=\"BannerSettings-Smb__Banner__Widgets__BannerSettings___automation_only-settings\"]/form/div[1]/div/ul/li[2]/a"
    BANNER_MODULE_SETTINGS_ELEMENT_VISIBILITY = \
        "//*[@id=\"BannerSettings-Smb__Banner__Widgets__BannerSettings___automation_only-tab-settings\"]/ul/li[1]/div[1]"
    SETTINGS_SHOW_BANNER_TITLE = \
        "//*[@id=\"BannerSettings-Smb__Banner__Widgets__BannerSettings___automation_only-tab-settings\"]/ul/li[1]/div[2]/ul/li[1]/div/label/span"

    BANNER_MODULE_LAYOUT_TAB = \
        "//*[@id=\"BannerSettings-Smb__Banner__Widgets__BannerSettings___automation_only-settings\"]/form/div[1]/div/ul/li[3]/a"
    BANNER_MODULE_LAYOUT_TYPE = \
        "//*[@id=\"privew_options_container\"]/ul/li[1]/div[1]"

####
# BLADE MODULE
####
    BLADE_IFRAME_TITLE = \
        "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div/div[1]/div[1]/h3"
    BLADE_IFRAME_CAPTION = \
        "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div/div[1]/div[1]/h4"
    BLADE_IFRAME_DESCRIPTION = \
        "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div/div[1]/div[2]"
    BLADE_IFRAME_CTA_BUTTON_ONE = \
        "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div/div[1]/div[3]/div/a"
    BLADE_IFRAME_CTA_BUTTON_TWO = \
        "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div/div[1]/div[4]/div/a"
    BLADE_IFRAME_IMAGE_LEFT = \
        "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div/div[1]/div"
    BLADE_IFRAME_IMAGE_RIGHT = \
        "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div/div[2]/div"

    SAVED_BLADE_RADIO_BUTTON = \
        "//*[@id=\"ple_column-0-modal-gallery\"]/div/form/div[2]/div[2]/fieldset/div[3]/label/span"
    BLADE_MODULE = \
        "//*[@id=\"ple_column-0\"]/div[3]/div/div/div"
    BLADE_TITLE = \
        "//*[@id=\"BladeSettings-SMB__Blade__Widgets__BladeSettings___automation_only-settings\"]/div/h4"
    BLADE_DONE_BUTTON = \
        "//*[@id=\"settingsForm\"]/div[2]/button/i"

    BLADE_CONTENT_TAB = \
        "//*[@id=\"settingsForm\"]/div[1]/div/div[1]/ul/li[1]/a"
    BLADE_CONTENT_MODULE_INFORMATION = \
        "//*[@id=\"tab-content\"]/ul/li[1]/div[1]"
    BLADE_CONTENT_TITLE = \
        "//*[@id=\"title\"]"
    BLADE_CONTENT_CAPTION = \
        "//*[@id=\"caption\"]"
    BLADE_CONTENT_MANAGE_CONTENT = \
        "//*[@id=\"tab-content\"]/ul/li[2]/div[1]"
    BLADE_CONTENT_SELECT_FROM_GALLERY = \
        "//*[contains(@id, 'media-finder-')]"
    BLADE_CONTENT_GALLERY = \
        "//*[@id=\"se__body\"]/div[12]/div/div/form/div"
    BLADE_CONTENT_ALT_TEXT = \
        "//*[@id=\"alt_text\"]"
    BLADE_CONTENT_IMAGE_TITLE = \
        "//*[@id=\"img_title\"]"
    BLADE_CONTENT_DESCRIPTION = \
        "//*[contains(@id, 'redactor-uuid')]"
    BLADE_CONTENT_MANAGE_CTA_BUTTONS = \
        "//*[@id=\"tab-content\"]/ul/li[3]/div[1]"
    BLADE_CONTENT_CTA_ONE_LINK_TEXT = \
        "//*[@id=\"cta1_buttonText\"]"
    BLADE_CONTENT_CTA_ONE_LINK_TYPE = \
        "//*[@id=\"cta1_linkType\"]"
    BLADE_CONTENT_CTA_ONE_LINK_PAGE = \
        "//*[@id=\"cta1_linkPage\"]"
    BLADE_CONTENT_CTA_ONE_URL = \
        "//*[@id=\"cta1_linkUrl\"]"
    BLADE_CONTENT_CTA_ONE_URL_ERROR = \
        "//*[@id=\"cta1_linkUrl-error\"]"
    BLADE_CONTENT_CTA_TWO_LINK_TEXT = \
        "//*[@id=\"cta2_buttonText\"]"
    BLADE_CONTENT_CTA_TWO_LINK_TYPE = \
        "//*[@id=\"cta2_linkType\"]"
    BLADE_CONTENT_CTA_TWO_LINK_PAGE = \
        "//*[@id=\"cta2_linkPage\"]"
    BLADE_CONTENT_CTA_TWO_URL = \
        "//*[@id=\"cta2_linkUrl\"]"
    BLADE_CONTENT_CTA_TWO_URL_ERROR = \
        "//*[@id=\"cta2_linkUrl-error\"]"

    BLADE_SETTINGS_TAB = \
        "//*[@id=\"settingsForm\"]/div[1]/div/div[1]/ul/li[2]/a"
    BLADE_SETTINGS_ELEMENT_VISIBILITY = \
        "//*[@id=\"tab-settings\"]/ul/li[1]/div[1]"
    BLADE_SETTINGS_SHOW_BLADE_TITLE = \
        "//*[@id=\"tab-settings\"]/ul/li[1]/div[2]/ul/li[1]/div/label/span"
    BLADE_SETTINGS_SHOW_BLADE_CAPTION = \
        "//*[@id=\"tab-settings\"]/ul/li[1]/div[2]/ul/li[2]/div/label/span"
    BLADE_SETTINGS_SHOW_READ_MORE = \
        "//*[@id=\"tab-settings\"]/ul/li[1]/div[2]/ul/li[3]/div/label/span"
    BLADE_SETTINGS_SHOW_CTA_ONE = \
        "//*[@id=\"tab-settings\"]/ul/li[1]/div[2]/ul/li[4]/div/label/span"
    BLADE_SETTINGS_SHOW_CTA_TWO = \
        "//*[@id=\"tab-settings\"]/ul/li[1]/div[2]/ul/li[5]/div/label/span"
    BLADE_SETTINGS_SETTINGS = \
        "//*[@id=\"tab-settings\"]/ul/li[2]/div[1]"
    BLADE_SETTINGS_SWAP_MEDIA_TEXT = \
        "//*[@id=\"tab-settings\"]/ul/li[2]/div[2]/ul/li[1]/div/label/span"
    BLADE_SETTINGS_MODULE_VISIBILITY = \
        "//*[@id=\"tab-settings\"]/ul/li[4]/div[1]"
    BLADE_SETTINGS_DESKTOP_MODULE = \
        "//*[@id=\"tab-settings\"]/ul/li[4]/div[2]/div/div/ul/li[1]/label"


####
# FEATURED BLOCK MODULE
####

    FEATURED_BLOCKS_MODULE_EDIT_BUTTON = \
        "/html/body/div[6]/div[2]/button/i"
    SAVED_FEATURED_BLOCK_RADIO_BUTTON = \
        "//*[@id=\"ple_column-0-modal-gallery\"]/div/form/div[2]/div[2]/fieldset/div[3]/label/span"
    FEATURED_BLOCKS_MODULE_HEADER = \
        "//*[@id=\"FeaturedblocksSettings-SMB__Featuredblocks__Widgets__FeaturedblocksSettings___automation_only-settings\"]/div"
    FEATURED_BLOCKS_TITLE = \
        "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div[1]/h2"
    FEATURED_BLOCKS_CAPTION_DISPLAY = \
        "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div[1]/h3"
    FEATURED_BLOCKS_BLOCK_TITLE = \
        "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div/ul/li/div/a/span[2]"
    FEATURED_BLOCKS_DESCRIPTION = \
        "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div[2]/ul/li/div/div[3]"

    FEATURED_BLOCKS_LAYOUT = \
        "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div[2]/ul/li/div"

    FEATURED_BLOCKS_CONTENT_TAB = \
        "//*[@id=\"FeaturedblocksSettings-SMB__Featuredblocks__Widgets__FeaturedblocksSettings___automation_only-settings\"]/form/div[1]/div/ul/li[1]/a"
    FEATURED_BLOCKS_MODULE_INFORMATION = \
        "//*[@id=\"tab-content\"]/ul/li[1]/div[1]"
    FEATURED_BLOCKS_CONTENT_TITLE = \
        "//*[@id=\"featured-blocks-title\"]"
    FEATURED_BLOCKS_CAPTION = \
        "//*[@id=\"featured-blocks-caption\"]"
    FEATURED_BLOCKS_MANAGE_CONTENT = \
        "//*[@id=\"tab-content\"]/ul/li[2]/div[1]"
    FEATURED_BLOCKS_CONTENT_ADD_CONTENT = \
        "//*[@id=\"tab-content\"]/ul/li[2]/div[2]/a"
    FEATURED_BLOCKS_EDIT_BUTTON = \
        "//*[contains(@id, 'link_link-')]/div[1]/div[2]/span/a[1]/i"
    FEATURED_BLOCKS_DELETE_BUTTON = \
        "//*[contains(@id, 'link_link-')]/div[1]/div[2]/span/a[2]"
    FEATURED_BLOCK = \
        "//*[contains(@id, 'link_link-')]/div[2]/div/div[2]/div[1]"
    FEATURED_BLOCK_IMAGE = \
        "//*[contains(@id, 'link_link-')]/div[2]/div/div[1]/img"
    DELETE_FEATURED_BLOCKS_MODAL = \
        "//*[@id=\"se__body\"]/div[8]/div[2]/h2"
    DELETE_FEATURED_BLOCKS_MODAL_CANCEL_BUTTON = \
        "//*[@id=\"se__body\"]/div[8]/div[2]/p[2]/button[1]"
    DELETE_FEATURED_BLOCKS_MODAL_OK_BUTTON = \
        "//*[@id=\"se__body\"]/div[8]/div[2]/p[2]/button[2]"
    FEATURED_BLOCK_LINK_APPEARANCE = \
        "//*[@id=\"featuredblock-appearance\"]"
    FEATURED_BLOCK_LINK_TYPE = \
        "//*[@id=\"featuredblock_type\"]"
    FEATURED_BLOCK_LINK_DROP_DOWN = \
        "//*[@id=\"featuredblock_internal\"]"
    FEATURED_BLOCK_EXTERNAL_LINK = \
        "//*[@id=\"url\"]"
    FEATURED_BLOCKS_ALT_TEXT = \
        "//*[@id=\"alt_text\"]"
    FEATURE_BLOCK_DONE_BUTTON = \
        "//*[@id=\"FeaturedblocksSettings-SMB__Featuredblocks__Widgets__FeaturedblocksSettings___automation_only-settings\"]/form/div[2]/button"

    FEATURED_BLOCKS_SAVE_CHANGES_MODAL = \
        "//*[@id=\"se__body\"]/div[8]/div[2]/p[1]"
    FEATURED_BLOCKS_SAVE_CHANGES_NO_BUTTON = \
        "//*[@id=\"se__body\"]/div[8]/div[2]/p[2]/button[1]"
    FEATURED_BLOCKS_SAVE_CHANGES_YES_BUTTON = \
        "//*[@id=\"se__body\"]/div[8]/div[2]/p[2]/button[2]"

    ADD_CONTENT_SELECT_FROM_GALLERY = \
        "//*[contains(@id, 'media-finder-')]/button"
    ADD_CONTENT_SELECT_GALLERY_IMAGE = \
        "//*[@id=\"MediaManager-ocmediamanager-item-list\"]/div/div/ul/li[1]/div[1]/div[2]/img"
    ADD_CONTENT_SELECT_GALLERY_IMAGE_TEXT = \
        "//*[@id=\"MediaManager-ocmediamanager-item-list\"]/div/div/ul/li[1]/div[2]/h4"
    ADD_CONTENT_SELECT_GALLERY_INSERT_BUTTON = \
        "//*[@id=\"se__body\"]/div[12]/div/div/form/div/div[4]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/button[1]"
    ADD_CONTENT_SELECT_GALLERY_CANCEL_BUTTON = \
        "//*[@id=\"se__body\"]/div[12]/div/div/form/div/div[4]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/button[3]"
    ADD_CONTENT_IMAGE_TEXT = \
        "//*[@id=\"image_wrapper\"]/div/div/div[1]/div/div[1]/span"
    ADD_CONTENT_IMAGE_CONTAINER = \
        "//*[@id=\"image_wrapper\"]/div/div/div[1]/div/img"
    ADD_CONTENT_REPLACE_BUTTON = \
        "//*[@id=\"image_wrapper\"]/div/div/div[1]/div[1]/a"
    ADD_CONTENT_BLOCK_TITLE = \
        "//*[@id=\"article_title\"]"
    ADD_BLOCK_TITLE_ERROR = \
        "//*[@id=\"article_title-error\"]"
    ADD_BLOCK_DESCRIPTION = \
        "//*[@id=\"article_description\"]"
    ADD_BLOCK_DESCRIPTION_ERROR = \
        "//*[@id=\"article_description-error\"]"
    ADD_BLOCK_LINK_APPEARANCE_DROP_DOWN = \
        "//*[@id=\"featuredblock-appearance\"]"
    ADD_BLOCK_LINK_TEXT_LABEL = \
        "//*[@id=\"FeaturedblocksSettings-SMB__Featuredblocks__Widgets__FeaturedblocksSettings___automation_only-settings-item\"]/form/div[2]/div[2]/label"
    ADD_BLOCK_BUTTON_TEXT_LABEL = \
        "//*[@id=\"FeaturedblocksSettings-SMB__Featuredblocks__Widgets__FeaturedblocksSettings___automation_only-settings-item\"]/form/div[2]/div[1]/label"
    ADD_BLOCK_LINK_TEXT_BOX = \
        "//*[@id=\"featuredblock-button-text\"]"
    ADD_BLOCK_LINK_TYPE_DROP_DOWN = \
        "//*[@id=\"featuredblock_type\"]"
    ADD_BLOCK_LINK_DROP_DOWN = \
        "//*[@id=\"featuredblock_internal\"]"
    ADD_CONTENT_CANCEL_BUTTON = \
        "//*[@id=\"FeaturedblocksSettings-SMB__Featuredblocks__Widgets__FeaturedblocksSettings___automation_only-settings-item\"]/form/div[3]/button[1]"
    ADD_CONTENT_SAVE_BUTTON = \
        "//*[@id=\"FeaturedblocksSettings-SMB__Featuredblocks__Widgets__FeaturedblocksSettings___automation_only-settings-item\"]/form/div[3]/button[2]"
    ADD_CONTENT_SAVE_BUTTON_TWO = \
        "//*[@id=\"FeaturedblocksSettings-SMB__Featuredblocks__Widgets__FeaturedblocksSettings___automation_only-settings-item\"]/form/div[4]/button[2]"
    FEATURED_BLOCKS_SETTINGS_TAB = \
        "//*[@id=\"FeaturedblocksSettings-SMB__Featuredblocks__Widgets__FeaturedblocksSettings___automation_only-settings\"]/form/div[1]/div/ul/li[2]"

    FEATURED_BLOCKS_SETTINGS_SHOW_TITLE = \
        "//*[@id=\"tab-settings\"]/ul/li[2]/div[2]/div[1]/span/label/span"
    FEATURED_BLOCKS_SETTINGS_SHOW_CAPTION = \
        "//*[@id=\"tab-settings\"]/ul/li[2]/div[2]/div[2]/span/label/span"
    FEATURED_BLOCKS_SETTINGS_SHOW_BLOCK_TITLE = \
        "//*[@id=\"tab-settings\"]/ul/li[2]/div[2]/div[5]/span/label/span"
    FEATURED_BLOCKS_SETTINGS_SHOW_BLOCK_DESCRIPTION = \
        "//*[@id=\"tab-settings\"]/ul/li[2]/div[2]/div[6]/span/label/span"

    FEATURED_BLOCKS_LAYOUT_TAB = \
        "//*[@id=\"FeaturedblocksSettings-SMB__Featuredblocks__Widgets__FeaturedblocksSettings___automation_only-settings\"]/form/div[1]/div/ul/li[3]/a"
    FEATURED_BLOCKS_LAYOUT_LABEL = \
        "//*[@id=\"privew_options_container\"]/ul/li[1]/div[2]/div/div/label"
    FEATURED_BLOCKS_LAYOUT_OVERLAY = \
        "//*[@id=\"privew_options_container\"]/ul/li[1]/div[2]/div/div/div[1]"
    FEATURED_BLOCKS_CHANGE_LAYOUT_BUTTON = \
        "//*[@id=\"privew_options_container\"]/ul/li[1]/div[2]/div/div/div[1]/a"
    FEATURED_BLOCKS_LAYOUT_ONE = \
        "//*[@id=\"picker_grid_a\"]/div"
    FEATURED_BLOCKS_LAYOUT_TWO = \
        "//*[@id=\"picker_flyup_a\"]/div"


####
# CTA MODULE
####

    CTA_MODULE_TITLE_DISPLAY = \
        "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div/div/h3"
    CTA_MODULE_CAPTION_DISPLAY = \
        "//*[@id=\"ple_column-0\"]/div[3]/div/div/div/div/div/h4"
    CTA_MODULE_LINK_DISPLAY = \
        "//*[@class='cta__link component__link--1']"


    CTA_MODULE_HEADER = \
        "//*[@id=\"CtaSettings-SMB__Cta__Widgets__CtaSettings___automation_only-settings\"]/div/h4"
    CTA_CONTENT_TAB = \
        "//*[@id=\"CtaSettings-SMB__Cta__Widgets__CtaSettings___automation_only-settings\"]/form/div[1]/div/ul/li[1]/a"
    CTA_MODULE_TITLE = \
        "//*[@id=\"title\"]"
    CTA_MODULE_CAPTION = \
        "//*[@id=\"caption\"]"
    CTA_MODULE_ONE_LINK_APPEARANCE = \
        "//*[@id=\"buttonStyle1\"]"
    CTA_MODULE_BUTTON_TEXT_BOX_ONE = \
        "//*[@id=\"buttonText1\"]"
    CTA_MODULE_SELECT_ICON_ONE = \
        "//*[@id=\"iconDiv1\"]/div/div[1]/div[2]"
    CTA_MODULE_BUTTON_ONE_LINK_TYPE = \
        "//*[@id=\"linkType1\"]"
    CTA_MODULE_LINK_PAGE_ONE_DROP_DOWN = \
        "//*[@id=\"linkPage1\"]"
    CTA_MODULE_EXTERNAL_URL_ONE = \
        "//*[@id=\"linkUrl1\"]"
    CTA_MODULE_PHONE_NUMBER_ONE = \
        "//*[@id=\"linkPhoneUrl1\"]"
    CTA_MODULE_TWO_LINK_APPEARANCE = \
        "//*[@id=\"buttonStyle2\"]"
    CTA_MODULE_LINK_TEXT_BOX_TWO = \
        "//*[@id=\"buttonText2\"]"
    CTA_MODULE_BUTTON_TEXT_BOX_TWO = \
        "//*[@id=\"buttonText2\"]"
    CTA_MODULE_SELECT_ICON_TWO = \
        "//*[@id=\"iconDiv2\"]/div/div[1]/div[2]"
    CTA_MODULE_TWO_BUTTON_LINK_TYPE = \
        "//*[@id=\"linkType2\"]"
    CTA_MODULE_LINK_PAGE_TWO_DROP_DOWN = \
        "//*[@id=\"linkPage2\"]"
    CTA_MODULE_EXTERNAL_URL_TWO = \
        "//*[@id=\"linkUrl2\"]"
    CTA_MODULE_PHONE_NUMBER_TWO = \
        "//*[@id=\"linkPhoneUrl2\"]"
    CTA_MODULE_DONE_BUTTON = \
        "//*[@id=\"CtaSettings-SMB__Cta__Widgets__CtaSettings___automation_only-settings\"]/form/div[2]/button"

    CTA_SETTINGS_TAB = \
        "//*[@id=\"CtaSettings-SMB__Cta__Widgets__CtaSettings___automation_only-settings\"]/form/div[1]/div/ul/li[2]/a"
    CTA_SETTINGS_SHOW_BUTTON_ONE = \
        "//*[@id=\"tab-settings\"]/ul/li[1]/ul/li[3]/div/label/span"
    CTA_SETTINGS_SHOW_BUTTON_TWO = \
        "//*[@id=\"tab-settings\"]/ul/li[1]/ul/li[4]/div/label/span"
























    MARTINDALE_LOGIN_PASS = "P@1n1nth3@55"






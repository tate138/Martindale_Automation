from library.page_data.martindale_app.martindale_data import HerokuPageData
from library.selenium_actions import SeleniumActions


class HerokuForgottenPasswordPage:

    @staticmethod
    def submit_email_for_forgotten_password(web_driver, user_email):
        #enter email
        text_field_forgotten_password_email = SeleniumActions.fetch_web_element(web_driver, HerokuPageData.TEXT_FIELD_FORGOT_PASSWORD_EMAIL)
        SeleniumActions.write_to_element(web_driver, text_field_forgotten_password_email, user_email)

        #click_button for submission
        button_forgotten_password = SeleniumActions.fetch_web_element(web_driver, HerokuPageData.BUTTON_FORGOT_PASSWORD_EMAIL)
        SeleniumActions.click_element(web_driver, button_forgotten_password)

    @staticmethod
    def verify_email_forgotten(web_driver):
        expected_text = "Your e-mail's been sent!"

        message_of_email_sent = SeleniumActions.fetch_web_element(web_driver, HerokuPageData.MESSAGE_OF_EMAIL_SENT)

        actual_text = SeleniumActions.read_web_element_text(message_of_email_sent)

        error_message = "Error\nexpected_text: " + expected_text + "\nactual_text : " + actual_text
        assert actual_text == expected_text, error_message



from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from generators import generate_email, generate_password
from locators import RegistrationLocators
from data import Data, Urls


class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get(Urls.REGISTER_URL)

        driver.find_element(*RegistrationLocators.NAME_FIELD).send_keys("Tatiana")

        driver.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys(generate_email())

        driver.find_element(*RegistrationLocators.PASSWORD_FIELD).send_keys(generate_password())

        driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Urls.LOGIN_URL))

        assert driver.current_url == Urls.LOGIN_URL

    def test_registration_with_invalid_password(self, driver):
        driver.get(Urls.REGISTER_URL)

        driver.find_element(*RegistrationLocators.NAME_FIELD).send_keys("Tatiana")

        driver.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys(generate_email())

        driver.find_element(*RegistrationLocators.PASSWORD_FIELD).send_keys("12345")

        driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

        error_message = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RegistrationLocators.PASSWORD_ERROR))

        assert error_message.is_displayed()
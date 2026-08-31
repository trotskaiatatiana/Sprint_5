from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import Data, Urls

from locators import (
    MainPageLocators,
    RegistrationLocators,
    LoginLocators,
    ForgotPasswordLocators
)

class TestLogin:

    def test_login_from_main_page(self, driver):
        driver.get(Urls.BASE_URL)

        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Urls.LOGIN_URL))

        driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys(Data.EMAIL)

        driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)

        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/"))

        assert driver.current_url == "https://stellarburgers.education-services.ru/"

    def test_login_from_personal_account(self, driver):
        driver.get(Urls.BASE_URL)

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Urls.LOGIN_URL))

        driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys(Data.EMAIL)

        driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)

        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/"))

        assert driver.current_url == "https://stellarburgers.education-services.ru/"

    def test_login_from_registration(self, driver):
        driver.get(Urls.REGISTER_URL)

        driver.find_element(*RegistrationLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Urls.LOGIN_URL))

        driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys(Data.EMAIL)

        driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)

        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/"))

        assert driver.current_url == "https://stellarburgers.education-services.ru/"

    def test_login_from_forgot_password(self, driver):
        driver.get(Urls.LOGIN_URL)

        driver.find_element(*LoginLocators.FORGOT_PASSWORD_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Urls.FORGOT_PASSWORD_URL))

        driver.find_element(*ForgotPasswordLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Urls.LOGIN_URL))

        driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys(Data.EMAIL)

        driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)

        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/"))

        assert driver.current_url == "https://stellarburgers.education-services.ru/"

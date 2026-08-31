from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import Data, Urls

from locators import (
    MainPageLocators,
    LoginLocators,
    PersonalAccountLocators
)

class TestPersonalAccount:

    def test_personal_account(self, driver):
        driver.get(Urls.BASE_URL)

        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Urls.LOGIN_URL))

        driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys(Data.EMAIL)

        driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)

        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/"))

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PersonalAccountLocators.LOGOUT_BUTTON))

        assert driver.current_url == "https://stellarburgers.education-services.ru/account/profile"

    def test_constructor_from_personal_account(self, driver):
        driver.get(Urls.BASE_URL)

        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/login"))

        driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys(Data.EMAIL)

        driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)

        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/"))

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PersonalAccountLocators.LOGOUT_BUTTON))

        driver.find_element(*PersonalAccountLocators.CONSTRUCTOR_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/"))

        assert driver.current_url == "https://stellarburgers.education-services.ru/"

    def test_logo_from_personal_account(self, driver):
        driver.get(Urls.BASE_URL)

        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/login"))

        driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys(Data.EMAIL)

        driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)

        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/"))

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PersonalAccountLocators.LOGOUT_BUTTON))

        driver.find_element(*PersonalAccountLocators.LOGO).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/"))

        assert driver.current_url == "https://stellarburgers.education-services.ru/"

    def test_logout(self, driver):
        driver.get(Urls.BASE_URL)

        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/login"))

        driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys(Data.EMAIL)

        driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(Data.PASSWORD)

        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/"))

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PersonalAccountLocators.LOGOUT_BUTTON))

        driver.find_element(*PersonalAccountLocators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/login"))

        assert driver.current_url == "https://stellarburgers.education-services.ru/login"
        
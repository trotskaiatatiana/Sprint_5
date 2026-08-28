from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import (
    MainPageLocators,
    RegistrationLocators,
    LoginLocators,
    ForgotPasswordLocators
)


def test_login_from_main_page(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/login"))

    driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys("tatianat53_123@mail.ru")

    driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys("12345qwer")

    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/"))

def test_login_from_personal_account(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/login"))

    driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys("tatianat53_123@mail.ru")

    driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys("12345qwer")

    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/"))

def test_login_from_registration(driver):
    driver.get("https://stellarburgers.education-services.ru/register")

    driver.find_element(*RegistrationLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/login"))

    driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys("tatianat53_123@mail.ru")

    driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys("12345qwer")

    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/"))

def test_login_from_forgot_password(driver):
    driver.get("https://stellarburgers.education-services.ru/login")

    driver.find_element(*LoginLocators.FORGOT_PASSWORD_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/forgot-password"))

    driver.find_element(*ForgotPasswordLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/login"))

    driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys("tatianat53_123@mail.ru")

    driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys("12345qwer")

    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be("https://stellarburgers.education-services.ru/"))
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import ConstructorLocators


def test_buns_section(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(*ConstructorLocators.SAUCES_TAB).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ConstructorLocators.SAUCE_ITEM))

    driver.find_element(*ConstructorLocators.BUNS_TAB).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ConstructorLocators.BUN_ITEM))

    assert driver.find_element(*ConstructorLocators.BUN_ITEM).is_displayed()


def test_sauces_section(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(*ConstructorLocators.SAUCES_TAB).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ConstructorLocators.SAUCE_ITEM))

    assert driver.find_element(*ConstructorLocators.SAUCE_ITEM).is_displayed()


def test_fillings_section(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(*ConstructorLocators.FILLINGS_TAB).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ConstructorLocators.FILLING_ITEM))

    assert driver.find_element(*ConstructorLocators.FILLING_ITEM).is_displayed()
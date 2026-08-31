from selenium.webdriver.support.wait import WebDriverWait
from data import Urls
from locators import ConstructorLocators


class TestConstructor:

    def test_buns_section(self, driver):
        driver.get(Urls.BASE_URL)

        driver.find_element(*ConstructorLocators.SAUCES_TAB).click()

        driver.find_element(*ConstructorLocators.BUNS_TAB).click()

        WebDriverWait(driver, 3).until(lambda driver: "tab_tab_type_current" in driver.find_element(*ConstructorLocators.BUNS_TAB).get_attribute("class"))

        assert "tab_tab_type_current" in driver.find_element(*ConstructorLocators.BUNS_TAB).get_attribute("class")


    def test_sauces_section(self, driver):
        driver.get(Urls.BASE_URL)

        driver.find_element(*ConstructorLocators.SAUCES_TAB).click()

        WebDriverWait(driver, 3).until(lambda driver: "tab_tab_type_current" in driver.find_element(*ConstructorLocators.SAUCES_TAB).get_attribute("class"))

        assert "tab_tab_type_current" in driver.find_element(*ConstructorLocators.SAUCES_TAB).get_attribute("class")


    def test_fillings_section(self, driver):
        driver.get(Urls.BASE_URL)

        driver.find_element(*ConstructorLocators.FILLINGS_TAB).click()

        WebDriverWait(driver, 3).until(lambda driver: "tab_tab_type_current" in driver.find_element(*ConstructorLocators.FILLINGS_TAB).get_attribute("class"))

        assert "tab_tab_type_current" in driver.find_element(*ConstructorLocators.FILLINGS_TAB).get_attribute("class")

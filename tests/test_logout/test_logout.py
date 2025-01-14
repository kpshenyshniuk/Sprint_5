from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.data import CommonData
from confest import driver
from tests.locators import Locators


class TestLogout:
    def test_get_constructor_page_by_constructor_button(self, driver):
        driver.get(Locators.link_login_page)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.email_field_login_page)))
        driver.find_element(By.XPATH, Locators.email_field_login_page).send_keys(CommonData.valid_email)
        driver.find_element(By.XPATH, Locators.password_field_login_page).send_keys(CommonData.valid_password)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.login_button_login_page)))
        driver.find_element(By.XPATH, Locators.login_button_login_page).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.button_profile_page)))
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.button_profile_page)))
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Locators.link_main_page))
        driver.find_element(By.XPATH, Locators.button_profile_page).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.exit_button_profile_page)))
        driver.find_element(By.XPATH, Locators.exit_button_profile_page).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.login_button_login_page)))
        driver.get(Locators.link_profile_page)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.login_button_login_page)))
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Locators.link_login_page))
        assert driver.current_url == Locators.link_login_page
        assert WebDriverWait(driver, 10).until(expected_conditions.invisibility_of_element_located((By.XPATH, Locators.email_field_profile_page)))

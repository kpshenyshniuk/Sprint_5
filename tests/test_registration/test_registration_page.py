from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.data import CommonData
from confest import driver
from tests.locators import Locators
from tests.links import Links


class TestRegistration:
    def test_registration(self, driver):
        driver.get(Links.link_registration_page)
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Links.link_registration_page))
        name_field = driver.find_element(By.XPATH, Locators.name_field_registration_page)
        name_field.send_keys(CommonData.random_name)
        email_field = driver.find_element(By.XPATH, Locators.email_field_registration_page)
        email_field.send_keys(CommonData.random_email)
        password_field = driver.find_element(By.XPATH, Locators.password_field_registration_page)
        password_field.send_keys(CommonData.password)
        assert name_field.get_attribute('value') == CommonData.random_name
        assert email_field.get_attribute('value') == CommonData.random_email
        assert password_field.get_attribute('value') == CommonData.password
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.register_button_registration_page)))
        driver.find_element(By.XPATH, Locators.register_button_registration_page).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Links.link_login_page))
        assert driver.current_url == Links.link_login_page

    def test_error_when_register_with_less_6_symbols_password(self, driver):
        driver.get(Links.link_registration_page)
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Links.link_registration_page))
        name_field = driver.find_element(By.XPATH, Locators.name_field_registration_page)
        name_field.send_keys(CommonData.random_name)
        email_field = driver.find_element(By.XPATH, Locators.email_field_registration_page)
        email_field.send_keys(CommonData.random_email)
        password_field = driver.find_element(By.XPATH, Locators.password_field_registration_page)
        password_field.send_keys(CommonData.invalid_password)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.register_button_registration_page)))
        driver.find_element(By.XPATH, Locators.register_button_registration_page).click()
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, Locators.error_text_registration_page),'Некорректный пароль'))
        password_field_error = driver.find_element(By.XPATH,Locators.error_text_registration_page).text
        assert password_field_error == 'Некорректный пароль'

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.data import CommonData
from confest import driver
from tests.locators import Locators


class TestGetPages:
    def test_get_profile_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.email_field_login_page)))
        driver.find_element(By.XPATH, Locators.email_field_login_page).send_keys(
            CommonData.valid_email)
        driver.find_element(By.XPATH, Locators.password_field_login_page).send_keys(
            CommonData.valid_password)
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.login_button_login_page)))
        driver.find_element(By.XPATH, Locators.login_button_login_page).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.make_order_button)))
        driver.get('https://stellarburgers.nomoreparties.site/account')
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, Locators.exit_button_profile_page)))
        email_field_value = driver.find_element(By.XPATH, Locators.email_field_profile_page).get_attribute(
            'value')
        assert email_field_value == CommonData.valid_email
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_get_profile_page_by_profile_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.email_field_login_page)))
        driver.find_element(By.XPATH, Locators.email_field_login_page).send_keys(
            CommonData.valid_email)
        driver.find_element(By.XPATH, Locators.password_field_login_page).send_keys(
            CommonData.valid_password)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.login_button_login_page)))
        driver.find_element(By.XPATH, Locators.login_button_login_page).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.button_profile_page)))
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.button_profile_page)))
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
        driver.find_element(By.XPATH, Locators.button_profile_page).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, Locators.email_field_profile_page)))
        email_field_value = driver.find_element(By.XPATH, Locators.email_field_profile_page).get_attribute('value')
        assert email_field_value == CommonData.valid_email
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_get_constructor_page_by_direct_link(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.email_field_login_page)))
        driver.find_element(By.XPATH, Locators.email_field_login_page).send_keys(
            CommonData.valid_email)
        driver.find_element(By.XPATH, Locators.password_field_login_page).send_keys(
            CommonData.valid_password)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.login_button_login_page)))
        driver.find_element(By.XPATH, Locators.login_button_login_page).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.button_profile_page)))
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.button_profile_page)))
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
        driver.find_element(By.XPATH, Locators.button_profile_page).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, Locators.button_constructor)))
        driver.get('https://stellarburgers.nomoreparties.site')
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.title_main_page)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert driver.find_element(By.XPATH, Locators.title_main_page).text == 'Соберите бургер'

    def test_get_constructor_page_by_constructor_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.email_field_login_page)))
        driver.find_element(By.XPATH, Locators.email_field_login_page).send_keys(
            CommonData.valid_email)
        driver.find_element(By.XPATH, Locators.password_field_login_page).send_keys(
            CommonData.valid_password)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.login_button_login_page)))
        driver.find_element(By.XPATH, Locators.login_button_login_page).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.button_profile_page)))
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.button_profile_page)))
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
        driver.find_element(By.XPATH, Locators.button_profile_page).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, Locators.button_constructor)))
        driver.find_element(By.XPATH, Locators.button_constructor).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.title_main_page)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert driver.find_element(By.XPATH, Locators.title_main_page).text == 'Соберите бургер'

    def test_get_constructor_page_by_logo_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.email_field_login_page)))
        driver.find_element(By.XPATH, Locators.email_field_login_page).send_keys(
            CommonData.valid_email)
        driver.find_element(By.XPATH, Locators.password_field_login_page).send_keys(
            CommonData.valid_password)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.login_button_login_page)))
        driver.find_element(By.XPATH, Locators.login_button_login_page).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.button_profile_page)))
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.button_profile_page)))
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
        driver.find_element(By.XPATH, Locators.button_profile_page).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div//a[@href='/']")))
        driver.find_element(By.XPATH, Locators.button_logo).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.title_main_page)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert driver.find_element(By.XPATH, Locators.title_main_page).text == 'Соберите бургер'

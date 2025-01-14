from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.data import CommonData
from confest import driver
from tests.locators import Locators


class TestSuccessfullLogin:
    def test_login_from_main_page(self,driver):
        driver.get(Locators.link_main_page)
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Locators.link_main_page))
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.button_enter_account)))
        driver.find_element(By.XPATH, Locators.button_enter_account).click()
        driver.find_element(By.XPATH,Locators.email_field_login_page).send_keys(CommonData.valid_email)
        driver.find_element(By.XPATH,Locators.password_field_login_page).send_keys(CommonData.valid_password)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH,Locators.login_button_login_page)))
        driver.find_element(By.XPATH,Locators.login_button_login_page).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Locators.link_main_page))
        assert driver.current_url == Locators.link_main_page
        driver.get(Locators.link_profile_page)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.email_field_profile_page)))
        assert driver.find_element(By.XPATH, Locators.email_field_profile_page).get_attribute('value') == CommonData.valid_email

    def test_login_from_profile_page(self,driver):
        driver.get(Locators.link_main_page)
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Locators.link_main_page))
        driver.find_element(By.XPATH,Locators.button_profile_page).click()
        driver.find_element(By.XPATH, Locators.email_field_login_page).send_keys(CommonData.valid_email)
        driver.find_element(By.XPATH, Locators.password_field_login_page).send_keys(CommonData.valid_password)
        driver.find_element(By.XPATH,Locators.login_button_login_page).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Locators.link_main_page))
        assert driver.current_url == Locators.link_main_page
        driver.get(Locators.link_profile_page)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.email_field_profile_page)))
        assert driver.find_element(By.XPATH, Locators.email_field_profile_page).get_attribute('value') == CommonData.valid_email


    def test_login_from_registration_page(self, driver):
        driver.get(Locators.link_registration_page)
        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(Locators.link_registration_page)
        )

        # Ждем, пока элемент появится в DOM
        element = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.button_enter_register_page))
        )

        # Скролл к элементу
        driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # Убедиться, что элемент кликабелен
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.button_enter_register_page))
        )

        # Клик по элементу
        element.click()

        # Остальной код теста
        driver.find_element(By.XPATH, Locators.email_field_login_page).send_keys(CommonData.valid_email)
        driver.find_element(By.XPATH, Locators.password_field_login_page).send_keys(CommonData.valid_password)
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.login_button_login_page))
        )
        driver.find_element(By.XPATH, Locators.login_button_login_page).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(Locators.link_main_page)
        )
        assert driver.current_url == Locators.link_main_page

        driver.get(Locators.link_profile_page)
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.email_field_profile_page))
        )
        assert driver.find_element(By.XPATH, Locators.email_field_profile_page).get_attribute('value') == CommonData.valid_email

    def test_login_from_forgot_password_page(self,driver):
        driver.get(Locators.link_forgot_password_page)
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Locators.link_forgot_password_page))
        element = driver.find_element(By.XPATH,Locators.button_enter_forgot_password_page)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        driver.find_element(By.XPATH,Locators.button_enter_forgot_password_page).click()
        driver.find_element(By.XPATH, Locators.email_field_login_page).send_keys(CommonData.valid_email)
        driver.find_element(By.XPATH, Locators.password_field_login_page).send_keys(CommonData.valid_password)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH,Locators.login_button_login_page)))
        driver.find_element(By.XPATH,Locators.login_button_login_page).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Locators.link_main_page))
        assert driver.current_url == Locators.link_main_page
        driver.get(Locators.link_profile_page)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.email_field_profile_page)))
        assert driver.find_element(By.XPATH, Locators.email_field_profile_page).get_attribute('value') == CommonData.valid_email

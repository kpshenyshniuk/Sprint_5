import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from confest import driver
from tests.locators import Locators


class TestGetBySections:
    def test_scroll_to_sauces(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')

        # Дождаться загрузки страницы
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.button_section_bread)))

        # Получить начальную позицию скролла
        initial_scroll_position = driver.execute_script("return document.querySelector(\"div.BurgerIngredients_ingredients__menuContainer__Xu3Mo\").scrollTop;")

        # Нажимаем на "Соусы"
        driver.find_element(By.XPATH, Locators.button_section_sauce).click()

        # Ждем изменения позиции скролла
        WebDriverWait(driver, 10).until(lambda d: driver.execute_script("return document.querySelector(\"div.BurgerIngredients_ingredients__menuContainer__Xu3Mo\").scrollTop;") > initial_scroll_position)

        # Получаем новую позицию скролла
        new_scroll_position = driver.execute_script("return document.querySelector(\"div.BurgerIngredients_ingredients__menuContainer__Xu3Mo\").scrollTop;")

        # Ожидаемая позиция скролла
        expected_scroll_position = driver.execute_script("""
            var container = document.querySelector("div.BurgerIngredients_ingredients__menuContainer__Xu3Mo");
            var element = container.querySelector("h2:nth-of-type(2)"); // Соусы
            var containerTop = container.getBoundingClientRect().top;
            var elementTop = element.getBoundingClientRect().top;
            return elementTop - containerTop + container.scrollTop;
        """)
        # Проверяем, что скролл выполнен до нужной позиции
        assert abs(new_scroll_position - expected_scroll_position) < 5

    def test_scroll_to_fillings(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')

        # Дождаться загрузки страницы
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.button_section_fillings)))

        # Получить начальную позицию скролла
        initial_scroll_position = driver.execute_script("return document.querySelector(\"div.BurgerIngredients_ingredients__menuContainer__Xu3Mo\").scrollTop;")

        # Нажимаем на "Соусы"
        driver.find_element(By.XPATH, Locators.button_section_fillings).click()
        time.sleep(1)

        # Ждем изменения позиции скролла
        WebDriverWait(driver, 10).until(lambda d: driver.execute_script("return document.querySelector(\"div.BurgerIngredients_ingredients__menuContainer__Xu3Mo\").scrollTop;") > initial_scroll_position)

        # Получаем новую позицию скролла
        new_scroll_position = driver.execute_script("return document.querySelector(\"div.BurgerIngredients_ingredients__menuContainer__Xu3Mo\").scrollTop;")

        # Ожидаемая позиция скролла
        expected_scroll_position = driver.execute_script("""
            var container = document.querySelector("div.BurgerIngredients_ingredients__menuContainer__Xu3Mo");
            var element = container.querySelector("h2:nth-of-type(3)"); // Начинки
            var containerTop = container.getBoundingClientRect().top;
            var elementTop = element.getBoundingClientRect().top;
            return elementTop - containerTop + container.scrollTop;
        """)
        # Проверяем, что скролл выполнен до нужной позиции
        assert abs(new_scroll_position - expected_scroll_position) < 5

    def test_scroll_to_bread_from_fillings(self, driver):
        driver.get(Locators.link_main_page)

        # Дождаться загрузки страницы
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.button_section_fillings)))
        driver.find_element(By.XPATH, Locators.button_section_fillings).click()
        time.sleep(1)

        # Получить начальную позицию скролла
        initial_scroll_position = driver.execute_script(
            "return document.querySelector(\"div.BurgerIngredients_ingredients__menuContainer__Xu3Mo\").scrollTop;")

        # Нажимаем на "Соусы"
        driver.find_element(By.XPATH, Locators.button_section_bread).click()
        time.sleep(1)

        # Ждем изменения позиции скролла
        WebDriverWait(driver, 10).until(lambda d: driver.execute_script(
            "return document.querySelector(\"div.BurgerIngredients_ingredients__menuContainer__Xu3Mo\").scrollTop;") < initial_scroll_position)

        # Получаем новую позицию скролла
        new_scroll_position = driver.execute_script(
            "return document.querySelector(\"div.BurgerIngredients_ingredients__menuContainer__Xu3Mo\").scrollTop;")

        # Ожидаемая позиция скролла
        expected_scroll_position = driver.execute_script("""
            var container = document.querySelector("div.BurgerIngredients_ingredients__menuContainer__Xu3Mo");
            var element = container.querySelector("h2:nth-of-type(1)"); // Булки
            var containerTop = container.getBoundingClientRect().top;
            var elementTop = element.getBoundingClientRect().top;
            return elementTop - containerTop + container.scrollTop;
        """)
        # Проверяем, что скролл выполнен до нужной позиции
        assert abs(new_scroll_position - expected_scroll_position) < 5

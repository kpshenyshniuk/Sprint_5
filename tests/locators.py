from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.data import CommonData
from confest import driver

class Locators:
    email_field_login_page = '//label[text()="Email"]/following-sibling::input'   # Локатор для поля Email на логин странице
    password_field_login_page = '//label[text()="Пароль"]/following-sibling::input' # Локатор для поля pawword на логин странице
    login_button_login_page = '//button[text()="Войти"]' # Локатор кнопки Войти на логин странице
    make_order_button = '//button[text()="Оформить заказ"]' # Локатор кнопки оформить заказ на главное странице
    exit_button_profile_page = '//button[text()="Выход"]' # Локатор кнопки выхода из личного профиля
    email_field_profile_page = '//label[text()="Логин"]/following-sibling::input[@value="kokokoko@gmail.com"]' # Локатор поля с email на странице profile
    button_profile_page = '//a[@href="/account"]' # Локатор кнопки перехода в личный кабинет
    button_constructor = '//a[@href="/" and contains(., "Конструктор")]' # Локатор кнопка Конструктор
    title_main_page = '//h1[text()="Соберите бургер"]' # Локатор Собери бургер на главной странице
    button_logo = "//div//a[@href='/']" # Локатор ЛОГО stellar burgers
    button_enter_account = '//button[contains(text(), "Войти в аккаунт")]' # Локатор кнопки Войти в аккаунт
    button_enter_register_page = '//p//following-sibling::a[@href="/login"]' # локатор кнопки Войти на странице Регистрации
    button_enter_forgot_password_page = '//p//following-sibling::a[@href="/login"]' # локатор кнопки Войти на странице Восстановления пароля
    name_field_registration_page = "//label[text()='Имя']/following-sibling::input" # Локатор поля Имя на странице регистрации
    email_field_registration_page = "//label[text()='Email']/following-sibling::input" # Локатор поля Email на странице регистрации
    password_field_registration_page = "//label[text()='Пароль']/following-sibling::input" # Локатор поля Пароль на странице регистрации
    register_button_registration_page = '//button[text()="Зарегистрироваться"]' # Кнопка Зарегистрироваться на странице регистрации
    error_text_registration_page = '//p[@class="input__error text_type_main-default"]' # Локатор текста с ошибкой при вводе не валидного пароля
    button_section_bread = '//span[text()="Булки"]' # Локатор кнопки раздела Булки
    button_section_sauce = '//span[text()="Соусы"]' # Локатор кнопки раздела Соусы
    button_section_fillings = '//span[text()="Начинки"]' # Локатор кнопки раздела Начинки
    div_with_ingredients_and_scroll = "div.BurgerIngredients_ingredients__menuContainer__Xu3Mo"
    link_login_page = 'https://stellarburgers.nomoreparties.site/login' # Линка на  страницу с авторизацией пользователя
    link_profile_page = 'https://stellarburgers.nomoreparties.site/account' # Линка на траницу с Личным кабинетом пользователя
    full_link_profile_page = 'https://stellarburgers.nomoreparties.site/account/profile' # линка на страницу с личным кабинетом полная линка
    link_main_page = "https://stellarburgers.nomoreparties.site/" # линка на главную страницу
    link_forgot_password_page = 'https://stellarburgers.nomoreparties.site/forgot-password' # Линка на страницу с восстановление пароля
    link_registration_page ='https://stellarburgers.nomoreparties.site/register' # линка на страницу с регистрацией

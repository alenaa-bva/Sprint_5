from selenium.webdriver.common.by import By

class LoginPageLocators:
    login_header = (By.XPATH, ".//div[contains(@class, 'Auth_login')]//h2[text()='Вход']") # Заголовок страницы
    lp_email_input = (By.XPATH, ".//label[text()='Email']/..//input[@name='name']") # Поле пароль на странице логина
    lp_password_input = (By.XPATH, ".//label[text()='Пароль']/..//input[@name='Пароль']") # Поле пароль на странице логина
    login_button = (By.XPATH, ".//form/button[text()='Войти']") # Кнопка «Войти»
    registration_link = (By.LINK_TEXT, "Зарегистрироваться") # Кнопка-ссылка "Зарегистрироваться"
    password_recovery_link = (By.LINK_TEXT, "Восстановить пароль")  # Кнопка-ссылка «Войти»

class RegistrationPageLocators:
    rp_name_input = (By.XPATH, ".//label[text()='Имя']/..//input[@name='name']") # Поле имя на странице регистрации
    rp_email_input = (By.XPATH, ".//label[text()='Email']/..//input[@name='name']") # Поле емейл на странице регистрации
    rp_password_input = (By.XPATH, ".//label[text()='Пароль']/..//input[@name='Пароль']") # Поле пароль на странице регистрации
    sign_up_button = (By.XPATH, ".//form/button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    rp_login_link = (By.LINK_TEXT, "Войти") # Кнопка-ссылка «Войти»

    # сообщения об ошибках
    error_message_existing_user = (By.XPATH, ".//p[text() = 'Такой пользователь уже существует']") # сообщение об ошибке 'Такой пользователь уже существует'
    error_message_incorrect_password = (By.XPATH, ".// p[text() = 'Некорректный пароль']") # сообщение об ошибке 'Некорректный пароль'

class HomePageLocators:
    go_to_account_button = (By.XPATH, ".//button[text()='Войти в аккаунт']") # Кнопка «Войти в аккаунт»
    place_an_order_button = (By.XPATH, './/div/button[text()= "Оформить заказ"]') # Кнопка «Оформить заказ»
    personal_account_button = (By.XPATH, ".//p[text()='Личный Кабинет']")  # Кнопка «Личный кабинет»

    # Секция "Соберите бургер"
    collect_a_burger_header= (By.XPATH, ".//h1[text()='Соберите бургер']")  # Заголовок «Соберите бургер»
    bread_tab = (By.XPATH, ".//span[text() = 'Булки']") # меню булок
    sauce_tab = (By.XPATH, ".//span[text() = 'Соусы']") # меню соусов
    fillings_tab = (By.XPATH, ".//span[text() = 'Начинки']") # меню начинок
    ingredients_section = (By.XPATH, ".//section[contains(@class, 'BurgerIngredients_ingredients')]") # секция ингридиентов для бургеров

    first_bread_ingredient = (By.XPATH, ".//div[contains(@class, 'BurgerIngredients_ingredients__menu')]/ul[1]/a[1]") # первый по счету ингридиент в секции булок
    breads_section_header = (By.XPATH, ".//div[contains(@class, 'BurgerIngredients_ingredients__menu')]/h2[text()='Булки']") # заголовок секции булок

    first_sauce_ingredient = (By.XPATH, ".//div[contains(@class, 'BurgerIngredients_ingredients__menu')]/ul[1]/a[1]")  # первый по счету ингридиент в секции соусов
    sauces_section_header = (By.XPATH, ".//div[contains(@class, 'BurgerIngredients_ingredients__menu')]/h2[text()='Соусы']")  # заголовок секции соусов

    first_filling_ingredient = (By.XPATH, ".//div[contains(@class, 'BurgerIngredients_ingredients__menu')]/ul[1]/a[1]")  # первый по счету ингридиент в секции начинок
    fillings_section_header = (By.XPATH, ".//div[contains(@class, 'BurgerIngredients_ingredients__menu')]/h2[text()='Начинки']")  # заголовок секции начинок

class ForgotPasswordPage:
    fp_login_link = (By.LINK_TEXT, "Войти")  # Кнопка-ссылка «Войти»

class PersonalAccountPage:
    profile_tab = (By.XPATH, ".//a[text()='Профиль']") # вкладка профиль
    pa_constructor_button = (By.XPATH, ".//p[text()='Конструктор']") # кнопка "конструктор"
    pa_logo = (By.CSS_SELECTOR, 'div[class*="AppHeader_header__logo"]') # лого Stellar Burgers
    pa_email_input = (By.XPATH, ".//div/input[@name='Name']") # Поле емейл
    logout_button = (By.XPATH, ".// button[text() = 'Выход']") # кнопка "Выход"

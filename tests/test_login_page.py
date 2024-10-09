from locators import HomePageLocators, RegistrationPageLocators, LoginPageLocators, ForgotPasswordPage

class TestLogin:

    def test_login_from_go_to_account_button(
            self,
            driver,
            register_user,
            wait_element_to_be_visible,
            wait_element_to_be_clickable,
            generate_login
    ):
        name = "Алена"
        login = generate_login()
        password = "123456"

        # регистрация
        register_user(name, login, password)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', "Регистрация не прошла"

        # переход на домашнюю страницу
        driver.get("https://stellarburgers.nomoreparties.site")

        wait_element_to_be_clickable(HomePageLocators.go_to_account_button)

        # переход на форму логина через кнопку войти в аккаунт
        driver.find_element(*HomePageLocators.go_to_account_button).click()

        # логин
        driver.find_element(*LoginPageLocators.lp_email_input).send_keys(login)
        driver.find_element(*LoginPageLocators.lp_password_input).send_keys(password)
        driver.find_element(*LoginPageLocators.login_button).click()

        wait_element_to_be_visible(HomePageLocators.place_an_order_button)

        assert driver.find_element(*HomePageLocators.place_an_order_button).text == 'Оформить заказ', \
            "Авторизация не прошла"


    def test_login_from_personal_account_button(
            self,
            driver,
            register_user,
            wait_element_to_be_visible,
            wait_element_to_be_clickable,
            generate_login
    ):
        name = "Алена"
        login = generate_login()
        password = "123456"

        # регистрация
        register_user(name, login, password)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', "Регистрация не прошла"

        # переход на домашнюю страницу
        driver.get("https://stellarburgers.nomoreparties.site")

        wait_element_to_be_clickable(HomePageLocators.personal_account_button)

        # переход на форму логина через кнопку личный кабинет
        driver.find_element(*HomePageLocators.personal_account_button).click()

        # логин
        driver.find_element(*LoginPageLocators.lp_email_input).send_keys(login)
        driver.find_element(*LoginPageLocators.lp_password_input).send_keys(password)
        driver.find_element(*LoginPageLocators.login_button).click()

        wait_element_to_be_visible(HomePageLocators.place_an_order_button)

        assert driver.find_element(*HomePageLocators.place_an_order_button).text == 'Оформить заказ', \
            "Авторизация не прошла"


    def test_login_from_registration_form(
            self,
            driver,
            register_user,
            wait_element_to_be_visible,
            wait_element_to_be_clickable,
            generate_login
    ):
        name = "Алена"
        login = generate_login()
        password = "123456"

        # регистрация
        register_user(name, login, password)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', "Регистрация не прошла"

        # Переход на форму регистрации из формы логина
        driver.find_element(*LoginPageLocators.registration_link).click()

        wait_element_to_be_clickable(RegistrationPageLocators.rp_login_link)

        # Переход на форму логина из формы регистрации
        driver.find_element(*RegistrationPageLocators.rp_login_link).click()

        # логин
        driver.find_element(*LoginPageLocators.lp_email_input).send_keys(login)
        driver.find_element(*LoginPageLocators.lp_password_input).send_keys(password)
        driver.find_element(*LoginPageLocators.login_button).click()

        wait_element_to_be_visible(HomePageLocators.place_an_order_button)

        assert driver.find_element(*HomePageLocators.place_an_order_button).text == 'Оформить заказ', \
            "Авторизация не прошла"


    def test_login_from_password_recovering_form(
            self,
            driver,
            register_user,
            wait_element_to_be_visible,
            wait_element_to_be_clickable,
            generate_login
    ):
        name = "Алена"
        login = generate_login()
        password = "123456"

        # регистрация
        register_user(name, login, password)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', "Регистрация не прошла"

        # Переход на форму восстановления пароля из формы логина
        driver.find_element(*LoginPageLocators.password_recovery_link).click()

        wait_element_to_be_clickable(ForgotPasswordPage.fp_login_link)

        # Переход на форму логина из формы восстановления пароля
        driver.find_element(*ForgotPasswordPage.fp_login_link).click()

        # логин
        driver.find_element(*LoginPageLocators.lp_email_input).send_keys(login)
        driver.find_element(*LoginPageLocators.lp_password_input).send_keys(password)
        driver.find_element(*LoginPageLocators.login_button).click()

        wait_element_to_be_visible(HomePageLocators.place_an_order_button)

        assert driver.find_element(*HomePageLocators.place_an_order_button).text == 'Оформить заказ', \
            "Авторизация не прошла"


from locators import HomePageLocators, LoginPageLocators, PersonalAccountPage

class TestProfile:

    def test_open_personal_account(
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

        # переход на форму логина
        driver.get("https://stellarburgers.nomoreparties.site/login")

        # логин
        driver.find_element(*LoginPageLocators.lp_email_input).send_keys(login)
        driver.find_element(*LoginPageLocators.lp_password_input).send_keys(password)
        driver.find_element(*LoginPageLocators.login_button).click()

        wait_element_to_be_visible(HomePageLocators.place_an_order_button)

        assert driver.find_element(*HomePageLocators.place_an_order_button).text == 'Оформить заказ', \
            "Авторизация не прошла"

        # переход в личный кабинет
        driver.find_element(*HomePageLocators.personal_account_button).click()

        wait_element_to_be_visible(PersonalAccountPage.pa_email_input)

        assert '/account/profile' in driver.current_url and driver.find_element(*PersonalAccountPage.pa_email_input).get_attribute("value") is not None


    def test_logout(
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

        # переход на форму логина
        driver.get("https://stellarburgers.nomoreparties.site/login")

        # логин
        driver.find_element(*LoginPageLocators.lp_email_input).send_keys(login)
        driver.find_element(*LoginPageLocators.lp_password_input).send_keys(password)
        driver.find_element(*LoginPageLocators.login_button).click()

        wait_element_to_be_visible(HomePageLocators.place_an_order_button)

        assert driver.find_element(*HomePageLocators.place_an_order_button).text == 'Оформить заказ', \
            "Авторизация не прошла"

        # переход в личный кабинет
        driver.find_element(*HomePageLocators.personal_account_button).click()

        wait_element_to_be_visible(PersonalAccountPage.pa_email_input)

        assert '/account/profile' in driver.current_url

        # выход из аккаунта
        driver.find_element(*PersonalAccountPage.logout_button).click()

        wait_element_to_be_visible(LoginPageLocators.login_header)

        assert '/login' in driver.current_url








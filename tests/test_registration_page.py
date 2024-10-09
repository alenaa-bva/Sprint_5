import pytest
from locators import RegistrationPageLocators, LoginPageLocators, HomePageLocators


class TestRegistration:

    @pytest.mark.parametrize("name, password", [
        ("Алена", "123_45"),
        ("Alena", "pasSword")
    ])
    def test_registration_success(
            self,
            driver,
            register_user,
            wait_element_to_be_visible,
            wait_element_to_be_clickable,
            generate_login,
            name,
            password
    ):
        login = generate_login()

        # регистрация
        driver.get("https://stellarburgers.nomoreparties.site")

        wait_element_to_be_clickable(HomePageLocators.go_to_account_button)

        driver.find_element(*HomePageLocators.go_to_account_button).click()

        wait_element_to_be_clickable(LoginPageLocators.registration_link)

        driver.find_element(*LoginPageLocators.registration_link).click()

        wait_element_to_be_visible(RegistrationPageLocators.rp_password_input)

        driver.find_element(*RegistrationPageLocators.rp_name_input).send_keys(name)
        driver.find_element(*RegistrationPageLocators.rp_email_input).send_keys(login)
        driver.find_element(*RegistrationPageLocators.rp_password_input).send_keys(password)
        driver.find_element(*RegistrationPageLocators.sign_up_button).click()

        wait_element_to_be_visible(LoginPageLocators.login_header)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', "Регистрация не прошла"

        # проверка, что пользователь действительно создан
        driver.get("https://stellarburgers.nomoreparties.site/login")

        # логин с созданным пользователем
        driver.find_element(*LoginPageLocators.lp_email_input).send_keys(login)
        driver.find_element(*LoginPageLocators.lp_password_input).send_keys(password)
        driver.find_element(*LoginPageLocators.login_button).click()

        wait_element_to_be_visible(HomePageLocators.place_an_order_button)

        assert driver.find_element(*HomePageLocators.place_an_order_button).text == 'Оформить заказ', \
            "Авторизация не прошла"


    def test_registration_existing_user(
            self,
            driver,
            register_user,
            wait_element_to_be_visible,
            wait_element_to_be_clickable,
            generate_login
    ):
        name = "Алена"
        password = "123456"
        login = generate_login()

        # регистрация
        register_user(name, login, password)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', "Регистрация не прошла"

        # попытка регистрации с существующим пользователем
        driver.get("https://stellarburgers.nomoreparties.site/register")

        wait_element_to_be_visible(RegistrationPageLocators.rp_password_input)

        driver.find_element(*RegistrationPageLocators.rp_name_input).send_keys(name)
        driver.find_element(*RegistrationPageLocators.rp_email_input).send_keys(login)
        driver.find_element(*RegistrationPageLocators.rp_password_input).send_keys(password)
        driver.find_element(*RegistrationPageLocators.sign_up_button).click()

        wait_element_to_be_visible(RegistrationPageLocators.error_message_existing_user)

        error_message = driver.find_element(*RegistrationPageLocators.error_message_existing_user).text

        assert ('/register' in driver.current_url and error_message == "Такой пользователь уже существует")


    @pytest.mark.parametrize("name, password", [
        ("Алена", "123_4"),
        ("Alena", " ")
    ])
    def test_registration_with_incorrect_password_failed(
            self,
            driver,
            register_user,
            wait_element_to_be_visible,
            wait_element_to_be_clickable,
            generate_login,
            name,
            password
    ):
        login = generate_login()

        # регистрация с некорректным паролем
        driver.get("https://stellarburgers.nomoreparties.site/register")

        wait_element_to_be_visible(RegistrationPageLocators.rp_password_input)

        driver.find_element(*RegistrationPageLocators.rp_name_input).send_keys(name)
        driver.find_element(*RegistrationPageLocators.rp_email_input).send_keys(login)
        driver.find_element(*RegistrationPageLocators.rp_password_input).send_keys(password)
        driver.find_element(*RegistrationPageLocators.sign_up_button).click()

        error_message = driver.find_element(*RegistrationPageLocators.error_message_incorrect_password).text

        wait_element_to_be_visible(RegistrationPageLocators.error_message_incorrect_password)

        assert error_message == "Некорректный пароль"

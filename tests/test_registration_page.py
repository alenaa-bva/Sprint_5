import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import LoginData
from helpers import generate_login
from locators import RegistrationPageLocators, LoginPageLocators, HomePageLocators


# вспомогательные функции
def wait_element_to_be_clickable(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

def wait_element_to_be_visible(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

def register_user(driver, name, login, password):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    wait_element_to_be_visible(driver,RegistrationPageLocators.rp_password_input)

    driver.find_element(*RegistrationPageLocators.rp_name_input).send_keys(name)
    driver.find_element(*RegistrationPageLocators.rp_email_input).send_keys(login)
    driver.find_element(*RegistrationPageLocators.rp_password_input).send_keys(password)
    driver.find_element(*RegistrationPageLocators.sign_up_button).click()

    wait_element_to_be_visible(driver, LoginPageLocators.login_header)

    return register_user


#тесты
class TestRegistration:

    @pytest.mark.parametrize("name, password", [
        ("Алена", "123_45"),
        ("Alena", "pasSword")
    ])
    def test_registration_success(
            self,
            driver,
            name,
            password
    ):
        login = generate_login()

        # регистрация
        driver.get("https://stellarburgers.nomoreparties.site")

        wait_element_to_be_clickable(driver, HomePageLocators.go_to_account_button).click()

        wait_element_to_be_clickable(driver, LoginPageLocators.registration_link).click()

        wait_element_to_be_visible(driver, RegistrationPageLocators.rp_password_input)

        driver.find_element(*RegistrationPageLocators.rp_name_input).send_keys(name)
        driver.find_element(*RegistrationPageLocators.rp_email_input).send_keys(login)
        driver.find_element(*RegistrationPageLocators.rp_password_input).send_keys(password)
        driver.find_element(*RegistrationPageLocators.sign_up_button).click()

        wait_element_to_be_visible(driver, LoginPageLocators.login_header)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', "Регистрация не прошла"

        # проверка, что пользователь действительно создан

        # логин с созданным пользователем
        driver.find_element(*LoginPageLocators.lp_email_input).send_keys(login)
        driver.find_element(*LoginPageLocators.lp_password_input).send_keys(password)
        driver.find_element(*LoginPageLocators.login_button).click()

        button = wait_element_to_be_visible(driver, HomePageLocators.place_an_order_button).text

        assert button == 'Оформить заказ', "Авторизация не прошла"


    def test_registration_existing_user(
            self,
            driver
    ):
        # попытка регистрации с существующим пользователем
        driver.get("https://stellarburgers.nomoreparties.site/register")

        wait_element_to_be_visible(driver, RegistrationPageLocators.rp_password_input)

        driver.find_element(*RegistrationPageLocators.rp_name_input).send_keys(LoginData.name)
        driver.find_element(*RegistrationPageLocators.rp_email_input).send_keys(LoginData.login)
        driver.find_element(*RegistrationPageLocators.rp_password_input).send_keys(LoginData.password)
        driver.find_element(*RegistrationPageLocators.sign_up_button).click()

        error_message = wait_element_to_be_visible(driver, RegistrationPageLocators.error_message_existing_user).text

        assert ('/register' in driver.current_url and error_message == "Такой пользователь уже существует")


    @pytest.mark.parametrize("name, password", [
        ("Алена", "123_4"),
        ("Alena", " ")
    ])
    def test_registration_with_incorrect_password_failed(
            self,
            driver,
            name,
            password
    ):
        login = generate_login()

        # регистрация с некорректным паролем
        driver.get("https://stellarburgers.nomoreparties.site/register")

        wait_element_to_be_visible(driver, RegistrationPageLocators.rp_password_input)

        driver.find_element(*RegistrationPageLocators.rp_name_input).send_keys(name)
        driver.find_element(*RegistrationPageLocators.rp_email_input).send_keys(login)
        driver.find_element(*RegistrationPageLocators.rp_password_input).send_keys(password)
        driver.find_element(*RegistrationPageLocators.sign_up_button).click()

        error_message = wait_element_to_be_visible(driver, RegistrationPageLocators.error_message_incorrect_password).text

        assert error_message == "Некорректный пароль"

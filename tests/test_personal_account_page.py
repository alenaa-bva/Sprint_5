from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import LoginData
from locators import HomePageLocators, LoginPageLocators, PersonalAccountPage

# вспомогательные функции
def wait_element_to_be_clickable(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

def wait_element_to_be_visible(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located(locator))


#тесты
class TestProfile:

    def test_open_personal_account(
            self,
            driver
    ):
        driver.get("https://stellarburgers.nomoreparties.site")

        # переход на форму логина через кнопку войти в аккаунт
        wait_element_to_be_clickable(driver, HomePageLocators.go_to_account_button).click()

        # логин
        driver.find_element(*LoginPageLocators.lp_email_input).send_keys(LoginData.login)
        driver.find_element(*LoginPageLocators.lp_password_input).send_keys(LoginData.password)
        driver.find_element(*LoginPageLocators.login_button).click()

        order_button = wait_element_to_be_visible(driver, HomePageLocators.place_an_order_button).text

        assert order_button == 'Оформить заказ', "Авторизация не прошла"

        # переход в личный кабинет
        driver.find_element(*HomePageLocators.personal_account_button).click()

        email_input = wait_element_to_be_visible(driver, PersonalAccountPage.pa_email_input).get_attribute("value")

        assert '/account/profile' in driver.current_url and email_input is not None


    def test_logout(
            self,
            driver
    ):
        driver.get("https://stellarburgers.nomoreparties.site")


        # переход на форму логина через кнопку войти в аккаунт
        wait_element_to_be_clickable(driver, HomePageLocators.go_to_account_button).click()

        # логин
        driver.find_element(*LoginPageLocators.lp_email_input).send_keys(LoginData.login)
        driver.find_element(*LoginPageLocators.lp_password_input).send_keys(LoginData.password)
        driver.find_element(*LoginPageLocators.login_button).click()

        order_button = wait_element_to_be_visible(driver, HomePageLocators.place_an_order_button).text

        assert order_button == 'Оформить заказ', "Авторизация не прошла"

        # переход в личный кабинет
        driver.find_element(*HomePageLocators.personal_account_button).click()

        wait_element_to_be_visible(driver, PersonalAccountPage.pa_email_input)

        assert '/account/profile' in driver.current_url

        # выход из аккаунта
        driver.find_element(*PersonalAccountPage.logout_button).click()

        wait_element_to_be_visible(driver, LoginPageLocators.login_header)

        assert '/login' in driver.current_url








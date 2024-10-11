import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import LoginData
from locators import LoginPageLocators, HomePageLocators, PersonalAccountPage


# вспомогательные функции
def wait_element_to_be_clickable(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

def wait_element_to_be_visible(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

#тесты
class TestConstructor:

    @pytest.mark.parametrize("button", [
        PersonalAccountPage.pa_constructor_button,
        PersonalAccountPage.pa_logo
    ])
    def test_switch_from_personal_account_to_constructor_by_click_on_header_element(
            self,
            driver,
            button
    ):
        driver.get("https://stellarburgers.nomoreparties.site/login")

        wait_element_to_be_visible(driver,LoginPageLocators.login_button)

        # логин
        driver.find_element(*LoginPageLocators.lp_email_input).send_keys(LoginData.login)
        driver.find_element(*LoginPageLocators.lp_password_input).send_keys(LoginData.password)
        driver.find_element(*LoginPageLocators.login_button).click()

        order_button = wait_element_to_be_visible(driver, HomePageLocators.place_an_order_button).text

        assert order_button == 'Оформить заказ', "Авторизация не прошла"


        # переход в личный кабинет
        driver.find_element(*HomePageLocators.personal_account_button).click()

        wait_element_to_be_visible(driver, PersonalAccountPage.profile_tab)

        # переход на страницу конструктора
        driver.find_element(*button).click()

        header = wait_element_to_be_visible(driver, HomePageLocators.collect_a_burger_header).text

        assert header == 'Соберите бургер'


    def test_move_to_bread_section(
            self,
            driver
    ):

        driver.get("https://stellarburgers.nomoreparties.site")

        wait_element_to_be_visible(driver, HomePageLocators.first_bread_ingredient)

        header = driver.find_element(*HomePageLocators.breads_section_header).text

        assert header == 'Булки'


    def test_move_to_sauce_section(
            self,
            driver
    ):

        driver.get("https://stellarburgers.nomoreparties.site")

        wait_element_to_be_visible(driver, HomePageLocators.ingredients_section)

        driver.find_element(*HomePageLocators.sauce_tab).click()

        wait_element_to_be_visible(driver, HomePageLocators.first_sauce_ingredient)

        header = driver.find_element(*HomePageLocators.sauces_section_header).text

        assert header == 'Соусы'


    def test_move_to_fillings_section(
            self,
            driver
    ):

        driver.get("https://stellarburgers.nomoreparties.site")

        wait_element_to_be_visible(driver, HomePageLocators.ingredients_section)

        driver.find_element(*HomePageLocators.fillings_tab).click()

        wait_element_to_be_visible(driver, HomePageLocators.first_filling_ingredient)

        header = driver.find_element(*HomePageLocators.fillings_section_header).text

        assert header == 'Начинки'




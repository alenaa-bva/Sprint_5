import pytest
from locators import LoginPageLocators, HomePageLocators, PersonalAccountPage


class TestConstructor:

    @pytest.mark.parametrize("button", [
        PersonalAccountPage.pa_constructor_button,
        PersonalAccountPage.pa_logo
    ])
    def test_switch_from_personal_account_to_constructor_by_click_on_header_element(
            self,
            driver,
            register_user,
            wait_element_to_be_visible,
            wait_element_to_be_clickable,
            generate_login,
            button
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

        wait_element_to_be_visible(PersonalAccountPage.profile_tab)

        # переход на страницу конструктора
        driver.find_element(*button).click()

        wait_element_to_be_visible(HomePageLocators.collect_a_burger_header)

        assert driver.find_element(*HomePageLocators.collect_a_burger_header).text == 'Соберите бургер'


    def test_move_to_bread_section(
            self,
            driver,
            wait_element_to_be_visible
    ):

        driver.get("https://stellarburgers.nomoreparties.site")

        wait_element_to_be_visible(HomePageLocators.first_bread_ingredient)

        header = driver.find_element(*HomePageLocators.breads_section_header).text

        assert header == 'Булки'


    def test_move_to_sauce_section(
            self,
            driver,
            wait_element_to_be_visible
    ):

        driver.get("https://stellarburgers.nomoreparties.site")

        wait_element_to_be_visible(HomePageLocators.ingredients_section)

        driver.find_element(*HomePageLocators.sauce_tab).click()

        wait_element_to_be_visible(HomePageLocators.first_sauce_ingredient)

        header = driver.find_element(*HomePageLocators.sauces_section_header).text

        assert header == 'Соусы'


    def test_move_to_fillings_section(
            self,
            driver,
            wait_element_to_be_visible
    ):

        driver.get("https://stellarburgers.nomoreparties.site")

        wait_element_to_be_visible(HomePageLocators.ingredients_section)

        driver.find_element(*HomePageLocators.fillings_tab).click()

        wait_element_to_be_visible(HomePageLocators.first_filling_ingredient)

        header = driver.find_element(*HomePageLocators.fillings_section_header).text

        assert header == 'Начинки'




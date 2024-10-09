import random

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver

from locators import LoginPageLocators, RegistrationPageLocators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def wait_element_to_be_clickable(driver):
    def wait(locator, timeout=5):
        return WebDriverWait(driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
    return wait

@pytest.fixture
def wait_element_to_be_visible(driver):
    def wait(locator, timeout=5):
        return WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
    return wait

@pytest.fixture
def register_user(driver, wait_element_to_be_clickable, wait_element_to_be_visible):
    def register(name, login, password):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        wait_element_to_be_visible(RegistrationPageLocators.rp_password_input)
        driver.find_element(*RegistrationPageLocators.rp_name_input).send_keys(name)
        driver.find_element(*RegistrationPageLocators.rp_email_input).send_keys(login)
        driver.find_element(*RegistrationPageLocators.rp_password_input).send_keys(password)
        driver.find_element(*RegistrationPageLocators.sign_up_button).click()

        wait_element_to_be_visible(LoginPageLocators.login_header)

    return register

@pytest.fixture
def generate_login():
    def login():
        base_login = "alenaibragimova1"
        three_random_digits = random.randint(100, 999)
        email = f"{base_login}{three_random_digits}@yandex.ru"
        return email
    return login

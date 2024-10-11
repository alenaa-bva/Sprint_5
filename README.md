### Проект автоматизации тестирования сервиса Stellar Burgers

## Описание

Этот проект содержит автоматизированные тесты для сервиса Stellar Burgers с использованием **Selenium WebDriver**. 

## Стек технологий

- **Python** — основной язык для написания тестов.
- **Selenium WebDriver** — для взаимодействия с браузером.
- **Pytest** — фреймворк для организации тестов и их выполнения.


## Установка

* Установить WebDriver 
   
   
   Chrome https://www.selenium.dev/documentation/getting_started/installing_browser_drivers/
   
   Firefox https://www.selenium.dev/documentation/getting_started/installing_browser_drivers/


* Установить Selenium
   ```
   pip install selenium
   ```


* Установка зависимостей:
    ```
    pip install -r requirements.txt
    ```

## Запуск тестов
  
* Команда для запуска всех тестов:
   ```
    pytest -v
   ```
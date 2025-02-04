# lesson7.6
Working with data and saving results / Работа с данными и сохранение результатов

---

# Парсинг товаров с помощью Selenium и запись в CSV

Этот проект демонстрирует использование Selenium для парсинга данных с сайта [Divan.ru](https://www.divan.ru) и записи результатов в CSV-файл.

## Требования

- Python 3.6 или выше
- Установленный браузер Firefox
- Geckodriver, совместимый с вашей версией Firefox

## Установка

1. Убедитесь, что у вас установлен Python.
2. Установите необходимые библиотеки:
   ```bash
   pip install selenium
   ```
3. Скачайте Geckodriver и убедитесь, что его путь добавлен в системную переменную `PATH`.

## Описание работы

### Парсинг данных

Сценарий:
1. Запускает Firefox с помощью Selenium WebDriver.
2. Загружает страницу категории "Свет" на [Divan.ru](https://www.divan.ru/category/svet).
3. Ожидает появления элементов с классом `LlPhw`, которые содержат информацию о товарах.
4. Для каждого элемента извлекает:
   - Название товара (`div.lsooF span`),
   - Цена товара (`div.pY3d2 span`),
   - Ссылка на товар (`a`).
5. Собранные данные сохраняются в список.

### Запись данных в CSV

После завершения парсинга данные записываются в файл `divan_fixtures.csv`. Структура файла:
- `Название`: Название товара,
- `Цена`: Цена товара,
- `Ссылка`: URL товара.

## Запуск

1. Сохраните код в файл `divan_parser.py`.
2. Запустите файл:
   ```bash
   python divan_parser.py
   ```
3. После завершения работы файл `divan_fixtures.csv` будет создан в текущей директории.

## Примечания

- Убедитесь, что структура HTML сайта не изменилась. Если изменения есть, обновите CSS-селекторы в коде.
- Selenium использует WebDriver для взаимодействия с браузером. Убедитесь, что версия Firefox и Geckodriver совместимы.

## Полезные ссылки

- [Документация Selenium](https://www.selenium.dev/documentation/)
- [Официальный сайт Divan.ru](https://www.divan.ru)

## Лицензия

Этот проект создан для учебных целей.

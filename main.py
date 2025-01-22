import csv  # Импортируем библиотеку для работы с CSV-файлами
from selenium import webdriver  # Импортируем WebDriver из Selenium
from selenium.webdriver.common.by import By  # Импортируем By для поиска элементов
from selenium.webdriver.support.ui import WebDriverWait  # Импортируем WebDriverWait для ожидания элементов
from selenium.webdriver.support import expected_conditions as EC  # Импортируем условия ожидания

# Инициализация драйвера Firefox
driver = webdriver.Firefox()  # Создаем экземпляр WebDriver для Firefox
url = "https://www.divan.ru/category/svet"  # URL-адрес для парсинга

# Открытие URL
driver.get(url)  # Загружаем страницу

# Ожидание загрузки элементов на странице
wait = WebDriverWait(driver, 10)  # Устанавливаем ожидание до 10 секунд
fixtures = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'LlPhw')))  # Ожидаем появления элементов с классом 'LlPhw'
print(len(fixtures))  # Выводим количество найденных элементов

parsed_data = []  # Список для хранения данных о товарах

# Парсинг данных
for fixture in fixtures:
    try:
        # Извлекаем название, цену и ссылку для каждого товара
        name = fixture.find_element(By.CSS_SELECTOR, 'div.lsooF span').text  # Название товара
        price = fixture.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text  # Цена товара
        link = fixture.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')  # Ссылка на товар
    except Exception as e:
        # Обработка исключений, если данные не удалось извлечь
        print(f'Произошла ошибка при парсинге: {e}')
        continue

    # Добавляем данные в список
    parsed_data.append([name, price, link])

# Закрытие драйвера
driver.quit()  # Завершаем работу WebDriver

# Запись данных в CSV файл
with open('divan_fixtures.csv', 'w', newline='', encoding='utf-8') as file:  # Открываем файл для записи
    writer = csv.writer(file)  # Создаем объект writer для записи CSV
    writer.writerow(['Название', 'Цена', 'Ссылка'])  # Записываем заголовок
    writer.writerows(parsed_data)  # Записываем данные о товарах

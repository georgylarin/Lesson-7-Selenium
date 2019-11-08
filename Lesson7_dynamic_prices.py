from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
driver = webdriver.Chrome()
driver.get('https://lenta.com/catalog/konditerskie-izdeliya/')

button = driver.find_element_by_class_name('popup__close')
button.click()

chrome_options = Options()
chrome_options.add_argument('--headless')

while True:
    try:
        button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'catalog__pagination-button'))
        )
        button.click()
    except Exception as e:
        print(e)
        break

goods = driver.find_elements_by_class_name('sku-card-small')
for good in goods:
    print(good.find_element_by_class_name('sku-card-small__title').text)
    print(good.find_element_by_class_name('sku-card-small__link-block').get_attribute('href'))
    print('Обычная цена:', good.find_element_by_class_name('price__regular--small').text.replace(',','.'))
    print('Цена по карте:', good.find_element_by_class_name('price__primary--small').text)
    print(50*'#')









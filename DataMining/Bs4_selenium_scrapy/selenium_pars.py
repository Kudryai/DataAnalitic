import undetected_chromedriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import csv

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_argument('enable-automation')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-browser-side-navigation')
options.add_argument("--remote-debugging-port=9222")
options.add_argument('user-agent=Mozilla/6.0')
options.add_argument('-disable-application-cache –media-cache-size=1 –disk-cache-size=1')
# options.add_argument("--headless")
options.add_argument("--log-level=3")

driver = undetected_chromedriver.Chrome(options)
try:
    url = "https://1000kem.ru/catalog/vse_dlya_doma_1/"
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    action = ActionChains(driver)
    driver.get(url)
    driver.implicitly_wait(10)
    action.move_to_element(driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/div[2]/div[1]/a[6]'))
    action.perform()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="catalog_sorter"]/div[1]/div/a[3]/span[1]'))).click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="catalog_sorter"]/div[1]/div/a[3]/span[1]'))).click()
    html2 = driver.find_elements(By.CSS_SELECTOR,'div.catalog-item-price')
    while True:
        driver.execute_script("document.querySelector('#ajaxpages_catalog_identifier > div.ajaxpages.personal-tabsheader > a > span.tabbg-center').click();")
        time.sleep(3)
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.nofollow'))).click()
        # html = driver.find_element(By.CSS_SELECTOR, 'div.catalog-item-name')
        html2 = driver.find_elements(By.CSS_SELECTOR,'div.catalog-item-price')

except Exception as ex:
    print(ex)

html = driver.page_source
# with open('/mnt/c/Users/user/Desktop/DataAnalyst/DataAnalyst/DataAnalyst/DataMining/Bs4_selenium_scrapy/ga.html', 'w') as file:
#     print(html, file=file)
driver.quit()
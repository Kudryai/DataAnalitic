import undetected_chromedriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
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
    url = "https://investmint.ru/lkoh"
    driver.get(url)
    driver.implicitly_wait(10)
    # actions = ActionChains(driver)
    # btn_gazpr = driver.find_element(By.LINK_TEXT,'Газпром').click()
    # actions.move_to_element(btn_gazpr)
    # actions.perform()
    # # WebDriverWait(driver, timeout=10).until(EC.invisibility_of_element((By.CSS_SELECTOR)))
    # WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.LINK_TEXT,'Газпром'))).click()

except Exception as ex:
    print(ex)
html = driver.page_source
with open('/mnt/c/Users/user/Desktop/DataAnalyst/DataAnalyst/DataAnalyst/DataMining/VK_API/Bs4_selenium_scrapy/Divki.html', 'w') as file:
    print(html, file=file)
driver.quit()
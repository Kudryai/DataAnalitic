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
    url = "https://nbcomputers.ru/"
    driver.get(url)
    SearchInput = driver.find_element(By.XPATH, "//input[@type='search']")
    SearchInput.send_keys("Lenovo")
    action = ActionChains(driver)
    but = driver.find_element(By.XPATH, "//button[@type='submit']")
    action.move_to_element(but)
    action.send_keys(Keys.ENTER).perform()
    driver.implicitly_wait(100)
    print(driver.title)
    time.sleep(30)
    # action = ActionChains(driver)

    # driver.implicitly_wait(10)
    # action.move_to_element(butt)
    # action.perform()
    # driver.implicitly_wait(10)
    # html = driver.page_source
    # with open('/mnt/c/Users/user/Desktop/DataAnalyst/DataAnalyst/DataAnalyst/DataMining/Bs4_selenium_scrapy/ga.html','w') as f:
    #     f.write(html)



except Exception as ex:
    print(ex)
# html = driver.page_source
# with open('/mnt/c/Users/user/Desktop/DataAnalyst/DataAnalyst/DataAnalyst/DataMining/VK_API/Bs4_selenium_scrapy/Divki.html', 'w') as file:
#     print(html, file=file)
driver.quit()
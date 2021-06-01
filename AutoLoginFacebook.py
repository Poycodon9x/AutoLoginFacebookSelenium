import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.set_window_size(700,800)

driver.get('https://wwww.facebook.com/login')
time.sleep(1)

driver.find_element_by_id('email').send_keys('UID')
time.sleep(1)

driver.find_element_by_id('pass').send_keys('Pass')
time.sleep(1)

driver.find_element_by_name('login').click()
time.sleep(4)

driver.get('https://wwww.facebook.com/thanoscute')
time.sleep(1)
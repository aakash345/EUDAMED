from selenium import webdriver
import pandas as pd
import numpy as np
import openpyxl
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
email = 'hemant@narang.com'
password = 'Welcome@2023'
url = "https://webgate.ec.europa.eu/eudamed/secure#/actors/view/01FN5XFNVJ8M96HTNA777CB01K"
op = webdriver.ChromeOptions()
# op.add_argument('headless')
op.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)

driver.get(url)
time.sleep(2)
email_field = driver.find_element('name','username')
email_field.send_keys(email)
button = driver.find_element('name','whoamiSubmit')
driver.execute_script("arguments[0].click();", button)
# driver.find_elements_by_css_selector('button.btn-next')[0].click()
pass_field = driver.find_element('name','password')
pass_field.send_keys(password)
button = driver.find_element('name','_submit')
driver.execute_script("arguments[0].click();", button)

elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('id', 'nav-menu-expandable-group-click-2')))
myLink = driver.find_element('id', 'nav-menu-expandable-group-click-2')
myLink.click()

elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('id', "device-device-management-menu-register-new-UDI-DI"))) 

myLink = driver.find_element('id', 'device-device-management-menu-register-new-UDI-DI')
myLink.click()

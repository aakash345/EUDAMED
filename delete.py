from selenium import webdriver
import openpyxl
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import json
email = 'hemant@narang.com'
cred = 'Welcome@2023'
url = "https://webgate.ec.europa.eu/eudamed/secure#/actors/view/01FN5XFNVJ8M96HTNA777CB01K"
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)

driver.get(url)
time.sleep(2)
def login():
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(('name', 'username')))
    email_field = driver.find_element('name','username')
    email_field.send_keys(email)
    button = driver.find_element('name','whoamiSubmit')
    driver.execute_script("arguments[0].click();", button)
    # driver.find_elements_by_css_selector('button.btn-next')[0].click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(('name', 'password')))
    pass_field = driver.find_element('name','password')
    pass_field.send_keys(cred)
    button = driver.find_element('name','_submit')
    driver.execute_script("arguments[0].click();", button)

def manage_page():
    WebDriverWait(driver, 80).until(EC.presence_of_element_located((By.ID, 'nav-menu-expandable-group-click-2')))
    homeLink = driver.find_element(By.ID, 'general-home')
    driver.execute_script("arguments[0].click();", homeLink)
    navLink = driver.find_element(By.ID, 'nav-menu-expandable-group-click-2')
    driver.execute_script("arguments[0].click();", navLink)
    WebDriverWait(driver, 80).until(EC.presence_of_element_located((By.ID, "device-device-management-menu-manage-basic-UDI-DI-device-mf-confirmer"))) 
    manageLink = driver.find_element(By.ID, 'device-device-management-menu-manage-basic-UDI-DI-device-mf-confirmer')
    driver.execute_script("arguments[0].click();", manageLink)
    time.sleep(3)

login()
manage_page()

elem=1
while(elem):
    try:
        elem = WebDriverWait(driver, 80).until(EC.presence_of_element_located((By.ID, "basic-udidis-nav-dropdown-0"))) 
    except:
        elem=0
    if(elem):
        drpdn_btn = driver.find_element(By.ID, "basic-udidis-nav-dropdown-0")
        driver.execute_script("arguments[0].click();", drpdn_btn)
        view_btn = driver.find_element(By.LINK_TEXT, "View Data")
        driver.execute_script("arguments[0].click();", view_btn)
        time.sleep(3)
        del_btn = driver.find_element(By.ID, "device-device-management-button-delete")
        driver.execute_script("arguments[0].click();", del_btn)
        time.sleep(2)
        final = driver.find_element(By.ID, "general-button-yes")
        driver.execute_script("arguments[0].click();", final)
        time.sleep(5)

driver.quit()
    



# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestWrongdat2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_wrongdat2(self):
    self.driver.get("https://webgate.ec.europa.eu/eudamed/secure#/actors/view/01FN5XFNVJ8M96HTNA777CB01K")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.CSS_SELECTOR, "#nav-menu-expandable-group-click-2 > span").click()
    self.driver.find_element(By.CSS_SELECTOR, "#device-device-management-menu-register-new-UDI-DI > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".radio-button-item:nth-child(1) > .radio-button-label").click()
    self.driver.find_element(By.CSS_SELECTOR, ".rw-dropdown-list-value").click()
    self.driver.find_element(By.CSS_SELECTOR, ".rw-list-option:nth-child(1)").click()
    self.driver.find_element(By.ID, "basicUdi-code").click()
    self.driver.find_element(By.ID, "basicUdi-code").send_keys("8907097349.0702V")
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .radio-button-group > .radio-button-item:nth-child(1) > .radio-button-label").click()
    self.driver.find_element(By.ID, "general-button-save-and-next").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".rw-dropdown-list-value").click()
    self.driver.find_element(By.CSS_SELECTOR, ".rw-list-option:nth-child(3)").click()
    self.driver.execute_script("window.scrollTo(0,556.7999877929688)")
    
    self.driver.find_element(By.CSS_SELECTOR, ".ecl-row:nth-child(1) > .ecl-col > .fieldset-border > .radio").click()
    
    self.driver.find_element(By.CSS_SELECTOR, ".eud-u-mr-xs:nth-child(2) #implantable").click()
    
    self.driver.find_element(By.CSS_SELECTOR, ".eud-u-mr-xs:nth-child(2) #measuringFunction").click()
    
    self.driver.find_element(By.CSS_SELECTOR, ".eud-u-mr-xs:nth-child(2) #reusable").click()
    
    self.driver.find_element(By.CSS_SELECTOR, ".eud-u-mr-xs:nth-child(2) #active").click()
    
    self.driver.find_element(By.CSS_SELECTOR, ".eud-u-mr-xs:nth-child(2) #administeringMedicine").click()

    #if no
    self.driver.find_element(By.CSS_SELECTOR, ".slider").click()
    self.driver.find_element(By.CSS_SELECTOR, ".slider").click()

    self.driver.find_element(By.ID, "deviceModel").click()
    self.driver.find_element(By.ID, "deviceModel").send_keys("349.070")
    
    self.driver.find_element(By.ID, "deviceName").click()
    self.driver.find_element(By.ID, "deviceName").send_keys("Lane Bone Holding forceps without Ratchet, 300mm")
    self.driver.find_element(By.ID, "general-button-save-and-next").click()
  
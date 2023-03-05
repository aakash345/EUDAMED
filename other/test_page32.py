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

class TestPage32():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_page32(self):
    self.driver.get("https://webgate.ec.europa.eu/eudamed/secure#/devices/udiDiRegistrationHome")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.CSS_SELECTOR, "#nav-menu-expandable-group-click-2 > span").click()
    self.driver.find_element(By.CSS_SELECTOR, "#device-device-management-menu-register-new-UDI-DI > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".radio-button-item:nth-child(1) span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".rw-dropdown-list-value").click()
    self.driver.find_element(By.CSS_SELECTOR, ".rw-list-option:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .radio-button-group > .radio-button-item:nth-child(1) span").click()
    self.driver.find_element(By.ID, "basicUdi-code").click()
    self.driver.find_element(By.ID, "basicUdi-code").send_keys("8907097349.0702V")
    self.driver.find_element(By.ID, "general-button-save-and-next").click()
    element = self.driver.find_element(By.ID, "general-button-save-and-next")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".rw-dropdown-list-value").click()
    self.driver.find_element(By.CSS_SELECTOR, ".rw-list-option:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".eud-u-mr-xs:nth-child(2) #measuringFunction").click()
    self.driver.find_element(By.CSS_SELECTOR, ".eud-u-mr-xs:nth-child(2) #reusable").click()
    self.driver.find_element(By.ID, "active").click()
    self.driver.find_element(By.CSS_SELECTOR, ".eud-u-mr-xs:nth-child(2) #administeringMedicine").click()
    self.driver.find_element(By.ID, "deviceModel").click()
    self.driver.find_element(By.ID, "deviceModel").send_keys("349.070")
    self.driver.find_element(By.ID, "deviceName").click()
    self.driver.find_element(By.ID, "deviceName").send_keys("Lane Bone Holding forceps without Ratchet, 300mm")
    self.driver.find_element(By.CSS_SELECTOR, "#general-button-save-and-next > span:nth-child(1)").click()
    
    self.driver.find_element(By.CSS_SELECTOR, "#udiDiData-0--primaryDi-issuingAgency_input .rw-dropdown-list-value").click()
    self.driver.find_element(By.CSS_SELECTOR, ".rw-list-option:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#udiDiData-0--primaryDi-issuingAgency_input .rw-dropdown-list-value").click()
    self.driver.find_element(By.CSS_SELECTOR, ".rw-list-option:nth-child(4)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#udiDiData-0--primaryDi-issuingAgency_input .rw-dropdown-list-value").click()
    self.driver.find_element(By.CSS_SELECTOR, ".rw-list-option:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ecl-row:nth-child(3) .slider:nth-child(2)").click()
    self.driver.find_element(By.ID, "cndCode").click()
    self.driver.find_element(By.ID, "cndCode").send_keys("L091303")
    self.driver.find_element(By.CSS_SELECTOR, "#general-button-find > span:nth-child(2)").click()
    self.driver.find_element(By.ID, "udiDiData-0--tradeName-texts-0--text").click()
    self.driver.find_element(By.ID, "udiDiData-0--tradeName-texts-0--text").send_keys("NET")
    self.driver.find_element(By.ID, "udiDiData-0--reference").click()
    self.driver.find_element(By.ID, "udiDiData-0--reference").send_keys("349.070")
    self.driver.find_element(By.CSS_SELECTOR, ".eud-u-mr-xs:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".control-label label").click()
    self.driver.find_element(By.CSS_SELECTOR, ".eu-checkbox:nth-child(1) > .no-class").click()
    self.driver.find_element(By.CSS_SELECTOR, ".eu-checkbox:nth-child(3) > .no-class").click()
    self.driver.find_element(By.ID, "udiDiData-0--additionalDescription-texts-0--text").click()
    self.driver.find_element(By.ID, "udiDiData-0--additionalDescription-texts-0--text").send_keys("Lane Bone Holding forceps without Ratchet, 300mm")
    self.driver.find_element(By.CSS_SELECTOR, ".radio-button-item:nth-child(1) span").click()
    self.driver.find_element(By.CSS_SELECTOR, "#udiDiData-0--additionalDescription-texts-0--language_input .rw-btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".rw-list-option:nth-child(6)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#udiDiData-0--tradeName-texts-0--language_input .svg-inline--fa").click()
    self.driver.find_element(By.CSS_SELECTOR, "#udiDiData-0--tradeName-texts-0--language_listbox > .rw-list-option:nth-child(7)").click()
    self.driver.find_element(By.ID, "udiDiData-0--primaryDi-code").click()
    self.driver.find_element(By.ID, "udiDiData-0--primaryDi-code").send_keys("08907097349.0702V0")
    self.driver.find_element(By.CSS_SELECTOR, ".glyphicon-chevron-right").click()
    self.driver.find_element(By.CSS_SELECTOR, ".done:nth-child(4) .label-wizard > span").click()
    self.driver.find_element(By.ID, "udiDiData-0--primaryDi-code").click()
    self.driver.find_element(By.ID, "udiDiData-0--primaryDi-code").send_keys("08907097112790")
    self.driver.find_element(By.ID, "general-button-save-and-next").click()
    self.driver.execute_script("window.scrollTo(0,2404)")
  
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

class TestPage4():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_page4(self):
    self.driver.get("https://webgate.ec.europa.eu/eudamed/secure#/devices/udiDiRegistrationHome")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.CSS_SELECTOR, ".radio-button-item:nth-child(1) span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".rw-dropdown-list-value").click()
    self.driver.find_element(By.CSS_SELECTOR, ".rw-list-option:nth-child(1)").click()
    self.driver.find_element(By.ID, "basicUdi-code").click()
    self.driver.find_element(By.ID, "basicUdi-code").send_keys("8907097349.0702V")
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .radio-button-group > .radio-button-item:nth-child(1) span").click()
    self.driver.find_element(By.CSS_SELECTOR, "#general-button-save-and-next > span:nth-child(1)").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".rw-dropdown-list-value").click()
    self.driver.find_element(By.CSS_SELECTOR, ".rw-list-option:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ecl-row:nth-child(2) > .ecl-col > .fieldset-border > .radio").click()
    self.driver.find_element(By.CSS_SELECTOR, ".eud-u-mr-xs:nth-child(2) #measuringFunction").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ecl-row:nth-child(3) .eud-u-mr-xs:nth-child(2)").click()
    self.driver.find_element(By.ID, "active").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ecl-row:nth-child(5) .eud-u-mr-xs:nth-child(2) > span").click()
    self.driver.find_element(By.ID, "deviceModel").click()
    self.driver.find_element(By.ID, "deviceModel").send_keys("349.070")
    self.driver.find_element(By.ID, "deviceName").click()
    self.driver.find_element(By.ID, "deviceName").send_keys("Lane Bone Holding forceps without Ratchet, 300mm")
    self.driver.find_element(By.CSS_SELECTOR, "#general-button-save-and-next > span:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ecl-row:nth-child(3) .slider:nth-child(2)").click()
    self.driver.find_element(By.ID, "cndCode").click()
    self.driver.find_element(By.ID, "cndCode").send_keys("L091303")
    self.driver.find_element(By.ID, "general-button-find").click()
    self.driver.find_element(By.ID, "udiDiData-0--tradeName-texts-0--text").click()
    self.driver.find_element(By.ID, "udiDiData-0--tradeName-texts-0--text").send_keys("NET")
    self.driver.find_element(By.CSS_SELECTOR, "#udiDiData-0--tradeName-texts-0--language_input .svg-inline--fa").click()
    self.driver.find_element(By.CSS_SELECTOR, ".rw-list-option:nth-child(7)").click()
    self.driver.find_element(By.ID, "udiDiData-0--reference").click()
    self.driver.find_element(By.ID, "udiDiData-0--reference").send_keys("349.070")
    self.driver.find_element(By.CSS_SELECTOR, ".eud-u-mr-xs:nth-child(1) > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".control-label label").click()
    self.driver.find_element(By.CSS_SELECTOR, ".eu-checkbox:nth-child(1) > .no-class").click()
    self.driver.find_element(By.CSS_SELECTOR, ".eu-checkbox:nth-child(3) > .no-class").click()
    self.driver.find_element(By.ID, "udiDiData-0--additionalDescription-texts-0--text").click()
    self.driver.find_element(By.ID, "udiDiData-0--additionalDescription-texts-0--text").send_keys("Lane Bone Holding forceps without Ratchet, 300mm")
    self.driver.find_element(By.CSS_SELECTOR, "#udiDiData-0--additionalDescription-texts-0--language_input .rw-btn").click()
    self.driver.find_element(By.CSS_SELECTOR, "#udiDiData-0--additionalDescription-texts-0--language_listbox > .rw-list-option:nth-child(6)").click()
    self.driver.find_element(By.NAME, "udiDiData[0].deviceStatus.type").click()
    self.driver.find_element(By.ID, "udiDiData-0--primaryDi-code").click()
    self.driver.find_element(By.ID, "udiDiData-0--primaryDi-code").send_keys("08907097349.0702V6")
    self.driver.find_element(By.CSS_SELECTOR, "#general-button-save-and-next > span:nth-child(1)").click()
    self.driver.find_element(By.LINK_TEXT, "UDI-DI identification information").click()
    self.driver.find_element(By.ID, "udiDiData-0--primaryDi-code").click()
    self.driver.find_element(By.ID, "udiDiData-0--primaryDi-code").send_keys("0089070971127906")
    self.driver.find_element(By.CSS_SELECTOR, "#general-button-save-and-next > span:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".done:nth-child(4) .label-wizard > span").click()
    self.driver.find_element(By.ID, "udiDiData-0--primaryDi-code").click()
    self.driver.find_element(By.ID, "udiDiData-0--primaryDi-code").send_keys("089070971127906")
    self.driver.find_element(By.ID, "udiDiData-0--primaryDi-code").click()
    self.driver.find_element(By.ID, "udiDiData-0--primaryDi-code").send_keys("08907097112796")
    self.driver.find_element(By.ID, "general-button-save-and-next").click()
    
    self.driver.find_element(By.CSS_SELECTOR, ".ecl-row:nth-child(2) > .col-md-12:nth-child(1) .slider:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ecl-row:nth-child(3) .eud-u-mr-xs:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ecl-col:nth-child(3) .slider").click()
    self.driver.find_element(By.CSS_SELECTOR, ".eud-u-mr-xs:nth-child(2) #udiDiData-0--sterilization").click()
    self.driver.find_element(By.CSS_SELECTOR, ".eud-u-mr-xs:nth-child(2) #udiDiData-0--sterile").click()
    self.driver.find_element(By.CSS_SELECTOR, ".eud-u-mr-xs:nth-child(2) #udiDiData-0--latex").click()
    self.driver.find_element(By.CSS_SELECTOR, ".eud-u-mr-xs:nth-child(2) #udiDiData-0--cmrSubstance").click()
    self.driver.find_element(By.CSS_SELECTOR, ".eud-u-mr-xs:nth-child(2) #udiDiData-0--endocrineDisruptor").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ecl-row:nth-child(8) .slider:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ecl-row:nth-child(9) .slider:nth-child(2)").click()
    self.driver.find_element(By.ID, "general-button-save-and-next").click()
  

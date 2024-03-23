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

class TestSuite1():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_t1(self):
    self.driver.get("https://www.selenium.dev/selenium-ide/")
    self.driver.set_window_size(1536, 864)
    self.driver.find_element(By.LINK_TEXT, "Docs").click()
    assert self.driver.title == "Getting Started · Selenium IDE"
    self.driver.close()
  
  def test_t2(self):
    self.driver.get("https://www.selenium.dev/")
    self.driver.set_window_size(1536, 864)
    read_more_selenium_ide = self.driver.find_element(By.CSS_SELECTOR, ".selenium-ide:nth-child(1)")
    self.driver.execute_script("arguments[0].scrollIntoView(false);", read_more_selenium_ide)
    time.sleep(1)
    read_more_selenium_ide.click()    
    self.driver.find_element(By.LINK_TEXT, "Help").click()
    self.driver.find_element(By.CSS_SELECTOR, ".docMainWrapper").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Need help?"
    self.driver.close()
  

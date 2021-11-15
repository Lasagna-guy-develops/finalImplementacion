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

class TestTC42():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tC42(self):
    self.driver.get("https://final-implementacion-smz.herokuapp.com/")
    self.driver.set_window_size(1920, 1024)
    self.driver.find_element(By.CSS_SELECTOR, "form:nth-child(3) > input").click()
    self.driver.find_element(By.CSS_SELECTOR, "form").click()
    self.driver.find_element(By.ID, "fact").click()
    self.driver.find_element(By.ID, "fact").send_keys("-2")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
  

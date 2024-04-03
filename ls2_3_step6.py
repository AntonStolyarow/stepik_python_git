#work with new tabs (switching to new tab)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  browser = webdriver.Chrome()
  link = 'http://suninjuly.github.io/redirect_accept.html'
  browser.get(link)
  button_troll = browser.find_element(By.CSS_SELECTOR, 'button.trollface')
  button_troll.click()
  new_page = browser.window_handles[1]
  to_new_page = browser.switch_to.window(new_page)
  x = browser.find_element(By.ID, 'input_value').text
  input_field = browser.find_element(By.ID,'answer')
  input_field.send_keys(calc(x))
  button_submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
  button_submit.click()
  alert_window = browser.switch_to.alert
  alert_window_data = alert_window.text
  addToClipBoard = alert_window_data.split(': ')[-1]
  print("HERE", addToClipBoard)
  alert_window.accept()

finally:
  browser.quit()  
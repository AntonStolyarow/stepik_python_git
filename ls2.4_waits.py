from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
try:
  link = 'http://suninjuly.github.io/explicit_wait2.html'
  browser.get(link)
  #WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "price")))
  WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100")
  )
  button = browser.find_element(By.ID, 'book')
  button.click()
  numbers = int((browser.find_element(By.ID, "input_value")).text)
  answer_field = browser.find_element(By.ID, "answer")
  answer_field.send_keys(calc(numbers))
  browser.find_element(By.ID, "solve").click()
  #take from answer from popup
  alert_window = browser.switch_to.alert
  alert_window_data = alert_window.text
  addToClipBoard = alert_window_data.split(': ')[-1]
  print("HERE", addToClipBoard)
  alert_window.accept()
  time.sleep(5)
  
finally:
  browser.quit()
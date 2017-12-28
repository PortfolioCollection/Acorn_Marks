from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests

acorn_url = 'https://acorn.utoronto.ca/sws/welcome.do?welcome.dispatch'
marks_url = 'https://acorn.utoronto.ca/sws/transcript/academic/main.do?main.dispatch'

wait_interval = 10

def read_credentials():
      login = open("credentials.txt","r")
      username = login.readline()
      password = login.readline()
      return (username,password)

def submit_credentials(driver):
      credentials = read_credentials()
      
      user = driver.find_element_by_name("user")
      user.clear()
      user.send_keys(credentials[0])    #Your username

      pas = driver.find_element_by_name("pass")
      pas.clear()
      pas.send_keys(credentials[1])     #Your password

      pas.send_keys(Keys.RETURN)

def login():
      driver = webdriver.Firefox()
      driver.get(acorn_url)

      try:
          element = WebDriverWait(driver, wait_interval).until(
              EC.presence_of_element_located((By.NAME , "user"))
          )

      finally:
            submit_credentials(driver)

      try:
          element = WebDriverWait(driver, wait_interval).until(
              EC.presence_of_element_located((By.CLASS_NAME , "acorn"))
          )
      finally:
            driver.get(marks_url)
            for course in driver.find_elements_by_class_name("courses"):
                  print(course.text)
            print("\n")
            a = input("Press a key to exit")
            driver.close()

if __name__ == "__main__":
      login();


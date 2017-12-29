from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests

login_url = 'https://weblogin.utoronto.ca/'
acorn_url = 'https://acorn.utoronto.ca/sws/welcome.do?welcome.dispatch#/'
marks_url = 'https://acorn.utoronto.ca/sws/transcript/academic/main.do?main.dispatch'

wait_interval = 10

def read_credentials():
      login = open("credentials.txt","r")
      username = login.readline()
      password = login.readline()
      return (username,password)

def submit_credentials(driver):
      credentials = read_credentials()
      username = credentials[0].strip()
      password = credentials[1].strip()
      user = driver.find_element_by_name("user")
      user.send_keys(username)    #Your username
      pas = driver.find_element_by_name("pass")
      pas.send_keys(password)     #Your password
      pas.send_keys(Keys.RETURN)

def login():
      driver = webdriver.PhantomJS()
      driver.get(acorn_url)

      wait = WebDriverWait(driver, 10)
      wait.until(lambda driver: driver.current_url == login_url)

      submit_credentials(driver)

      wait.until(lambda driver: driver.current_url == acorn_url)

      driver.get(marks_url)
      for course in driver.find_elements_by_class_name("courses"):
            print(course.text)
      print("\n")
            
      a = input("Press a key to exit")           
      driver.close()

if __name__ == "__main__":
      login();


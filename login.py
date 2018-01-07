from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
import files
import credentials
import email_sender
import time
import os.path

login_url = 'https://weblogin.utoronto.ca/'
acorn_url = 'https://acorn.utoronto.ca/sws/welcome.do?welcome.dispatch#/'
marks_url = 'https://acorn.utoronto.ca/sws/transcript/academic/main.do?main.dispatch'

wait_interval = 10

def submit_credentials(driver):
      info = credentials.read_credentials();
      username = info[0].strip()
      password = info[1].strip()
      user = driver.find_element_by_name("user")
      user.send_keys(username)    #Your username
      pas = driver.find_element_by_name("pass")
      pas.send_keys(password)     #Your password
      pas.send_keys(Keys.RETURN)

def login():
      TIMEOUT = 300
      update = False
      if os.path.exists("saved"):
        update = True
        
      while True:
            print("...............................")  
            print ("Logging in ACORN")
            requests.packages.urllib3.disable_warnings()
            info = credentials.read_credentials()
            username, password, gmail_address, gmail_password, to_address = info
            driver = weblogin(username,password)
            update,body = files.update_file(update,driver)

            if(update):
                  email_sender.send_mail(info,body)
                  # update the file on the next iteartion 
                  update = False
                  # reset email body
                  body = ""
            print ("Recheck in " + str(TIMEOUT) + " seconds ... \n")
            time.sleep(TIMEOUT)         

      driver.close()

def weblogin(username,password):
      driver = webdriver.PhantomJS()
      driver.get(acorn_url)

      wait = WebDriverWait(driver, 10)
      wait.until(lambda driver: driver.current_url == login_url)
      
      submit_credentials(driver)

      wait.until(lambda driver: driver.current_url == acorn_url)

      driver.get(marks_url)
      return driver

if __name__ == "__main__":
      login();


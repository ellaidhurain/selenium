from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import unittest
import csv

class TestMail(unittest.TestCase):
    
    def setUp(self):
        chrome_options = Options()
        
        # Initialize the webdriver
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    
    def tearDown(self):
        # Close the browser
        self.driver.quit()
       
    # add news
    def test_add_mail(self):
        driver = self.driver
        with open('data/regional_school_data.csv', 'r') as f:
            reader = csv.reader(f)
            # Skip the header row
            next(reader)
            for row in reader:
                school_mail = row[8]
                
                wait = WebDriverWait(driver, 10)
                driver.get("https://www.yopmail.com/en/")
                
                
                wait.until(EC.element_to_be_clickable((By.ID, "login")))
                email_input = driver.find_element(By.ID, "login")
                email_input.clear()
                email_input.send_keys(school_mail)
                
                wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "md")))
                check_inbox_button = driver.find_element(By.XPATH, '//*[@id="refreshbut"]/button')
                check_inbox_button.click()

                inbox_loaded = EC.presence_of_element_located((By.XPATH, "//*[@id='webmail']/div[1]/div/main/div[1]/div/div[1]"))
                wait.until(inbox_loaded)

                email_address = driver.find_element(By.CLASS_NAME, "bname").text
                print("Email address:", email_address)
                
                wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "hlink.bl")))
                element = driver.find_element(By.CLASS_NAME, "hlink.bl")
                element.click()
                
                # time.sleep(10)

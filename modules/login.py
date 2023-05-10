import json
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import csv
from selenium.common.exceptions import StaleElementReferenceException


# # Read the JSON file
with open('config/login_data.json') as f:
    login = json.load(f)

class TestLogin(unittest.TestCase):

    def setUp(self):
        # Initialize the webdriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser
        self.driver.quit()
        
    def test_login_valid(self):
        d = self.driver
        
        # open csv file
        with open('data/login.csv', 'r') as f:
            # read data
            reader = csv.reader(f)
            # Skip the header row
            next(reader)
            
            # loop all values in sheet
            for row in reader:
                username = row[0]
                password = row[1]
                
                # loop all values in json
                for data in login["login_data"]:
                    # time.sleep(10)
                    # navigate to the home page and click login
                    wait = WebDriverWait(d, timeout=10)
                    time.sleep(1)
                  
                    d.get(data['valid_home_link'])
                    
                    d.find_element(By.LINK_TEXT, "Login").click()
                    
                    # Wait for the login page to load
                    wait.until(EC.url_matches(data["valid_login_link"]))

                    # verify text with assert method
                    act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
                    exp_title = data["login_confirm_text"]

                    self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

                    # invalid login check
                    d.find_element(By.NAME, "Username").send_keys(username)
                    d.find_element(By.NAME, "Password").send_keys(password)
                    d.find_element(By.XPATH, data["login_btn_locator"]).click()

                    # time.sleep(2)
                    # Wait for the page to load after login
                    wait.until(EC.url_matches(data["valid_dashboard_link"]))
                    wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
                    # time.sleep(2)
                    ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
                    li_elements = ul_element.find_elements(By.TAG_NAME,"li")
                    li_elements[0].click() 
                  
                    wait.until(EC.url_matches(data["valid_dashboard_link"]),)
                    act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

                    exp_title = data["dashboard_confirm_text"]

                    self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

                    
                    d.find_element(By.XPATH,data["profile_menu_locator"]).click()
                    
                    time.sleep(1)
                    
                    settings_ul_element = d.find_element(By.XPATH, data["settings_ul_locator"]) 
                    settings_li_element = settings_ul_element.find_elements(By.TAG_NAME,"li")
                    
                    settings_li_element[2].click()
                    
                    wait.until(EC.url_matches(data["valid_login_link"]))
                    
                    act_title = d.find_element(By.XPATH, data["logout_confirm_text_locator"]).text
                    exp_title = data["logout_confirm_text"]

                    self.assertEqual(act_title, exp_title, f"logout failed: expected '{exp_title}', but got '{act_title}'")

                    


    def test_login_invalid(self):
        d = self.driver
        with open('data/login.csv', 'r') as f:
            reader = csv.reader(f)
            # Skip the header row
            next(reader)
            for row in reader:
                invalid_username = row[2]
                invalid_password = row[3]
                
                for data in login["login_data"]:
                    # time.sleep(10)
                    # navigate to the home page and click login
                    d.get(data['valid_home_link'])
                    d.find_element(By.LINK_TEXT, "Login").click()
                    wait = WebDriverWait(d, 10)

                    # Wait for the login page to load
                    wait.until(EC.url_matches(data["valid_login_link"]))

                    # verify text with assert method
                    act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
                    exp_title = data["login_confirm_text"]

                    self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

                    # invalid login check
                    d.find_element(By.NAME, "Username").send_keys(invalid_username)
                    d.find_element(By.NAME, "Password").send_keys(invalid_password)
                    d.find_element(By.XPATH, data["login_btn_locator"]).click()

                    self.assertEqual(d.current_url, data["valid_login_link"], "Login with invalid credentials should not have been successful")

    def test_logout(self):
        d = self.driver
        with open('data/login.csv', 'r') as f:
            reader = csv.reader(f)
            # Skip the header row
            next(reader)
            for row in reader:
                username = row[0]
                password = row[1]
                
                for data in login["login_data"]:
                    # time.sleep(10)
                    # navigate to the home page and click login
                    d.get(data['valid_home_link'])
                    d.find_element(By.LINK_TEXT, "Login").click()
                    wait = WebDriverWait(d, 10)

                    # Wait for the login page to load
                    wait.until(EC.url_matches(data["valid_login_link"]))

                    # verify text with assert method
                    act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
                    exp_title = data["login_confirm_text"]

                    self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

                    # invalid login check
                    d.find_element(By.NAME, "Username").send_keys(username)
                    d.find_element(By.NAME, "Password").send_keys(password)
                    d.find_element(By.XPATH, data["login_btn_locator"]).click()

                    # time.sleep(2)
                    # Wait for the page to load after login
                    wait.until(EC.url_matches(data["valid_dashboard_link"]))
                    wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
                    # time.sleep(2)
                    ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
                    li_element = ul_element.find_elements(By.TAG_NAME,"li")
                    li_element[0].click()

                    wait.until(EC.url_matches(data["valid_dashboard_link"]))
                    act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

                    exp_title = data["dashboard_confirm_text"]

                    self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

                    # logout menu
                    d.find_element(By.XPATH,data["profile_menu_locator"]).click()
                    
                    settings_ul_element = d.find_element(By.XPATH, data["settings_ul_locator"]) 
                    settings_li_element = settings_ul_element.find_elements(By.TAG_NAME,"li")
                    
                    settings_li_element[2].click()
                    
                    wait.until(EC.url_matches(data["valid_login_link"]))
                    
                    act_title = d.find_element(By.XPATH, data["logout_confirm_text_locator"]).text
                    exp_title = data["logout_confirm_text"]

                    self.assertEqual(act_title, exp_title, f"logout failed: expected '{exp_title}', but got '{act_title}'")

                    time.sleep(10)
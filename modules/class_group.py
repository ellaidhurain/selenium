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
import sys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import Select

# # Read the JSON file
with open('config/login_data.json') as f:
    login = json.load(f)
    
class TestClassGroup(unittest.TestCase):
    
    def setUp(self):
        # Initialize the webdriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser
        self.driver.quit()

    def test_add_class_group(self):
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
                        li_elements[2].click()    
                    
                        # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
                        # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

                        # exp_title = data["dashboard_confirm_text"]

                        # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[4]")),)
                        class_group_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[4]")
                        class_group_module.click()
    
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[1]/div[2]/button")),)
                        class_group_add = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[1]/div[2]/button")
                        class_group_add.click()                    
    
                        wait.until(EC.element_to_be_clickable((By.NAME, "Group")),)
                        class_group_add = d.find_element(By.NAME, "Group")
                        class_group_add.send_keys("6th")
                    
                        # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[2]/p/label/span[1]/input")),)
                        # class_group_all = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[2]/p/label/span[1]/input")
                        # class_group_all.click()
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[2]/div/div/div")),)
                        class_group_all = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[2]/div/div/div")
                        class_group_all.click()
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")),)
                        class_group_all_ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
                        class_group_li = class_group_all_ul.find_elements(By.TAG_NAME,"li")
                        class_group_li[0].click()
                        
                        class_group_all_ul.send_keys(Keys.ESCAPE)
                            
                        # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[3]/button[1]")),)
                        # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[3]/button[1]")
                        # cancel_btn.click()
                    
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[3]/button[2]")),)
                        save_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[3]/button[2]")
                        save_btn.click()

                        sleep(5)
                        
                        
    # def test_add_class_group(self):
    #         d = self.driver
    #         # open csv file
    #         with open('data/login.csv', 'r') as f:
    #             # read data
    #             reader = csv.reader(f)
    #             # Skip the header row
    #             next(reader)
                
    #             # loop all values in sheet
    #             for row in reader:
    #                 username = row[0]
    #                 password = row[1]
                    
    #                 # loop all values in json
    #                 for data in login["login_data"]:
    #                     # time.sleep(10)
    #                     # navigate to the home page and click login
    #                     wait = WebDriverWait(d, timeout=10)
    #                     time.sleep(1)
                    
    #                     d.get(data['valid_home_link'])
                        
    #                     d.find_element(By.LINK_TEXT, "Login").click()
                        
    #                     # Wait for the login page to load
    #                     wait.until(EC.url_matches(data["valid_login_link"]))

    #                     # verify text with assert method
    #                     act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
    #                     exp_title = data["login_confirm_text"]

    #                     self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

    #                     # invalid login check
    #                     d.find_element(By.NAME, "Username").send_keys(username)
    #                     d.find_element(By.NAME, "Password").send_keys(password)
    #                     d.find_element(By.XPATH, data["login_btn_locator"]).click()

    #                     # time.sleep(2)
    #                     # Wait for the page to load after login
    #                     wait.until(EC.url_matches(data["valid_dashboard_link"]))
    #                     wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
    #                     # time.sleep(2)
    #                     ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
    #                     li_elements = ul_element.find_elements(By.TAG_NAME,"li")
    #                     li_elements[2].click()    
                    
    #                     # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                     # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                     # exp_title = data["dashboard_confirm_text"]

    #                     # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[4]")),)
    #                     class_group_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[4]")
    #                     class_group_module.click()
    
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[2]/div[1]/li/a/button")),)
    #                     class_group_edit = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[2]/div[1]/li/a/button")
    #                     class_group_edit.click()                    
    
    #                     wait.until(EC.element_to_be_clickable((By.NAME, "Group")),)
    #                     class_group_add = d.find_element(By.NAME, "Group")
    #                     class_group_add.send_keys(Keys.CONTROL + "a")
    #                     class_group_add.send_keys(Keys.BACK_SPACE)
    #                     class_group_add.send_keys("6th")
                    
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[2]/p/label/span[1]/input")),)
    #                     # class_group_all = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[2]/p/label/span[1]/input")
    #                     # class_group_all.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[2]/div/div/div")),)
    #                     class_group_all = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[2]/div/div/div")
    #                     class_group_all.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")),)
    #                     class_group_all_ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                     class_group_li = class_group_all_ul.find_elements(By.TAG_NAME,"li")
    #                     class_group_li[0].click()
    #                     class_group_li[1].click()
                        
    #                     class_group_all_ul.send_keys(Keys.ESCAPE)
                            
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[3]/button[1]")),)
    #                     # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[3]/button[1]")
    #                     # cancel_btn.click()
                    
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[3]/button[2]")),)
    #                     save_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[3]/button[2]")
    #                     save_btn.click()

    #                     sleep(5)
                        
                        
    # def test_delete_class_group(self):
    #         d = self.driver
    #         # open csv file
    #         with open('data/login.csv', 'r') as f:
    #             # read data
    #             reader = csv.reader(f)
    #             # Skip the header row
    #             next(reader)
                
    #             # loop all values in sheet
    #             for row in reader:
    #                 username = row[0]
    #                 password = row[1]
                    
    #                 # loop all values in json
    #                 for data in login["login_data"]:
    #                     # time.sleep(10)
    #                     # navigate to the home page and click login
    #                     wait = WebDriverWait(d, timeout=10)
    #                     time.sleep(1)
                    
    #                     d.get(data['valid_home_link'])
                        
    #                     d.find_element(By.LINK_TEXT, "Login").click()
                        
    #                     # Wait for the login page to load
    #                     wait.until(EC.url_matches(data["valid_login_link"]))

    #                     # verify text with assert method
    #                     act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
    #                     exp_title = data["login_confirm_text"]

    #                     self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

    #                     # invalid login check
    #                     d.find_element(By.NAME, "Username").send_keys(username)
    #                     d.find_element(By.NAME, "Password").send_keys(password)
    #                     d.find_element(By.XPATH, data["login_btn_locator"]).click()

    #                     # time.sleep(2)
    #                     # Wait for the page to load after login
    #                     wait.until(EC.url_matches(data["valid_dashboard_link"]))
    #                     wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
    #                     # time.sleep(2)
    #                     ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
    #                     li_elements = ul_element.find_elements(By.TAG_NAME,"li")
    #                     li_elements[2].click()    
                    
    #                     # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                     # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                     # exp_title = data["dashboard_confirm_text"]

    #                     # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[4]")),)
    #                     class_group_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[4]")
    #                     class_group_module.click()
    
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[2]/div[1]/li/button")),)
    #                     class_group_delete = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[2]/div[1]/li/button")
    #                     class_group_delete.click()                    
                                
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div/button[1]")),)
    #                     # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div/button[1]")
    #                     # cancel_btn.click()
                    
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div/button[2]")),)
    #                     confirm_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div/button[2]")
    #                     confirm_btn.click()

    #                     sleep(5)
                        
                        

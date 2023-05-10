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

class TestCommunication(unittest.TestCase):
    
    def setUp(self):
        # Initialize the webdriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser
        self.driver.quit()


    # def test_compose_message(self):

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
    #                     li_elements[0].click()    
                    
    #                     # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                     # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                     # exp_title = data["dashboard_confirm_text"]

    #                     # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")
                                
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[17]")))
                        
    #                     communication_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[17]")
    #                     communication_module.click()
    
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[1]/div[2]/button")))
                        
    #                     compose_message = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[1]/div[2]/button")
    #                     compose_message.click()
    
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/form/div[1]/div/div/div")))
                        
    #                     to = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/form/div[1]/div/div/div")
    #                     to.click()
                       
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                        
    #                     to_ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                     li = to_ul.find_elements(By.TAG_NAME,"li")
    #                     sleep(1)
    #                     li[1].click()
    #                     li[2].click()
                        
    #                     to_ul.send_keys(Keys.ESCAPE)
                        
                        
    
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/form/div[2]/div/div/input")))
                        
    #                     subject = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/form/div[2]/div/div/input")
    #                     subject.send_keys("hi how are you?")
    
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/form/div[3]/div/div[2]/div/div/div/div/div/div")))
                        
    #                     message = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/form/div[3]/div/div[2]/div/div/div/div/div/div")
    #                     message.send_keys("this is a message from campuzone school")
                        
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/div/button[1]")))
                        
    #                     # add_to_draft = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/div/button[1]")
    #                     # add_to_draft.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/div/button[2]")))
                        
    #                     send = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/div/button[2]")
    #                     send.click()
                        
    #                     sleep(5)

    # def test_forward_message(self):

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
    #                     li_elements[0].click()    
                    
    #                     # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                     # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                     # exp_title = data["dashboard_confirm_text"]

    #                     # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")
                                
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[17]")))
                        
    #                     communication_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[17]")
    #                     communication_module.click()
    
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div/div/button[2]")))
                        
    #                     send_items_tab = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div/div/button[2]")
    #                     send_items_tab.click()
    
    #                     wait.until(EC.element_to_be_clickable((By.TAG_NAME, "tbody")))
                        
    #                     forward_message = d.find_element(By.TAG_NAME, "tbody")
    #                     tr_ul = forward_message.find_elements(By.TAG_NAME, "tr")
    #                     td_li = tr_ul[0].find_elements(By.TAG_NAME, "td")
    #                     td_li[2].click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/button[1]")))
    #                     sleep(2)
    #                     forward = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/button[1]")
    #                     forward.click()
                        
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/button[2]")))
    #                     # sleep(2)
    #                     # print = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/button[2]")
    #                     # print.click()
                       
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/form/div[1]/div/div/div")))
                        
    #                     to = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/form/div[1]/div/div/div")
    #                     to.click()
                       
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                        
    #                     to_ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                     li = to_ul.find_elements(By.TAG_NAME,"li")
    #                     sleep(1)
    #                     li[1].click()
    #                     li[2].click()
                        
    #                     to_ul.send_keys(Keys.ESCAPE)
                        
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/div/button[1]")))
                        
    #                     # add_to_draft = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/div/button[1]")
    #                     # add_to_draft.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/div/button[2]")))
                        
    #                     send = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/div/button[2]")
    #                     send.click()
                        
    #                     sleep(5)

    def test_draft_message(self):

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
                    
                        # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
                        # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

                        # exp_title = data["dashboard_confirm_text"]

                        # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")
                                
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[17]")))
                        
                        communication_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[17]")
                        communication_module.click()
    
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div/div/button[3]")))
                        
                        draft_items_tab = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div/div/button[3]")
                        draft_items_tab.click()
    
                        wait.until(EC.element_to_be_clickable((By.TAG_NAME, "tbody")))
                        
                        forward_message = d.find_element(By.TAG_NAME, "tbody")
                        tr_ul = forward_message.find_elements(By.TAG_NAME, "tr")
                        td_li = tr_ul[0].find_elements(By.TAG_NAME, "td")
                        td_li[1].click()
                       
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/form/div[1]/div/div/div")))
                        
                        to = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/form/div[1]/div/div/div")
                        to.click()
                       
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                        
                        to_ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
                        li = to_ul.find_elements(By.TAG_NAME,"li")
                        sleep(1)
                        li[1].click()
                        li[2].click()
                        
                        to_ul.send_keys(Keys.ESCAPE)
                        
                        # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/div/button[1]")))
                        
                        # add_to_draft = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/div/button[1]")
                        # add_to_draft.click()
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/div/button[2]")))
                        
                        send = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[1]/div/div/button[2]")
                        send.click()
                        
                        sleep(5)

                        
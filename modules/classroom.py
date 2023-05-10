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

# # Read the JSON file
with open('config/login_data.json') as f:
    login = json.load(f)

with open('config/classroom.json') as f:
    classroom = json.load(f)

class TestClassRoom(unittest.TestCase):

    def setUp(self):
        # Initialize the webdriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser
        self.driver.quit()

    # def test_class_room_add(self):
    #     d = self.driver
        
    #     # open csv file
    #     with open('data/login.csv', 'r') as f:
    #         # read data
    #         reader = csv.reader(f)
    #         # Skip the header row
    #         next(reader)
            
    #         # loop all values in sheet
    #         for row in reader:
    #             username = row[0]
    #             password = row[1]
                
    #             # loop all values in json
    #             for data in login["login_data"]:
    #                 # time.sleep(10)
    #                 # navigate to the home page and click login
    #                 wait = WebDriverWait(d, timeout=10)
    #                 time.sleep(1)
                  
    #                 d.get(data['valid_home_link'])
                    
    #                 d.find_element(By.LINK_TEXT, "Login").click()
                    
    #                 # Wait for the login page to load
    #                 wait.until(EC.url_matches(data["valid_login_link"]))

    #                 # verify text with assert method
    #                 act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
    #                 exp_title = data["login_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 # invalid login check
    #                 d.find_element(By.NAME, "Username").send_keys(username)
    #                 d.find_element(By.NAME, "Password").send_keys(password)
    #                 d.find_element(By.XPATH, data["login_btn_locator"]).click()

    #                 # time.sleep(2)
    #                 # Wait for the page to load after login
    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]))
    #                 wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
    #                 # time.sleep(2)
    #                 ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
    #                 li_elements = ul_element.find_elements(By.TAG_NAME,"li")
    #                 li_elements[1].click() 
                  
    #                 # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                 # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 # exp_title = data["dashboard_confirm_text"]

    #                 # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 with open('data/class_room.csv', 'r') as f:
    #                     reader = csv.reader(f)
    #                     # Skip the two header row
    #                     next(reader)
                        
    #                     for row in reader:
    #                         class_name = row[0]
    #                         section = row[1]
    #                         classroom_no = row[2]
    #                         notes = row[2]
                            
    #                         for class_room_data in classroom["classroom_data"]:
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["classroom_module"])))
                                
    #                             calendar_module = d.find_element(By.XPATH, class_room_data["classroom_module"])
    #                             calendar_module.click()
                                    
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["add_new_classroom"])))
    #                             add_new_classroom = d.find_element(By.XPATH, class_room_data["add_new_classroom"])
    #                             add_new_classroom.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME,"Class_name")))
    #                             add_new_classroom = d.find_element(By.NAME,"Class_name")
    #                             add_new_classroom.send_keys(class_name)
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/div/div/div")))
    #                             class_group = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/div/div/div")
    #                             class_group.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[3]/ul")))
                                
    #                             ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
    #                             li = ul.find_elements(By.TAG_NAME,"li")
    #                             li[0].click()
                                
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div/div/div")))
    #                             standard = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div/div/div")
    #                             standard.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[3]/ul")))
                                
    #                             ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
    #                             li = ul.find_elements(By.TAG_NAME,"li")
    #                             # sleep(2)
    #                             li[0].click()
    #                             # sleep(2)
                                
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME,"Section")))
    #                             Section = d.find_element(By.NAME,"Section")
    #                             Section.send_keys(section)
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME,"Class_room_no")))
    #                             Class_room_no = d.find_element(By.NAME,"Class_room_no")
    #                             Class_room_no.send_keys(classroom_no)
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME,"Notes")))
    #                             Notes = d.find_element(By.NAME,"Notes")
    #                             Notes.send_keys(notes)
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[7]/button[1]")))
    #                             # cancel_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[7]/button[1]")
    #                             # cancel_btn.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[7]/button[2]")))
    #                             save_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[7]/button[2]")
    #                             save_btn.click()
                                
                                
    #                             sleep(5)
        
    # def test_class_room_edit(self):
    #     d = self.driver
        
    #     # open csv file
    #     with open('data/login.csv', 'r') as f:
    #         # read data
    #         reader = csv.reader(f)
    #         # Skip the header row
    #         next(reader)
            
    #         # loop all values in sheet
    #         for row in reader:
    #             username = row[0]
    #             password = row[1]
                
    #             # loop all values in json
    #             for data in login["login_data"]:
    #                 # time.sleep(10)
    #                 # navigate to the home page and click login
    #                 wait = WebDriverWait(d, timeout=10)
    #                 time.sleep(1)
                  
    #                 d.get(data['valid_home_link'])
                    
    #                 d.find_element(By.LINK_TEXT, "Login").click()
                    
    #                 # Wait for the login page to load
    #                 wait.until(EC.url_matches(data["valid_login_link"]))

    #                 # verify text with assert method
    #                 act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
    #                 exp_title = data["login_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 # invalid login check
    #                 d.find_element(By.NAME, "Username").send_keys(username)
    #                 d.find_element(By.NAME, "Password").send_keys(password)
    #                 d.find_element(By.XPATH, data["login_btn_locator"]).click()

    #                 # time.sleep(2)
    #                 # Wait for the page to load after login
    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]))
    #                 wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
    #                 # time.sleep(2)
    #                 ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
    #                 li_elements = ul_element.find_elements(By.TAG_NAME,"li")
    #                 li_elements[1].click() 
                  
    #                 # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                 # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 # exp_title = data["dashboard_confirm_text"]

    #                 # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 with open('data/class_room.csv', 'r') as f:
    #                     reader = csv.reader(f)
    #                     # Skip the two header row
    #                     next(reader)
                        
    #                     for row in reader:
    #                         class_name = row[0]
    #                         section = row[1]
    #                         classroom_no = row[2]
    #                         notes = row[2]
                            
    #                         for class_room_data in classroom["classroom_data"]:
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["classroom_module"])))
                                
    #                             calendar_module = d.find_element(By.XPATH, class_room_data["classroom_module"])
    #                             calendar_module.click()
                                    
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["add_new_classroom"])))
    #                             parent_div = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div")
    #                             child_div = parent_div.find_elements(By.TAG_NAME,"div")
    #                             ul = child_div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/ul")
    #                             li = ul.find_element(By.TAG_NAME,"li")
                                
    #                             button = li.find_elements(By.TAG_NAME,"button")
                                
    #                             edit_btn = button[0].click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME,"Class_name")))
    #                             Class_name = d.find_element(By.NAME,"Class_name")
    #                             Class_name.click()
    #                             Class_name.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             Class_name.send_keys(Keys.BACKSPACE)
                              
    #                             Class_name.send_keys(class_name)
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/div/div/div")))
    #                             class_group = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/div/div/div")
    #                             class_group.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[3]/ul")))
                                
    #                             ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
    #                             li = ul.find_elements(By.TAG_NAME,"li")
    #                             li[2].click()
                                
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div/div/div")))
    #                             standard = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div/div/div")
    #                             standard.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[3]/ul")))
                                
    #                             ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
    #                             li = ul.find_elements(By.TAG_NAME,"li")
    #                             # sleep(2)
    #                             li[0].click()
    #                             # sleep(2)
                                
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME,"Section")))
    #                             Section = d.find_element(By.NAME,"Section")
    #                             Section.click()
    #                             Section.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             Section.send_keys(Keys.BACKSPACE)
    #                             Section.send_keys(section)
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME,"Class_room_no")))
    #                             Class_room_no = d.find_element(By.NAME,"Class_room_no")
    #                             Class_room_no.click()
    #                             Class_room_no.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             Class_room_no.send_keys(Keys.BACKSPACE)
                               
    #                             Class_room_no.send_keys(classroom_no)
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME,"Notes")))
    #                             Notes = d.find_element(By.NAME,"Notes")
    #                             Class_room_no.click()
    #                             Class_room_no.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             Class_room_no.send_keys(Keys.BACKSPACE)
                               
    #                             Notes.send_keys(notes)
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[7]/button[1]")))
    #                             # cancel_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[7]/button[1]")
    #                             # cancel_btn.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[7]/button[2]")))
    #                             save_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[7]/button[2]")
    #                             save_btn.click()

    # def test_class_room_delete(self):
    #     d = self.driver
        
    #     # open csv file
    #     with open('data/login.csv', 'r') as f:
    #         # read data
    #         reader = csv.reader(f)
    #         # Skip the header row
    #         next(reader)
            
    #         # loop all values in sheet
    #         for row in reader:
    #             username = row[0]
    #             password = row[1]
                
    #             # loop all values in json
    #             for data in login["login_data"]:
    #                 # time.sleep(10)
    #                 # navigate to the home page and click login
    #                 wait = WebDriverWait(d, timeout=10)
    #                 time.sleep(1)
                  
    #                 d.get(data['valid_home_link'])
                    
    #                 d.find_element(By.LINK_TEXT, "Login").click()
                    
    #                 # Wait for the login page to load
    #                 wait.until(EC.url_matches(data["valid_login_link"]))

    #                 # verify text with assert method
    #                 act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
    #                 exp_title = data["login_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 # invalid login check
    #                 d.find_element(By.NAME, "Username").send_keys(username)
    #                 d.find_element(By.NAME, "Password").send_keys(password)
    #                 d.find_element(By.XPATH, data["login_btn_locator"]).click()

    #                 # time.sleep(2)
    #                 # Wait for the page to load after login
    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]))
    #                 wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
    #                 # time.sleep(2)
    #                 ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
    #                 li_elements = ul_element.find_elements(By.TAG_NAME,"li")
    #                 li_elements[1].click() 
                  
    #                 # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                 # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 # exp_title = data["dashboard_confirm_text"]

    #                 # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 with open('data/class_room.csv', 'r') as f:
    #                     reader = csv.reader(f)
    #                     # Skip the two header row
    #                     next(reader)
                        
    #                     for row in reader:
    #                         class_name = row[0]
    #                         section = row[1]
    #                         classroom_no = row[2]
    #                         notes = row[2]
                            
    #                         for class_room_data in classroom["classroom_data"]:
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["classroom_module"])))
                                
    #                             calendar_module = d.find_element(By.XPATH, class_room_data["classroom_module"])
    #                             calendar_module.click()
                                    
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["add_new_classroom"])))
    #                             parent_div = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div")
    #                             child_div = parent_div.find_elements(By.TAG_NAME,"div")
    #                             ul = child_div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/ul")
    #                             li = ul.find_element(By.TAG_NAME,"li")
                                
    #                             button = li.find_elements(By.TAG_NAME,"button")
                                
    #                             edit_btn = button[1].click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div/button[1]")))
    #                             # cancel_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div/button[1]")
    #                             # cancel_btn.click()

    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div/button[2]")))
    #                             sure_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div/button[2]")
    #                             sure_btn.click()
                                
    #                             # sleep(5)
    
    # def test_class_room_search(self):
    #     d = self.driver
        
    #     # open csv file
    #     with open('data/login.csv', 'r') as f:
    #         # read data
    #         reader = csv.reader(f)
    #         # Skip the header row
    #         next(reader)
            
    #         # loop all values in sheet
    #         for row in reader:
    #             username = row[0]
    #             password = row[1]
                
    #             # loop all values in json
    #             for data in login["login_data"]:
    #                 # time.sleep(10)
    #                 # navigate to the home page and click login
    #                 wait = WebDriverWait(d, timeout=10)
    #                 time.sleep(1)
                  
    #                 d.get(data['valid_home_link'])
                    
    #                 d.find_element(By.LINK_TEXT, "Login").click()
                    
    #                 # Wait for the login page to load
    #                 wait.until(EC.url_matches(data["valid_login_link"]))

    #                 # verify text with assert method
    #                 act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
    #                 exp_title = data["login_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 # invalid login check
    #                 d.find_element(By.NAME, "Username").send_keys(username)
    #                 d.find_element(By.NAME, "Password").send_keys(password)
    #                 d.find_element(By.XPATH, data["login_btn_locator"]).click()

    #                 # time.sleep(2)
    #                 # Wait for the page to load after login
    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]))
    #                 wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
    #                 # time.sleep(2)
    #                 ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
    #                 li_elements = ul_element.find_elements(By.TAG_NAME,"li")
    #                 li_elements[1].click() 
                  
    #                 # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                 # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 # exp_title = data["dashboard_confirm_text"]

    #                 # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 for class_room_data in classroom["classroom_data"]:
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["classroom_module"])))
                        
    #                     calendar_module = d.find_element(By.XPATH, class_room_data["classroom_module"])
    #                     calendar_module.click()
                            
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[1]/div[1]/div/div/input")))
    #                     search_bar = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[1]/div[1]/div/div/input")
                        
    #                     search_key ="martin"
    #                     ActionChains(d).click(search_bar).perform()
    #                     for character in search_key:
    #                         ActionChains(d).send_keys(character).perform()
    
    # def test_class_room_add_new_academic_year(self):
    #     d = self.driver
        
    #     # open csv file
    #     with open('data/login.csv', 'r') as f:
    #         # read data
    #         reader = csv.reader(f)
    #         # Skip the header row
    #         next(reader)
            
    #         # loop all values in sheet
    #         for row in reader:
    #             username = row[0]
    #             password = row[1]
                
    #             # loop all values in json
    #             for data in login["login_data"]:
    #                 # time.sleep(10)
    #                 # navigate to the home page and click login
    #                 wait = WebDriverWait(d, timeout=10)
    #                 time.sleep(1)
                  
    #                 d.get(data['valid_home_link'])
                    
    #                 d.find_element(By.LINK_TEXT, "Login").click()
                    
    #                 # Wait for the login page to load
    #                 wait.until(EC.url_matches(data["valid_login_link"]))

    #                 # verify text with assert method
    #                 act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
    #                 exp_title = data["login_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 # invalid login check
    #                 d.find_element(By.NAME, "Username").send_keys(username)
    #                 d.find_element(By.NAME, "Password").send_keys(password)
    #                 d.find_element(By.XPATH, data["login_btn_locator"]).click()

    #                 # time.sleep(2)
    #                 # Wait for the page to load after login
    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]))
    #                 wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
    #                 # time.sleep(2)
    #                 ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
    #                 li_elements = ul_element.find_elements(By.TAG_NAME,"li")
    #                 li_elements[1].click() 
                  
    #                 # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                 # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 # exp_title = data["dashboard_confirm_text"]

    #                 # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 with open('data/class_room.csv', 'r') as f:
    #                     reader = csv.reader(f)
    #                     # Skip the two header row
    #                     next(reader)
                        
    #                     for row in reader:
    #                         # class_strength = row[5]
    #                         # notes = row[6]
                            
    #                         for class_room_data in classroom["classroom_data"]:
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["classroom_module"])))
                                
    #                             calendar_module = d.find_element(By.XPATH, class_room_data["classroom_module"])
    #                             calendar_module.click()
                                    
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["add_new_classroom"])))
    #                             parent_div = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div")
    #                             child_div = parent_div.find_elements(By.TAG_NAME,"div")
    #                             ul = child_div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/ul")
    #                             li = ul.find_element(By.TAG_NAME,"li")
    #                             div = li.find_elements(By.TAG_NAME,"div")
    #                             inside = div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[3]/ul/li/div[2]/p[1]")
    #                             action = ActionChains(d)
    #                             action.move_to_element(inside).click().perform()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["add_new_classroom_academic_year"])))
    #                             add = d.find_element(By.XPATH,class_room_data["add_new_classroom_academic_year"])
    #                             add.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["year"])))
    #                             year_input = d.find_element(By.XPATH,class_room_data["year"])
    #                             year_input.click()
                                
    #                             ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
    #                             li = ul.find_elements(By.TAG_NAME, "li")
                                
    #                             li[0].click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["teacher"])))
    #                             teacher = d.find_element(By.XPATH,class_room_data["teacher"])
    #                             teacher.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["year"])))
    #                             teacher_ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
    #                             li = teacher_ul.find_elements(By.TAG_NAME, "li")
                                
    #                             li[0].click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME,"Class_strength")))
    #                             Class_strength = d.find_element(By.NAME,"Class_strength")
    #                             Class_strength.send_keys("200")
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME,"Name")))
    #                             Name = d.find_element(By.NAME,"Name")
    #                             Name.send_keys("new class")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[6]/button[1]")))
    #                             # cancel_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[6]/button[1]")
    #                             # cancel_btn.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[6]/button[2]")))
    #                             save_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[6]/button[2]")
    #                             save_btn.click()
                                
                                
                                
    #                             sleep(5)
                                
    # def test_class_room_edit_new_academic_year(self):
    #     d = self.driver
        
    #     # open csv file
    #     with open('data/login.csv', 'r') as f:
    #         # read data
    #         reader = csv.reader(f)
    #         # Skip the header row
    #         next(reader)
            
    #         # loop all values in sheet
    #         for row in reader:
    #             username = row[0]
    #             password = row[1]
                
    #             # loop all values in json
    #             for data in login["login_data"]:
    #                 # time.sleep(10)
    #                 # navigate to the home page and click login
    #                 wait = WebDriverWait(d, timeout=10)
    #                 time.sleep(1)
                  
    #                 d.get(data['valid_home_link'])
                    
    #                 d.find_element(By.LINK_TEXT, "Login").click()
                    
    #                 # Wait for the login page to load
    #                 wait.until(EC.url_matches(data["valid_login_link"]))

    #                 # verify text with assert method
    #                 act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
    #                 exp_title = data["login_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 # invalid login check
    #                 d.find_element(By.NAME, "Username").send_keys(username)
    #                 d.find_element(By.NAME, "Password").send_keys(password)
    #                 d.find_element(By.XPATH, data["login_btn_locator"]).click()

    #                 # time.sleep(2)
    #                 # Wait for the page to load after login
    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]))
    #                 wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
    #                 # time.sleep(2)
    #                 ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
    #                 li_elements = ul_element.find_elements(By.TAG_NAME,"li")
    #                 li_elements[1].click() 
                  
    #                 # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                 # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 # exp_title = data["dashboard_confirm_text"]

    #                 # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 with open('data/class_room.csv', 'r') as f:
    #                     reader = csv.reader(f)
    #                     # Skip the two header row
    #                     next(reader)
                        
    #                     for row in reader:
    #                         # class_strength = row[5]
    #                         # notes = row[6]
                            
    #                         for class_room_data in classroom["classroom_data"]:
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["classroom_module"])))
                                
    #                             calendar_module = d.find_element(By.XPATH, class_room_data["classroom_module"])
    #                             calendar_module.click()
                                    
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["add_new_classroom"])))
    #                             parent_div = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div")
    #                             child_div = parent_div.find_elements(By.TAG_NAME,"div")
    #                             ul = child_div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/ul")
    #                             li = ul.find_element(By.TAG_NAME,"li")
    #                             div = li.find_elements(By.TAG_NAME,"div")
    #                             inside = div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[3]/ul/li/div[2]/p[1]")
    #                             action = ActionChains(d)
    #                             action.move_to_element(inside).click().perform()
                                
    #                             wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
    #                             table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                             table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                             table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
    #                             button = table_cell[3].find_elements(By.TAG_NAME, "button")

    #                             edit_btn = button[0]
    #                             edit_btn.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["year"])))
    #                             year_input = d.find_element(By.XPATH,class_room_data["year"])
    #                             year_input.click()
                                
    #                             ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
    #                             li = ul.find_elements(By.TAG_NAME, "li")
                                
    #                             li[0].click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["teacher"])))
    #                             teacher = d.find_element(By.XPATH,class_room_data["teacher"])
    #                             teacher.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["year"])))
    #                             teacher_ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
    #                             li = teacher_ul.find_elements(By.TAG_NAME, "li")
                                
    #                             li[0].click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME,"Class_strength")))
    #                             Class_strength = d.find_element(By.NAME,"Class_strength")
                                
    #                             Class_strength.click()
    #                             Class_strength.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             Class_strength.send_keys(Keys.BACKSPACE)
                              
    #                             Class_strength.send_keys("201")
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME,"Name")))
    #                             Notes = d.find_element(By.NAME,"Name")
                                
    #                             Notes.click()
    #                             Notes.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             Notes.send_keys(Keys.BACKSPACE)
                              
    #                             Notes.clear()
    #                             Notes.send_keys("new class")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[6]/button[1]")))
    #                             # cancel_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[6]/button[1]")
    #                             # cancel_btn.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[6]/button[2]")))
    #                             save_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[6]/button[2]")
    #                             save_btn.click()                                                                   
                                
    # def test_class_room_delete_academic_year(self):
    #     d = self.driver
        
    #     # open csv file
    #     with open('data/login.csv', 'r') as f:
    #         # read data
    #         reader = csv.reader(f)
    #         # Skip the header row
    #         next(reader)
            
    #         # loop all values in sheet
    #         for row in reader:
    #             username = row[0]
    #             password = row[1]
                
    #             # loop all values in json
    #             for data in login["login_data"]:
    #                 # time.sleep(10)
    #                 # navigate to the home page and click login
    #                 wait = WebDriverWait(d, timeout=10)
    #                 time.sleep(1)
                  
    #                 d.get(data['valid_home_link'])
                    
    #                 d.find_element(By.LINK_TEXT, "Login").click()
                    
    #                 # Wait for the login page to load
    #                 wait.until(EC.url_matches(data["valid_login_link"]))

    #                 # verify text with assert method
    #                 act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
    #                 exp_title = data["login_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 # invalid login check
    #                 d.find_element(By.NAME, "Username").send_keys(username)
    #                 d.find_element(By.NAME, "Password").send_keys(password)
    #                 d.find_element(By.XPATH, data["login_btn_locator"]).click()

    #                 # time.sleep(2)
    #                 # Wait for the page to load after login
    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]))
    #                 wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
    #                 # time.sleep(2)
    #                 ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
    #                 li_elements = ul_element.find_elements(By.TAG_NAME,"li")
    #                 li_elements[1].click() 
                  
    #                 # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                 # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 # exp_title = data["dashboard_confirm_text"]

    #                 # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

                            
    #                 for class_room_data in classroom["classroom_data"]:
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["classroom_module"])))
                        
    #                     calendar_module = d.find_element(By.XPATH, class_room_data["classroom_module"])
    #                     calendar_module.click()
                            
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["add_new_classroom"])))
    #                     parent_div = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div")
    #                     child_div = parent_div.find_elements(By.TAG_NAME,"div")
    #                     ul = child_div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/ul")
    #                     li = ul.find_element(By.TAG_NAME,"li")
    #                     div = li.find_elements(By.TAG_NAME,"div")
    #                     inside = div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[3]/ul/li/div[2]/p[1]")
    #                     action = ActionChains(d)
    #                     action.move_to_element(inside).click().perform()
                        
    #                     wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
    #                     table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                     table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                     table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
    #                     button = table_cell[3].find_elements(By.TAG_NAME, "button")

    #                     delete_btn = button[1]
    #                     delete_btn.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div/button[1]")))
    #                     cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div/button[1]")
    #                     cancel_btn.click()
                        
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div/button[2]")))
    #                     # sure_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div/button[2]")
    #                     # sure_btn.click()
                        
                        
                        
                        
    #                     sleep(5)
                    
    # def test_class_room_search_academic_academic_year(self):
    #     d = self.driver
        
    #     # open csv file
    #     with open('data/login.csv', 'r') as f:
    #         # read data
    #         reader = csv.reader(f)
    #         # Skip the header row
    #         next(reader)
            
    #         # loop all values in sheet
    #         for row in reader:
    #             username = row[0]
    #             password = row[1]
                
    #             # loop all values in json
    #             for data in login["login_data"]:
       
    #                 wait = WebDriverWait(d, timeout=10)
    #                 time.sleep(1)
                  
    #                 d.get(data['valid_home_link'])
                    
    #                 d.find_element(By.LINK_TEXT, "Login").click()
                    
    #                 # Wait for the login page to load
    #                 wait.until(EC.url_matches(data["valid_login_link"]))

    #                 # verify text with assert method
    #                 act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
    #                 exp_title = data["login_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 # invalid login check
    #                 d.find_element(By.NAME, "Username").send_keys(username)
    #                 d.find_element(By.NAME, "Password").send_keys(password)
    #                 d.find_element(By.XPATH, data["login_btn_locator"]).click()

                  
    #                 # Wait for the page to load after login
    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]))
    #                 wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
                
    #                 ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
    #                 li_elements = ul_element.find_elements(By.TAG_NAME,"li")
    #                 li_elements[1].click() 
                  
    #                 # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                 # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 # exp_title = data["dashboard_confirm_text"]

    #                 # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

                            
    #                 for class_room_data in classroom["classroom_data"]:
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["classroom_module"])))
                        
    #                     calendar_module = d.find_element(By.XPATH, class_room_data["classroom_module"])
    #                     calendar_module.click()
                            
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["add_new_classroom"])))
    #                     parent_div = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div")
    #                     child_div = parent_div.find_elements(By.TAG_NAME,"div")
    #                     ul = child_div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/ul")
    #                     li = ul.find_element(By.TAG_NAME,"li")
    #                     div = li.find_elements(By.TAG_NAME,"div")
    #                     inside = div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[3]/ul/li/div[2]/p[1]")
    #                     action = ActionChains(d)
    #                     action.move_to_element(inside).click().perform()
                        
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div[1]/div/div/input")))
    #                     # search_bar = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div[1]/div/div/input")

    #                     # ActionChains(d).click(search_bar).perform()
    #                     # for character in "calen":
    #                     #     ActionChains(d).send_keys(character).perform()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[4]/div/div[3]/div/nav")))
                        
    #                     pagination = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[4]/div/div[3]/div/nav")
    #                     ul = pagination.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[4]/div/div[3]/div/nav/ul")
    #                     li = ul.find_elements(By.TAG_NAME, "li")
    #                     li[1].click()
                                    
    #                     sleep(5)
                 
    # ---- students -----       
    # def test_class_room_add_students(self):
    #     d = self.driver
        
    #     # open csv file
    #     with open('data/login.csv', 'r') as f:
    #         # read data
    #         reader = csv.reader(f)
    #         # Skip the header row
    #         next(reader)
            
    #         # loop all values in sheet
    #         for row in reader:
    #             username = row[0]
    #             password = row[1]
                
    #             # loop all values in json
    #             for data in login["login_data"]:
    #                 # time.sleep(10)
    #                 # navigate to the home page and click login
    #                 wait = WebDriverWait(d, timeout=10)
    #                 time.sleep(1)
                  
    #                 d.get(data['valid_home_link'])
                    
    #                 d.find_element(By.LINK_TEXT, "Login").click()
                    
    #                 # Wait for the login page to load
    #                 wait.until(EC.url_matches(data["valid_login_link"]))

    #                 # verify text with assert method
    #                 act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
    #                 exp_title = data["login_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 # invalid login check
    #                 d.find_element(By.NAME, "Username").send_keys(username)
    #                 d.find_element(By.NAME, "Password").send_keys(password)
    #                 d.find_element(By.XPATH, data["login_btn_locator"]).click()

    #                 # time.sleep(2)
    #                 # Wait for the page to load after login
    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]))
    #                 wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
    #                 # time.sleep(2)
    #                 ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
    #                 li_elements = ul_element.find_elements(By.TAG_NAME,"li")
    #                 li_elements[1].click() 
                  
    #                 # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                 # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 # exp_title = data["dashboard_confirm_text"]

    #                 # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

                            
    #                 for class_room_data in classroom["classroom_data"]:
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["classroom_module"])))
                        
    #                     calendar_module = d.find_element(By.XPATH, class_room_data["classroom_module"])
    #                     calendar_module.click()
                            
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["add_new_classroom"])))
    #                     parent_div = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div")
    #                     child_div = parent_div.find_elements(By.TAG_NAME,"div")
    #                     ul = child_div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/ul")
    #                     li = ul.find_element(By.TAG_NAME,"li")
    #                     div = li.find_elements(By.TAG_NAME,"div")
    #                     inside = div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[3]/ul/li/div[2]/p[1]")
    #                     action = ActionChains(d)
    #                     action.move_to_element(inside).click().perform()
                        
    #                     wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
    #                     table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                     table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                     table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
    #                     year_btn = table_cell[0].find_element(By.TAG_NAME, "p")

    #                     year_btn.click()
                        
    #                     sleep(1)
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div[2]/button")))
    #                     add_new_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div[2]/button")
    #                     add_new_btn.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[1]/div/div/div")))
    #                     student = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[1]/div/div/div")
    #                     student.click()
                        
    #                     ul = student.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
    #                     # li = ul.find_elements(By.TAG_NAME, "li")
    #                     li = ul.find_element(By.TAG_NAME, "button")
    #                     li.click()
                        
    #                     li.send_keys(Keys.ESCAPE)
                        
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[2]/button[1]")))
    #                     # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[2]/button[1]")
    #                     # cancel_btn.click()
    #                     sleep(1)
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[2]/button[2]")))
    #                     save_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[2]/button[2]")
    #                     save_btn.click()
                        
                        
    #                     sleep(5)
    
    # def test_class_room_search_students(self):
    #     d = self.driver
        
    #     # open csv file
    #     with open('data/login.csv', 'r') as f:
    #         # read data
    #         reader = csv.reader(f)
    #         # Skip the header row
    #         next(reader)
            
    #         # loop all values in sheet
    #         for row in reader:
    #             username = row[0]
    #             password = row[1]
                
    #             # loop all values in json
    #             for data in login["login_data"]:
    #                 # time.sleep(10)
    #                 # navigate to the home page and click login
    #                 wait = WebDriverWait(d, timeout=10)
    #                 time.sleep(1)
                  
    #                 d.get(data['valid_home_link'])
                    
    #                 d.find_element(By.LINK_TEXT, "Login").click()
                    
    #                 # Wait for the login page to load
    #                 wait.until(EC.url_matches(data["valid_login_link"]))

    #                 # verify text with assert method
    #                 act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
    #                 exp_title = data["login_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 # invalid login check
    #                 d.find_element(By.NAME, "Username").send_keys(username)
    #                 d.find_element(By.NAME, "Password").send_keys(password)
    #                 d.find_element(By.XPATH, data["login_btn_locator"]).click()

    #                 # time.sleep(2)
    #                 # Wait for the page to load after login
    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]))
    #                 wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
    #                 # time.sleep(2)
    #                 ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
    #                 li_elements = ul_element.find_elements(By.TAG_NAME,"li")
    #                 li_elements[0].click() 
                  
    #                 # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                 # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 # exp_title = data["dashboard_confirm_text"]

    #                 # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

                            
    #                 for class_room_data in classroom["classroom_data"]:
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["classroom_module"])))
                        
    #                     calendar_module = d.find_element(By.XPATH, class_room_data["classroom_module"])
    #                     calendar_module.click()
                            
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["add_new_classroom"])))
    #                     parent_div = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div")
    #                     child_div = parent_div.find_elements(By.TAG_NAME,"div")
    #                     ul = child_div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/ul")
    #                     li = ul.find_element(By.TAG_NAME,"li")
    #                     div = li.find_elements(By.TAG_NAME,"div")
    #                     inside = div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[3]/ul/li/div[2]/p[1]")
    #                     action = ActionChains(d)
    #                     action.move_to_element(inside).click().perform()
                        
    #                     wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
    #                     table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                     table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                     table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
    #                     year_btn = table_cell[0].find_element(By.TAG_NAME, "p")

    #                     year_btn.click()
                        
    #                     sleep(1)
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div[1]/div/div/input")))
    #                     # add_new_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div[1]/div/div/input")
                      
    #                     # ActionChains(d).click(add_new_btn).perform()
    #                     # for character in "arya":
    #                     #     ActionChains(d).send_keys(character).perform()
                            
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[5]/div/div[3]/div/nav")))
                        
    #                     pagination = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[5]/div/div[3]/div/nav")
    #                     ul = pagination.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[5]/div/div[3]/div/nav/ul")
    #                     li = ul.find_elements(By.TAG_NAME, "li")
    #                     li[1].click()
                        
                        
    #                     sleep(5)
   
    # ---- subjects ----                     
    # def test_class_room_add_subjects(self):
    #     d = self.driver
        
    #     # open csv file
    #     with open('data/login.csv', 'r') as f:
    #         # read data
    #         reader = csv.reader(f)
    #         # Skip the header row
    #         next(reader)
            
    #         # loop all values in sheet
    #         for row in reader:
    #             username = row[0]
    #             password = row[1]
                
    #             # loop all values in json
    #             for data in login["login_data"]:
    #                 # time.sleep(10)
    #                 # navigate to the home page and click login
    #                 wait = WebDriverWait(d, timeout=10)
    #                 time.sleep(1)
                  
    #                 d.get(data['valid_home_link'])
                    
    #                 d.find_element(By.LINK_TEXT, "Login").click()
                    
    #                 # Wait for the login page to load
    #                 wait.until(EC.url_matches(data["valid_login_link"]))

    #                 # verify text with assert method
    #                 act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
    #                 exp_title = data["login_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 # invalid login check
    #                 d.find_element(By.NAME, "Username").send_keys(username)
    #                 d.find_element(By.NAME, "Password").send_keys(password)
    #                 d.find_element(By.XPATH, data["login_btn_locator"]).click()

    #                 # time.sleep(2)
    #                 # Wait for the page to load after login
    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]))
    #                 wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
    #                 # time.sleep(2)
    #                 ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
    #                 li_elements = ul_element.find_elements(By.TAG_NAME,"li")
    #                 li_elements[0].click() 
                  
    #                 # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                 # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 # exp_title = data["dashboard_confirm_text"]

    #                 # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

                            
    #                 for class_room_data in classroom["classroom_data"]:
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["classroom_module"])))
                        
    #                     calendar_module = d.find_element(By.XPATH, class_room_data["classroom_module"])
    #                     calendar_module.click()
                            
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["add_new_classroom"])))
    #                     parent_div = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div")
    #                     child_div = parent_div.find_elements(By.TAG_NAME,"div")
    #                     ul = child_div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/ul")
    #                     li = ul.find_element(By.TAG_NAME,"li")
    #                     div = li.find_elements(By.TAG_NAME,"div")
    #                     inside = div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[3]/ul/li/div[2]/p[1]")
    #                     action = ActionChains(d)
    #                     action.move_to_element(inside).click().perform()
                        
                        
    #                     wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
    #                     table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                     table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                     table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
    #                     year_btn = table_cell[0].find_element(By.TAG_NAME, "p")

    #                     year_btn.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[4]/div/div/div/button[2]")))
    #                     subject_tab = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[4]/div/div/div/button[2]")
    #                     subject_tab.click()
                    
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div[2]/button")))
    #                     add_new_subject = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div[2]/button")
    #                     add_new_subject.click()
                    
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[1]/div/div/div")))
    #                     accounts = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[1]/div/div/div")
    #                     accounts.click()
                    
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
    #                     ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                     li = ul.find_elements(By.TAG_NAME,"li")
    #                     li[0].click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[3]/div/div/div")))
    #                     staff = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[3]/div/div/div")
    #                     staff.click()
                    
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
    #                     ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                     li = ul.find_elements(By.TAG_NAME,"li")
    #                     li[0].click()
                    
                    
    #                     wait.until(EC.element_to_be_clickable((By.NAME, "Subject_hour")))
    #                     Subject_hour = d.find_element(By.NAME, "Subject_hour")
    #                     Subject_hour.send_keys("10")
                    
    #                     wait.until(EC.element_to_be_clickable((By.NAME, "Name")))
    #                     notes = d.find_element(By.NAME, "Name")
    #                     notes.send_keys("new subject")
                    
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[6]/button[1]")))
    #                     # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[6]/button[1]")
    #                     # cancel_btn.click()
                    
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[6]/button[2]")))
    #                     save_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[6]/button[2]")
    #                     save_btn.click()
                    
                        
                    
    #                     sleep(5)
                        
    # def test_class_room_edit_subjects(self):
    #     d = self.driver
        
    #     # open csv file
    #     with open('data/login.csv', 'r') as f:
    #         # read data
    #         reader = csv.reader(f)
    #         # Skip the header row
    #         next(reader)
            
    #         # loop all values in sheet
    #         for row in reader:
    #             username = row[0]
    #             password = row[1]
                
    #             # loop all values in json
    #             for data in login["login_data"]:
    #                 # time.sleep(10)
    #                 # navigate to the home page and click login
    #                 wait = WebDriverWait(d, timeout=10)
    #                 time.sleep(1)
                  
    #                 d.get(data['valid_home_link'])
                    
    #                 d.find_element(By.LINK_TEXT, "Login").click()
                    
    #                 # Wait for the login page to load
    #                 wait.until(EC.url_matches(data["valid_login_link"]))

    #                 # verify text with assert method
    #                 act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
    #                 exp_title = data["login_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 # invalid login check
    #                 d.find_element(By.NAME, "Username").send_keys(username)
    #                 d.find_element(By.NAME, "Password").send_keys(password)
    #                 d.find_element(By.XPATH, data["login_btn_locator"]).click()

    #                 # time.sleep(2)
    #                 # Wait for the page to load after login
    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]))
    #                 wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
    #                 # time.sleep(2)
    #                 ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
    #                 li_elements = ul_element.find_elements(By.TAG_NAME,"li")
    #                 li_elements[0].click() 
                  
    #                 # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                 # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 # exp_title = data["dashboard_confirm_text"]

    #                 # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

                            
    #                 for class_room_data in classroom["classroom_data"]:
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["classroom_module"])))
                        
    #                     calendar_module = d.find_element(By.XPATH, class_room_data["classroom_module"])
    #                     calendar_module.click()
                            
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["add_new_classroom"])))
    #                     parent_div = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div")
    #                     child_div = parent_div.find_elements(By.TAG_NAME,"div")
    #                     ul = child_div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/ul")
    #                     li = ul.find_element(By.TAG_NAME,"li")
    #                     div = li.find_elements(By.TAG_NAME,"div")
    #                     inside = div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[3]/ul/li/div[2]/p[1]")
    #                     action = ActionChains(d)
    #                     action.move_to_element(inside).click().perform()
                        
                        
    #                     wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
    #                     table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                     table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                     table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
    #                     year_btn = table_cell[0].find_element(By.TAG_NAME, "p")

    #                     year_btn.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[4]/div/div/div/button[2]")))
    #                     subject_tab = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[4]/div/div/div/button[2]")
    #                     subject_tab.click()
                    
    #                     wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
    #                     table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                     table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                     table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
    #                     button = table_cell[4].find_elements(By.TAG_NAME, "button")

    #                     edit_btn = button[0]
    #                     button = wait.until(EC.element_to_be_clickable(edit_btn))
    #                     actions = ActionChains(d)
    #                     actions.move_to_element(edit_btn).perform()
    #                     sleep(1)
    #                     edit_btn.click()
                    
                                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[1]/div/div/div")))
    #                     accounts = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[1]/div/div/div")
    #                     accounts.click()
                    
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
    #                     ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                     li = ul.find_elements(By.TAG_NAME,"li")
    #                     li[0].click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[3]/div/div/div")))
    #                     staff = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[3]/div/div/div")
    #                     staff.click()
                    
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
    #                     ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                     li = ul.find_elements(By.TAG_NAME,"li")
    #                     li[0].click()
                    
                    
    #                     wait.until(EC.element_to_be_clickable((By.NAME, "Subject_hour")))
    #                     Subject_hour = d.find_element(By.NAME, "Subject_hour")
    #                     Subject_hour.click()
    #                     Subject_hour.send_keys(Keys.CONTROL + "a")
    #                     Subject_hour.send_keys(Keys.BACKSPACE)
    #                     Subject_hour.send_keys("10")
                    
    #                     wait.until(EC.element_to_be_clickable((By.NAME, "Name")))
    #                     notes = d.find_element(By.NAME, "Name")
    #                     notes.click()
    #                     notes.send_keys(Keys.CONTROL + "a")
    #                     notes.send_keys(Keys.BACKSPACE)
    #                     notes.send_keys("new subject")
                    
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[6]/button[1]")))
    #                     # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[6]/button[1]")
    #                     # cancel_btn.click()
                    
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[6]/button[2]")))
    #                     save_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div[6]/button[2]")
    #                     save_btn.click()
                    
                        
                    
    #                     sleep(5)

    # def test_class_room_delete_subjects(self):
    #     d = self.driver
        
    #     # open csv file
    #     with open('data/login.csv', 'r') as f:
    #         # read data
    #         reader = csv.reader(f)
    #         # Skip the header row
    #         next(reader)
            
    #         # loop all values in sheet
    #         for row in reader:
    #             username = row[0]
    #             password = row[1]
                
    #             # loop all values in json
    #             for data in login["login_data"]:
    #                 # time.sleep(10)
    #                 # navigate to the home page and click login
    #                 wait = WebDriverWait(d, timeout=10)
    #                 time.sleep(1)
                  
    #                 d.get(data['valid_home_link'])
                    
    #                 d.find_element(By.LINK_TEXT, "Login").click()
                    
    #                 # Wait for the login page to load
    #                 wait.until(EC.url_matches(data["valid_login_link"]))

    #                 # verify text with assert method
    #                 act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
    #                 exp_title = data["login_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 # invalid login check
    #                 d.find_element(By.NAME, "Username").send_keys(username)
    #                 d.find_element(By.NAME, "Password").send_keys(password)
    #                 d.find_element(By.XPATH, data["login_btn_locator"]).click()

    #                 # time.sleep(2)
    #                 # Wait for the page to load after login
    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]))
    #                 wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
    #                 # time.sleep(2)
    #                 ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
    #                 li_elements = ul_element.find_elements(By.TAG_NAME,"li")
    #                 li_elements[0].click() 
                  
    #                 # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                 # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 # exp_title = data["dashboard_confirm_text"]

    #                 # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

                            
    #                 for class_room_data in classroom["classroom_data"]:
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["classroom_module"])))
                        
    #                     calendar_module = d.find_element(By.XPATH, class_room_data["classroom_module"])
    #                     calendar_module.click()
                            
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["add_new_classroom"])))
    #                     parent_div = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div")
    #                     child_div = parent_div.find_elements(By.TAG_NAME,"div")
    #                     ul = child_div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/ul")
    #                     li = ul.find_element(By.TAG_NAME,"li")
    #                     div = li.find_elements(By.TAG_NAME,"div")
    #                     inside = div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[3]/ul/li/div[2]/p[1]")
    #                     action = ActionChains(d)
    #                     action.move_to_element(inside).click().perform()
                        
                        
    #                     wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
    #                     table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                     table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                     table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
    #                     year_btn = table_cell[0].find_element(By.TAG_NAME, "p")

    #                     year_btn.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[4]/div/div/div/button[2]")))
    #                     subject_tab = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[4]/div/div/div/button[2]")
    #                     subject_tab.click()
                    
    #                     wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
    #                     table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                     table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                     table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
    #                     button = table_cell[4].find_elements(By.TAG_NAME, "button")

    #                     delete_btn = button[1]
    #                     button = wait.until(EC.element_to_be_clickable(delete_btn))
    #                     actions = ActionChains(d)
    #                     actions.move_to_element(delete_btn).perform()
    #                     sleep(1)
    #                     delete_btn.click()

    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div/button[1]")))
    #                     cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div/button[1]")
    #                     cancel_btn.click()
                        
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div/button[2]")))
    #                     # sure_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div/form/div/button[2]")
    #                     # sure_btn.click()
                                        
                        
    #                     sleep(5)
    
    # def test_class_room_search_subjects(self):
    #     d = self.driver
        
    #     # open csv file
    #     with open('data/login.csv', 'r') as f:
    #         # read data
    #         reader = csv.reader(f)
    #         # Skip the header row
    #         next(reader)
            
    #         # loop all values in sheet
    #         for row in reader:
    #             username = row[0]
    #             password = row[1]
                
    #             # loop all values in json
    #             for data in login["login_data"]:
    #                 # time.sleep(10)
    #                 # navigate to the home page and click login
    #                 wait = WebDriverWait(d, timeout=10)
    #                 time.sleep(1)
                  
    #                 d.get(data['valid_home_link'])
                    
    #                 d.find_element(By.LINK_TEXT, "Login").click()
                    
    #                 # Wait for the login page to load
    #                 wait.until(EC.url_matches(data["valid_login_link"]))

    #                 # verify text with assert method
    #                 act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
    #                 exp_title = data["login_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 # invalid login check
    #                 d.find_element(By.NAME, "Username").send_keys(username)
    #                 d.find_element(By.NAME, "Password").send_keys(password)
    #                 d.find_element(By.XPATH, data["login_btn_locator"]).click()

    #                 # time.sleep(2)
    #                 # Wait for the page to load after login
    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]))
    #                 wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
    #                 # time.sleep(2)
    #                 ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
    #                 li_elements = ul_element.find_elements(By.TAG_NAME,"li")
    #                 li_elements[0].click() 
                  
    #                 # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                 # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 # exp_title = data["dashboard_confirm_text"]

    #                 # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

                            
    #                 for class_room_data in classroom["classroom_data"]:
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["classroom_module"])))
                        
    #                     calendar_module = d.find_element(By.XPATH, class_room_data["classroom_module"])
    #                     calendar_module.click()
                            
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, class_room_data["add_new_classroom"])))
    #                     parent_div = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div")
    #                     child_div = parent_div.find_elements(By.TAG_NAME,"div")
    #                     ul = child_div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/ul")
    #                     li = ul.find_element(By.TAG_NAME,"li")
    #                     li.click()
    #                     wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
    #                     table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                     table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                     table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
    #                     year_btn = table_cell[0].find_element(By.TAG_NAME, "p")

    #                     year_btn.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[4]/div/div/div/button[2]")))
    #                     subject_tab = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div[1]/div/div/input")
    #                     subject_tab.click()
                        
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[4]/div/div/div/button[2]")))
    #                     # search_bar = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div[1]/div/div/input")
                        
    #                     # ActionChains(d).click(search_bar).perform()
    #                     # for character in "maths":
    #                     #     ActionChains(d).send_keys(character).perform()
                            
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[5]/div/div[3]/div/nav")))
                        
    #                     pagination = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[5]/div/div[3]/div/nav")
    #                     ul = pagination.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[5]/div/div[3]/div/nav/ul")
    #                     li = ul.find_elements(By.TAG_NAME, "li")
    #                     li[1].click()
                          
                    
                        
    #                     sleep(5)
     
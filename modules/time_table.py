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

with open('config/time_table.json') as f:
    time_table = json.load(f)

class TestTimeTable(unittest.TestCase):
    
    def setUp(self):
        # Initialize the webdriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser
        self.driver.quit()

        
    # def test_time_table_add(self):

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
                                
    #                     for time_table_data in time_table["time_table_data"]:
                            
    #                         wait.until(EC.element_to_be_clickable((By.XPATH, time_table_data["time_table_module"])))
                            
    #                         time_table_module = d.find_element(By.XPATH, time_table_data["time_table_module"])
    #                         time_table_module.click()
                            
        #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[1]")))
        #                     parent_div = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div")
        #                     child_div = parent_div.find_elements(By.TAG_NAME,"div")
        #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/ul")))
                            
        #                     ul = child_div[2].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/ul")
        #                     li = ul.find_element(By.TAG_NAME,"li")
        #                     li.click()
                        
        #                     wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
        #                     table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
        #                     table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
        #                     table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
        #                     year_btn = table_cell[0].find_element(By.TAG_NAME, "p")

        #                     year_btn.click()
                            
        #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div[2]/button[1]")))
        #                     add_timetable = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div[2]/button[1]")
        #                     add_timetable.click()
                            
        #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[1]/div/div/div")))
        #                     day = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[1]/div/div/div")
        #                     day.click()
                            
        #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
        #                     day_ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
        #                     li = day_ul.find_elements(By.TAG_NAME, "li")
        #                     li[0].click()
                            
        #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/div/div/div")))
        #                     slot_time = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/div/div/div")
        #                     slot_time.click()
                            
        #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
        #                     day_ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
        #                     li = day_ul.find_elements(By.TAG_NAME, "li")
        #                     li[0].click()
                            
        #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div/div/div")))
        #                     subject = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div/div/div")
        #                     subject.click()
                            
        #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
        #                     day_ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
        #                     li = day_ul.find_elements(By.TAG_NAME, "li")
        #                     li[0].click()
                            
        #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[1]")))
        #                     # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[1]")
        #                     # cancel_btn.click()
                            
                            
        #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[2]")))
        #                     save_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[2]")
        #                     save_btn.click()
                            
                        
                        
    #                     sleep(5)
                        
    # def test_time_table_edit(self):

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
                                
    #                     for time_table_data in time_table["time_table_data"]:
                            
    #                         wait.until(EC.element_to_be_clickable((By.XPATH, time_table_data["time_table_module"])))
                            
    #                         time_table_module = d.find_element(By.XPATH, time_table_data["time_table_module"])
    #                         time_table_module.click()
                            
    #                         wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[1]")))
    #                         parent_div = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div")
    #                         child_div = parent_div.find_elements(By.TAG_NAME,"div")
    #                         wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/ul")))
                            
    #                         ul = child_div[2].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/ul")
    #                         li = ul.find_element(By.TAG_NAME,"li")
    #                         li.click()
                        
    #                         wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
    #                         table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                         table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                         table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
    #                         year_btn = table_cell[0].find_element(By.TAG_NAME, "p")

    #                         year_btn.click()
                            
    #                         wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div[2]/button[2]")))
    #                         edit_timetable = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[3]/div[2]/button[2]")
    #                         edit_timetable.click()
                            
    #                         wait.until(EC.element_to_be_clickable((By.TAG_NAME, "tbody")))
    #                         ul = d.find_element(By.TAG_NAME, "tbody")
    #                         li = ul.find_elements(By.TAG_NAME,"tr")
    #                         td = li[0].find_elements(By.TAG_NAME,"td")
    #                         td[1].click()
                            
    #                         wait.until(EC.element_to_be_clickable((By.ID, "Subject")))
    #                         dd = d.find_element(By.ID, "Subject")
    #                         select = Select(dd)
                            
    #                         select.select_by_index(0) 
                            
    #                         dd.send_keys(Keys.ESCAPE)

                            
    #                         # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[5]/button[1]")))
    #                         # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[5]/button[1]")
    #                         # cancel_btn.click()
                            
                            
    #                         wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[5]/button[2]")))
    #                         save_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[5]/button[2]")
    #                         save_btn.click()
                            
                            
                            
    #                         sleep(5)
                            
                    
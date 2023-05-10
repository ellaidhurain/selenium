from datetime import datetime
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
import pdb

# # Read the JSON file
with open('config/login_data.json') as f:
    login = json.load(f)

with open('config/calendar.json') as f:
    calendar = json.load(f)

class TestCalendar(unittest.TestCase):

    def setUp(self):
        # Initialize the webdriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser
        self.driver.quit()
        
    # def test_calendar_add_academic_year(self):
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
                  
    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                 act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 exp_title = data["dashboard_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 with open('data/calendar.csv', 'r') as f:
    #                     reader = csv.reader(f)
    #                     # Skip the two header row
    #                     next(reader)
    #                     next(reader)
    #                     for row in reader:
    #                         start_year = row[0]
    #                         # end_year = row[1]
    #                         # calendar_name = row[2]
    #                         # calendar_code = row[3]
    #                         # school_open = row[4]
    #                         # last_working_day = row[5]
    #                         # last_class_day = row[6]
    #                         # description = row[7]
    #                         # g_holiday_name = row[8]
    #                         # g_holiday_date = row[9]
    #                         # g_notes = row[10]
    #                         # o_holiday_name = row[11]
    #                         # o_holiday_start_date = row[12]
    #                         # o_holiday_end_date = row[13]
    #                         # o_notes = row[14]
    #                         # event_name = row[15]
    #                         # event_start_date = row[16]
    #                         # event_end_date = row[17]
    #                         # event_note = row[18]
    #                         # description = row[19]
    #                         # exam_start_date = row[20]
    #                         # exam_end_date = row[21]
    #                         # notes = row[22]
    #                         # slot_from_time = row[23]
    #                         # slot_to_time = row[24]
    #                         # notes = row[25]

    #                         for calendar_data in calendar["calendar_data"]:
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["calendar_module_locator"])))
                                
    #                             calendar_module = d.find_element(By.XPATH, calendar_data["calendar_module_locator"])
    #                             calendar_module.click()
                                
    #                             wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div/h5/span")))
                                
    #                             exp_txt = d.find_element(By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div/h5/span").text
    #                             act_txt = "Academic Year"
                                
    #                             self.assertEqual(exp_txt,act_txt ,f"calendar page open failed: expected '{exp_txt}', but got '{act_txt}'")
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["add_academic_year_btn"])))
                                
    #                             add_academic_year = d.find_element(By.XPATH, calendar_data["add_academic_year_btn"])
    #                             add_academic_year.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["start_date"])))
    #                             d.find_element(By.XPATH, calendar_data["start_date"]).send_keys("26-03-2022")
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["end_date"])))
    #                             d.find_element(By.XPATH, calendar_data["end_date"]).send_keys("26-03-2023")
                                
    #                             # time.sleep(2)
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["status"])))
    #                             d.find_element(By.XPATH, calendar_data["status"]).click()
                                
    #                             # time.sleep(2)
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["active"])))
    #                             d.find_element(By.XPATH, calendar_data["Inactive"]).click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["close_btn"])))
    #                             # d.find_element(By.XPATH, calendar_data["close_btn"]).click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["save_btn"])))
    #                             d.find_element(By.XPATH, calendar_data["save_btn"]).click()
                                
    #                             # if academic year is already exist
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["academic_error"])))
    #                             act_txt = d.find_element(By.XPATH, calendar_data["academic_error"]).text
    #                             exp_txt = "Academic year is already exist"
                                
    #                             if act_txt == exp_txt:
    #                                 print("Academic year already exists. Quitting the program.")
    #                                 self.driver.quit()
    
    
    
                                                                                          
    # def test_academic_year_edit(self):
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
                  
    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                 act_title = d.find_element(By.XPATH, `q m["dashboard_confirm_text_locator"]).text

    #                 exp_title = data["dashboard_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 with open('data/calendar.csv', 'r') as f:
    #                     reader = csv.reader(f)
    #                     # Skip the two header row
    #                     next(reader)
    #                     next(reader)
    #                     for row in reader:
    #                         start_year = row[0]
    #                         end_year = row[1]
                            
    #                         for calendar_data in calendar["calendar_data"]:
                                            
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["calendar_module_locator"])))
                                
    #                             calendar_module = d.find_element(By.XPATH, calendar_data["calendar_module_locator"])
    #                             calendar_module.click()
                                
    #                             wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div/h5/span")))
                                
    #                             exp_txt = d.find_element(By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div/h5/span").text
    #                             act_txt = "Academic Year"
                                
    #                             self.assertEqual(exp_txt,act_txt ,f"calendar page open failed: expected '{exp_txt}', but got '{act_txt}'")

    #                             # time.sleep(5)
    #                             wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/main/div[2]/div/li[1]/a/button")))
                                # ul = d.find_element(By.XPATH,"//*[@id='root']/div[2]/main/div[2]/div")
                                # li = ul.find_elements(By.TAG_NAME, "li")
                                
                                # edit_btn = li[0].find_element(By.TAG_NAME, "a")
                                # edit_btn.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["start_date"])))
    #                             d.find_element(By.XPATH, calendar_data["start_date"]).send_keys(start_year)
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["end_date"])))
    #                             d.find_element(By.XPATH, calendar_data["end_date"]).send_keys(end_year)
                                
    #                             # time.sleep(2)
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["status"])))
    #                             d.find_element(By.XPATH, calendar_data["status"]).click()
                                
    #                             # time.sleep(2)
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["active"])))
    #                             d.find_element(By.XPATH, calendar_data["Inactive"]).click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["close_btn"])))
    #                             # d.find_element(By.XPATH, calendar_data["close_btn"]).click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["save_btn"])))
    #                             d.find_element(By.XPATH, calendar_data["save_btn"]).click()
                                   

                                                
    # def test_academic_year_delete(self):
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
                  
    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                 act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 exp_title = data["dashboard_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 for calendar_data in calendar["calendar_data"]:
                                    
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["calendar_module_locator"])))
                        
    #                     calendar_module = d.find_element(By.XPATH, calendar_data["calendar_module_locator"])
    #                     calendar_module.click()
                        
    #                     wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div/h5/span")))
                        
    #                     exp_txt = d.find_element(By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div/h5/span").text
    #                     act_txt = "Academic Year"
                        
    #                     self.assertEqual(exp_txt,act_txt ,f"calendar page open failed: expected '{exp_txt}', but got '{act_txt}'")

    #                     # delete btn
    #                     wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='root']/div[2]/main/div[2]/div/li[1]/button")))
                            # ul = d.find_element(By.XPATH,"//*[@id='root']/div[2]/main/div[2]/div")
                            # li = ul.find_elements(By.TAG_NAME, "li")
                                
                            # delete_btn = li[0].find_element(By.TAG_NAME, "button")
                            # delete_btn.click()
                                    
    #                     
    #                     # cancel btn
    #                     wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='root']/div[2]/main/div[2]/div/div[2]/div/form/div/button[1]")))
    #                     d.find_element(By.XPATH,"//*[@id='root']/div[2]/main/div[2]/div/div[2]/div/form/div/button[1]").click() 
                        
    #                     # save btn
    #                     wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='root']/div[2]/main/div[2]/div/div[2]/div/form/div/button[2]")))
    #                     d.find_element(By.XPATH,"//*[@id='root']/div[2]/main/div[2]/div/div[2]/div/form/div/button[1]").click() 
                        
    def test_add_new_calendar(self):
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
                    li_elements[1].click() 
                  
                    # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
                    # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

                    # exp_title = data["dashboard_confirm_text"]

                    # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

                    with open('data/calendar.csv', 'r') as f:
                        reader = csv.reader(f)
                        # Skip the two header row
                        next(reader)
                        next(reader)
                        for row in reader:
                        
                            calendar_name = row[2]
                            calendar_code = row[3]
                            school_open = row[4]
                            last_working_day = row[5]
                            last_class_day = row[6]
                            description = row[7]
                            g_holiday_name = row[8]
                            g_holiday_date = row[9]
                            g_notes = row[10]
                            o_holiday_name = row[11]
                            o_holiday_start_date = row[12]
                            o_holiday_end_date = row[13]
                            o_notes = row[14]
                            event_name = row[15]
                            event_start_date = row[16]
                            event_end_date = row[17]
                            event_note = row[18]
                            exam_description = row[19]
                            exam_start_date = row[20]
                            exam_end_date = row[21]
                            ex_notes = row[22]
                            slot_from_time = row[23]
                            slot_to_time = row[24]
                            s_notes = row[25]

                            for calendar_data in calendar["calendar_data"]:
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["calendar_module_locator"])))
                                
                                calendar_module = d.find_element(By.XPATH, calendar_data["calendar_module_locator"])
                                calendar_module.click()
                                
                                wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div/h5/span")))
                                
                                exp_txt = d.find_element(By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div/h5/span").text
                                act_txt = "Academic Year"
                                
                                self.assertEqual(exp_txt,act_txt ,f"calendar page open failed: expected '{exp_txt}', but got '{act_txt}'")
                               
                                # time.sleep(2)
                                wait.until(EC.visibility_of_element_located((By.XPATH, calendar_data["calendar_inside"])))
                                
                                d.find_element(By.XPATH,calendar_data["calendar_inside"]).click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["add_new_calender"])))
                                time.sleep(1)
                                add_btn = d.find_element(By.XPATH, calendar_data["add_new_calender"])
                                action = ActionChains(d)
                                action.move_to_element(add_btn).click().perform()
                                # time.sleep(4)
                                wait.until(EC.presence_of_element_located((By.XPATH, calendar_data["calendar_name_input"]))) 
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["calendar_name_input"])))
                                
                                calendar_name_input = d.find_element(By.XPATH, calendar_data["calendar_name_input"])
                                ActionChains(d).click(calendar_name_input).perform()
                                for character in calendar_name:
                                    ActionChains(d).send_keys(character).perform()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["calendar_code_input"])))
                                
                                calendar_code_input = d.find_element(By.XPATH, calendar_data["calendar_code_input"])
                                ActionChains(d).click(calendar_code_input).perform()
                                for character in calendar_code:
                                    ActionChains(d).send_keys(character).perform()

                            
                                d.find_element(By.XPATH, calendar_data["calendar_type_dropdown"]).click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["calendar_staff_type"])))
                                d.find_element(By.XPATH, calendar_data["calendar_staff_type"]).click()
                                # # d.find_element(By.XPATH, calendar_data["calendar_student_type"]).click()
                
                                # # time.sleep(2)
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["school_open_date_input"])))
                                d.find_element(By.XPATH, calendar_data["school_open_date_input"]).send_keys(last_working_day)
                                
                                # time.sleep(2)
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["last_working_day_input"])))
                                d.find_element(By.XPATH, calendar_data["last_working_day_input"]).send_keys(last_working_day)
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["last_day_class_input"])))
                                d.find_element(By.XPATH, calendar_data["last_day_class_input"]).send_keys(last_class_day)
                                
                                # time.sleep(2)
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["description_input"])))
                                
                                description_input = d.find_element(By.XPATH, calendar_data["description_input"])
                                ActionChains(d).click(description_input).perform()
                                for character in description:
                                    ActionChains(d).send_keys(character).perform()

                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["status_dropdown"])))
                                
                                d.find_element(By.XPATH, calendar_data["status_dropdown"]).click()
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["status_active"])))
                                
                                d.find_element(By.XPATH, calendar_data["status_active"]).click()
                                # d.find_element(By.XPATH, calendar_data["status_nonActive"]).click()
                                
                                time.sleep(2)
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["week_day_start_droptdown"])))
                                d.find_element(By.XPATH, calendar_data["week_day_start_droptdown"]).click()
                                
                                wait.until(EC.presence_of_all_elements_located((By.XPATH, calendar_data["dropdown_ul_locator"])))
                        
                                                                # Find the dropdown element
                                dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".MuiSelect-select")))

                                # Move the mouse to the center of the dropdown element and click it
                                action = ActionChains(d)
                                action.move_to_element(dropdown).click().perform()

                                # Wait for the dropdown list to appear and find all the options
                                ul_element = wait.until(EC.presence_of_element_located((By.XPATH, calendar_data["dropdown_ul_locator"])))
                                li_elements = ul_element.find_elements(By.TAG_NAME, "li")

                                # Click the first option in the dropdown list
                                li_elements[0].click()
                                
                                dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, calendar_data["working_day_group"])))

                                label_elements1 = d.find_element(By.XPATH, calendar_data["working_day_label1"])
                                label_elements2 = d.find_element(By.XPATH, calendar_data["working_day_label2"])
                                label_elements3 = d.find_element(By.XPATH, calendar_data["working_day_label3"])
                                label_elements4 = d.find_element(By.XPATH, calendar_data["working_day_label4"])
                                label_elements5 = d.find_element(By.XPATH, calendar_data["working_day_label5"])
                                label_elements6 = d.find_element(By.XPATH, calendar_data["working_day_label6"])
                                label_elements7 = d.find_element(By.XPATH, calendar_data["working_day_label7"])
                                
                                 # Click the first option in the dropdown list
                                label_elements1.click()
                                label_elements2.click()
                                label_elements3.click()
                                label_elements4.click()
                                label_elements5.click()
                                label_elements6.click()
                                label_elements7.click()
                                
                                dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, calendar_data["working_weekends1"])))

                                label_elements1 = d.find_element(By.XPATH, calendar_data["working_weekends1"])
                                label_elements2 = d.find_element(By.XPATH, calendar_data["working_weekends2"])
                                label_elements3 = d.find_element(By.XPATH, calendar_data["working_weekends3"])
                                label_elements4 = d.find_element(By.XPATH, calendar_data["working_weekends4"])
                                label_elements5 = d.find_element(By.XPATH, calendar_data["working_weekends5"])
                                
                                label_elements1.click()
                                label_elements2.click()
                                label_elements3.click()
                                label_elements4.click()
                                label_elements5.click()
                                
                                # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["c_back_btn"])))
                                # back_btn = d.find_element(By.XPATH, calendar_data["c_back_btn"])
                                # action = ActionChains(d)
                                # action.move_to_element(back_btn).click().perform()
                                # back_btn.click()
                                
                              
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["save_btn"])))
                                save_btn = d.find_element(By.XPATH, calendar_data["save_btn"])
                                action = ActionChains(d)
                                action.move_to_element(save_btn).click().perform()
                                                                
                                # govt holidays
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["govt_holidays_tab"])))
                                gh_btn = d.find_element(By.XPATH, calendar_data["govt_holidays_tab"])
                                action = ActionChains(d)
                                action.move_to_element(gh_btn).click().perform()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["add_new_holiday"])))
                                add_new_holiday = d.find_element(By.XPATH, calendar_data["add_new_holiday"])
                                add_new_holiday.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["holiday_name_input"])))
                                holiday_name_input = d.find_element(By.XPATH, calendar_data["holiday_name_input"])
                                actions = ActionChains(d)
                                actions.click(holiday_name_input).perform()
                                holiday_name_input.clear()  # Clear any existing value in the input field
                                holiday_name_input.send_keys(g_holiday_name)
                                actions.move_by_offset(0, 0).click().perform()  # Remove focus from the input field

                                start_date_input = d.find_element(By.XPATH, calendar_data["gh_start_date"])
                                start_date_input.clear()
                                start_date_input.send_keys(g_holiday_date)
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["gh_notes"])))
                                holiday_notes_input = d.find_element(By.XPATH, calendar_data["gh_notes"])
                                holiday_notes_input.clear()  # Clear any existing value in the input field
                                holiday_notes_input.send_keys(g_notes)
                                                                  
                                # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["gh_cancel_btn"])))
                                # # holiday_cancel_btn = d.find_element(By.XPATH, calendar_data["gh_cancel_btn"])
                                # # holiday_cancel_btn.click()
                                
                                sleep(1)
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["gh_save_btn"])))
                                holiday_save_btn = d.find_element(By.XPATH, calendar_data["gh_save_btn"])
                                holiday_save_btn.click()
                                
                                # sleep(1)

                                wait.until(EC.visibility_of_element_located((By.XPATH,calendar_data["check_box_label"])))
                                wait.until(EC.element_to_be_clickable((By.XPATH,calendar_data["check_box_label"])))
                                table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
                                table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
                                table_cells = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
                                
                                label = table_cells[1].find_element(By.XPATH, calendar_data["check_box_input"])   
                             
                                select_btn = label.find_element(By.XPATH, calendar_data["check_box_input"])
                                select_btn.click()
                                
                                # time.sleep(5) 
                                
                                # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["c_back_btn"])))
                                # back_btn = d.find_element(By.XPATH, calendar_data["c_back_btn"])
                                # action = ActionChains(d)
                                # action.move_to_element(back_btn).click().perform()
                                
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["check_box_save_btn"])))
                                save_btn = d.find_element(By.XPATH, calendar_data["check_box_save_btn"])
                                action = ActionChains(d)
                                action.move_to_element(save_btn).click().perform()
                                
                                # sleep(1)
                                
                               
                                # # time.sleep(5) 
                                # # # # ----- other holidays -----
                             
                                wait.until(EC.visibility_of_element_located((By.XPATH, calendar_data["other_holiday_tab"])))
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["other_holiday_tab"])))
                                oh_btn = d.find_element(By.XPATH, calendar_data["other_holiday_tab"])
                                
                                action = ActionChains(d)
                                action.move_to_element(oh_btn).click().perform()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["add_other_holiday_btn"])))
                                add_new_holiday = d.find_element(By.XPATH, calendar_data["add_other_holiday_btn"])
                                add_new_holiday.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["o_holiday_name"])))
                                holiday_name_input = d.find_element(By.XPATH, calendar_data["o_holiday_name"])
                                actions = ActionChains(d)
                                actions.click(holiday_name_input).perform()
                                holiday_name_input.clear()  # Clear any existing value in the input field
                                holiday_name_input.send_keys(o_holiday_name)
                                actions.move_by_offset(0, 0).click().perform()  # Remove focus from the input field

                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["o_holiday_type_drop_down"])))
                                holiday_type = d.find_element(By.XPATH, calendar_data["o_holiday_type_drop_down"])
                                holiday_type.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["regional_holiday_option"])))
                                holiday_type = d.find_element(By.XPATH, calendar_data["regional_holiday_option"])
                                holiday_type.click()
                                
                                # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["event_holiday"])))
                                # holiday_type = d.find_element(By.XPATH, calendar_data["event_holiday"])
                                # holiday_type.click()
                                
                                start_date_input = d.find_element(By.XPATH, calendar_data["o_start_date"])
                                start_date_input.clear()
                                start_date_input.send_keys(o_holiday_start_date)
                                
                                
                                start_date_input = d.find_element(By.XPATH, calendar_data["o_end_date"])
                                start_date_input.clear()
                                start_date_input.send_keys("02")
                                
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["o_notes"])))
                                holiday_notes_input = d.find_element(By.XPATH, calendar_data["o_notes"])
                                holiday_notes_input.clear()  # Clear any existing value in the input field
                                holiday_notes_input.send_keys(o_notes)
                                
                                
                                # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["o_cancel_btn"])))
                                # holiday_cancel_btn = d.find_element(By.XPATH, calendar_data["o_cancel_btn"])
                                # holiday_cancel_btn.click()
                                
                                sleep(1)
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["o_save_btn"])))
                                holiday_save_btn = d.find_element(By.XPATH, calendar_data["o_save_btn"])
                                holiday_save_btn.click()
                                sleep(1)
                                
                                
                                wait.until(EC.visibility_of_element_located((By.XPATH,calendar_data["check_box_label"])))
                                wait.until(EC.element_to_be_clickable((By.XPATH,calendar_data["check_box_label"])))
                                table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
                                table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
                                table_cells = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
                                
                                label = table_cells[1].find_element(By.XPATH, calendar_data["check_box_input"])   
                             
                                select_btn = label.find_element(By.XPATH, calendar_data["check_box_input"])
                                select_btn.click()
                                
                                # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["c_back_btn"])))
                                # back_btn = d.find_element(By.XPATH, calendar_data["c_back_btn"])
                                # action = ActionChains(d)
                                # action.move_to_element(back_btn).click().perform()
                            
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["check_box_save_btn"])))
                                save_btn = d.find_element(By.XPATH, calendar_data["check_box_save_btn"])
                                action = ActionChains(d)
                                action.move_to_element(save_btn).click().perform()
                                
                                
                                # events
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["events_tab"])))
                                oh_btn = d.find_element(By.XPATH, calendar_data["events_tab"])
                                action = ActionChains(d)
                                action.move_to_element(oh_btn).click().perform()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["add_new_event_btn"])))
                                add_new_event = d.find_element(By.XPATH, calendar_data["add_new_event_btn"])
                                add_new_event.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["event_name_input"])))
                                holiday_name_input = d.find_element(By.XPATH, calendar_data["event_name_input"])
                                actions = ActionChains(d)
                                actions.click(holiday_name_input).perform()
                                holiday_name_input.clear()  # Clear any existing value in the input field
                                holiday_name_input.send_keys(event_name)
                                actions.move_by_offset(0, 0).click().perform()  # Remove focus from the input field

                                
                                # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["is_holiday"])))  
                                checkbox = d.find_element(By.XPATH, "//*[@id='form2']/div[1]/div[2]/label/span[1]/input")                           
                                checkbox.click()

                                
                                start_date_input = d.find_element(By.XPATH, calendar_data["e_start_date"])
                                start_date_input.clear()
                                start_date_input.send_keys(event_start_date)
                                
                                start_date_input = d.find_element(By.XPATH, calendar_data["e_end_date"])
                                start_date_input.clear()
                                start_date_input.send_keys("02")
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["e_notes"])))
                                holiday_notes_input = d.find_element(By.XPATH, calendar_data["e_notes"])
                                holiday_notes_input.clear()  # Clear any existing value in the input field
                                holiday_notes_input.send_keys(event_note)
                                
                                # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["e_cancel_btn"])))
                                # holiday_cancel_btn = d.find_element(By.XPATH, calendar_data["e_cancel_btn"])
                                # holiday_cancel_btn.click()
                                
                                sleep(1)
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["e_save_btn"])))
                                holiday_save_btn = d.find_element(By.XPATH, calendar_data["e_save_btn"])
                                holiday_save_btn.click()
                                
                                time.sleep(1)
                                
                                
                                wait.until(EC.visibility_of_element_located((By.XPATH,calendar_data["check_box_label"])))
                                wait.until(EC.element_to_be_clickable((By.XPATH,calendar_data["check_box_label"])))
                                table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
                                table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
                                table_cells = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
                                
                                label = table_cells[1].find_element(By.XPATH, calendar_data["check_box_input"])   
                             
                                select_btn = label.find_element(By.XPATH, calendar_data["check_box_input"])
                                select_btn.click()
                                
                                # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["c_back_btn"])))
                                # back_btn = d.find_element(By.XPATH, calendar_data["c_back_btn"])
                                # action = ActionChains(d)
                                # action.move_to_element(back_btn).click().perform()
                                
                                
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["check_box_save_btn"])))
                                save_btn = d.find_element(By.XPATH, calendar_data["check_box_save_btn"])
                                action = ActionChains(d)
                                action.move_to_element(save_btn).click().perform()
                                
                                
                                 # #------ exam details ---------
                                 
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_tab"])))
                                oh_btn = d.find_element(By.XPATH, calendar_data["exam_tab"])
                                action = ActionChains(d)
                                action.move_to_element(oh_btn).click().perform()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["add_exam_btn"])))
                                add_new_exam = d.find_element(By.XPATH, calendar_data["add_exam_btn"])
                                add_new_exam.click()
                                
                    
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_description"])))
                                ex_desc = d.find_element(By.XPATH, calendar_data["exam_description"])
                                actions = ActionChains(d)
                                actions.click(ex_desc).perform()
                                ex_desc.clear()  # Clear any existing value in the input field
                                ex_desc.send_keys(exam_description)
                                actions.move_by_offset(0, 0).click().perform()  # Remove focus from the input field

                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_start_date"])))
                                ex_start_date = d.find_element(By.XPATH, calendar_data["exam_start_date"])
                                ex_start_date.send_keys("25-02-2023")
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_end_date"])))
                                ex_end_date = d.find_element(By.XPATH, calendar_data["exam_end_date"])
                                ex_end_date.send_keys("26-02")
                                
                                # sleep(10)
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["e_notes"])))
                                ex_note = d.find_element(By.XPATH, calendar_data["e_notes"])
                                ex_note.clear()  # Clear any existing value in the input field
                                ex_note.send_keys(ex_notes)
                                                                
                                # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_cancel_btn"])))
                                # # holiday_cancel_btn = d.find_element(By.XPATH, calendar_data["exam_cancel_btn"])
                                # # holiday_cancel_btn.click()
                                
                                sleep(1)
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_save_btn"])))
                                holiday_save_btn = d.find_element(By.XPATH, calendar_data["exam_save_btn"])
                                holiday_save_btn.click()
                                
                                sleep(1)
                                
                                # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["c_back_btn"])))
                                # back_btn = d.find_element(By.XPATH, calendar_data["c_back_btn"])
                                # action = ActionChains(d)
                                # action.move_to_element(back_btn).click().perform()
                                
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["check_box_save_btn"])))
                                save_btn = d.find_element(By.XPATH, calendar_data["check_box_save_btn"])
                                action = ActionChains(d)
                                action.move_to_element(save_btn).click().perform()
                                
                                
                                
    #                             # ------ slot details ------
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["slot_tab"])))
                                oh_btn = d.find_element(By.XPATH, calendar_data["slot_tab"])
                                action = ActionChains(d)
                                action.move_to_element(oh_btn).click().perform()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["add_new_slot"])))
                                add_new_slot = d.find_element(By.XPATH, calendar_data["add_new_slot"])
                                add_new_slot.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["slot_dropdown"])))
                                add_slot = d.find_element(By.XPATH, calendar_data["slot_dropdown"])
                                add_slot.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["slot_ul"])))
                                add_new_slot_ul = d.find_element(By.XPATH, calendar_data["slot_ul"])
                                li = add_new_slot_ul.find_elements(By.TAG_NAME, "li")
                                li[0].click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["hour_type_dropdown"])))
                                add_new_slot = d.find_element(By.XPATH, calendar_data["hour_type_dropdown"])
                                add_new_slot.click()
                    
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["hour_type_ul"])))
                                add_new_hour_ul = d.find_element(By.XPATH, calendar_data["hour_type_ul"])
                                li = add_new_hour_ul.find_elements(By.TAG_NAME, "li")
                                li[0].click()
                                
                                sleep(1)
                                wait.until(EC.visibility_of_element_located((By.XPATH, calendar_data["from_time"])))
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["from_time"])))
                                slot_start_time = d.find_element(By.XPATH, calendar_data["from_time"])
                                slot_start_time.clear()
 
                                slot_start_time.click()
                                slot_start_time.send_keys("7:30")
                                slot_start_time.send_keys(" AM")
                                
                               
                                input_element = d.find_element(By.XPATH,'//input[@name="Slot_from_time"]')
                                input_element.click()
                                input_element.send_keys(slot_from_time)

                                                                
                                # # to time
                                sleep(2)
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["to_time"])))
                                slot_end_time_input = d.find_element(By.XPATH, calendar_data["to_time"])
                                slot_end_time_input.clear()
                                slot_end_time_input.send_keys(slot_to_time)

                                # form_element = d.find_element(By.XPATH,'//form')
                                # form_element.submit()
                                # other_element = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div[2]/div[1]/header/div/div/p")
                                # other_element.click()
                                # sleep(10)
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["slot_notes"])))
                                s_note = d.find_element(By.XPATH, calendar_data["slot_notes"])
                                actions = ActionChains(d)
                                actions.click(s_note).perform()
                                s_note.clear()  # Clear any existing value in the input field
                                s_note.send_keys(s_notes)
                                actions.move_by_offset(0, 0).click().perform()  # Remove focus from the input field
                                
                                
                                # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_cancel_btn"])))
                                # holiday_cancel_btn = d.find_element(By.XPATH, calendar_data["exam_cancel_btn"])
                                # holiday_cancel_btn.click()
                                
                                sleep(1)
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_save_btn"])))
                                holiday_save_btn = d.find_element(By.XPATH, calendar_data["exam_save_btn"])
                                holiday_save_btn.click()
                                
                                # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["c_back_btn"])))
                                # back_btn = d.find_element(By.XPATH, calendar_data["c_back_btn"])
                                # action = ActionChains(d)
                                # action.move_to_element(back_btn).click().perform()
                                
                                
                                # sleep(5)
                                wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["check_box_save_btn"])))
                                save_btn = d.find_element(By.XPATH, calendar_data["check_box_save_btn"])
                                action = ActionChains(d)
                                action.move_to_element(save_btn).click().perform()
                                
                                
                                sleep(10)
                      
                                

    # def test_edit_copy_calendar(self):
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
                  
    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                 act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 exp_title = data["dashboard_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 with open('data/calendar.csv', 'r') as f:
    #                     reader = csv.reader(f)
    #                     # Skip the two header row
    #                     next(reader)
    #                     next(reader)
    #                     for row in reader:
                        
    #                         calendar_name = row[2]
    #                         calendar_code = row[3]
    #                         school_open = row[4]
    #                         last_working_day = row[5]
    #                         last_class_day = row[6]
    #                         description = row[7]
    #                         g_holiday_name = row[8]
    #                         g_holiday_date = row[9]
    #                         g_notes = row[10]
    #                         o_holiday_name = row[11]
    #                         o_holiday_start_date = row[12]
    #                         o_holiday_end_date = row[13]
    #                         o_notes = row[14]
    #                         event_name = row[15]
    #                         event_start_date = row[16]
    #                         event_end_date = row[17]
    #                         event_note = row[18]
    #                         ex_description = row[19]
    #                         exam_start_date = row[20]
    #                         exam_end_date = row[21]
    #                         exam_notes = row[22]
    #                         slot_from_time = row[23]
    #                         slot_to_time = row[24]
    #                         slot_notes = row[25]

    #                         for calendar_data in calendar["calendar_data"]:
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["calendar_module_locator"])))
                                
    #                             calendar_module = d.find_element(By.XPATH, calendar_data["calendar_module_locator"])
    #                             calendar_module.click()
                                
    #                             wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div/h5/span")))
                                
    #                             # exp_txt = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[1]/h5/span").text
    #                             # act_txt = "Academic Year Details"
                                
    #                             # self.assertEqual(exp_txt,act_txt ,f"calendar page open failed: expected '{exp_txt}', but got '{act_txt}'")

    #                             # time.sleep(2)
    #                             wait.until(EC.visibility_of_element_located((By.XPATH, calendar_data["calendar_inside"])))
                                
    #                             ul = d.find_element(By.XPATH,"//*[@id='root']/div[2]/main/div[2]/div")
    #                             li = ul.find_elements(By.TAG_NAME, "li")
    #                             print(len(li))
    #                             li[0].click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
    #                             table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                             table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                             table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
    #                             buttons = table_cell[2].find_elements(By.TAG_NAME, "button")

    #                             edit_btn = buttons[0]
    #                             edit_btn.click()
                                
    #                             # copy_btn = buttons[2]
    #                             # copy_btn.click()
                            
    #                             # time.sleep(4)
    # #                           # wait.until(EC.presence_of_element_located((By.XPATH, calendar_data["calendar_name_input"]))) 
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["calendar_name_input"])))
                                
    #                             # calendar_name_input = d.find_element(By.XPATH, calendar_data["calendar_name_input"])
                                
    #                             # actions = ActionChains(d)
    #                             # actions.click(calendar_name_input).perform()
    #                             # d.execute_script("arguments[0].value = arguments[1];", calendar_name_input, calendar_name)
    #                             # d.execute_script("arguments[0].dispatchEvent(new Event('change'));", calendar_name_input)
    #                             # d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", calendar_name_input, calendar_name)
                                
                            
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["calendar_code_input"])))
                                
    #                             # calendar_code_input = d.find_element(By.XPATH, calendar_data["calendar_code_input"])
    #                             # actions = ActionChains(d)
    #                             # actions.click(calendar_code_input).perform()
    #                             # d.execute_script("arguments[0].value = arguments[1];", calendar_code_input, calendar_code)
    #                             # d.execute_script("arguments[0].dispatchEvent(new Event('change'));", calendar_code_input)
    #                             # d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", calendar_code_input, calendar_code)
                            
    #                             # d.find_element(By.XPATH, calendar_data["classGroup_type_dropdown"]).click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["classGroup_type_dropdown"])))
    #                             # ul = d.find_element(By.XPATH, calendar_data["classGroup_type_dropdown_ul"])
    #                             # li = ul.find_elements(By.TAG_NAME, "li")
                                
    #                             # li[0].click()
                                
    #                             # date_str = school_open
    #                             # date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    #                             # formatted_date = datetime.strftime(date_obj, "%Y-%m-%d")
                                
    #                             # # time.sleep(2)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["school_open_date_input"])))
    #                             # date_field = d.find_element(By.XPATH, calendar_data["school_open_date_input"])
    #                             # date_field.clear()
    #                             # actions = ActionChains(d)
    #                             # actions.click(date_field).perform()
    #                             # d.execute_script("arguments[0].value = arguments[1];", date_field, formatted_date)
    #                             # d.execute_script("arguments[0].dispatchEvent(new Event('change'));", date_field)
    #                             # d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", date_field, formatted_date)
                              
    #                             # date_str = last_working_day
    #                             # date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    #                             # formatted_date = datetime.strftime(date_obj, "%Y-%m-%d")
                                
    #                             # # time.sleep(2)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["last_working_day_input"])))
    #                             # date_field = d.find_element(By.XPATH, calendar_data["last_working_day_input"])
    #                             # date_field.clear()
    #                             # actions = ActionChains(d)
    #                             # actions.click(date_field).perform()
    #                             # d.execute_script("arguments[0].value = arguments[1];", date_field, formatted_date)
    #                             # d.execute_script("arguments[0].dispatchEvent(new Event('change'));", date_field)
    #                             # d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", date_field, formatted_date)
                              
    #                             # date_str = last_class_day
    #                             # date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    #                             # formatted_date = datetime.strftime(date_obj, "%Y-%m-%d")
                                
    #                             # # time.sleep(2)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["last_day_class_input"])))
    #                             # date_field = d.find_element(By.XPATH, calendar_data["last_day_class_input"])
    #                             # date_field.clear()
    #                             # actions = ActionChains(d)
    #                             # actions.click(date_field).perform()
    #                             # d.execute_script("arguments[0].value = arguments[1];", date_field, formatted_date)
    #                             # d.execute_script("arguments[0].dispatchEvent(new Event('change'));", date_field)
    #                             # d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", date_field, formatted_date)
                              
                                
                              
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["description_input"])))
                                
    #                             # description_input = d.find_element(By.XPATH, calendar_data["description_input"])
    #                             # actions = ActionChains(d)
    #                             # actions.click(description_input).perform()
    #                             # d.execute_script("arguments[0].value = arguments[1];", description_input, description)
    #                             # d.execute_script("arguments[0].dispatchEvent(new Event('change'));", description_input)
    #                             # d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", description_input, description)
                              
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["status_dropdown"])))
                                
    #                             # d.find_element(By.XPATH, calendar_data["status_dropdown"]).click()
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["status_active"])))
                                
    #                             # d.find_element(By.XPATH, calendar_data["status_active"]).click()
    #                             # d.find_element(By.XPATH, calendar_data["status_nonActive"]).click()
                                
    #                             # # # time.sleep(3)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["week_day_start_droptdown"])))
    #                             # d.find_element(By.XPATH, calendar_data["week_day_start_droptdown"]).click()
                                
    #                             # wait.until(EC.presence_of_all_elements_located((By.XPATH, calendar_data["dropdown_ul_locator"])))
                        
    #                             # #                                 # Find the dropdown element
    #                             # dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".MuiSelect-select")))

    #                             # # Move the mouse to the center of the dropdown element and click it
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(dropdown).click().perform()

    #                             # # # Wait for the dropdown list to appear and find all the options
    #                             # ul_element = wait.until(EC.presence_of_element_located((By.XPATH, calendar_data["dropdown_ul_locator"])))
    #                             # li_elements = ul_element.find_elements(By.TAG_NAME, "li")

    #                             # # # Click the first option in the dropdown list
    #                             # li_elements[0].click()
                                
    #                             # dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, calendar_data["working_day_group"])))

    #                             # label_elements1 = d.find_element(By.XPATH, calendar_data["working_day_label1"])
    #                             # label_elements2 = d.find_element(By.XPATH, calendar_data["working_day_label2"])
    #                             # label_elements3 = d.find_element(By.XPATH, calendar_data["working_day_label3"])
    #                             # label_elements4 = d.find_element(By.XPATH, calendar_data["working_day_label4"])
    #                             # label_elements5 = d.find_element(By.XPATH, calendar_data["working_day_label5"])
    #                             # label_elements6 = d.find_element(By.XPATH, calendar_data["working_day_label6"])
    #                             # label_elements7 = d.find_element(By.XPATH, calendar_data["working_day_label7"])
                                
    #                             #  # Click the first option in the dropdown list
    #                             # label_elements1.click()
    #                             # label_elements2.click()
    #                             # label_elements3.click()
    #                             # label_elements4.click()
    #                             # label_elements5.click()
    #                             # label_elements6.click()
    #                             # # label_elements7.click()
                                
    #                             # # dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, calendar_data["working_weekends1"])))

    #                             # # label_elements1 = d.find_element(By.XPATH, calendar_data["working_weekends1"])
    #                             # # label_elements2 = d.find_element(By.XPATH, calendar_data["working_weekends2"])
    #                             # # label_elements3 = d.find_element(By.XPATH, calendar_data["working_weekends3"])
    #                             # # label_elements4 = d.find_element(By.XPATH, calendar_data["working_weekends4"])
    #                             # # label_elements5 = d.find_element(By.XPATH, calendar_data["working_weekends5"])
                                
    #                             # # label_elements1.click()
    #                             # # label_elements2.click()
    #                             # # label_elements3.click()
    #                             # # label_elements4.click()
    #                             # # label_elements5.click()
                                
    #                             # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["c_back_btn"])))
    #                             # # back_btn = d.find_element(By.XPATH, calendar_data["c_back_btn"])
                                
    #                             # # action = ActionChains(d)
    #                             # # action.move_to_element(back_btn).click().perform()

    #                             # # back_btn.click()
                                
                              
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["save_btn"])))
    #                             # save_btn = d.find_element(By.XPATH, calendar_data["save_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(save_btn).click().perform()
                                
    #                             # sleep(1)
                                
    #                             # # govt holidays
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["govt_holidays_tab"])))
    #                             # gh_btn = d.find_element(By.XPATH, calendar_data["govt_holidays_tab"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(gh_btn).click().perform()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["add_new_holiday"])))
    #                             # add_new_holiday = d.find_element(By.XPATH, calendar_data["add_new_holiday"])
    #                             # add_new_holiday.click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["holiday_name_input"])))
    #                             # holiday_name_input = d.find_element(By.XPATH, calendar_data["holiday_name_input"])
    #                             # actions = ActionChains(d)
    #                             # actions.click(holiday_name_input).perform()
    #                             # holiday_name_input.clear()  # Clear any existing value in the input field
    #                             # holiday_name_input.send_keys(g_holiday_name)
    #                             # actions.move_by_offset(0, 0).click().perform()  # Remove focus from the input field

    #                             # start_date_input = d.find_element(By.XPATH, calendar_data["gh_start_date"])
    #                             # start_date_input.clear()
    #                             # start_date_input.send_keys(g_holiday_date)
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["gh_notes"])))
    #                             # holiday_notes_input = d.find_element(By.XPATH, calendar_data["gh_notes"])
    #                             # holiday_notes_input.clear()  # Clear any existing value in the input field
    #                             # holiday_notes_input.send_keys(g_notes)
                                                                  
    #                             # # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["gh_cancel_btn"])))
    #                             # # # holiday_cancel_btn = d.find_element(By.XPATH, calendar_data["gh_cancel_btn"])
    #                             # # # holiday_cancel_btn.click()
                                
    #                             # sleep(1)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["gh_save_btn"])))
    #                             # holiday_save_btn = d.find_element(By.XPATH, calendar_data["gh_save_btn"])
    #                             # holiday_save_btn.click()
                                
    #                             # sleep(1)

    #                             # wait.until(EC.visibility_of_element_located((By.XPATH,calendar_data["check_box_label"])))
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH,calendar_data["check_box_label"])))
    #                             # table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                             # table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                             # table_cells = table_rows[1].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
                                
    #                             # label = table_cells[1].find_element(By.XPATH, calendar_data["check_box_input"])   
                             
    #                             # select_btn = label.find_element(By.XPATH, calendar_data["check_box_input"])
    #                             # select_btn.click()
                                
    #                             # # time.sleep(5) 
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["check_box_save_btn"])))
    #                             # save_btn = d.find_element(By.XPATH, calendar_data["check_box_save_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(save_btn).click().perform()
                                
    #                             # sleep(1)
                                
                               
    #                             # # time.sleep(5) 
    #                             # # # # ----- other holidays -----
                             
    #                             # wait.until(EC.visibility_of_element_located((By.XPATH, calendar_data["other_holiday_tab"])))
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["other_holiday_tab"])))
    #                             # oh_btn = d.find_element(By.XPATH, calendar_data["other_holiday_tab"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(oh_btn).click().perform()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["add_other_holiday_btn"])))
    #                             # add_new_holiday = d.find_element(By.XPATH, calendar_data["add_other_holiday_btn"])
    #                             # add_new_holiday.click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["o_holiday_name"])))
    #                             # holiday_name_input = d.find_element(By.XPATH, calendar_data["o_holiday_name"])
    #                             # actions = ActionChains(d)
    #                             # actions.click(holiday_name_input).perform()
    #                             # holiday_name_input.clear()  # Clear any existing value in the input field
    #                             # holiday_name_input.send_keys(o_holiday_name)
    #                             # actions.move_by_offset(0, 0).click().perform()  # Remove focus from the input field

                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["o_holiday_type_drop_down"])))
    #                             # holiday_type = d.find_element(By.XPATH, calendar_data["o_holiday_type_drop_down"])
    #                             # holiday_type.click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["regional_holiday_option"])))
    #                             # holiday_type = d.find_element(By.XPATH, calendar_data["regional_holiday_option"])
    #                             # holiday_type.click()
                                
    #                             # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["event_holiday"])))
    #                             # # holiday_type = d.find_element(By.XPATH, calendar_data["event_holiday"])
    #                             # # holiday_type.click()
    #                             # start_date_input = d.find_element(By.XPATH, calendar_data["o_start_date"])
    #                             # start_date_input.clear()
    #                             # start_date_input.send_keys(o_holiday_start_date)
                                
                                
                                
    #                             # start_date_input = d.find_element(By.XPATH, calendar_data["o_end_date"])
    #                             # start_date_input.clear()
    #                             # start_date_input.send_keys("02")
                                
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["o_notes"])))
    #                             # holiday_notes_input = d.find_element(By.XPATH, calendar_data["o_notes"])
    #                             # holiday_notes_input.clear()  # Clear any existing value in the input field
    #                             # holiday_notes_input.send_keys(o_notes)
                                
                                
    #                             # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["o_cancel_btn"])))
    #                             # # holiday_cancel_btn = d.find_element(By.XPATH, calendar_data["o_cancel_btn"])
    #                             # # holiday_cancel_btn.click()
                                
    #                             # sleep(1)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["o_save_btn"])))
    #                             # holiday_save_btn = d.find_element(By.XPATH, calendar_data["o_save_btn"])
    #                             # holiday_save_btn.click()
    #                             # sleep(1)
                                
                                
    #                             # wait.until(EC.visibility_of_element_located((By.XPATH,calendar_data["check_box_label"])))
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH,calendar_data["check_box_label"])))
    #                             # table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                             # table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                             # table_cells = table_rows[1].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
                                
    #                             # label = table_cells[1].find_element(By.XPATH, calendar_data["check_box_input"])   
                             
    #                             # select_btn = label.find_element(By.XPATH, calendar_data["check_box_input"])
    #                             # select_btn.click()
                                
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["check_box_save_btn"])))
    #                             # save_btn = d.find_element(By.XPATH, calendar_data["check_box_save_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(save_btn).click().perform()
                                
                                
    #                             # # events
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["events_tab"])))
    #                             # oh_btn = d.find_element(By.XPATH, calendar_data["events_tab"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(oh_btn).click().perform()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["add_new_event_btn"])))
    #                             # add_new_event = d.find_element(By.XPATH, calendar_data["add_new_event_btn"])
    #                             # add_new_event.click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["event_name_input"])))
    #                             # holiday_name_input = d.find_element(By.XPATH, calendar_data["event_name_input"])
    #                             # actions = ActionChains(d)
    #                             # actions.click(holiday_name_input).perform()
    #                             # holiday_name_input.clear()  # Clear any existing value in the input field
    #                             # holiday_name_input.send_keys(event_name)
    #                             # actions.move_by_offset(0, 0).click().perform()  # Remove focus from the input field

                                
    #                             # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["is_holiday"])))  
                                  # checkbox = d.find_element(By.XPATH, "//*[@id='form2']/div[1]/div[2]/label/span[1]/input")

                                  # click the checkbox
                                  # checkbox.click()

                                
    #                             # start_date_input = d.find_element(By.XPATH, calendar_data["e_start_date"])
    #                             # start_date_input.clear()
    #                             # start_date_input.send_keys(event_start_date)
                                
    #                             # start_date_input = d.find_element(By.XPATH, calendar_data["e_end_date"])
    #                             # start_date_input.clear()
    #                             # start_date_input.send_keys("02")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["e_notes"])))
    #                             # holiday_notes_input = d.find_element(By.XPATH, calendar_data["e_notes"])
    #                             # holiday_notes_input.clear()  # Clear any existing value in the input field
    #                             # holiday_notes_input.send_keys(event_note)
                                
    #                             # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["e_cancel_btn"])))
    #                             # # holiday_cancel_btn = d.find_element(By.XPATH, calendar_data["e_cancel_btn"])
    #                             # # holiday_cancel_btn.click()
                                
    #                             # sleep(1)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["e_save_btn"])))
    #                             # holiday_save_btn = d.find_element(By.XPATH, calendar_data["e_save_btn"])
    #                             # holiday_save_btn.click()
                                
    #                             # time.sleep(1)
                                
                                
    #                             # wait.until(EC.visibility_of_element_located((By.XPATH,calendar_data["check_box_label"])))
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH,calendar_data["check_box_label"])))
    #                             # table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                             # table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                             # table_cells = table_rows[1].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
                                
    #                             # label = table_cells[1].find_element(By.XPATH, calendar_data["check_box_input"])   
                             
    #                             # select_btn = label.find_element(By.XPATH, calendar_data["check_box_input"])
    #                             # select_btn.click()
                                
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["check_box_save_btn"])))
    #                             # save_btn = d.find_element(By.XPATH, calendar_data["check_box_save_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(save_btn).click().perform()
                                
                                
    #                              # ------ exam details ---------
                                 
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_tab"])))
    #                             # oh_btn = d.find_element(By.XPATH, calendar_data["exam_tab"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(oh_btn).click().perform()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["add_exam_btn"])))
    #                             # add_new_exam = d.find_element(By.XPATH, calendar_data["add_exam_btn"])
    #                             # add_new_exam.click()
                                
                    
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_description"])))
    #                             # ex_desc = d.find_element(By.XPATH, calendar_data["exam_description"])
    #                             # actions = ActionChains(d)
    #                             # actions.click(ex_desc).perform()
    #                             # ex_desc.clear()  # Clear any existing value in the input field
    #                             # ex_desc.send_keys(ex_description)
    #                             # actions.move_by_offset(0, 0).click().perform()  # Remove focus from the input field

                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_start_date"])))
    #                             # ex_start_date = d.find_element(By.XPATH, calendar_data["exam_start_date"])
    #                             # ex_start_date.send_keys("25-02-2023")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_end_date"])))
    #                             # ex_end_date = d.find_element(By.XPATH, calendar_data["exam_end_date"])
    #                             # ex_end_date.send_keys("26-02")
                                
    #                             # sleep(10)
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["e_notes"])))
    #                             # ex_desc = d.find_element(By.XPATH, calendar_data["e_notes"])
    #                             # ex_desc.clear()  # Clear any existing value in the input field
    #                             # ex_desc.send_keys(exam_notes)
                                                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_cancel_btn"])))
    #                             # holiday_cancel_btn = d.find_element(By.XPATH, calendar_data["exam_cancel_btn"])
    #                             # holiday_cancel_btn.click()
                                
    #                             # sleep(1)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_save_btn"])))
    #                             # holiday_save_btn = d.find_element(By.XPATH, calendar_data["exam_save_btn"])
    #                             # holiday_save_btn.click()
                                
    #                             # sleep(1)
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["check_box_save_btn"])))
    #                             # save_btn = d.find_element(By.XPATH, calendar_data["check_box_save_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(save_btn).click().perform()
                                
                                
                                
    # #                             # ------ slot details ------
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["slot_tab"])))
    #                             oh_btn = d.find_element(By.XPATH, calendar_data["slot_tab"])
                                
    #                             action = ActionChains(d)
    #                             action.move_to_element(oh_btn).click().perform()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["add_new_slot"])))
    #                             add_new_slot = d.find_element(By.XPATH, calendar_data["add_new_slot"])
    #                             add_new_slot.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["slot_dropdown"])))
    #                             add_slot = d.find_element(By.XPATH, calendar_data["slot_dropdown"])
    #                             add_slot.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["slot_ul"])))
    #                             add_new_exam_ul = d.find_element(By.XPATH, calendar_data["slot_ul"])
    #                             li = add_new_exam_ul.find_elements(By.TAG_NAME, "li")
    #                             li[0].click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["hour_type_dropdown"])))
    #                             add_new_exam = d.find_element(By.XPATH, calendar_data["hour_type_dropdown"])
    #                             add_new_exam.click()
                    
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["hour_type_ul"])))
    #                             add_new_exam_ul = d.find_element(By.XPATH, calendar_data["hour_type_ul"])
    #                             li = add_new_exam_ul.find_elements(By.TAG_NAME, "li")
    #                             li[0].click()
                                
    #                             sleep(1)
    #                             wait.until(EC.visibility_of_element_located((By.XPATH, calendar_data["from_time"])))
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["from_time"])))
    #                             slot_start_time = d.find_element(By.XPATH, calendar_data["from_time"])
    #                             slot_start_time.clear()
 
                                # slot_start_time.click()
                                # slot_start_time.send_keys("7:30")
                                # slot_start_time.send_keys(" AM")
                                
                               
                                # input_element = d.find_element(By.XPATH,'//input[@name="Slot_from_time"]')
                                # input_element.click()
                                # input_element.send_keys(slot_from_time)

                                                                
                                # # # to time
                                # sleep(2)
                                # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["to_time"])))
                                # slot_end_time_input = d.find_element(By.XPATH, calendar_data["to_time"])
                                # slot_end_time_input.clear()
                                # slot_end_time_input.send_keys(slot_to_time)

                                # # form_element = d.find_element(By.XPATH,'//form')
                                # # form_element.submit()
                                # # other_element = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div[2]/div[1]/header/div/div/p")
                                # # other_element.click()
                                # # sleep(10)
                                # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["slot_notes"])))
                                # s_note = d.find_element(By.XPATH, calendar_data["slot_notes"])
                                # actions = ActionChains(d)
                                # actions.click(s_note).perform()
                                # s_note.clear()  # Clear any existing value in the input field
                                # s_note.send_keys(slot_notes)
                                # actions.move_by_offset(0, 0).click().perform()  # Remove focus from the input field
                                
                                
                                # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_cancel_btn"])))
                                # # holiday_cancel_btn = d.find_element(By.XPATH, calendar_data["exam_cancel_btn"])
                                # # holiday_cancel_btn.click()
                                
                                # sleep(1)
                                # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_save_btn"])))
                                # holiday_save_btn = d.find_element(By.XPATH, calendar_data["exam_save_btn"])
                                # holiday_save_btn.click()
                                
                                # # sleep(5)
                                # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["check_box_save_btn"])))
                                # # save_btn = d.find_element(By.XPATH, calendar_data["check_box_save_btn"])
                                
                                # # action = ActionChains(d)
                                # # action.move_to_element(save_btn).click().perform()
                                
                                
                                      
                                # time.sleep(5)
   
   
    # def test_delete_calendar(self):
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
                  
    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                 act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 exp_title = data["dashboard_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 for calendar_data in calendar["calendar_data"]:
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["calendar_module_locator"])))
                        
    #                     calendar_module = d.find_element(By.XPATH, calendar_data["calendar_module_locator"])
    #                     calendar_module.click()
                        
    #                     wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div/h5/span")))
                        
    #                     exp_txt = d.find_element(By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div/h5/span").text
    #                     act_txt = "Academic Year"
                        
    #                     self.assertEqual(exp_txt,act_txt ,f"calendar page open failed: expected '{exp_txt}', but got '{act_txt}'")

    #                     # time.sleep(2)
    #                     wait.until(EC.visibility_of_element_located((By.XPATH, calendar_data["calendar_inside"])))
                        
    #                     # d.find_element(By.XPATH,calendar_data["calendar_inside"]).click()
    #                     ul = d.find_element(By.XPATH,"//*[@id='root']/div[2]/main/div[2]/div")
    #                     li = ul.find_elements(By.TAG_NAME, "li")
    #                     li[0].click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
    #                     table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                     table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                     table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
    #                     buttons = table_cell[2].find_elements(By.TAG_NAME, "button")
    
    #                     delete_btn = buttons[1]
    #                     delete_btn.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[4]/div/form/div/button[1]")))
    #                     cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[4]/div/form/div/button[1]")
    #                     cancel_btn.click()
                        
    #                     sleep(5)
                        
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[4]/div/form/div/button[2]")))
    #                     # confirm_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[4]/div/form/div/button[2]")
    #                     # confirm_btn.click()
                       
                                  
    # def test_search_calendar(self):
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
                  
    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                 act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 exp_title = data["dashboard_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 for calendar_data in calendar["calendar_data"]:
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["calendar_module_locator"])))
                        
    #                     calendar_module = d.find_element(By.XPATH, calendar_data["calendar_module_locator"])
    #                     calendar_module.click()
                        
    #                     wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div/h5/span")))
                        
    #                     exp_txt = d.find_element(By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div/h5/span").text
    #                     act_txt = "Academic Year"
                        
    #                     self.assertEqual(exp_txt,act_txt ,f"calendar page open failed: expected '{exp_txt}', but got '{act_txt}'")

    #                     # time.sleep(2)
    #                     wait.until(EC.visibility_of_element_located((By.XPATH, calendar_data["calendar_inside"])))
                        
    #                     # d.find_element(By.XPATH,calendar_data["calendar_inside"]).click()
    #                     ul = d.find_element(By.XPATH,"//*[@id='root']/div[2]/main/div[2]/div")
    #                     li = ul.find_elements(By.TAG_NAME, "li")
    #                     li[0].click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["search_by_calendar"])))
                        
    #                     search_calendar = d.find_element(By.XPATH, calendar_data["search_by_calendar"])
    #                     # search_calendar.send_keys("Calendar(1-5)")
    #                     # Clear any existing text from the search input field
    #                     search_calendar.clear()

    #                     # Type the search query letter by letter
    #                     search_query = "Calendar(1-5)"
                        #   sleep(5)
    #                     for char in search_query:
    #                         ActionChains(d).move_to_element(search_calendar).send_keys(char).perform()

                        
    #                     sleep(5)
                        
    
    # def test_edit_calendar_holidays(self):
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
                  
    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                 act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 exp_title = data["dashboard_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 with open('data/calendar.csv', 'r') as f:
    #                     reader = csv.reader(f)
    #                     # Skip the two header row
    #                     next(reader)
    #                     next(reader)
    #                     for row in reader:
                        
    #                         calendar_name = row[2]
    #                         calendar_code = row[3]
    #                         school_open = row[4]
    #                         last_working_day = row[5]
    #                         last_class_day = row[6]
    #                         description = row[7]
    #                         g_holiday_name = row[8]
    #                         g_holiday_date = row[9]
    #                         g_notes = row[10]
    #                         o_holiday_name = row[11]
    #                         o_holiday_start_date = row[12]
    #                         o_holiday_end_date = row[13]
    #                         o_notes = row[14]
    #                         event_name = row[15]
    #                         event_start_date = row[16]
    #                         event_end_date = row[17]
    #                         event_note = row[18]
    #                         ex_description = row[19]
    #                         exam_start_date = row[20]
    #                         exam_end_date = row[21]
    #                         exam_notes = row[22]
    #                         slot_from_time = row[23]
    #                         slot_to_time = row[24]
    #                         slot_notes = row[25]

    #                         for calendar_data in calendar["calendar_data"]:
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["calendar_module_locator"])))
                                
    #                             calendar_module = d.find_element(By.XPATH, calendar_data["calendar_module_locator"])
    #                             calendar_module.click()
                                
    #                             wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div/h5/span")))
                                
    #                             exp_txt = d.find_element(By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div/h5/span").text
    #                             act_txt = "Academic Year"
                                
    #                             self.assertEqual(exp_txt,act_txt ,f"calendar page open failed: expected '{exp_txt}', but got '{act_txt}'")

    #                             # time.sleep(2)
    #                             wait.until(EC.visibility_of_element_located((By.XPATH, calendar_data["calendar_inside"])))
                                
    #                             d.find_element(By.XPATH,calendar_data["calendar_inside"]).click()
    #                             ul = d.find_element(By.XPATH,"//*[@id='root']/div[2]/main/div[2]/div")
    #                             li = ul.find_elements(By.TAG_NAME, "li")
    #                             li[0].click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
                                
    #                             table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                             table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                             table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
                                
    #                             buttons = table_cell[2].find_elements(By.TAG_NAME, "button")
                             
    #                             edit_btn = buttons[0]
    #                             edit_btn.click()
                            
    #                             # # time.sleep(4)
    #                             # wait.until(EC.presence_of_element_located((By.XPATH, calendar_data["calendar_name_input"]))) 
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["calendar_name_input"])))
                                
    #                             # calendar_name_input = d.find_element(By.XPATH, calendar_data["calendar_name_input"])
                                
    #                             # actions = ActionChains(d)
    #                             # actions.click(calendar_name_input).perform()
    #                             # d.execute_script("arguments[0].value = arguments[1];", calendar_name_input, calendar_name)
    #                             # d.execute_script("arguments[0].dispatchEvent(new Event('change'));", calendar_name_input)
    #                             # d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", calendar_name_input, calendar_name)
                                
                            
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["calendar_code_input"])))
                                
    #                             # calendar_code_input = d.find_element(By.XPATH, calendar_data["calendar_code_input"])
    #                             # actions = ActionChains(d)
    #                             # actions.click(calendar_code_input).perform()
    #                             # d.execute_script("arguments[0].value = arguments[1];", calendar_code_input, calendar_code)
    #                             # d.execute_script("arguments[0].dispatchEvent(new Event('change'));", calendar_code_input)
    #                             # d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", calendar_code_input, calendar_code)
                            
    #                             # d.find_element(By.XPATH, calendar_data["classGroup_type_dropdown"]).click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["classGroup_type_dropdown"])))
    #                             # ul = d.find_element(By.XPATH, calendar_data["classGroup_type_dropdown_ul"])
    #                             # li = ul.find_elements(By.TAG_NAME, "li")
                                
    #                             # li[0].click()
                                
    #                             # date_str = school_open
    #                             # date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    #                             # formatted_date = datetime.strftime(date_obj, "%Y-%m-%d")
                                
    #                             # # time.sleep(2)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["school_open_date_input"])))
    #                             # date_field = d.find_element(By.XPATH, calendar_data["school_open_date_input"])
    #                             # date_field.clear()
    #                             # actions = ActionChains(d)
    #                             # actions.click(date_field).perform()
    #                             # d.execute_script("arguments[0].value = arguments[1];", date_field, formatted_date)
    #                             # d.execute_script("arguments[0].dispatchEvent(new Event('change'));", date_field)
    #                             # d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", date_field, formatted_date)
                              
    #                             # date_str = last_working_day
    #                             # date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    #                             # formatted_date = datetime.strftime(date_obj, "%Y-%m-%d")
                                
    #                             # # time.sleep(2)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["last_working_day_input"])))
    #                             # date_field = d.find_element(By.XPATH, calendar_data["last_working_day_input"])
    #                             # date_field.clear()
    #                             # actions = ActionChains(d)
    #                             # actions.click(date_field).perform()
    #                             # d.execute_script("arguments[0].value = arguments[1];", date_field, formatted_date)
    #                             # d.execute_script("arguments[0].dispatchEvent(new Event('change'));", date_field)
    #                             # d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", date_field, formatted_date)
                              
    #                             # date_str = last_class_day
    #                             # date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    #                             # formatted_date = datetime.strftime(date_obj, "%Y-%m-%d")
                                
    #                             # # time.sleep(2)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["last_day_class_input"])))
    #                             # date_field = d.find_element(By.XPATH, calendar_data["last_day_class_input"])
    #                             # date_field.clear()
    #                             # actions = ActionChains(d)
    #                             # actions.click(date_field).perform()
    #                             # d.execute_script("arguments[0].value = arguments[1];", date_field, formatted_date)
    #                             # d.execute_script("arguments[0].dispatchEvent(new Event('change'));", date_field)
    #                             # d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", date_field, formatted_date)
                              
                                
                              
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["description_input"])))
                                
    #                             # description_input = d.find_element(By.XPATH, calendar_data["description_input"])
    #                             # actions = ActionChains(d)
    #                             # actions.click(description_input).perform()
    #                             # d.execute_script("arguments[0].value = arguments[1];", description_input, description)
    #                             # d.execute_script("arguments[0].dispatchEvent(new Event('change'));", description_input)
    #                             # d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", description_input, description)
                              
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["status_dropdown"])))
                                
    #                             # d.find_element(By.XPATH, calendar_data["status_dropdown"]).click()
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["status_active"])))
                                
    #                             # d.find_element(By.XPATH, calendar_data["status_active"]).click()
    #                             # d.find_element(By.XPATH, calendar_data["status_nonActive"]).click()
                                
    #                             # # # time.sleep(3)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["week_day_start_droptdown"])))
    #                             # d.find_element(By.XPATH, calendar_data["week_day_start_droptdown"]).click()
                                
    #                             # wait.until(EC.presence_of_all_elements_located((By.XPATH, calendar_data["dropdown_ul_locator"])))
                        
    #                             # #                                 # Find the dropdown element
    #                             # dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".MuiSelect-select")))

    #                             # # Move the mouse to the center of the dropdown element and click it
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(dropdown).click().perform()

    #                             # # # Wait for the dropdown list to appear and find all the options
    #                             # ul_element = wait.until(EC.presence_of_element_located((By.XPATH, calendar_data["dropdown_ul_locator"])))
    #                             # li_elements = ul_element.find_elements(By.TAG_NAME, "li")

    #                             # # # Click the first option in the dropdown list
    #                             # li_elements[0].click()
                                
    #                             # dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, calendar_data["working_day_group"])))

    #                             # label_elements1 = d.find_element(By.XPATH, calendar_data["working_day_label1"])
    #                             # label_elements2 = d.find_element(By.XPATH, calendar_data["working_day_label2"])
    #                             # label_elements3 = d.find_element(By.XPATH, calendar_data["working_day_label3"])
    #                             # label_elements4 = d.find_element(By.XPATH, calendar_data["working_day_label4"])
    #                             # label_elements5 = d.find_element(By.XPATH, calendar_data["working_day_label5"])
    #                             # label_elements6 = d.find_element(By.XPATH, calendar_data["working_day_label6"])
    #                             # label_elements7 = d.find_element(By.XPATH, calendar_data["working_day_label7"])
                                
    #                             #  # Click the first option in the dropdown list
    #                             # label_elements1.click()
    #                             # label_elements2.click()
    #                             # label_elements3.click()
    #                             # label_elements4.click()
    #                             # label_elements5.click()
    #                             # label_elements6.click()
    #                             # # label_elements7.click()
                                
    #                             # # dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, calendar_data["working_weekends1"])))

    #                             # # label_elements1 = d.find_element(By.XPATH, calendar_data["working_weekends1"])
    #                             # # label_elements2 = d.find_element(By.XPATH, calendar_data["working_weekends2"])
    #                             # # label_elements3 = d.find_element(By.XPATH, calendar_data["working_weekends3"])
    #                             # # label_elements4 = d.find_element(By.XPATH, calendar_data["working_weekends4"])
    #                             # # label_elements5 = d.find_element(By.XPATH, calendar_data["working_weekends5"])
                                
    #                             # # label_elements1.click()
    #                             # # label_elements2.click()
    #                             # # label_elements3.click()
    #                             # # label_elements4.click()
    #                             # # label_elements5.click()
                                
    #                             # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["c_back_btn"])))
    #                             # # back_btn = d.find_element(By.XPATH, calendar_data["c_back_btn"])
                                
    #                             # # action = ActionChains(d)
    #                             # # action.move_to_element(back_btn).click().perform()

    #                             # # back_btn.click()
                                
    #                             # -- save --
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["save_btn"])))
    #                             # save_btn = d.find_element(By.XPATH, calendar_data["save_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(save_btn).click().perform()
                                
    #                             # -- cancel --
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["cancel_btn"])))
    #                             # cancel_btn = d.find_element(By.XPATH, calendar_data["cancel_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(cancel_btn).click().perform()
                                
    #                             # -- print --
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["print_btn"])))
    #                             # print_btn = d.find_element(By.XPATH, calendar_data["print_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(print_btn).click().perform()
                                
    #                             # sleep(1)
                                
    #                             # # ----- govt holidays ------
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["govt_holidays_tab"])))
    #                             # gh_btn = d.find_element(By.XPATH, calendar_data["govt_holidays_tab"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(gh_btn).click().perform()
                     
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["pagination_nav"])))
    #                             # pagination_nav = d.find_element(By.XPATH, calendar_data["pagination_nav"])
    #                             # pagination_ul = pagination_nav.find_element(By.XPATH, calendar_data["pagination_ul_element"])
    #                             # pagination_li = pagination_ul.find_elements(By.TAG_NAME, "li")
                                
    #                             # pagination_btn = pagination_li[2]
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(pagination_btn).click().perform()
                                
    #                             # wait.until(EC.visibility_of_element_located((By.XPATH,calendar_data["check_box_label"])))
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH,calendar_data["check_box_label"])))
    #                             # table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                             # table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                             # table_cells = table_rows[1].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
                                
                                
    #                             # print(len(table_cells))

    #                             # edt_btn = table_cells[1].find_element(By.TAG_NAME, "a")
    #                             # edt_btn.click()
                                
    #                             # delete_btn = table_cells[1].find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[6]/button")
    #                             # delete_btn.click()
                                
    #                             # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div/button[1]")
    #                             # cancel_btn.click()
                                
    #                             # confirm_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div/button[2]")
    #                             # confirm_btn.click()
                                
    #                             # sleep(5)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["holiday_name_input"])))
    #                             # holiday_name_input = d.find_element(By.XPATH, calendar_data["holiday_name_input"])
    #                             # actions = ActionChains(d)
    #                             # actions.click(holiday_name_input).perform()
    #                             # # actions.send_keys(Keys.BACKSPACE * 10).perform()
    #                             # d.execute_script("arguments[0].value = '';", holiday_name_input)
                                
    #                             # holiday_name_input.send_keys(g_holiday_name)
    #                             # actions.move_by_offset(0, 0).click().perform()  # Remove focus from the input field

    #                             # start_date_input = d.find_element(By.XPATH, calendar_data["gh_start_date"])
    #                             # start_date_input.clear()
    #                             # start_date_input.send_keys(g_holiday_date)
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["gh_notes"])))
    #                             # holiday_notes_input = d.find_element(By.XPATH, calendar_data["gh_notes"])
    #                             # actions = ActionChains(d)
    #                             # actions.click(holiday_notes_input).perform()
    #                             # d.execute_script("arguments[0].value = '';", holiday_notes_input)
                                
    #                             # # # Use the keyboard to select all the text in the input field and delete it
    #                             # # actions = ActionChains(d)
    #                             # # actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
                                
    #                             # holiday_notes_input.send_keys(g_notes)
    #                             # actions.move_by_offset(0, 0).click().perform()  # Remove focus from the input field

                                
    #                             # # sleep(5)
                                                    
    #                             # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["gh_cancel_btn"])))
    #                             # # holiday_cancel_btn = d.find_element(By.XPATH, calendar_data["gh_cancel_btn"])
    #                             # # holiday_cancel_btn.click()
                                
    #                             # # sleep(1)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["gh_save_btn"])))
    #                             # holiday_save_btn = d.find_element(By.XPATH, calendar_data["gh_save_btn"])
    #                             # holiday_save_btn.click()
                                
    #                             # sleep(1)

    #                             # wait.until(EC.visibility_of_element_located((By.XPATH,calendar_data["check_box_label"])))
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH,calendar_data["check_box_label"])))
    #                             # table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                             # table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                             # table_cells = table_rows[1].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
                                
    #                             # label = table_cells[1].find_element(By.XPATH, calendar_data["check_box_input"])   
                             
    #                             # select_btn = label.find_element(By.XPATH, calendar_data["check_box_input"])
    #                             # select_btn.click()
                                
    #                             # # time.sleep(5) 
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["check_box_save_btn"])))
    #                             # save_btn = d.find_element(By.XPATH, calendar_data["check_box_save_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(save_btn).click().perform()
                                
    #                             # -- cancel --
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["cancel_btn"])))
    #                             # cancel_btn = d.find_element(By.XPATH, calendar_data["cancel_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(cancel_btn).click().perform()
                                
    #                             # -- print --
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["print_btn"])))
    #                             # print_btn = d.find_element(By.XPATH, calendar_data["print_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(print_btn).click().perform()
    #                             # sleep(1)
                                
                               
    #                             # # time.sleep(5) 
    #                             # # # # ----- other holidays -----
                             
    #                             # wait.until(EC.visibility_of_element_located((By.XPATH, calendar_data["other_holiday_tab"])))
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["other_holiday_tab"])))
    #                             # oh_btn = d.find_element(By.XPATH, calendar_data["other_holiday_tab"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(oh_btn).click().perform()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["pagination_nav"])))
    #                             # pagination_nav = d.find_element(By.XPATH, calendar_data["pagination_nav"])
    #                             # pagination_ul = pagination_nav.find_element(By.XPATH, calendar_data["pagination_ul_element"])
    #                             # pagination_li = pagination_ul.find_elements(By.TAG_NAME, "li")
                                
    #                             # pagination_btn = pagination_li[2]
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(pagination_btn).click().perform()
                                
                                
    #                             # wait.until(EC.visibility_of_element_located((By.XPATH,calendar_data["check_box_label"])))
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH,calendar_data["check_box_label"])))
    #                             # table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                             # table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                             # table_cells = table_rows[1].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
                                
                                
    #                             # # print(len(table_cells))

    #                             # edt_btn = table_cells[1].find_element(By.TAG_NAME, "a")
    #                             # edt_btn.click()
                                
    #                             # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div/button[1]")
    #                             # cancel_btn.click()
                                
    #                             # confirm_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div/button[2]")
    #                             # confirm_btn.click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["o_holiday_name"])))
    #                             # o_holiday_name_input = d.find_element(By.XPATH, calendar_data["o_holiday_name"])
    #                             # actions = ActionChains(d)
    #                             # actions.click(o_holiday_name_input).perform()
    #                             # d.execute_script("arguments[0].value = '';", o_holiday_name_input)
                                
    #                             # o_holiday_name_input.send_keys(o_holiday_name)
    #                             # actions.move_by_offset(0, 0).click().perform()  # Remove focus from the input field

    #                             # # sleep(5)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["o_holiday_type_drop_down"])))
    #                             # holiday_type = d.find_element(By.XPATH, calendar_data["o_holiday_type_drop_down"])
    #                             # holiday_type.click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["regional_holiday_option"])))
    #                             # holiday_type = d.find_element(By.XPATH, calendar_data["regional_holiday_option"])
    #                             # holiday_type.click()
                                
    #                             # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["event_holiday"])))
    #                             # # holiday_type = d.find_element(By.XPATH, calendar_data["event_holiday"])
    #                             # # holiday_type.click()
                                
    #                             # start_date_input = d.find_element(By.XPATH, calendar_data["o_start_date"])
    #                             # start_date_input.clear()
    #                             # start_date_input.send_keys(o_holiday_start_date)
                                
                                
    #                             # start_date_input = d.find_element(By.XPATH, calendar_data["o_end_date"])
    #                             # start_date_input.clear()
    #                             # start_date_input.send_keys("02")
                                
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["o_notes"])))
    #                             # o_holiday_notes_input = d.find_element(By.XPATH, calendar_data["o_notes"])
    #                             # actions = ActionChains(d)
    #                             # actions.click(o_holiday_notes_input).perform()
    #                             # d.execute_script("arguments[0].value = '';", o_holiday_notes_input)
                                
    #                             # o_holiday_notes_input.send_keys(o_notes)
                                
                                
    #                             # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["o_cancel_btn"])))
    #                             # # holiday_cancel_btn = d.find_element(By.XPATH, calendar_data["o_cancel_btn"])
    #                             # # holiday_cancel_btn.click()
                                
    #                             # # sleep(1)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["o_save_btn"])))
    #                             # holiday_save_btn = d.find_element(By.XPATH, calendar_data["o_save_btn"])
    #                             # holiday_save_btn.click()
                                
    #                             # sleep(2)
                                
                                
    #                             # wait.until(EC.visibility_of_element_located((By.XPATH,calendar_data["check_box_label"])))
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH,calendar_data["check_box_label"])))
    #                             # table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                             # table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                             # table_cells = table_rows[1].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
                                
    #                             # label = table_cells[1].find_element(By.XPATH, calendar_data["check_box_input"])   
                             
    #                             # select_btn = label.find_element(By.XPATH, calendar_data["check_box_input"])
    #                             # select_btn.click()
                                
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["check_box_save_btn"])))
    #                             # save_btn = d.find_element(By.XPATH, calendar_data["check_box_save_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(save_btn).click().perform()
                                
    #                             # -- cancel --
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["cancel_btn"])))
    #                             # cancel_btn = d.find_element(By.XPATH, calendar_data["cancel_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(cancel_btn).click().perform()
                                
    #                             # -- print --
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["print_btn"])))
    #                             # print_btn = d.find_element(By.XPATH, calendar_data["print_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(print_btn).click().perform()
                                
    #                             # sleep(2)
    #                             # ----- events -----
                                
    #                             # wait.until(EC.visibility_of_all_elements_located((By.XPATH, calendar_data["events_tab"])))
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["events_tab"])))
    #                             # event_tab = d.find_element(By.XPATH, calendar_data["events_tab"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(event_tab).click().perform()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["pagination_nav"])))
    #                             # pagination_nav = d.find_element(By.XPATH, calendar_data["pagination_nav"])
    #                             # pagination_ul = pagination_nav.find_element(By.XPATH, calendar_data["pagination_ul_element"])
    #                             # pagination_li = pagination_ul.find_elements(By.TAG_NAME, "li")
                                
    #                             # pagination_btn = pagination_li[2]
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(pagination_btn).click().perform()
                                
                                                        
    #                             # # sleep(5)                               
    #                             # wait.until(EC.visibility_of_element_located((By.XPATH,calendar_data["check_box_label"])))
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH,calendar_data["check_box_label"])))
    #                             # table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                             # table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                             # table_cells = table_rows[1].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
                                                                                    
    #                             # # sleep(3)
    #                             # # Scroll the element to the right by 1000 pixels
    #                             # d.execute_script("arguments[0].scrollLeft += 1500;", table_cells)

    #                             # # Scroll the element into view
    #                             # d.execute_script("arguments[0].scrollIntoView();", table_cells[1])

    #                             # # table_cells[1] is constant for edit button
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='delete']")))
                                
    #                             #     # Find the edit button element
    #                             # edt_btn = table_cells[1].find_element(By.XPATH, "//button[@aria-label='delete']")

    #                             # actions = ActionChains(d)
    #                             # actions.move_to_element(table_cells[1]).click(edt_btn).perform()
                                
                                
    #                             # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div/button[1]")
    #                             # cancel_btn.click()
                                
    #                             # confirm_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div/button[2]")
    #                             # confirm_btn.click()
                                
    #                             # # sleep(2)
                                
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["event_name_input"])))
    #                             # e_holiday_name_input = d.find_element(By.XPATH, calendar_data["event_name_input"])
    #                             # actions = ActionChains(d)
    #                             # actions.click(e_holiday_name_input).perform()
    #                             # d.execute_script("arguments[0].value = '';", e_holiday_name_input)
    #                             # d.execute_script("arguments[0].value = arguments[1];", e_holiday_name_input, event_name)
    #                             # d.execute_script("arguments[0].dispatchEvent(new Event('change'));", e_holiday_name_input)
    #                             # d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", e_holiday_name_input, event_name)
                                        
    #                             # # e_holiday_name_input.send_keys(event_name)
    #                             # # actions.move_by_offset(0, 0).click().perform()  # Remove focus from the input field
                                
    #                             # # wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='form2']/div[1]/div[2]/label/span[1]/input")))

    #                             # # locate the element
    #                             # checkbox = d.find_element(By.XPATH, "//*[@id='form2']/div[1]/div[2]/label/span[1]/input")

    #                             # # click the checkbox
    #                             # checkbox.click()
                                
    #                             # sleep(5)
                                
    #                             # start_date_input = d.find_element(By.XPATH, calendar_data["e_start_date"])
    #                             # start_date_input.clear()
    #                             # start_date_input.send_keys(event_start_date)
                                
    #                             # start_date_input = d.find_element(By.XPATH, calendar_data["e_end_date"])
    #                             # start_date_input.clear()
    #                             # start_date_input.send_keys("02")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["e_notes"])))
    #                             # holiday_notes_input = d.find_element(By.XPATH, calendar_data["e_notes"])
    #                             # d.execute_script("arguments[0].value = '';", holiday_notes_input)
                                
    #                             # holiday_notes_input.send_keys(event_note)
    #                             # actions.move_by_offset(0, 0).click().perform()  # Remove focus from the input field
                                
    #                             # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["e_cancel_btn"])))
    #                             # # holiday_cancel_btn = d.find_element(By.XPATH, calendar_data["e_cancel_btn"])
    #                             # # holiday_cancel_btn.click()
                                
    #                             # sleep(2)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["e_save_btn"])))
    #                             # holiday_save_btn = d.find_element(By.XPATH, calendar_data["e_save_btn"])
    #                             # holiday_save_btn.click()
                                
    #                             # time.sleep(5)
                                
                                
    #                             # # wait.until(EC.visibility_of_element_located((By.XPATH,calendar_data["check_box_label"])))
    #                             # # wait.until(EC.element_to_be_clickable((By.XPATH,calendar_data["check_box_label"])))
    #                             # # table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                             # # table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                             # # table_cells = table_rows[1].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
                                
    #                             # # label = table_cells[1].find_element(By.XPATH, calendar_data["check_box_input"])   

    #                             # # wait.until(EC.element_to_be_clickable((By.XPATH,calendar_data["check_box_input"])))
                                
    #                             # # select_btn = label.find_element(By.XPATH, calendar_data["check_box_input"])
    #                             # # select_btn.click()
                                
    #                             # sleep(2)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["check_box_save_btn"])))
    #                             # save_btn = d.find_element(By.XPATH, calendar_data["check_box_save_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(save_btn).click().perform()
                                
    #                             # -- cancel --
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["cancel_btn"])))
    #                             # cancel_btn = d.find_element(By.XPATH, calendar_data["cancel_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(cancel_btn).click().perform()
                                
    #                             # -- print --
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["print_btn"])))
    #                             # print_btn = d.find_element(By.XPATH, calendar_data["print_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(print_btn).click().perform()
                                
                                
    #                             # #  ------ exam details ---------
    #                             # sleep(2)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_tab"])))
    #                             # oh_btn = d.find_element(By.XPATH, calendar_data["exam_tab"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(oh_btn).click().perform()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["pagination_nav"])))
    #                             # pagination_nav = d.find_element(By.XPATH, calendar_data["pagination_nav"])
    #                             # pagination_ul = pagination_nav.find_element(By.XPATH, calendar_data["pagination_ul_element"])
    #                             # pagination_li = pagination_ul.find_elements(By.TAG_NAME, "li")
                                
    #                             # pagination_btn = pagination_li[2]
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(pagination_btn).click().perform()
                                
                                
    #                             # sleep(5)                               
    #                             # # wait.until(EC.visibility_of_element_located((By.XPATH,calendar_data["check_box_label"])))
    #                             # wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"MuiDataGrid-virtualScrollerRenderZone")))
    #                             # table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                             # table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                             # # print(len(table_rows),"hi") 
                                
    #                             # table_cells = table_rows[1].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
                                                                                    
                                
    #                             # # table_cells[1] is constant for edit button
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='delete']")))
                                
    #                             #     # Find the edit button element
    #                             # edt_btn = table_cells[1].find_element(By.XPATH, "//button[@aria-label='delete']")
    #                             # actions = ActionChains(d)
    #                             # actions.move_to_element(edt_btn).click(edt_btn).perform()
                                
                                
    #                             # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div/button[1]")
    #                             # cancel_btn.click()
                                
    #                             # confirm_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div/button[2]")
    #                             # confirm_btn.click()
                    
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_description"])))
    #                             # ex_desc = d.find_element(By.XPATH, calendar_data["exam_description"])
    #                             # actions = ActionChains(d)
    #                             # actions.click(ex_desc).perform()
    #                             # d.execute_script("arguments[0].value = '';", ex_desc)
    #                             # d.execute_script("arguments[0].value = arguments[1];", ex_desc, ex_description)
    #                             # d.execute_script("arguments[0].dispatchEvent(new Event('change'));", ex_desc)
    #                             # d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", ex_desc, ex_description)
                                
                                
    #                             # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_start_date"])))
    #                             # # ex_start_date = d.find_element(By.XPATH, calendar_data["exam_start_date"])
    #                             # # ex_start_date.send_keys("25-02-2023")
                                
    #                             # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_end_date"])))
    #                             # # ex_end_date = d.find_element(By.XPATH, calendar_data["exam_end_date"])
    #                             # # ex_end_date.send_keys("26-02")
                                
    #                             # sleep(2)
                                
    #                             # # wait.until(EC.visibility_of_element_located((By.XPATH, calendar_data["e_notes"])))
    #                             # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["e_notes"])))
    #                             # # ex_notes = d.find_element(By.XPATH, calendar_data["e_notes"])
    #                             # # ex_notes.send_keys("hi")
    #                             # # # actions = ActionChains(d)
    #                             # # actions.click(ex_notes).perform()
    #                             # # d.execute_script("arguments[0].value = '';", ex_notes)
    #                             # # d.execute_script("arguments[0].value = arguments[1];", ex_notes, exam_notes)
    #                             # # d.execute_script("arguments[0].dispatchEvent(new Event('change'));", ex_notes)
    #                             # # d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", ex_notes, exam_notes)
                                                                
    #                             # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_cancel_btn"])))
    #                             # # holiday_cancel_btn = d.find_element(By.XPATH, calendar_data["exam_cancel_btn"])
    #                             # # holiday_cancel_btn.click()
                                
    #                             # sleep(1)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_save_btn"])))
    #                             # holiday_save_btn = d.find_element(By.XPATH, calendar_data["exam_save_btn"])
    #                             # holiday_save_btn.click()
                                
    #                             # sleep(5)
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["check_box_save_btn"])))
    #                             # save_btn = d.find_element(By.XPATH, calendar_data["check_box_save_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(save_btn).click().perform()
                                
    #                             # -- cancel --
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["cancel_btn"])))
    #                             # cancel_btn = d.find_element(By.XPATH, calendar_data["cancel_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(cancel_btn).click().perform()
                                
    #                             # -- print --
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["print_btn"])))
    #                             # print_btn = d.find_element(By.XPATH, calendar_data["print_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(print_btn).click().perform()
                                
                                                            
    #                             # # ------ slot details ------
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["slot_tab"])))
    #                             # oh_btn = d.find_element(By.XPATH, calendar_data["slot_tab"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(oh_btn).click().perform()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["pagination_nav"])))
    #                             # pagination_nav = d.find_element(By.XPATH, calendar_data["pagination_nav"])
    #                             # pagination_ul = pagination_nav.find_element(By.XPATH, calendar_data["pagination_ul_element"])
    #                             # pagination_li = pagination_ul.find_elements(By.TAG_NAME, "li")
                                
    #                             # pagination_btn = pagination_li[2]
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(pagination_btn).click().perform()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"MuiDataGrid-virtualScrollerRenderZone")))
    #                             # table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                             # table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                             # # print(len(table_rows),"hi") 
                                
    #                             # table_cells = table_rows[1].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
                                                                                    
    #                             # # table_cells[1] is constant for edit button
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='delete']")))
                                
    #                             # # Find the edit button element
    #                             # edt_btn = table_cells[0].find_element(By.XPATH, "//button[@aria-label='delete']")
    #                             # actions = ActionChains(d)
    #                             # actions.move_to_element(edt_btn).click(edt_btn).perform()
    #                             # print(len(table_cells))
                                
                                
    #                             # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div/button[1]")
    #                             # cancel_btn.click()
                                
    #                             # confirm_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div/button[2]")
    #                             # confirm_btn.click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["slot_dropdown"])))
    #                             # add_slot = d.find_element(By.XPATH, calendar_data["slot_dropdown"])
    #                             # add_slot.click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["slot_ul"])))
    #                             # add_new_exam_ul = d.find_element(By.XPATH, calendar_data["slot_ul"])
    #                             # li = add_new_exam_ul.find_elements(By.TAG_NAME, "li")
    #                             # li[0].click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["hour_type_dropdown"])))
    #                             # add_new_exam = d.find_element(By.XPATH, calendar_data["hour_type_dropdown"])
    #                             # add_new_exam.click()
                    
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["hour_type_ul"])))
    #                             # add_new_exam_ul = d.find_element(By.XPATH, calendar_data["hour_type_ul"])
    #                             # li = add_new_exam_ul.find_elements(By.TAG_NAME, "li")
    #                             # li[0].click()
                                
    #                             # sleep(1)
    #                             # wait.until(EC.visibility_of_element_located((By.XPATH, calendar_data["from_time"])))
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["from_time"])))
    #                             # slot_start_time = d.find_element(By.XPATH, calendar_data["from_time"])
    #                             # slot_start_time.clear()

    #                             # # # Convert time string to datetime object and format to required format
    #                             # # time_obj = datetime.strptime("7:30 PM", "%I:%M %p")
    #                             # # time_str = time_obj.strftime("%I:%M:%S %p")
                                                                
    #                             # # slot_start_time.click()
    #                             # # slot_start_time.send_keys(time_str)
    #                             # # # d.execute_script("arguments[0].value = arguments[1];", slot_start_time, time_str)

    #                             # # # # to time
    #                             # # sleep(5)
    #                             # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["to_time"])))
    #                             # # slot_end_time_input = d.find_element(By.XPATH, calendar_data["to_time"])
    #                             # # slot_end_time_input.clear()
    #                             # # slot_end_time_input.send_keys("7:45")
    #                             # # # d.execute_script("arguments[0].value = arguments[1]", slot_end_time_input, "7:30 PM") 
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["slot_notes"])))
    #                             # s_note = d.find_element(By.XPATH, calendar_data["slot_notes"])
    #                             # actions = ActionChains(d)
    #                             # actions.click(s_note).perform()
    #                             # d.execute_script("arguments[0].value = '';", s_note)
    #                             # s_note.send_keys(slot_notes)
    #                             # actions.move_by_offset(0, 0).click().perform()  # Remove focus from the input field
                                
                                
    #                             # # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_cancel_btn"])))
    #                             # # holiday_cancel_btn = d.find_element(By.XPATH, calendar_data["exam_cancel_btn"])
    #                             # # holiday_cancel_btn.click()
                                
    #                             # sleep(1)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["exam_save_btn"])))
    #                             # holiday_save_btn = d.find_element(By.XPATH, calendar_data["exam_save_btn"])
    #                             # holiday_save_btn.click()
                                
    #                             # sleep(5)
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["check_box_save_btn"])))
    #                             # save_btn = d.find_element(By.XPATH, calendar_data["check_box_save_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(save_btn).click().perform()
                                                                      
    #                             # -- cancel --
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["cancel_btn"])))
    #                             # cancel_btn = d.find_element(By.XPATH, calendar_data["cancel_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(cancel_btn).click().perform()
                                
    #                             # -- print --
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, calendar_data["print_btn"])))
    #                             # print_btn = d.find_element(By.XPATH, calendar_data["print_btn"])
                                
    #                             # action = ActionChains(d)
    #                             # action.move_to_element(print_btn).click().perform()
                                
                                
                                
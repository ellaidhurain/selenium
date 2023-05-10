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

with open('config/lesson_plan.json') as f:
    lesson_plan = json.load(f)

class TestLessonPlan(unittest.TestCase):

    def setUp(self):
        # Initialize the webdriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser
        self.driver.quit()

    # def test_lesson_plan_add(self):
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

    #                 with open('data/lesson_plan.csv', 'r') as f:
    #                     reader = csv.reader(f)
    #                     # Skip the two header row
    #                     next(reader)
    #                     next(reader)
                        
    #                     for row in reader:
    #                         unit_name = row[0]
    #                         unit_notes = row[1]
    #                         subunit_name = row[2]
    #                         topic = row[3]
                            
    #                         for lesson_plan_data in lesson_plan["lesson_plan_data"]:
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, lesson_plan_data["lesson_plan_module"])))
                                
    #                             lesson_plan_module = d.find_element(By.XPATH, lesson_plan_data["lesson_plan_module"])
    #                             lesson_plan_module.click()
                                    
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, lesson_plan_data["parent_div"])))
    #                             classroom_ul = d.find_element(By.XPATH, lesson_plan_data["parent_div"])
    #                             li = classroom_ul.find_elements(By.TAG_NAME,"div")
    #                             wait.until(
    #                                         EC.presence_of_element_located((By.XPATH, '//p[text()="I-A"]'))
    #                                     )
    #                             cl_li = d.find_element(By.XPATH,'//p[text()="I-A"]')
    #                             cl_li.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
    #                             table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                             table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                             table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
    #                             year_btn = table_cell[0].find_element(By.TAG_NAME, "p")

    #                             year_btn.click()                         
                                
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div")))
    #                             parent_div = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div")
    #                             child_div = parent_div.find_elements(By.TAG_NAME,"div")
                                # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/ul")))
                        
    #                             ul = child_div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/ul")
    #                             li = ul.find_element(By.TAG_NAME,"li")
    #                             div = li.find_elements(By.TAG_NAME,"div")
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/ul/li/div[2]/p[1]")))
                                
    #                             inside = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/ul/li/div[2]/p[1]")
    #                             action = ActionChains(d)
    #                             action.move_to_element(inside).click().perform()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[2]/div[2]/button[1]")))
                                
    #                             # add_unit = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div[2]/div[2]/button[1]")
    #                             # add_unit.click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.NAME, "Name")))
                                
    #                             # add_unit_name = d.find_element(By.NAME,"Name")
    #                             # add_unit_name.send_keys("unit1")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.NAME, "Notes")))
                                
    #                             # add_unit_notes = d.find_element(By.NAME,"Notes")
    #                             # add_unit_notes.send_keys("unit1 notes")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[2]/div/div/input")))
                                
    #                             # unit_theory_time = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[2]/div/div/input")
    #                             # unit_theory_time.send_keys("10")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[4]/div/div/input")))
                                
    #                             # unit_quiz_time = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[4]/div/div/input")
    #                             # unit_quiz_time.send_keys("20")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[6]/div/div/input")))
                                
    #                             # unit_test_time = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[6]/div/div/input")
    #                             # unit_test_time.send_keys("15")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[8]/div/div/input")))
                                
    #                             # unit_homework_time = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[8]/div/div/input")
    #                             # unit_homework_time.send_keys("25")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[10]/div/div/input")))
                                
    #                             # unit_others_time = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[10]/div/div/input")
    #                             # unit_others_time.send_keys("30")
                                
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[1]")))
                                
    #                             # cancel_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[1]")
    #                             # cancel_btn.click()
                                
    #                             # # # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[2]")))
                                
    #                             # # # save_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[2]")
    #                             # # # save_btn.click()
                                
    #                             # ## ---- subunit ---- 
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[2]/div[2]/button[2]")))
                                
    #                             # add_subunit = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div[2]/div[2]/button[2]")
    #                             # add_subunit.click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/main/div[2]/div[2]/div/form/div[1]/div/div/div")))
                                
    #                             # select_unit_name = d.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div[2]/div[2]/div/form/div[1]/div/div/div")
    #                             # select_unit_name.click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
    #                             # add_unit_name_ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
    #                             # li = add_unit_name_ul.find_elements(By.TAG_NAME, "li")
    #                             # li[1].click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.NAME, "Name")))
                                
    #                             # add_subunit_name = d.find_element(By.NAME,"Name")
    #                             # add_subunit_name.send_keys("subunit")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[2]/div/div/input")))
                                
    #                             # unit_theory_time = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[2]/div/div/input")
    #                             # unit_theory_time.send_keys("10")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[4]/div/div/input")))
                                
    #                             # unit_quiz_time = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[4]/div/div/input")
    #                             # unit_quiz_time.send_keys("20")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[6]/div/div/input")))
                                
    #                             # unit_test_time = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[6]/div/div/input")
    #                             # unit_test_time.send_keys("15")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[8]/div/div/input")))
                                
    #                             # unit_homework_time = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[8]/div/div/input")
    #                             # unit_homework_time.send_keys("25")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[10]/div/div/input")))
                                
    #                             # unit_others_time = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[10]/div/div/input")
    #                             # unit_others_time.send_keys("30")
                                
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[1]")))
                                
    #                             # cancel_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[1]")
    #                             # cancel_btn.click()
                                
    #                             # # # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[2]")))
                                
    #                             # # # save_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[2]")
    #                             # # # save_btn.click()
                                
    #                             ## ---- topic ---- 
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[2]/div[2]/button[3]")))
                                
    #                             # add_topic = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div[2]/div[2]/button[3]")
    #                             # add_topic.click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[1]/div[1]/div/div")))
                                
    #                             # select_unit_name = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[1]/div[1]/div/div")
    #                             # select_unit_name.click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
    #                             # add_unit_name_ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
    #                             # li = add_unit_name_ul.find_elements(By.TAG_NAME, "li")
    #                             # li[1].click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[1]/div[2]/div/div")))
                                
    #                             # select_subunit_name = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[1]/div[2]/div/div")
    #                             # select_subunit_name.click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
    #                             # add_unit_name_ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
    #                             # li = add_unit_name_ul.find_elements(By.TAG_NAME, "li")
    #                             # # li[0].click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.NAME, "Name")))
                                
    #                             # add_topic_name = d.find_element(By.NAME,"Name")
    #                             # add_topic_name.send_keys("topic")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[2]/div/div/input")))
                                
    #                             # unit_theory_time = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[2]/div/div/input")
    #                             # unit_theory_time.send_keys("10")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[4]/div/div/input")))
                                
    #                             # unit_quiz_time = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[4]/div/div/input")
    #                             # unit_quiz_time.send_keys("20")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[6]/div/div/input")))
                                
    #                             # unit_test_time = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[6]/div/div/input")
    #                             # unit_test_time.send_keys("15")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[8]/div/div/input")))
                                
    #                             # unit_homework_time = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[8]/div/div/input")
    #                             # unit_homework_time.send_keys("25")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[10]/div/div/input")))
                                
    #                             # unit_others_time = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[10]/div/div/input")
    #                             # unit_others_time.send_keys("30")
                                
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[1]")))
                                
    #                             # cancel_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[1]")
    #                             # cancel_btn.click()
                                
    #                             # # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[2]")))
                                
    #                             # # save_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[2]")
    #                             # # save_btn.click()
                                
                                
                                
    #                             sleep(5)
                            
    # def test_lesson_plan_edit(self):
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

    #                 with open('data/lesson_plan.csv', 'r') as f:
    #                     reader = csv.reader(f)
    #                     # Skip the two header row
    #                     next(reader)
    #                     next(reader)
                        
    #                     for row in reader:
    #                         unit_name = row[0]
    #                         unit_notes = row[1]
    #                         subunit_name = row[2]
    #                         topic = row[3]
                            
    #                         for lesson_plan_data in lesson_plan["lesson_plan_data"]:
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, lesson_plan_data["lesson_plan_module"])))
                                
    #                             lesson_plan_module = d.find_element(By.XPATH, lesson_plan_data["lesson_plan_module"])
    #                             lesson_plan_module.click()
                                    
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, lesson_plan_data["parent_div"])))
    #                             classroom_ul = d.find_element(By.XPATH, lesson_plan_data["parent_div"])
    #                             li = classroom_ul.find_elements(By.TAG_NAME,"div")
    #                             wait.until(
    #                                         EC.presence_of_element_located((By.XPATH, '//p[text()="I-A"]'))
    #                                     )
    #                             cl_li = d.find_element(By.XPATH,'//p[text()="I-A"]')
    #                             cl_li.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
    #                             table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                             table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                             table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
    #                             year_btn = table_cell[0].find_element(By.TAG_NAME, "p")

    #                             year_btn.click()                         
                                
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div")))
    #                             parent_div = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div")
    #                             child_div = parent_div.find_elements(By.TAG_NAME,"div")
    #                             ul = child_div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/ul")
    #                             li = ul.find_element(By.TAG_NAME,"li")
    #                             div = li.find_elements(By.TAG_NAME,"div")
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/ul/li/div[2]/p[1]")))
                                
    #                             inside = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/ul/li/div[2]/p[1]")
    #                             action = ActionChains(d)
    #                             action.move_to_element(inside).click().perform()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[3]/div/table/tbody/tr[1]/td[9]/button[1]")))
    #                             # edit_unit_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div[3]/div/table/tbody/tr[1]/td[9]/button[1]")
    #                             # edit_unit_btn.click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.NAME, "Name")))
                                
    #                             # add_unit_name = d.find_element(By.NAME,"Name")
    #                             # add_unit_name.click()
    #                             # add_unit_name.send_keys(Keys.CONTROL + "a")
    #                             # add_unit_name.send_keys(Keys.BACKSPACE)
    #                             # add_unit_name.send_keys("unit1")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.NAME, "Notes")))
                               
    #                             # add_unit_notes = d.find_element(By.NAME,"Notes")
    #                             # add_unit_notes.click()
    #                             # add_unit_notes.send_keys(Keys.CONTROL + "a")
    #                             # add_unit_notes.send_keys(Keys.BACKSPACE)
    #                             # add_unit_notes.send_keys("unit1 notes")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[1]")))
                                
    #                             # cancel_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[1]")
    #                             # cancel_btn.click()
                                
    #                             # # # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[2]")))
                                
    #                             # # # save_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[2]")
    #                             # # # save_btn.click()
                                
                                
    #                             ## ---- subunit ---- 
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[3]/div/table/tbody/tr[2]/td[9]/button[1]")))
                                
    #                             # edit_subunit = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div[3]/div/table/tbody/tr[2]/td[9]/button[1]")
    #                             # edit_subunit.click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.NAME, "Name")))
    #                             # add_subunit_name = d.find_element(By.NAME,"Name")
    #                             # add_subunit_name.click()
    #                             # add_subunit_name.send_keys(Keys.CONTROL + "a")
    #                             # add_subunit_name.send_keys(Keys.BACKSPACE)
                                
    #                             # add_subunit_name.send_keys("subunit")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/div[2]/div/div/input")))
                                
    #                             # unit_theory_time = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/div[2]/div/div/input")
    #                             # unit_theory_time.click()
    #                             # unit_theory_time.send_keys(Keys.CONTROL + "a")
    #                             # unit_theory_time.send_keys(Keys.BACKSPACE)
                                
    #                             # unit_theory_time.send_keys("20")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/div[4]/div/div/input")))
                                
    #                             # unit_quiz_time = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/div[4]/div/div/input")
    #                             # unit_quiz_time.click()
    #                             # unit_quiz_time.send_keys(Keys.CONTROL + "a")
    #                             # unit_quiz_time.send_keys(Keys.BACKSPACE)
    #                             # unit_quiz_time.send_keys("20")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/div[6]/div/div/input")))
                                
    #                             # unit_test_time = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/div[6]/div/div/input")
    #                             # unit_test_time.click()
    #                             # unit_test_time.send_keys(Keys.CONTROL + "a")
    #                             # unit_test_time.send_keys(Keys.BACKSPACE)
    #                             # unit_test_time.send_keys("15")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/div[8]/div/div/input")))
                                
    #                             # unit_homework_time = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/div[8]/div/div/input")
    #                             # unit_homework_time.click()
    #                             # unit_homework_time.send_keys(Keys.CONTROL + "a")
    #                             # unit_homework_time.send_keys(Keys.BACKSPACE)
    #                             # unit_homework_time.send_keys("25")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/div[10]/div/div/input")))
                                
    #                             # unit_others_time = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/div[10]/div/div/input")
    #                             # unit_others_time.click()
    #                             # unit_others_time.send_keys(Keys.CONTROL + "a")
    #                             # unit_others_time.send_keys(Keys.BACKSPACE)
    #                             # unit_others_time.send_keys("30")
                                
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/button[1]")))
                                
    #                             # cancel_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/button[1]")
    #                             # cancel_btn.click()
                                
    #                             # # # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/button[2]")))
                                
    #                             # # # save_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/button[2]")
    #                             # # # save_btn.click()
                                
    #                             ## --- topic ---
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[3]/div/table/tbody/tr[3]/td[9]/button[1]")))
                                
    #                             # edit_topic = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div[3]/div/table/tbody/tr[3]/td[9]/button[1]")
    #                             # edit_topic.click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.NAME, "Name")))
    #                             # add_subunit_name = d.find_element(By.NAME,"Name")
    #                             # add_subunit_name.click()
    #                             # add_subunit_name.send_keys(Keys.CONTROL + "a")
    #                             # add_subunit_name.send_keys(Keys.BACKSPACE)
                                
    #                             # add_subunit_name.send_keys("topic")
                                
    #                             # add_subunit_notes = d.find_element(By.NAME,"Notes")
    #                             # add_subunit_notes.click()
    #                             # add_subunit_notes.send_keys(Keys.CONTROL + "a")
    #                             # add_subunit_notes.send_keys(Keys.BACKSPACE)
                                
    #                             # add_subunit_notes.send_keys("notes")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[2]/div/div/input")))
                                
    #                             # unit_theory_time = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[2]/div/div/input")
    #                             # unit_theory_time.click()
    #                             # unit_theory_time.send_keys(Keys.CONTROL + "a")
    #                             # unit_theory_time.send_keys(Keys.BACKSPACE)
                                
    #                             # unit_theory_time.send_keys("20")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[4]/div/div/input")))
                                
    #                             # unit_quiz_time = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[4]/div/div/input")
    #                             # unit_quiz_time.click()
    #                             # unit_quiz_time.send_keys(Keys.CONTROL + "a")
    #                             # unit_quiz_time.send_keys(Keys.BACKSPACE)
    #                             # unit_quiz_time.send_keys("20")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[6]/div/div/input")))
                                
    #                             # unit_test_time = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[6]/div/div/input")
    #                             # unit_test_time.click()
    #                             # unit_test_time.send_keys(Keys.CONTROL + "a")
    #                             # unit_test_time.send_keys(Keys.BACKSPACE)
    #                             # unit_test_time.send_keys("15")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[8]/div/div/input")))
                                
    #                             # unit_homework_time = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[8]/div/div/input")
    #                             # unit_homework_time.click()
    #                             # unit_homework_time.send_keys(Keys.CONTROL + "a")
    #                             # unit_homework_time.send_keys(Keys.BACKSPACE)
    #                             # unit_homework_time.send_keys("25")
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[10]/div/div/input")))
                                
    #                             # unit_others_time = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/div[10]/div/div/input")
    #                             # unit_others_time.click()
    #                             # unit_others_time.send_keys(Keys.CONTROL + "a")
    #                             # unit_others_time.send_keys(Keys.BACKSPACE)
    #                             # unit_others_time.send_keys("30")
                                
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[1]")))
                                
    #                             # cancel_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[4]/button[1]")
    #                             # cancel_btn.click()
                                
    #                             # # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/button[2]")))
                                
    #                             # # save_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/button[2]")
    #                             # # save_btn.click()

    
    # def test_lesson_plan_delete(self):
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

    #                 with open('data/lesson_plan.csv', 'r') as f:
    #                     reader = csv.reader(f)
    #                     # Skip the two header row
    #                     next(reader)
    #                     next(reader)
                        
    #                     for row in reader:
    #                         unit_name = row[0]
    #                         unit_notes = row[1]
    #                         subunit_name = row[2]
    #                         topic = row[3]
                            
    #                         for lesson_plan_data in lesson_plan["lesson_plan_data"]:
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, lesson_plan_data["lesson_plan_module"])))
                                
    #                             lesson_plan_module = d.find_element(By.XPATH, lesson_plan_data["lesson_plan_module"])
    #                             lesson_plan_module.click()
                                    
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, lesson_plan_data["parent_div"])))
    #                             classroom_ul = d.find_element(By.XPATH, lesson_plan_data["parent_div"])
    #                             li = classroom_ul.find_elements(By.TAG_NAME,"div")
    #                             wait.until(
    #                                         EC.presence_of_element_located((By.XPATH, '//p[text()="I-A"]'))
    #                                     )
    #                             cl_li = d.find_element(By.XPATH,'//p[text()="I-A"]')
    #                             cl_li.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
    #                             table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                             table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                             table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
    #                             year_btn = table_cell[0].find_element(By.TAG_NAME, "p")

    #                             year_btn.click()                         
                                
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div")))
    #                             parent_div = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div")
    #                             child_div = parent_div.find_elements(By.TAG_NAME,"div")
    #                             ul = child_div[1].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/ul")
    #                             li = ul.find_element(By.TAG_NAME,"li")
    #                             div = li.find_elements(By.TAG_NAME,"div")
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/ul/li/div[2]/p[1]")))
                                
    #                             inside = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/ul/li/div[2]/p[1]")
    #                             action = ActionChains(d)
    #                             action.move_to_element(inside).click().perform()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[3]/div/table/tbody/tr[1]/td[9]/button[2]")))
    #                             delete_btn = d.find_element(By.XPATH,'button.MuiButtonBase-root.MuiIconButton-root.MuiIconButton-sizeLarge[aria-label="delete"]')
    #                             # delete_btn.click()
    #                             action = ActionChains(d)
    #                             action.move_to_element(delete_btn).click().perform()
                                
    #                             sleep(5)
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div/button[1]")))
    #                             cancel_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div/button[1]")
    #                             delete_button = d.find_element(By.XPATH,'//button[@class="MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeLarge css-1gzpori" and @aria-label="delete"]')

    #                             delete_button.click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div/form/div/button[2]")))
    #                             # save_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div[2]/div/form/div/button[3]")
    #                             # save_btn.click()
                                
                                
    # def test_lesson_plan_search(self):
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


                            
    #                 for lesson_plan_data in lesson_plan["lesson_plan_data"]:
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, lesson_plan_data["lesson_plan_module"])))
                        
    #                     lesson_plan_module = d.find_element(By.XPATH, lesson_plan_data["lesson_plan_module"])
    #                     lesson_plan_module.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[1]/div/div/div/input")))
                        
    #                     lesson_plan_search = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[1]/div/div/div/input")
                        
    #                     ActionChains(d).click(lesson_plan_search).perform()
    #                     for character in "b":
    #                         ActionChains(d).send_keys(character).perform()
                        
                            

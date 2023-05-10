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

class TestReports(unittest.TestCase):
    
    def setUp(self):
        # Initialize the webdriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser
        self.driver.quit()

        
    # def test_tc_report_create(self):

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
                                
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[14]")))
                        
    #                     reports_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[14]")
    #                     reports_module.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[1]/li")))
                       
    #                     tc_template = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[1]/li")
    #                     tc_template.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[1]/div/div/div")))
                       
    #                     class_standard = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[1]/div/div/div")
    #                     class_standard.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
    #                     sleep(1)
    #                     class_standard_ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                     li = class_standard_ul.find_elements(By.TAG_NAME, "li")
    #                     li[0].click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[2]/div/div/div")))
                        
    #                     academic_year = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[2]/div/div/div")
    #                     academic_year.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                       
    #                     academic_year_ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                     sleep(1)
    #                     li = academic_year_ul.find_elements(By.TAG_NAME, "li")
    #                     li[0].click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[3]/div/div/div")))
                        
    #                     student = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[3]/div/div/div")
    #                     student.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                       
    #                     student_ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                     sleep(1)
    #                     li = student_ul.find_elements(By.TAG_NAME, "li")
    #                     li[0].click()
                        
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[1]/li")))
                        
    #                     # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[1]/li")
    #                     # cancel_btn.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[4]/button[2]")))
                        
    #                     save_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div[1]/div/form/div[4]/button[2]")
    #                     save_btn.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[1]/div[1]/button")))
                        
    #                     edit_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[1]/div[1]/button")
    #                     edit_btn.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[18]/div/div/input")))
                        
    #                     class_studied = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[18]/div/div/input")
    #                     class_studied.send_keys("10th")
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[20]/div/div/input")))
                        
    #                     school = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[20]/div/div/input")
    #                     school.send_keys("campuzone school")
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[22]/div/div/input")))
                        
    #                     is_failed = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[22]/div/div/input")
    #                     is_failed.send_keys("No")
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[24]/div/div/input")))
                        
    #                     subject_studied = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[24]/div/div/input")
    #                     subject_studied.send_keys("Tamil")
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[26]/div/div/input")))
                        
    #                     is_qualified = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[26]/div/div/input")
    #                     is_qualified.send_keys("11 th standard")
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[28]/div/div/input")))
                        
    #                     total_working_days = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[28]/div/div/input")
    #                     total_working_days.send_keys("364")
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[30]/div/div/input")))
                        
    #                     total_working_days_present = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[30]/div/div/input")
    #                     total_working_days_present.send_keys("320")
                        
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[32]/div/div/input")))
                        
    #                     Ncc = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[32]/div/div/input")
    #                     Ncc.send_keys("Yes")
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[34]/div/div/input")))
                        
    #                     game_played = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[34]/div/div/input")
    #                     game_played.send_keys("cricket")
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[36]/div/div/input")))
                        
    #                     genral_conduct = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[36]/div/div/input")
    #                     genral_conduct.send_keys("No")
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[38]/div/div/input")))
                        
    #                     date_of_application = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[38]/div/div/input")
    #                     date_of_application.send_keys("12-04-2023")
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[42]/div/div/input")))
                        
    #                     reason_for_leaving = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[2]/div[2]/div/div[42]/div/div/input")
    #                     reason_for_leaving.send_keys("joining to another school")
                        
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[1]")))
                        
    #                     # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[1]")
    #                     # cancel_btn.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[2]")))
                        
    #                     save_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[2]")
    #                     save_btn.click()
                        
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[1]")))
                        
    #                     # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[1]")
    #                     # cancel_btn.click()
                        
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[2]")))
                        
    #                     # print_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[2]")
    #                     # print_btn.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[3]")))
                        
    #                     preview_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[3]")
    #                     preview_btn.click()
                        
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[4]")))
                        
    #                     # download_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[4]")
    #                     # download_btn.click()
                        
    #                     sleep(10)
                        
    # def test_conduct_certificate_create(self):
            
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
                                
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[14]")))
                        
    #                     reports_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[14]")
    #                     reports_module.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[2]/li")))
                       
    #                     conduct = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[2]/li")
    #                     conduct.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[1]/div[1]/button")))
                       
    #                     conduct_edit = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[1]/div[1]/button")
    #                     conduct_edit.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.NAME, "name")))
                       
    #                     name = d.find_element(By.NAME, "name")
    #                     name.send_keys("ellaidhurai")
                        
                        
    #                     wait.until(EC.element_to_be_clickable((By.NAME, "parentname")))
                       
    #                     name = d.find_element(By.NAME, "parentname")
    #                     name.send_keys("natraj")
                        
    #                     wait.until(EC.element_to_be_clickable((By.NAME, "house")))
                       
    #                     name = d.find_element(By.NAME, "house")
    #                     name.send_keys("234/a")
                        
    #                     wait.until(EC.element_to_be_clickable((By.NAME, "post")))
                       
    #                     name = d.find_element(By.NAME, "post")
    #                     name.send_keys("pappankulam")
                        
    #                     wait.until(EC.element_to_be_clickable((By.NAME, "year")))
                       
    #                     name = d.find_element(By.NAME, "year")
    #                     name.send_keys("2023")
                        
    #                     wait.until(EC.element_to_be_clickable((By.NAME, "character")))
                       
    #                     name = d.find_element(By.NAME, "character")
    #                     name.send_keys("good")
                        
    #                     wait.until(EC.element_to_be_clickable((By.NAME, "place")))
                       
    #                     name = d.find_element(By.NAME, "place")
    #                     name.send_keys("tiruppur")
                        
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[1]")))
                       
    #                     # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[1]")
    #                     # cancel_btn.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[2]")))
                       
    #                     save_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[2]")
    #                     save_btn.click()
  
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[1]")))
                        
    #                     # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[1]")
    #                     # cancel_btn.click()
                        
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[2]")))
                        
    #                     # print_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[2]")
    #                     # print_btn.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[3]")))
                        
    #                     preview_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[3]")
    #                     preview_btn.click()
                        
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[4]")))
                        
    #                     # download_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[4]")
    #                     # download_btn.click()
        
    #                     sleep(5)
    
    def test_bonafide_certificate_create(self):
            
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
                                
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[14]")))
                        
                        reports_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[14]")
                        reports_module.click()
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[3]/li")))
                       
                        bonofide = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[3]/li")
                        bonofide.click()
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[1]/div[1]/button")))
                       
                        bonofide_edit = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[1]/div[1]/button")
                        bonofide_edit.click()
                        
                        wait.until(EC.element_to_be_clickable((By.NAME, "name")))
                       
                        name = d.find_element(By.NAME, "name")
                        name.send_keys("ellaidhurai")
                        
                        
                        wait.until(EC.element_to_be_clickable((By.NAME, "parentname")))
                       
                        name = d.find_element(By.NAME, "parentname")
                        name.send_keys("natraj")
                        
                        wait.until(EC.element_to_be_clickable((By.NAME, "house")))
                       
                        name = d.find_element(By.NAME, "house")
                        name.send_keys("234/a")
                        
                        wait.until(EC.element_to_be_clickable((By.NAME, "post")))
                       
                        name = d.find_element(By.NAME, "post")
                        name.send_keys("pappankulam")
                        
                        wait.until(EC.element_to_be_clickable((By.NAME, "year")))
                       
                        name = d.find_element(By.NAME, "year")
                        name.send_keys("2023")
                        
                        wait.until(EC.element_to_be_clickable((By.NAME, "character")))
                       
                        name = d.find_element(By.NAME, "character")
                        name.send_keys("good")
                        
                        wait.until(EC.element_to_be_clickable((By.NAME, "place")))
                       
                        name = d.find_element(By.NAME, "place")
                        name.send_keys("tiruppur")
                        
                        # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[1]")))
                       
                        # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[1]")
                        # cancel_btn.click()
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[2]")))
                       
                        save_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[2]")
                        save_btn.click()
  
                        # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[1]")))
                        
                        # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[1]")
                        # cancel_btn.click()
                        
                        # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[2]")))
                        
                        # print_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[2]")
                        # print_btn.click()
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[3]")))
                        
                        preview_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[3]")
                        preview_btn.click()
                        
                        # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[4]")))
                        
                        # download_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[4]")
                        # download_btn.click()
        
                        sleep(5)
                        
    def test_on_duty_certificate_create(self):
            
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
                                
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[14]")))
                        
                        reports_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[14]")
                        reports_module.click()
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[4]/li")))
                       
                        on_duty = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[4]/li")
                        on_duty.click()
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[1]/div[1]/button")))
                       
                        on_duty_edit = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[1]/div[1]/button")
                        on_duty_edit.click()
                        
                        wait.until(EC.element_to_be_clickable((By.NAME, "name")))
                       
                        name = d.find_element(By.NAME, "name")
                        name.send_keys("ellaidhurai")
                        
                        
                        wait.until(EC.element_to_be_clickable((By.NAME, "parentname")))
                       
                        name = d.find_element(By.NAME, "parentname")
                        name.send_keys("natraj")
                        
                        wait.until(EC.element_to_be_clickable((By.NAME, "house")))
                       
                        name = d.find_element(By.NAME, "house")
                        name.send_keys("234/a")
                        
                        wait.until(EC.element_to_be_clickable((By.NAME, "post")))
                       
                        name = d.find_element(By.NAME, "post")
                        name.send_keys("pappankulam")
                        
                        wait.until(EC.element_to_be_clickable((By.NAME, "year")))
                       
                        name = d.find_element(By.NAME, "year")
                        name.send_keys("2023")
                        
                        wait.until(EC.element_to_be_clickable((By.NAME, "character")))
                       
                        name = d.find_element(By.NAME, "character")
                        name.send_keys("good")
                        
                        wait.until(EC.element_to_be_clickable((By.NAME, "place")))
                       
                        name = d.find_element(By.NAME, "place")
                        name.send_keys("tiruppur")
                        
                        # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[1]")))
                       
                        # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[1]")
                        # cancel_btn.click()
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[2]")))
                       
                        save_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[2]")
                        save_btn.click()
  
                        # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[1]")))
                        
                        # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[1]")
                        # cancel_btn.click()
                        
                        # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[2]")))
                        
                        # print_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[2]")
                        # print_btn.click()
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[3]")))
                        
                        preview_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[3]")
                        preview_btn.click()
                        
                        # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[4]")))
                        
                        # download_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/section/div[3]/button[4]")
                        # download_btn.click()
        
                        sleep(5)
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

class TestExams(unittest.TestCase):
    
    def setUp(self):
        # Initialize the webdriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser
        self.driver.quit()

        
    # def test_exams_add(self):

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
                                
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[12]")))
                        
    #                     exam_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[12]")
    #                     exam_module.click()
                        
    #                     exam_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[11]")
    #                     exam_module.click()
                        
    #                     exam_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[12]")
    #                     exam_module.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div")))
    #                     parent_div = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div")
    #                     child_div = parent_div.find_elements(By.TAG_NAME,"div")
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/ul")))
                        
    #                     ul = child_div[2].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/ul")
    #                     li = ul.find_element(By.TAG_NAME,"li")
    #                     li.click()
    #                     sleep(5)
    #                     wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
    #                     table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                     table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                     table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
    #                     year_btn = table_cell[0].find_element(By.TAG_NAME, "p")

    #                     year_btn.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[1]/a/button")))
    #                     add_new_exam = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[1]/a/button")
    #                     add_new_exam.click()
            

    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div[1]/div/div/input")))
    #                     ex_desc = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div[1]/div/div/input")
    #                     actions = ActionChains(d)
    #                     actions.click(ex_desc).perform()
    #                     ex_desc.clear()  # Clear any existing value in the input field
    #                     ex_desc.send_keys("new exam")
    #                     actions.move_by_offset(0, 0).click().perform()  # Remove focus from the input field

            
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div/input")))
    #                     ex_start_date = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div/input")
    #                     ex_start_date.send_keys("12-04-2023")
            
    #                     wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div/div/input")))
    #                     ex_end_date = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div/div/input")
    #                     ex_end_date.send_keys("13-04")
            
    #                     # sleep(10)
            
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div[4]/div/div/input")))
    #                     ex_desc = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div[4]/div/div/input")
    #                     ex_desc.clear()  # Clear any existing value in the input field
    #                     ex_desc.send_keys("exam_notes")
                                            
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/form/div[2]/button[1]")))
    #                     # holiday_cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/form/div[2]/button[1]")
    #                     # holiday_cancel_btn.click()
            
    #                     sleep(1)
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/form/div[2]/button[2]")))
    #                     holiday_save_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/form/div[2]/button[2]")
    #                     holiday_save_btn.click()
            


    # def test_exams_add(self):

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
                                
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[12]")))
                        
    #                     exam_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[12]")
    #                     exam_module.click()
                        
    #                     exam_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[11]")
    #                     exam_module.click()
                        
    #                     exam_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[12]")
    #                     exam_module.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div")))
    #                     parent_div = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div")
    #                     child_div = parent_div.find_elements(By.TAG_NAME,"div")
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/ul")))
                        
    #                     ul = child_div[2].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/ul")
    #                     li = ul.find_element(By.TAG_NAME,"li")
    #                     li.click()
    #                     # sleep(5)
    #                     wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
    #                     table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                     table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                     table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
    #                     year_btn = table_cell[0].find_element(By.TAG_NAME, "p")

    #                     year_btn.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
    #                     table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
    #                     table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
    #                     table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/p")))
    #                     new_btn = d.find_element(By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/p")
    #                     # new_btn = table_cell[0].find_element(By.TAG_NAME, "p")
    #                     new_btn.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/main/div[2]/div/div[3]/button')))
    #                     add_exam_btn = d.find_element(By.XPATH, '//*[@id="root"]/div[2]/main/div[2]/div/div[3]/button')
    #                     add_exam_btn.click()
                        
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="outlined-required"]')))
    #                     subject = d.find_element(By.XPATH, '//*[@id="outlined-required"]')
    #                     subject.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul')))
    #                     subject_ul = d.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul')
    #                     li = subject_ul.find_elements(By.TAG_NAME, "li")
    #                     li[1].click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.NAME, 'Date')))
    #                     date = d.find_element(By.NAME, 'Date')
    #                     date.send_keys("21")
                        
    #                     wait.until(EC.element_to_be_clickable((By.NAME, 'From_time')))
    #                     From_time = d.find_element(By.NAME, 'From_time')
    #                     From_time.click()
    #                     From_time.send_keys("04:30 PM")
                        
    #                     wait.until(EC.element_to_be_clickable((By.NAME, 'To_time')))
    #                     To_time = d.find_element(By.NAME, 'To_time')
    #                     To_time.click()
    #                     To_time.send_keys("05:30 PM")
                        
    #                     wait.until(EC.element_to_be_clickable((By.NAME, 'Max_mark')))
    #                     Max_mark = d.find_element(By.NAME, 'Max_mark')
    #                     Max_mark.send_keys("100")
                        
    #                     wait.until(EC.element_to_be_clickable((By.NAME, 'Pass_mark')))
    #                     Pass_mark = d.find_element(By.NAME, 'Pass_mark')
    #                     Pass_mark.send_keys("99")
                        
    #                     wait.until(EC.element_to_be_clickable((By.NAME, 'Notes')))
    #                     Notes = d.find_element(By.NAME, 'Notes')
    #                     Notes.send_keys("new notes")
                        
    #                     sleep(20)
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/button[1]')))
    #                     # cancel_btn = d.find_element(By.NAME, '/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/button[1]')
    #                     # cancel_btn.click()
                        
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/button[2]')))
    #                     save_btn = d.find_element(By.XPATH, '/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/button[2]')
    #                     save_btn.click()
                        
    def test_add_marks(self):

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
                                
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[12]")))
                        
                        exam_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[12]")
                        exam_module.click()
                        
                        exam_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[11]")
                        exam_module.click()
                        
                        exam_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[12]")
                        exam_module.click()
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div")))
                        parent_div = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div")
                        child_div = parent_div.find_elements(By.TAG_NAME,"div")
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/ul")))
                        
                        ul = child_div[2].find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/ul")
                        li = ul.find_element(By.TAG_NAME,"li")
                        li.click()
                        # sleep(5)
                        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
                        table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
                        table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
                        table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
                        year_btn = table_cell[0].find_element(By.TAG_NAME, "p")

                        year_btn.click()
                        
                        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")))
                        table_li = d.find_element(By.CLASS_NAME, "MuiDataGrid-virtualScrollerRenderZone")
                        table_rows = table_li.find_elements(By.CLASS_NAME, "MuiDataGrid-row")
                        table_cell = table_rows[0].find_elements(By.CLASS_NAME, "MuiDataGrid-cell--withRenderer")
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/p")))
                        desc_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/p")
                        desc_btn.click()
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/main/div[2]/div/div[4]/div/div/div[2]/div[2]/div/div/div/div/div[3]')))
                        add_marks_btn = d.find_element(By.XPATH, '//*[@id="root"]/div[2]/main/div[2]/div/div[4]/div/div/div[2]/div[2]/div/div/div/div/div[3]')
                        add_marks_btn.click()
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[1]/div/div/div/div/button[3]')))
                        edit_marks_tab = d.find_element(By.XPATH, '/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[1]/div/div/div/div/button[3]')
                        edit_marks_tab.click()
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/table/tbody/tr/td[2]/div/div')))
                        select_btn = d.find_element(By.XPATH, '/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[2]/table/tbody/tr/td[2]/div/div')
                        select_btn.click()
                        
                        sleep(1)
                        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul')))
                        present = d.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul')
                        li = present.find_elements(By.TAG_NAME, "li")
                        li[0].click()
                        
                        
                        wait.until(EC.element_to_be_clickable((By.NAME, 'Obtained_mark')))
                        Obtained_mark = d.find_element(By.NAME, 'Obtained_mark')
                        Obtained_mark.send_keys("50")
                        
                        # wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/button[1]')))
                        # cancel_btn = d.find_element(By.XPATH, '/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/button[1]')
                        # cancel_btn.click()
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/button[2]')))
                        save_btn = d.find_element(By.XPATH, '/html/body/div/div[2]/main/div[2]/div[2]/div/form/div[3]/button[2]')
                        save_btn.click()
                        
                        sleep(5)
            
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

class TestRole(unittest.TestCase):
    
    def setUp(self):
        # Initialize the webdriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser
        self.driver.quit()

        
    # def test_add_roles(self):

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
    #                     # act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
    #                     # exp_title = data["login_confirm_text"]

    #                     # self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

    #                     # invalid login check
    #                     d.find_element(By.NAME, "Username").send_keys(username)
    #                     d.find_element(By.NAME, "Password").send_keys(password)
    #                     d.find_element(By.XPATH, data["login_btn_locator"]).click()

    #                     # time.sleep(2)
    #                     # Wait for the page to load after login
    #                     wait.until(EC.url_matches(data["valid_dashboard_link"]))
    #                     # wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
    #                     # time.sleep(2)
    #                     # ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
    #                     # li_elements = ul_element.find_elements(By.TAG_NAME,"li")
    #                     # li_elements[2].click()    
                    
    #                     # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
    #                     # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                     # exp_title = data["dashboard_confirm_text"]

    #                     # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")
                        
                        
    #                     with open('data/roles.csv', 'r') as f:
    #                         # read data
    #                         reader = csv.reader(f)
    #                         # Skip the header row
    #                         next(reader)
                            
    #                         # loop all values in sheet
    #                         for row in reader:
    #                             name = row[0]
    #                             note = row[1]
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[2]")),)
    #                             role_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[2]")
    #                             role_module.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[1]/div[2]/button")),)
    #                             add_role_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[1]/div[2]/button")
    #                             add_role_btn.click()
                        
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "name")))
    #                             role_name = d.find_element(By.NAME, "name")
    #                             role_name.send_keys(name)
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Notes")))
    #                             role_notes = d.find_element(By.NAME, "Notes")
    #                             role_notes.send_keys(note)
                                
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[1]/div/form/div[3]/button[1]")),)
    #                             # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[1]/div/form/div[3]/button[1]")
    #                             # cancel_btn.click()
                            
                        
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[1]/div/form/div[3]/button[2]")),)
    #                             save_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[1]/div/form/div[3]/button[2]")
    #                             save_btn.click()
                                
    #                             sleep(5)
                                
                        
    def test_add_role_permission(self):
            
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
                        # wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
                        # # time.sleep(2)
                        # ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
                        # li_elements = ul_element.find_elements(By.TAG_NAME,"li")
                        # li_elements[2].click()    
                    
                        # wait.until(EC.url_matches(data["valid_dashboard_link"]),)
                        # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

                        # exp_title = data["dashboard_confirm_text"]

                        # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[2]")),)
                        role_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[2]")
                        role_module.click()

                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/ul")),)
                        sleep(2)
                        permission_btn_ul = d.find_element(By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div[2]/div/ul")
                        
                        li = permission_btn_ul.find_elements(By.TAG_NAME, "li")
                        btn = li[0].find_elements(By.TAG_NAME,"button")
                        btn[0].click()
                        
                        wait.until(EC.element_to_be_clickable((By.TAG_NAME, "tbody")),)
                        sleep(2)
                        Attendance = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(1) td label span:nth-child(1)")
                        Attendance[0].click() # create
                        Attendance[1].click() # update
                        Attendance[2].click() # view
                        Attendance[3].click() # delete
                        
                        Assign_Students = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(2) td label span:nth-child(1)")
                        Assign_Students[0].click() # create
                        Assign_Students[1].click() # update
                        Assign_Students[2].click() # view
                        Assign_Students[3].click() # delete
                        
                        Class_Details = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(3) td label span:nth-child(1)")
                        Class_Details[0].click() # create
                        Class_Details[1].click() # update
                        Class_Details[2].click() # view
                        Class_Details[3].click() # delete
                        
                        Class_Subjects = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(4) td label span:nth-child(1)")
                        Class_Subjects[0].click() # create
                        Class_Subjects[1].click() # update
                        Class_Subjects[2].click() # view
                        Class_Subjects[3].click() # delete
                        
                        Class_Yearly_Details = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(5) td label span:nth-child(1)")
                        Class_Yearly_Details[0].click() # create
                        Class_Yearly_Details[1].click() # update
                        Class_Yearly_Details[2].click() # view
                        Class_Yearly_Details[3].click() # delete
                        
                        File_attachments = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(6) td label span:nth-child(1)")
                        File_attachments[0].click() # create
                        File_attachments[1].click() # update
                        File_attachments[2].click() # view
                        File_attachments[3].click() # delete
                        
                        Message = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(7) td label span:nth-child(1)")
                        Message[0].click() # create
                        Message[1].click() # update
                        Message[2].click() # view
                        Message[3].click() # delete
                        
                        Message_Status = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(8) td label span:nth-child(1)")
                        Message_Status[0].click() # create
                        Message_Status[1].click() # update
                        Message_Status[2].click() # view
                        Message_Status[3].click() # delete
                        
                        Exam_Detail = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(9) td label span:nth-child(1)")
                        Exam_Detail[0].click() # create
                        Exam_Detail[1].click() # update
                        Exam_Detail[2].click() # view
                        Exam_Detail[3].click() # delete
                        
                        Exam_Reports = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(10) td label span:nth-child(1)")
                        Exam_Reports[0].click() # create
                        Exam_Reports[1].click() # update
                        Exam_Reports[2].click() # view
                        Exam_Reports[3].click() # delete
                        Exam_Reports[4].click() # approve
                        Exam_Reports[5].click() # publish
                        
                        Results = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(11) td label span:nth-child(1)")
                        Results[0].click() # create
                        Results[1].click() # update
                        Results[2].click() # view
                        Results[3].click() # delete
                        
                        Category = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(12) td label span:nth-child(1)")
                        Category[0].click() # create
                        Category[1].click() # update
                        Category[2].click() # view
                        Category[3].click() # delete
                        
                        Components = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(13) td label span:nth-child(1)")
                        Components[0].click() # create
                        Components[1].click() # update
                        Components[2].click() # view
                        Components[3].click() # delete
                        
                        Fickle_User = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(14) td label span:nth-child(1)")
                        Fickle_User[0].click() # create
                        Fickle_User[1].click() # update
                        Fickle_User[2].click() # view
                        Fickle_User[3].click() # delete
                        
                        File_Uploads = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(15) td label span:nth-child(1)")
                        File_Uploads[0].click() # create
                        File_Uploads[1].click() # update
                        File_Uploads[2].click() # view
                        File_Uploads[3].click() # delete
                        
                        Forms = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(16) td label span:nth-child(1)")
                        Forms[0].click() # create
                        Forms[1].click() # update
                        Forms[2].click() # view
                        Forms[3].click() # delete
                        
                        Role = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(17) td label span:nth-child(1)")
                        Role[0].click() # create
                        Role[1].click() # update
                        Role[2].click() # view
                        Role[3].click() # delete
                        
                        Organization = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(18) td label span:nth-child(1)")
                        Organization[0].click() # create
                        Organization[1].click() # update
                        Organization[2].click() # view
                        Organization[3].click() # delete
                        
                        Page_Details = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(19) td label span:nth-child(1)")
                        Page_Details[0].click() # create
                        Page_Details[1].click() # update
                        Page_Details[2].click() # view
                        Page_Details[3].click() # delete
                        
                        Pages = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(20) td label span:nth-child(1)")
                        Pages[0].click() # create
                        Pages[1].click() # update
                        Pages[2].click() # view
                        Pages[3].click() # delete
                        
                        Sections = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(21) td label span:nth-child(1)")
                        Sections[0].click() # create
                        Sections[1].click() # update
                        Sections[2].click() # view
                        Sections[3].click() # delete
                        
                        Website_Data = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(22) td label span:nth-child(1)")
                        Website_Data[0].click() # create
                        Website_Data[1].click() # update
                        Website_Data[2].click() # view
                        Website_Data[3].click() # delete
                        
                        Contestants = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(23) td label span:nth-child(1)")
                        Contestants[0].click() # create
                        Contestants[1].click() # update
                        Contestants[2].click() # view
                        Contestants[3].click() # delete
                        
                        Contest_Page_Details = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(24) td label span:nth-child(1)")
                        Contest_Page_Details[0].click() # create
                        Contest_Page_Details[1].click() # update
                        Contest_Page_Details[2].click() # view
                        Contest_Page_Details[3].click() # delete
                        
                        Contest_Pages = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(25) td label span:nth-child(1)")
                        Contest_Pages[0].click() # create
                        Contest_Pages[1].click() # update
                        Contest_Pages[2].click() # view
                        Contest_Pages[3].click() # delete
                        
                        New_Contestants = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(26) td label span:nth-child(1)")
                        New_Contestants[0].click() # create
                        New_Contestants[1].click() # update
                        New_Contestants[2].click() # view
                        New_Contestants[3].click() # delete
                        
                        Lesson_Plan = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(27) td label span:nth-child(1)")
                        Lesson_Plan[0].click() # create
                        Lesson_Plan[1].click() # update
                        Lesson_Plan[2].click() # view
                        Lesson_Plan[3].click() # delete
                        
                        Records = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(28) td label span:nth-child(1)")
                        Records[0].click() # create
                        Records[1].click() # update
                        Records[2].click() # view
                        Records[3].click() # delete
                        
                        Events = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(29) td label span:nth-child(1)")
                        Events[0].click() # create
                        Events[1].click() # update
                        Events[2].click() # view
                        Events[3].click() # delete
                        
                        News = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(30) td label span:nth-child(1)")
                        News[0].click() # create
                        News[1].click() # update
                        News[2].click() # view
                        News[3].click() # delete
                        
                        News_Attachments = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(31) td label span:nth-child(1)")
                        News_Attachments[0].click() # create
                        News_Attachments[1].click() # update
                        News_Attachments[2].click() # view
                        News_Attachments[3].click() # delete
                        
                        Templates = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(32) td label span:nth-child(1)")
                        Templates[0].click() # create
                        Templates[1].click() # update
                        Templates[2].click() # view
                        Templates[3].click() # delete
                        
                        User_Template = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(33) td label span:nth-child(1)")
                        User_Template[0].click() # create
                        User_Template[1].click() # update
                        User_Template[2].click() # view
                        User_Template[3].click() # delete
                        
                        Academic_Year = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(34) td label span:nth-child(1)")
                        Academic_Year[0].click() # create
                        Academic_Year[1].click() # update
                        Academic_Year[2].click() # view
                        Academic_Year[3].click() # delete
                        
                        Calendar_Model = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(35) td label span:nth-child(1)")
                        Calendar_Model[0].click() # create
                        Calendar_Model[1].click() # update
                        Calendar_Model[2].click() # view
                        Calendar_Model[3].click() # delete
                        # Calendar_Model[4].click() # approve
                        # Calendar_Model[5].click() # publish
                        
                        Class_Group = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(36) td label span:nth-child(1)")
                        Class_Group[0].click() # create
                        Class_Group[1].click() # update
                        Class_Group[2].click() # view
                        Class_Group[3].click() # delete
                        
                        Culture_Events = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(37) td label span:nth-child(1)")
                        Culture_Events[0].click() # create
                        Culture_Events[1].click() # update
                        Culture_Events[2].click() # view
                        Culture_Events[3].click() # delete
                        
                        Exam_Schedule = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(38) td label span:nth-child(1)")
                        Exam_Schedule[0].click() # create
                        Exam_Schedule[1].click() # update
                        Exam_Schedule[2].click() # view
                        Exam_Schedule[3].click() # delete
                        
                        Government_Holiday = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(39) td label span:nth-child(1)")
                        Government_Holiday[0].click() # create
                        Government_Holiday[1].click() # update
                        Government_Holiday[2].click() # view
                        Government_Holiday[3].click() # delete
                        
                        Holidays = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(40) td label span:nth-child(1)")
                        Holidays[0].click() # create
                        Holidays[1].click() # update
                        Holidays[2].click() # view
                        Holidays[3].click() # delete
                        
                        Slots = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(41) td label span:nth-child(1)")
                        Slots[0].click() # create
                        Slots[1].click() # update
                        Slots[2].click() # view
                        Slots[3].click() # delete
                        
                        Terms = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(42) td label span:nth-child(1)")
                        Terms[0].click() # create
                        Terms[1].click() # update
                        Terms[2].click() # view
                        Terms[3].click() # delete
                        
                        Working_Hours = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(43) td label span:nth-child(1)")
                        Working_Hours[0].click() # create
                        Working_Hours[1].click() # update
                        Working_Hours[2].click() # view
                        Working_Hours[3].click() # delete
                        
                        Departments = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(44) td label span:nth-child(1)")
                        Departments[0].click() # create
                        Departments[1].click() # update
                        Departments[2].click() # view
                        Departments[3].click() # delete
                        
                        Email_Otp = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(45) td label span:nth-child(1)")
                        Email_Otp[0].click() # create
                        Email_Otp[1].click() # update
                        Email_Otp[2].click() # view
                        Email_Otp[3].click() # delete
                        
                        Invoice_Details = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(46) td label span:nth-child(1)")
                        Invoice_Details[0].click() # create
                        Invoice_Details[1].click() # update
                        Invoice_Details[2].click() # view
                        Invoice_Details[3].click() # delete
                        
                        Mobile_Otp = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(47) td label span:nth-child(1)")
                        Mobile_Otp[0].click() # create
                        Mobile_Otp[1].click() # update
                        Mobile_Otp[2].click() # view
                        Mobile_Otp[3].click() # delete
                        
                        Offer_Details = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(48) td label span:nth-child(1)")
                        Offer_Details[0].click() # create
                        Offer_Details[1].click() # update
                        Offer_Details[2].click() # view
                        Offer_Details[3].click() # delete
                        
                        Otp = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(49) td label span:nth-child(1)")
                        Otp[0].click() # create
                        Otp[1].click() # update
                        Otp[2].click() # view
                        Otp[3].click() # delete
                        
                        Package_Tools = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(50) td label span:nth-child(1)")
                        Package_Tools[0].click() # create
                        Package_Tools[1].click() # update
                        Package_Tools[2].click() # view
                        Package_Tools[3].click() # delete
                        
                        Packages = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(51) td label span:nth-child(1)")
                        Packages[0].click() # create
                        Packages[1].click() # update
                        Packages[2].click() # view
                        Packages[3].click() # delete
                        
                        Standard = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(52) td label span:nth-child(1)")
                        Standard[0].click() # create
                        Standard[1].click() # update
                        Standard[2].click() # view
                        Standard[3].click() # delete
                        
                        Subjects = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(53) td label span:nth-child(1)")
                        Subjects[0].click() # create
                        Subjects[1].click() # update
                        Subjects[2].click() # view
                        Subjects[3].click() # delete
                        
                        Subscription = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(54) td label span:nth-child(1)")
                        Subscription[0].click() # ceate
                        Subscription[1].click() # update
                        Subscription[2].click() # view
                        Subscription[3].click() # delete
                        
                        Staff_Profile = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(55) td label span:nth-child(1)")
                        Staff_Profile[0].click() # create
                        Staff_Profile[1].click() # update
                        Staff_Profile[2].click() # view
                        Staff_Profile[3].click() # delete
                        
                        Parent_Profile = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(56) td label span:nth-child(1)")
                        Parent_Profile[0].click() # create
                        Parent_Profile[1].click() # update
                        Parent_Profile[2].click() # view
                        Parent_Profile[3].click() # delete
                        
                        Student_Profile = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(57) td label span:nth-child(1)")
                        Student_Profile[0].click() # create
                        Student_Profile[1].click() # update
                        Student_Profile[2].click() # view
                        Student_Profile[3].click() # delete
                        
                        Timetable = d.find_elements(By.CSS_SELECTOR, "tbody tr:nth-child(58) td label span:nth-child(1)")
                        Timetable[0].click() # create
                        Timetable[1].click() # update
                        Timetable[2].click() # view
                        Timetable[3].click() # delete
                        
                        # wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[1]/div/div[4]/button[1]")))
                        # cancel_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[1]/div/div[4]/button[1]")
                        # cancel_btn.click()
                        
                        wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[1]/div/div[4]/button[2]")))
                        save_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[1]/div/div[4]/button[2]")
                        save_btn.click()
                        
                        sleep(2)
    
    
    # def test_delete_role(self):
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

    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[2]")),)
    #                     role_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[2]")
    #                     role_module.click()

    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/ul")),)
    #                     sleep(2)
    #                     role_list = d.find_element(By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div[2]/div/ul")
                        
    #                     li = role_list.find_elements(By.TAG_NAME, "li")
    #                     delete_btn = li[1].find_elements(By.TAG_NAME,"button")
    #                     delete_btn[1].click()

    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[1]/div/form/div/button[1]")),)
    #                     cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[1]/div/form/div/button[1]")
    #                     cancel_btn.click()
                        
    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[1]/div/form/div/button[2]")),)
    #                     # confirm_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[1]/div/form/div/button[2]")
    #                     # confirm_btn.click()

    # def test_edit_role(self):
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

    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[2]")),)
    #                     role_module = d.find_element(By.XPATH, "/html/body/div/div[2]/div/div/ul/div/ul/li[2]")
    #                     role_module.click()

    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/ul")),)
    #                     sleep(2)
    #                     role_list = d.find_element(By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div[2]/div/ul")
                        
    #                     li = role_list.find_elements(By.TAG_NAME, "li")
    #                     edit_btn = li[1].find_elements(By.TAG_NAME,"button")
    #                     edit_btn[2].click()
                        
                        
    #                     wait.until(EC.element_to_be_clickable((By.NAME, "name")),)
    #                     name = d.find_element(By.NAME, "name")
    #                     name.send_keys(Keys.CONTROL + "a")
    #                     name.send_keys(Keys.BACK_SPACE)
    #                     name.send_keys("staff2")
                        
    #                     wait.until(EC.element_to_be_clickable((By.NAME, "Notes")),)
    #                     notes = d.find_element(By.NAME, "Notes")
    #                     notes.send_keys(Keys.CONTROL + "a")
    #                     notes.send_keys(Keys.BACK_SPACE)
    #                     notes.send_keys("staff note added2")
                        

    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[1]/div/form/div[3]/button[1]")),)
    #                     # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[1]/div/form/div[3]/button[1]")
    #                     # cancel_btn.click()
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[1]/div/form/div[3]/button[2]")),)
    #                     sleep(2)
    #                     confirm_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div[1]/div/form/div[3]/button[2]")
    #                     confirm_btn.click()

    #                     sleep(5)
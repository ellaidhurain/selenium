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
import pdb
from time import sleep
import logging
from selenium.common.exceptions import TimeoutException



# # Read the JSON file
with open('config/login_data.json') as f:
    login = json.load(f)

with open('config/staffs.json') as f:
    staffs = json.load(f)

class TestStaffs(unittest.TestCase):

    def setUp(self):
        # Initialize the webdriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser
        self.driver.quit()
        
    def test_add_staff(self):
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

                    with open('data/staffs.csv', 'r') as f:
                        reader = csv.reader(f)
                        # Skip the two header row
                        next(reader)
                        next(reader)
                        for row in reader:
                            s_first_name = row[0]
                            s_middle_name = row[1]
                            s_last_name = row[2]
                            s_staff_id = row[3]
                            s_aadhaar_no = row[4]
                            s_skills = row[5]
                            s_hobbies = row[6]
                            s_awards = row[7]
                            s_recognitions = row[8]
                            s_email = row[9]
                            s_mobile_no = row[10]
                            s_alt_mob = row[11]
                            s_nationality = row[12]
                            s_religion = row[13]
                            s_community = row[14]
                            s_scar = row[15]
                            s_mole = row[16]
                            s_medical_history = row[17]
                            s_temp_address = row[18]
                            s_temp_city = row[19]
                            s_temp_state = row[20]
                            s_temp_pincode = row[21]
                            s_perm_address = row[22]
                            s_perm_city = row[23]
                            s_perm_state = row[24]
                            s_perm_pincode = row[25]
                            
                            for staff_data in staffs["staff_data"]:
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, staff_data["staff_module"])))
                                
                                staff_module = d.find_element(By.XPATH, staff_data["staff_module"])
                                staff_module.click()

                                wait.until(EC.element_to_be_clickable((By.XPATH, staff_data["add_new_staff"])))
                                
                                add_new_staff = d.find_element(By.XPATH, staff_data["add_new_staff"])
                                add_new_staff.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, staff_data["first_name_input"])))
                                # sleep(5)
                                
                                first_name = d.find_element(By.XPATH, staff_data["first_name_input"])
                                first_name.send_keys(s_first_name)
                                # sleep(5)
                                wait.until(EC.element_to_be_clickable((By.XPATH, staff_data["middle_name_input"])))
                                
                                middle_name = d.find_element(By.XPATH, staff_data["middle_name_input"])
                                middle_name.send_keys(s_middle_name)
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, staff_data["last_name_input"])))
                                
                                last_name = d.find_element(By.XPATH, staff_data["last_name_input"])
                                last_name.send_keys(s_last_name)
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, staff_data["staff_id_input"])))
                                
                                staff_id = d.find_element(By.XPATH, staff_data["staff_id_input"])
                                staff_id.send_keys(s_staff_id)
                                
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, staff_data["date_of_birth"])))
                                
                                date_of_birth = d.find_element(By.XPATH, staff_data["date_of_birth"])
                                date_of_birth.send_keys("12-03-2010")
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, staff_data["select_gender"])))
                                
                                select_gender =  d.find_element(By.XPATH, staff_data["select_gender"])
                                select_gender.click()
                                
                                wait.until(EC.element_to_be_clickable((d.find_element(By.XPATH, staff_data["gender_ul"])))) 
                                gender_ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
                                li = gender_ul.find_elements(By.TAG_NAME, "li")[1]
                                actions = ActionChains(d)
                                actions.click(li).perform()
                                
                                wait.until(EC.element_to_be_clickable((d.find_element(By.XPATH,staff_data["martial_status"])))) 
                                maritial_status =  d.find_element(By.XPATH, staff_data["martial_status"])
                                actions = ActionChains(d)
                                actions.click(maritial_status).perform()
                                                                
                                
                                
                                wait.until(EC.element_to_be_clickable((d.find_element(By.XPATH, staff_data["martial_ul"])))) 
                                martial_ul = d.find_element(By.XPATH, staff_data["martial_ul"])
                                li = martial_ul.find_elements(By.TAG_NAME, "li")[1]
                                
                                actions = ActionChains(d)
                                actions.click(li).perform()
                                

                                wait.until(EC.element_to_be_clickable((d.find_element(By.NAME, "Aadhaar_no")))) 
                                aadhaar_no = d.find_element(By.NAME,"Aadhaar_no")
                                aadhaar_no.send_keys(s_aadhaar_no)
                                
                                
                                skills = d.find_element(By.NAME, "Skills")
                                skills.send_keys(s_skills)
                                
                                
                                hobbies_input = d.find_element(By.NAME, "Hobbies")
                                hobbies_input.send_keys(s_hobbies)
                               
                                
                                awards_input = d.find_element(By.NAME, "Awards")
                                awards_input.send_keys(s_awards)
                                
                                recognitions_input = d.find_element(By.NAME, "Recognitions")
                                recognitions_input.send_keys(s_recognitions)
                                # sleep(5)
                                email_input = d.find_element(By.NAME, "Mail_id")
                                email_input.send_keys(s_email)
                                
                                mobile_number_input = d.find_element(By.NAME, "Mobile_no")
                                mobile_number_input.send_keys(s_mobile_no)
                                
                                alternative_number_input = d.find_element(By.NAME, "Alt_mob_no")
                                alternative_number_input.send_keys(s_alt_mob)
                                
                                nationality_input = d.find_element(By.NAME , "Nationality")
                                nationality_input.send_keys(s_nationality)
                                
                                religion_input = d.find_element(By.NAME, "Religion")
                                religion_input.send_keys(s_religion)
                                
                                caste_input = d.find_element(By.XPATH, staff_data["caste_input"])
                                caste_input.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["caste_ul"])))
                                caste_ul = d.find_element(By.XPATH, staff_data["caste_ul"])
                                li = caste_ul.find_elements(By.TAG_NAME, "li")
                                li[0].click()
                                
                                wait.until(EC.element_to_be_clickable((By.NAME,"Community")))
                                community_ul = d.find_element(By.NAME,"Community")
                                community_ul.send_keys(s_community)
                                
                                scar_input = d.find_element(By.NAME, "Scar")
                                scar_input.send_keys(s_scar)
                                
                                mole_input = d.find_element(By.NAME, "Mole")
                                mole_input.send_keys(s_mole)
                                
                                blood_group_input = d.find_element(By.XPATH, staff_data["blood_group_input"])
                                blood_group_input.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["blood_group_ul"])))
                                
                                blood_group_ul = d.find_element(By.XPATH, staff_data["blood_group_ul"])
                                li = blood_group_ul.find_elements(By.TAG_NAME,"li")
                                li[0].click()
                                
                                wait.until(EC.element_to_be_clickable((By.NAME,"Medical_history")))
                                
                                medical_history = d.find_element(By.NAME,"Medical_history")
                                medical_history.send_keys(s_medical_history)
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["language_known_input"])))
                                sleep(2)
                                language_known_input = d.find_element(By.XPATH, staff_data["language_known_input"])
                                language_known_input.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["language_known_input_ul"])))
                                
                                language_known_input_ul = d.find_element(By.XPATH, staff_data["language_known_input_ul"])
                                li = language_known_input_ul.find_elements(By.TAG_NAME,"li" )
                                li[0].click()
                                                                
                                language_known_input_ul.send_keys(Keys.ESCAPE)
                                sleep(2)
                                wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["mother_tongue_input"])))
                                
                                mother_tongue_input = d.find_element(By.XPATH, staff_data["mother_tongue_input"])
                                mother_tongue_input.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["mother_tongue_input_ul"])))
                                mother_tongue_input_ul = d.find_element(By.XPATH, staff_data["mother_tongue_input_ul"])
                                li = mother_tongue_input_ul.find_elements(By.TAG_NAME,"li" )
                                li[0].click()
                                
                                sleep(1)
                                wait.until(EC.element_to_be_clickable((By.NAME, "Address")))
                                
                                temp_address_input = d.find_element(By.NAME, "Address")
                                ActionChains(d).click(temp_address_input).perform()
                                for character in s_temp_address:
                                    ActionChains(d).send_keys(character).perform()
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "City")))
                                
                                t_city_input = d.find_element(By.NAME, "City")
                                ActionChains(d).click(t_city_input).perform()
                                for character in s_temp_city:
                                    ActionChains(d).send_keys(character).perform()
                                
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "State")))
                                
                                t_state_input = d.find_element(By.NAME, "State")
                                ActionChains(d).click(t_state_input).perform()
                                for character in s_temp_state:
                                    ActionChains(d).send_keys(character).perform()
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "Pincode")))
                                t_pincode_input = d.find_element(By.NAME, "Pincode")
                                ActionChains(d).click(t_pincode_input).perform()
                                for character in s_temp_pincode:
                                    ActionChains(d).send_keys(character).perform()
                               
                                # same_as_temp_checkbox = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[2]/div[2]/label/span[1]/input")
                                # same_as_temp_checkbox.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[3]/div/div[1]/div/div/input")))
                                
                                temp_address_input = d.find_element(By.XPATH , "/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[3]/div/div[1]/div/div/input")
                                ActionChains(d).click(temp_address_input).perform()
                                for character in s_perm_address:
                                    ActionChains(d).send_keys(character).perform()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[1]/div/div/div[2]/div/div/input")))
                                
                                t_city_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[3]/div/div[2]/div/div/input")
                                ActionChains(d).click(t_city_input).perform()
                                for character in s_perm_city:
                                    ActionChains(d).send_keys(character).perform()
                                
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[3]/div/div[3]/div/div/input")))
                                
                                t_state_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[3]/div/div[3]/div/div/input")
                                ActionChains(d).click(t_state_input).perform()
                                for character in s_perm_state:
                                    ActionChains(d).send_keys(character).perform()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[3]/div/div[4]/div/div/input")))
                                t_pincode_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[3]/div/div[4]/div/div/input")
                                ActionChains(d).click(t_pincode_input).perform()
                                for character in s_perm_pincode:
                                    ActionChains(d).send_keys(character).perform()
                                
                                                                # wait for the Next button to become clickable
                                next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Next')]")))
                                # click the Next button
                                next_button.click()
                                
                                # # Wait for the "back" button element to be clickable
                                # # back_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'back')]")))
                                # # # Click the "back" button
                                # # back_button.click()

                                # # # Wait for the "cancel" button element to be clickable
                                # # cancel_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'cancel')]")))
                                # # # Click the "cancel" button
                                # # cancel_button.click()

                                
                                # # # Find the "Next" button and click it
                                # # try:
                                # #     next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(., 'Next')]')))
                                # #     next_button.click()
                                # # except TimeoutException:
                                # #     logging.error('Timed out waiting for Next button to become clickable')
                                # # except Exception as e:
                                # #     logging.error('Encountered an error while clicking Next button: {}'.format(str(e)))
                                # # else:
                                # #     logging.info('Successfully clicked Next button')
                                
                                
                                # ---- job details ----
                               
                                # get all the buttons in the tabbed menu
                                wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"MuiTab-root")))

                                # tabs = d.find_elements(By.CLASS_NAME,"MuiTab-root")

                                # job_tab = tabs[1].click()
                                                            

                                # ---- job details ----
                                with open('data/staffs2.csv', 'r') as f:
                                    reader = csv.reader(f)
                                    # Skip the two header row
                                    next(reader)
                                    # next(reader)
                                    for row in reader:
                                        j_designation = row[0]
                                        j_description = row[1]
                                        j_bank_name = row[2]
                                        j_branch_name = row[3]
                                        j_account_number = row[4]
                                        j_ifsc_code = row[5]
                                        j_pan_number = row[6]
                                        e_college = row[7]
                                        e_course = row[8]
                                        e_collge_specialization = row[9]
                                        e_school = row[10]
                                        e_school_specialization = row[11]
                                        e_percentage = row[12]
                                        e_cgpa = row[13]
                                        e_total_marks = row[14]
                                        e_gained_marks = row[15]
                                        w_designation = row[16]
                                        w_name_of_institution = row[17]
                                        w_location = row[18]
                                        w_notes = row[19]
                                      
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME,"Designation")))
                                        
                                        designation = d.find_element(By.NAME,"Designation")
                                        designation.clear()
                                        designation.send_keys(j_designation)

                                        wait.until(EC.element_to_be_clickable((By.NAME,"Date_of_joining")))
                                
                                        date_of_joining = d.find_element(By.NAME,"Date_of_joining")
                                        date_of_joining.send_keys("04-01-2023")

                                        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="demo-multiple-name"]')))
                                
                                        department = d.find_element(By.XPATH,'//*[@id="demo-multiple-name"]')
                                        department.click()
                                        
                                        wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[3]/ul")))
                                
                                        ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
                                        li = ul.find_elements(By.TAG_NAME, "li")
                                        li[0].click()
                                        ul.send_keys(Keys.ESCAPE)
                                        
                                        wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["role_group_input"])))
                                
                                        role_group = d.find_element(By.XPATH,staff_data["role_group_input"])
                                        role_group.click()
                                        
                                        wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[3]/ul")))
                                
                                        ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
                                        li = ul.find_elements(By.TAG_NAME, "li")
                                        li[0].click()
                                
                                        wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["status_input"])))
                                        
                                        status = d.find_element(By.XPATH,staff_data["status_input"])
                                        status.click()
                                        
                                        wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[3]/ul")))
                                
                                        ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
                                        li = ul.find_elements(By.TAG_NAME, "li")
                                        li[0].click()
                                        
                                        wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["choose_calendar_input"])))
                                
                                        
                                        choose_calendar = d.find_element(By.XPATH,staff_data["choose_calendar_input"])
                                        choose_calendar.click()

                                        wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[3]/ul")))
                                
                                        ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
                                        li = ul.find_elements(By.TAG_NAME, "li")
                                        li[0].click()
                                        
                                        wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["nature_of_appoinment_input"])))
                                
                                        
                                        nature_of_appoinment = d.find_element(By.XPATH,staff_data["nature_of_appoinment_input"])
                                        nature_of_appoinment.click()
                                        
                                        wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[3]/ul")))
                                
                                        ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
                                        li = ul.find_elements(By.TAG_NAME, "li")
                                        li[0].click()
                                        
                                       
                                        wait.until(EC.element_to_be_clickable((By.NAME,"Description")))
                                
                                        department = d.find_element(By.NAME,"Description")
                                        department.send_keys(j_description)
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME,"Bank_name")))
                                
                                        department = d.find_element(By.NAME,"Bank_name")
                                        department.send_keys(j_bank_name)                                        
                                        
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME,"Branch_name")))
                                
                                        department = d.find_element(By.NAME,"Branch_name")
                                        department.send_keys(j_branch_name)
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME,"Account_no")))
                                
                                        department = d.find_element(By.NAME,"Account_no")
                                        department.send_keys(j_account_number)
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME,"Ifsc_code")))
                                
                                        department = d.find_element(By.NAME,"Ifsc_code")
                                        department.send_keys(j_ifsc_code)
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME,"Pan_no")))
                                
                                        department = d.find_element(By.NAME,"Pan_no")
                                        department.send_keys(j_pan_number)
                                        
                                        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Next')]")))
                                        # click the Next button
                                        next_button.click()
                                        
                                    
                                        # back_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'back')]")))
                                        # # Click the "back" button
                                        # back_button.click()
                                        
                                        
                                        # ---- educational details ---
                                        # tabs = d.find_elements(By.CLASS_NAME,"MuiTab-root")

                                        # educational_tab = tabs[2].click()
                                        
                                        add_new_education = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div/div[2]/div/div/div/div/div/button")
                                        add_new_education.click()
                                        
                                        wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["degree_input"])))
                                
                                        degree = d.find_element(By.XPATH,staff_data["degree_input"])
                                        degree.click()
                                        
                                        wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[3]/ul")))
                                
                                        ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
                                        li = ul.find_elements(By.TAG_NAME, "li")
                                        li[2].click()
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME,"College")))
                                
                                        college = d.find_element(By.NAME,"College")
                                        college.send_keys(e_college)
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME,"Course_name")))
                                
                                        course = d.find_element(By.NAME,"Course_name")
                                        course.send_keys(e_course)
                                        
                                        medium = d.find_element(By.XPATH,staff_data["medium_dd"])
                                        medium.click()
                                        
                                        wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[3]/ul")))
                                
                                        ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
                                        li = ul.find_elements(By.TAG_NAME, "li")
                                        li[0].click()
                                        
                                        wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["e_specialization"])))
                                
                                        specialization = d.find_element(By.XPATH,staff_data["e_specialization"])
                                        specialization.send_keys(e_collge_specialization)
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME,"year_of_passing")))
                                
                                        year_of_passing = d.find_element(By.NAME,"year_of_passing")
                                        year_of_passing.send_keys("01-04-2023")
                                        
                                        marks_type = d.find_element(By.XPATH,staff_data["marks_type"])
                                        marks_type.click()
                                        
                                        wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[3]/ul")))
                                
                                        ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
                                        li = ul.find_elements(By.TAG_NAME, "li")
                                        li[1].click()
                                        
                                        wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["percentage_input"])))
                                
                                        percentage = d.find_element(By.NAME,"percentage")
                                        percentage.send_keys("80")
                                        
                                        # sleep(5)
                                        # delete_icon = d.find_element(By.XPATH,"//svg[@data-testid='DeleteIcon']")
                                        
                                        # action = ActionChains(d)
                                        # action.move_to_element(delete_icon).click().perform()
                                        # wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div/div[2]/div/div/div/div/div[2]/button")))
                                
                                        # add_new_education_bottom = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div/div[2]/div/div/div/div/div[2]/button")
                                        # add_new_education_bottom.click()      
                                        
                                        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Next')]")))
                                        # click the Next button
                                        next_button.click()  
                                        
                                        # tabs = d.find_elements(By.CLASS_NAME,"MuiTab-root")

                                        # experiance_tab = tabs[3].click()      
                                        
                                        add_new_experiance = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div/div[2]/div/div/div/div/div/button")
                                        add_new_experiance.click()    
                                        
                                        
                                        wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["w_designation_input"])))
                                
                                        percentage = d.find_element(By.NAME,"Designation")
                                        percentage.send_keys(w_designation)
                                        
                                        
                                        wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["w_name_of_institution"])))
                                
                                        percentage = d.find_element(By.NAME,"Name_of_Institution")
                                        percentage.send_keys(w_name_of_institution)
                                                   
                                        
                                        wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["w_location_input"])))
                                
                                        percentage = d.find_element(By.NAME,"Location")
                                        percentage.send_keys(w_location)
                                                   
                                        
                                        marks_type = d.find_element(By.XPATH,staff_data["w_experience_from"])
                                        marks_type.send_keys("06-04-2023")
                                                                                
                                        marks_type = d.find_element(By.XPATH,staff_data["w_experience_to"])
                                        marks_type.send_keys("07")

                                        wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["w_notes"])))
                                
                                        percentage = d.find_element(By.NAME,"Notes")
                                        percentage.send_keys(w_notes)
                                        
                                        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Next')]")))
                                        # click the Next button
                                        next_button.click()  
                                        
                                                                                
                                        with open('data/staffs3.csv', 'r') as f:
                                            reader = csv.reader(f)
                                            # Skip the two header row
                                            next(reader)
                                            # next(reader)
                                            for row in reader:
                                                
                                                father_name = row[0]
                                                father_occupation = row[1]
                                                father_email = row[2]
                                                father_phone = row[3]
                                                
                                                mother_name = row[4]
                                                mother_occupation = row[5]
                                                mother_email = row[6]
                                                mother_phone = row[7]
                                                
                                                guardian_name = row[8]
                                                guardian_occupation = row[9]
                                                guardian_email = row[10]
                                                guardian_phone = row[11]
                                                guardian_relation = row[12]
                                        
                                                # tabs = d.find_elements(By.CLASS_NAME,"MuiTab-root")

                                                # family_tab = tabs[4].click()      
                                                
                                                
                                                wait.until(EC.element_to_be_clickable((By.NAME,"Father_name")))
                                        
                                                f_father_name = d.find_element(By.NAME,"Father_name")
                                                f_father_name.send_keys(father_name)
                                                
                                                f_father_occupation = d.find_element(By.NAME,"Father_occupation")
                                                f_father_occupation.send_keys(father_occupation)
                                                
                                                f_father_email = d.find_element(By.NAME,"Father_email")
                                                f_father_email.send_keys(father_email)
                                                
                                                f_father_phone = d.find_element(By.NAME,"Father_Phone")
                                                f_father_phone.send_keys(father_phone)
                                                
                                                f_mother_name = d.find_element(By.NAME,"Mother_name")
                                                f_mother_name.send_keys(mother_name)
                                                
                                                f_mother_occupation = d.find_element(By.NAME,"Mother_occupation")
                                                f_mother_occupation.send_keys(mother_occupation)
                                                
                                                f_mother_email = d.find_element(By.NAME,"Mother_email")
                                                f_mother_email.send_keys(mother_email)
                                                
                                                f_mother_phone = d.find_element(By.NAME,"Mother_Phone")
                                                f_mother_phone.send_keys(mother_phone)
                                                
                                                f_guardian_checkbox = d.find_element(By.NAME,"Guardian_info")
                                                f_guardian_checkbox.click()
                                                
                                                wait.until(EC.element_to_be_clickable((By.NAME,"Guardian_name")))
                                                
                                                f_guardian_name = d.find_element(By.NAME,"Guardian_name")
                                                f_guardian_name.send_keys(guardian_name)
                                                
                                                f_guardian_occupation = d.find_element(By.NAME,"Gaurdian_occupation")
                                                f_guardian_occupation.send_keys(guardian_occupation)
                                                
                                                f_guardian_email = d.find_element(By.NAME,"Guardian_email")
                                                f_guardian_email.send_keys(guardian_email)
                                                
                                                f_guardian_phone = d.find_element(By.NAME,"Guardian_Phone")
                                                f_guardian_phone.send_keys(guardian_phone)
                                                
                                                f_guardian_relation = d.find_element(By.NAME,"Guardian_relation")
                                                f_guardian_relation.send_keys(guardian_relation)
                                                
                                                save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Save')]")))
                                                # click the Next button
                                                save_button.click()  
                                                        
                                                                                        
                                                sleep(2000)

    # def test_update_staff(self):
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

    #                 with open('data/staffs.csv', 'r') as f:
    #                     reader = csv.reader(f)
    #                     # Skip the two header row
    #                     next(reader)
    #                     next(reader)
    #                     for row in reader:
    #                         s_first_name = row[0]
    #                         s_middle_name = row[1]
    #                         s_last_name = row[2]
    #                         s_staff_id = row[3]
    #                         s_aadhaar_no = row[4]
    #                         s_skills = row[5]
    #                         s_hobbies = row[6]
    #                         s_awards = row[7]
    #                         s_recognitions = row[8]
    #                         s_email = row[9]
    #                         s_mobile_no = row[10]
    #                         s_alt_mob = row[11]
    #                         s_nationality = row[12]
    #                         s_religion = row[13]
    #                         s_community = row[14]
    #                         s_scar = row[15]
    #                         s_mole = row[16]
    #                         s_medical_history = row[17]
    #                         s_temp_address = row[18]
    #                         s_temp_city = row[19]
    #                         s_temp_state = row[20]
    #                         s_temp_pincode = row[21]
    #                         s_perm_address = row[22]
    #                         s_perm_city = row[23]
    #                         s_perm_state = row[24]
    #                         s_perm_pincode = row[25]
                            
    #                         for staff_data in staffs["staff_data"]:
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, staff_data["staff_module"])))
                                
    #                             staff_module = d.find_element(By.XPATH, staff_data["staff_module"])
    #                             staff_module.click()

    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/div/div/table/tbody")))
                                
    #                             edit_staff = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/div/div/table/tbody")
    #                             li = edit_staff.find_elements(By.TAG_NAME, "tr")
    #                             td = li[1].find_elements(By.TAG_NAME, "td")
                                
    #                             index = 0  # index of the button to select
   
    #                             button_elements = td[5].find_elements(By.TAG_NAME, "button")

    #                             if len(button_elements) > index:
    #                                 button_elements[0].click()
    #                             else:
    #                                 print(f"No button found at index {index}")
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, staff_data["first_name_input"])))
    #                             # sleep(2)
                                
    #                             first_name = d.find_element(By.XPATH, staff_data["first_name_input"])
    #                             first_name.clear()
    #                             first_name.send_keys(s_first_name)
    #                             # sleep(5)
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, staff_data["middle_name_input"])))
                                
    #                             middle_name = d.find_element(By.XPATH, staff_data["middle_name_input"])
    #                             middle_name.clear()
    #                             middle_name.send_keys(s_middle_name)
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, staff_data["last_name_input"])))
                                
    #                             last_name = d.find_element(By.XPATH, staff_data["last_name_input"])
    #                             last_name.clear()
    #                             last_name.send_keys(s_last_name)
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, staff_data["staff_id_input"])))
                                
    #                             staff_id = d.find_element(By.XPATH, staff_data["staff_id_input"])
    #                             staff_id.clear()
    #                             staff_id.send_keys(s_staff_id)
                                
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, staff_data["date_of_birth"])))
                                
    #                             date_of_birth = d.find_element(By.XPATH, staff_data["date_of_birth"])
    #                             date_of_birth.clear()
    #                             date_of_birth.send_keys("12-03-2010")
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, staff_data["select_gender"])))
                                
    #                             select_gender =  d.find_element(By.XPATH, staff_data["select_gender"])
    #                             select_gender.click()
                                
    #                             wait.until(EC.element_to_be_clickable((d.find_element(By.XPATH, staff_data["gender_ul"])))) 
    #                             gender_ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                             li = gender_ul.find_elements(By.TAG_NAME, "li")[1]
    #                             actions = ActionChains(d)
    #                             actions.click(li).perform()
                                
    #                             wait.until(EC.element_to_be_clickable((d.find_element(By.XPATH,staff_data["martial_status"])))) 
    #                             maritial_status =  d.find_element(By.XPATH, staff_data["martial_status"])
    #                             actions = ActionChains(d)
    #                             actions.click(maritial_status).perform()
                                                                
                                
                                
    #                             wait.until(EC.element_to_be_clickable((d.find_element(By.XPATH, staff_data["martial_ul"])))) 
    #                             martial_ul = d.find_element(By.XPATH, staff_data["martial_ul"])
    #                             li = martial_ul.find_elements(By.TAG_NAME, "li")[1]
                                
    #                             actions = ActionChains(d)
    #                             actions.click(li).perform()
                                

    #                             wait.until(EC.element_to_be_clickable((d.find_element(By.NAME, "Aadhaar_no")))) 
    #                             aadhaar_no = d.find_element(By.NAME,"Aadhaar_no")
    #                             aadhaar_no.clear()
    #                             aadhaar_no.send_keys(s_aadhaar_no)
                               
                                
    #                             skills = d.find_element(By.NAME, "Skills")
    #                             skills.clear()
    #                             skills.send_keys(s_skills)
                                
                                
    #                             hobbies_input = d.find_element(By.NAME, "Hobbies")
    #                             hobbies_input.clear()
    #                             hobbies_input.send_keys(s_hobbies)
                               
                                
    #                             awards_input = d.find_element(By.NAME, "Awards")
    #                             awards_input.clear()
    #                             awards_input.send_keys(s_awards)
                                
    #                             recognitions_input = d.find_element(By.NAME, "Recognitions")
    #                             recognitions_input.clear()
    #                             recognitions_input.send_keys(s_recognitions)
    #                             # sleep(5)
    #                             email_input = d.find_element(By.NAME, "Mail_id")
    #                             email_input.clear()
    #                             email_input.send_keys(s_email)
                                
    #                             mobile_number_input = d.find_element(By.NAME, "Mobile_no")
    #                             mobile_number_input.clear()
    #                             mobile_number_input.send_keys(s_mobile_no)
                                
    #                             alternative_number_input = d.find_element(By.NAME, "Alt_mob_no")
    #                             alternative_number_input.clear()
    #                             alternative_number_input.send_keys("")
                                
    #                             nationality_input = d.find_element(By.NAME , "Nationality")
    #                             nationality_input.clear()
    #                             nationality_input.send_keys(s_nationality)
                                
    #                             religion_input = d.find_element(By.NAME, "Religion")
    #                             religion_input.clear()
    #                             religion_input.send_keys(s_religion)
                                
    #                             caste_input = d.find_element(By.XPATH, staff_data["caste_input"])
    #                             caste_input.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["caste_ul"])))
    #                             caste_ul = d.find_element(By.XPATH, staff_data["caste_ul"])
    #                             li = caste_ul.find_elements(By.TAG_NAME, "li")
    #                             li[0].click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME,"Community")))
    #                             community_ul = d.find_element(By.NAME,"Community")
    #                             community_ul.clear()
    #                             community_ul.send_keys(s_community)
                                
    #                             scar_input = d.find_element(By.NAME, "Scar")
    #                             scar_input.clear()
    #                             scar_input.send_keys(s_scar)
                                
    #                             mole_input = d.find_element(By.NAME, "Mole")
    #                             mole_input.clear()
    #                             mole_input.send_keys(s_mole)
                                
    #                             blood_group_input = d.find_element(By.XPATH, staff_data["blood_group_input"])
    #                             blood_group_input.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["blood_group_ul"])))
                                
    #                             blood_group_ul = d.find_element(By.XPATH, staff_data["blood_group_ul"])
    #                             li = blood_group_ul.find_elements(By.TAG_NAME,"li")
    #                             li[0].click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME,"Medical_history")))
                                
    #                             medical_history = d.find_element(By.NAME,"Medical_history")
    #                             medical_history.clear()
    #                             medical_history.send_keys(s_medical_history)
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["language_known_input"])))
    #                             sleep(1)
    #                             language_known_input = d.find_element(By.XPATH, staff_data["language_known_input"])
    #                             language_known_input.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["language_known_input_ul"])))
                                
    #                             language_known_input_ul = d.find_element(By.XPATH, staff_data["language_known_input_ul"])
    #                             li = language_known_input_ul.find_elements(By.TAG_NAME,"li" )
    #                             li[0].click()
                                                                
    #                             language_known_input_ul.send_keys(Keys.ESCAPE)
    #                             sleep(1)
    #                             wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["mother_tongue_input"])))
                                
    #                             mother_tongue_input = d.find_element(By.XPATH, staff_data["mother_tongue_input"])
    #                             mother_tongue_input.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["mother_tongue_input_ul"])))
    #                             mother_tongue_input_ul = d.find_element(By.XPATH, staff_data["mother_tongue_input_ul"])
    #                             li = mother_tongue_input_ul.find_elements(By.TAG_NAME,"li" )
    #                             li[0].click()

    #                             sleep(1)
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Address")))
                                
    #                             temp_address_input = d.find_element(By.NAME, "Address")
    #                             temp_address_input.click()
    #                             temp_address_input.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             temp_address_input.send_keys(Keys.BACKSPACE)
    #                             ActionChains(d).click(temp_address_input).perform()
                                
    #                             for character in s_temp_address:
    #                                 ActionChains(d).send_keys(character).perform()
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "City")))
                                
    #                             t_city_input = d.find_element(By.NAME, "City")
    #                             t_city_input.click()
    #                             t_city_input.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             t_city_input.send_keys(Keys.BACKSPACE)
    #                             ActionChains(d).click(t_city_input).perform()
    #                             for character in s_temp_city:
    #                                 ActionChains(d).send_keys(character).perform()
                                
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "State")))
    #                             t_state_input = d.find_element(By.NAME, "State")
    #                             t_state_input.click()
    #                             t_state_input.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             t_state_input.send_keys(Keys.BACKSPACE)
                                
    #                             ActionChains(d).click(t_state_input).perform()
    #                             for character in s_temp_state:
    #                                 ActionChains(d).send_keys(character).perform()
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Pincode")))
    #                             t_pincode_input = d.find_element(By.NAME, "Pincode")
    #                             t_pincode_input.click()
    #                             t_pincode_input.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             t_pincode_input.send_keys(Keys.BACKSPACE)
                                
    #                             ActionChains(d).click(t_pincode_input).perform()
    #                             for character in s_temp_pincode:
    #                                 ActionChains(d).send_keys(character).perform()
                               
    #                             # same_as_temp_checkbox = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[2]/div[2]/label/span[1]/input")
    #                             # same_as_temp_checkbox.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[3]/div/div[1]/div/div/input")))
                                
    #                             perm_address_input = d.find_element(By.XPATH , "/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[3]/div/div[1]/div/div/input")
    #                             perm_address_input.click()
    #                             perm_address_input.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             perm_address_input.send_keys(Keys.BACKSPACE)
    #                             ActionChains(d).click(perm_address_input).perform()
    #                             for character in s_perm_address:
    #                                 ActionChains(d).send_keys(character).perform()
                                
    #                             sleep(1)
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[1]/div/div/div[2]/div/div/input")))
                                
    #                             p_city_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[3]/div/div[2]/div/div/input")
    #                             p_city_input.click()
    #                             p_city_input.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             p_city_input.send_keys(Keys.BACKSPACE)
                                
    #                             ActionChains(d).click(p_city_input).perform()
    #                             for character in s_perm_city:
    #                                 ActionChains(d).send_keys(character).perform()
                                
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[3]/div/div[3]/div/div/input")))
                                
    #                             p_state_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[3]/div/div[3]/div/div/input")
    #                             p_state_input.click()
    #                             p_state_input.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             p_state_input.send_keys(Keys.BACKSPACE)
                                
    #                             ActionChains(d).click(p_state_input).perform()
    #                             for character in s_perm_state:
    #                                 ActionChains(d).send_keys(character).perform()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[3]/div/div[4]/div/div/input")))
    #                             p_pincode_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[3]/div/div[4]/div/div/input")
    #                             p_pincode_input.click()
    #                             p_pincode_input.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             p_pincode_input.send_keys(Keys.BACKSPACE)
                                
    #                             ActionChains(d).click(p_pincode_input).perform()
    #                             for character in s_perm_pincode:
    #                                 ActionChains(d).send_keys(character).perform()
                                
    #                                                             # wait for the Next button to become clickable
    #                             next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Next')]")))
    #                             next_button.click()
                                
    #                             # # Wait for the "back" button element to be clickable
    #                             # # back_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'back')]")))
    #                             # # # Click the "back" button
    #                             # # back_button.click()

    #                             # # # Wait for the "cancel" button element to be clickable
    #                             # # cancel_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'cancel')]")))
    #                             # # # Click the "cancel" button
    #                             # # cancel_button.click()

                                
    #                             # # # Find the "Next" button and click it
    #                             # # try:
    #                             # #     next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(., 'Next')]')))
    #                             # #     next_button.click()
    #                             # # except TimeoutException:
    #                             # #     logging.error('Timed out waiting for Next button to become clickable')
    #                             # # except Exception as e:
    #                             # #     logging.error('Encountered an error while clicking Next button: {}'.format(str(e)))
    #                             # # else:
    #                             # #     logging.info('Successfully clicked Next button')
                                
                                
    #                             # ---- job details ----
                               
    #                             # get all the buttons in the tabbed menu
    #                             wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"MuiTab-root")))

    #                             # tabs = d.find_elements(By.CLASS_NAME,"MuiTab-root")

    #                             # job_tab = tabs[1].click()
                                                            

    #                             # ---- job details ----
    #                             with open('data/staffs2.csv', 'r') as f:
    #                                 reader = csv.reader(f)
    #                                 # Skip the two header row
    #                                 next(reader)
    #                                 # next(reader)
    #                                 for row in reader:
    #                                     j_designation = row[0]
    #                                     j_description = row[1]
    #                                     j_bank_name = row[2]
    #                                     j_branch_name = row[3]
    #                                     j_account_number = row[4]
    #                                     j_ifsc_code = row[5]
    #                                     j_pan_number = row[6]
    #                                     e_college = row[7]
    #                                     e_course = row[8]
    #                                     e_collge_specialization = row[9]
    #                                     e_school = row[10]
    #                                     e_school_specialization = row[11]
    #                                     e_percentage = row[12]
    #                                     e_cgpa = row[13]
    #                                     e_total_marks = row[14]
    #                                     e_gained_marks = row[15]
    #                                     w_designation = row[16]
    #                                     w_name_of_institution = row[17]
    #                                     w_location = row[18]
    #                                     w_notes = row[19]
                                      
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME,"Designation")))
                                        
    #                                     designation = d.find_element(By.NAME,"Designation")
    #                                     designation.clear()
    #                                     designation.send_keys(j_designation)

    #                                     wait.until(EC.element_to_be_clickable((By.NAME,"Date_of_joining")))
                                
    #                                     date_of_joining = d.find_element(By.NAME,"Date_of_joining")
    #                                     date_of_joining.clear()
    #                                     date_of_joining.send_keys("04-01-2023")

    #                                     wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="demo-multiple-name"]')))
                                
    #                                     # department = d.find_element(By.XPATH,'//*[@id="demo-multiple-name"]')
    #                                     # department.click()
                                        
    #                                     # wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[3]/ul")))
    #                                     # sleep(5)
    #                                     # ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
    #                                     # li = ul.find_elements(By.TAG_NAME, "li")
    #                                     # li[0].click()
    #                                     # ul.send_keys(Keys.ESCAPE)
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["role_group_input"])))
                                
    #                                     role_group = d.find_element(By.XPATH,staff_data["role_group_input"])
    #                                     role_group.click()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[3]/ul")))
                                
    #                                     ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
    #                                     li = ul.find_elements(By.TAG_NAME, "li")
    #                                     li[0].click()
                                
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["status_input"])))
                                        
    #                                     status = d.find_element(By.XPATH,staff_data["status_input"])
    #                                     status.click()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[3]/ul")))
                                
    #                                     ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
    #                                     li = ul.find_elements(By.TAG_NAME, "li")
    #                                     li[0].click()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["choose_calendar_input"])))
                                
                                        
    #                                     choose_calendar = d.find_element(By.XPATH,staff_data["choose_calendar_input"])
    #                                     choose_calendar.click()

    #                                     wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[3]/ul")))
                                
    #                                     ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
    #                                     li = ul.find_elements(By.TAG_NAME, "li")
    #                                     li[0].click()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["nature_of_appoinment_input"])))
                                
                                        
    #                                     nature_of_appoinment = d.find_element(By.XPATH,staff_data["nature_of_appoinment_input"])
    #                                     nature_of_appoinment.click()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[3]/ul")))
                                
    #                                     ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
    #                                     li = ul.find_elements(By.TAG_NAME, "li")
    #                                     li[0].click()
                                        
                                       
    #                                     wait.until(EC.element_to_be_clickable((By.NAME,"Description")))
                                
    #                                     department = d.find_element(By.NAME,"Description")
    #                                     department.clear()
    #                                     department.send_keys(j_description)
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME,"Bank_name")))
                                
    #                                     department = d.find_element(By.NAME,"Bank_name")
    #                                     department.clear()
    #                                     department.send_keys(j_bank_name)                                        
                                        
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME,"Branch_name")))
                                
    #                                     department = d.find_element(By.NAME,"Branch_name")
    #                                     department.clear()
    #                                     department.send_keys(j_branch_name)
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME,"Account_no")))
                                
    #                                     department = d.find_element(By.NAME,"Account_no")
    #                                     department.clear()
    #                                     department.send_keys(j_account_number)
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME,"Ifsc_code")))
                                
    #                                     department = d.find_element(By.NAME,"Ifsc_code")
    #                                     department.send_keys(j_ifsc_code)
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME,"Pan_no")))
                                
    #                                     department = d.find_element(By.NAME,"Pan_no")
    #                                     department.clear()
    #                                     department.send_keys(j_pan_number)
                                        
    #                                     next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Next')]")))
    #                                     # click the Next button
    #                                     next_button.click()
                                        
                                    
    #                                     # back_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'back')]")))
    #                                     # # Click the "back" button
    #                                     # back_button.click()
                                        
                                        
    #                                     # ---- educational details ---
    #                                     # tabs = d.find_elements(By.CLASS_NAME,"MuiTab-root")

    #                                     # educational_tab = tabs[2].click()
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div/div[2]/div/div/div/div/div/button")))
                                
    #                                     add_new_education = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div/div[2]/div/div/div/div/div/button")
    #                                     add_new_education.click()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["degree_input"])))
                                
    #                                     degree = d.find_element(By.XPATH,staff_data["degree_input"])
    #                                     degree.click()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[3]/ul")))
                                
    #                                     ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
    #                                     li = ul.find_elements(By.TAG_NAME, "li")
    #                                     li[2].click()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME,"College")))
                                
    #                                     college = d.find_element(By.NAME,"College")
    #                                     college.clear()
    #                                     college.send_keys(e_college)
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME,"Course_name")))
                                
    #                                     course = d.find_element(By.NAME,"Course_name")
    #                                     course.clear()
    #                                     course.send_keys(e_course)
                                        
    #                                     medium = d.find_element(By.XPATH,staff_data["medium_dd"])
    #                                     medium.click()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[3]/ul")))
                                
    #                                     ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
    #                                     li = ul.find_elements(By.TAG_NAME, "li")
    #                                     li[0].click()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["e_specialization"])))
                                
    #                                     specialization = d.find_element(By.XPATH,staff_data["e_specialization"])
    #                                     specialization.clear()
    #                                     specialization.send_keys(e_collge_specialization)
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME,"year_of_passing")))
                                
    #                                     year_of_passing = d.find_element(By.NAME,"year_of_passing")
    #                                     year_of_passing.send_keys("01-04-2023")
                                        
    #                                     marks_type = d.find_element(By.XPATH,staff_data["marks_type"])
    #                                     marks_type.click()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[3]/ul")))
                                
    #                                     ul = d.find_element(By.XPATH,"/html/body/div[2]/div[3]/ul")
    #                                     li = ul.find_elements(By.TAG_NAME, "li")
    #                                     li[1].click()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["percentage_input"])))
                                
    #                                     percentage = d.find_element(By.NAME,"percentage")
    #                                     percentage.clear()
    #                                     percentage.send_keys("80")
                                        
    #                                     # sleep(5)
    #                                     # delete_icon = d.find_element(By.XPATH,"//svg[@data-testid='DeleteIcon']")
                                        
    #                                     # action = ActionChains(d)
    #                                     # action.move_to_element(delete_icon).click().perform()
    #                                     # wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div/div[2]/div/div/div/div/div[2]/button")))
                                
    #                                     # add_new_education_bottom = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div/div[2]/div/div/div/div/div[2]/button")
    #                                     # add_new_education_bottom.click()      
                                        
    #                                     next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Next')]")))
    #                                     # click the Next button
    #                                     next_button.click()  
                                        
    #                                     # tabs = d.find_elements(By.CLASS_NAME,"MuiTab-root")

    #                                     # experiance_tab = tabs[3].click()      
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div/div[2]/div/div/div/div/div/button")))
                                
    #                                     add_new_experiance = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div/div/form/div[1]/div/div[2]/div/div/div/div/div/button")
    #                                     add_new_experiance.click()    
                                        
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["w_designation_input"])))
                                
    #                                     percentage = d.find_element(By.NAME,"Designation")
    #                                     percentage.clear()
    #                                     percentage.send_keys(w_designation)
                                        
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["w_name_of_institution"])))
                                
    #                                     percentage = d.find_element(By.NAME,"Name_of_Institution")
    #                                     percentage.send_keys(w_name_of_institution)
                                                   
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["w_location_input"])))
                                
    #                                     percentage = d.find_element(By.NAME,"Location")
    #                                     percentage.clear()
    #                                     percentage.send_keys(w_location)
                                                   
                                        
    #                                     marks_type = d.find_element(By.XPATH,staff_data["w_experience_from"])
    #                                     marks_type.clear()
    #                                     marks_type.send_keys("06-04-2023")
                                                                                
    #                                     marks_type = d.find_element(By.XPATH,staff_data["w_experience_to"])
    #                                     marks_type.clear()
    #                                     marks_type.send_keys("07")

    #                                     wait.until(EC.element_to_be_clickable((By.XPATH,staff_data["w_notes"])))
                                
    #                                     percentage = d.find_element(By.NAME,"Notes")
    #                                     percentage.clear()
    #                                     percentage.send_keys(w_notes)
                                        
    #                                     next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Next')]")))
    #                                     # click the Next button
    #                                     next_button.click()  
                                        
                                                                                
    #                                     with open('data/staffs3.csv', 'r') as f:
    #                                         reader = csv.reader(f)
    #                                         # Skip the two header row
    #                                         next(reader)
    #                                         # next(reader)
    #                                         for row in reader:
                                                
    #                                             father_name = row[0]
    #                                             father_occupation = row[1]
    #                                             father_email = row[2]
    #                                             father_phone = row[3]
                                                
    #                                             mother_name = row[4]
    #                                             mother_occupation = row[5]
    #                                             mother_email = row[6]
    #                                             mother_phone = row[7]
                                                
    #                                             guardian_name = row[8]
    #                                             guardian_occupation = row[9]
    #                                             guardian_email = row[10]
    #                                             guardian_phone = row[11]
    #                                             guardian_relation = row[12]
                                        
    #                                             # tabs = d.find_elements(By.CLASS_NAME,"MuiTab-root")

    #                                             # family_tab = tabs[4].click()      
                                                
                                                
    #                                             wait.until(EC.element_to_be_clickable((By.NAME,"Father_name")))
                                        
    #                                             f_father_name = d.find_element(By.NAME,"Father_name")
    #                                             f_father_name.clear()
    #                                             f_father_name.send_keys(father_name)
                                                
    #                                             f_father_occupation = d.find_element(By.NAME,"Father_occupation")
    #                                             f_father_occupation.clear()
    #                                             f_father_occupation.send_keys(father_occupation)
                                                
    #                                             f_father_email = d.find_element(By.NAME,"Father_email")
    #                                             f_father_email.clear()
    #                                             f_father_email.send_keys(father_email)
                                                
    #                                             f_father_phone = d.find_element(By.NAME,"Father_Phone")
    #                                             f_father_phone.clear()
    #                                             f_father_phone.send_keys(father_phone)
                                                
    #                                             f_mother_name = d.find_element(By.NAME,"Mother_name")
    #                                             f_mother_name.clear()
    #                                             f_mother_name.send_keys(mother_name)
                                                
    #                                             f_mother_occupation = d.find_element(By.NAME,"Mother_occupation")
    #                                             f_mother_occupation.clear()
    #                                             f_mother_occupation.send_keys(mother_occupation)
                                                
    #                                             f_mother_email = d.find_element(By.NAME,"Mother_email")
    #                                             f_mother_email.clear()
    #                                             f_mother_email.send_keys(mother_email)
                                                
    #                                             f_mother_phone = d.find_element(By.NAME,"Mother_Phone")
    #                                             f_mother_phone.clear()
    #                                             f_mother_phone.send_keys(mother_phone)
                                                
    #                                             f_guardian_checkbox = d.find_element(By.NAME,"Guardian_info")
    #                                             f_guardian_checkbox.click()
                                                
    #                                             wait.until(EC.element_to_be_clickable((By.NAME,"Guardian_name")))
                                                
    #                                             f_guardian_name = d.find_element(By.NAME,"Guardian_name")
    #                                             f_guardian_name.clear()
    #                                             f_guardian_name.send_keys(guardian_name)
                                                
    #                                             f_guardian_occupation = d.find_element(By.NAME,"Gaurdian_occupation")
    #                                             f_guardian_occupation.clear()
    #                                             f_guardian_occupation.send_keys(guardian_occupation)
                                                
    #                                             f_guardian_email = d.find_element(By.NAME,"Guardian_email")
    #                                             f_guardian_email.clear()
    #                                             f_guardian_email.send_keys(guardian_email)
                                                
    #                                             f_guardian_phone = d.find_element(By.NAME,"Guardian_Phone")
    #                                             f_guardian_phone.clear()
    #                                             f_guardian_phone.send_keys(guardian_phone)
                                                
    #                                             f_guardian_relation = d.find_element(By.NAME,"Guardian_relation")
    #                                             f_guardian_relation.clear()
    #                                             f_guardian_relation.send_keys(guardian_relation)
                                                
    #                                             save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Save')]")))
    #                                             # click the Next button
    #                                             save_button.click()  
                                                        
                                                                                        
    #                                             sleep(60)
                                               
    # def test_delete_staff(self):
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

    #                 for staff_data in staffs["staff_data"]:
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, staff_data["staff_module"])))
                        
    #                     staff_module = d.find_element(By.XPATH, staff_data["staff_module"])
    #                     staff_module.click()

    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/div/div/table/tbody")))
                        
    #                     edit_staff = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/div/div/table/tbody")
    #                     li = edit_staff.find_elements(By.TAG_NAME, "tr")
    #                     td = li[0].find_elements(By.TAG_NAME, "td")
                        
    #                     index = 0  # index of the button to select

    #                     button_elements = td[5].find_elements(By.TAG_NAME, "button")

    #                     if len(button_elements) > index:
    #                         button_elements[1].click()
    #                     else:
    #                         print(f"No button found at index {index}")
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/div/button[1]")))
                        
    #                     # confirm_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/div/button[1]")
    #                     # confirm_btn.click()
                        
    #                     cancel_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/div/button[2]")
    #                     cancel_btn.click()
                        
    #                     # sleep(5)
                                                                                
    # def test_search_staff(self):
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

    #                 for staff_data in staffs["staff_data"]:
                        
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, staff_data["staff_module"])))
                        
    #                     staff_module = d.find_element(By.XPATH, staff_data["staff_module"])
    #                     staff_module.click()

    #                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[1]/div[1]/div/div/input")))
                        
    #                     search_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[1]/div[1]/div/div/input")
    #                     search_key ="martin"
    #                     ActionChains(d).click(search_btn).perform()
    #                     sleep(2)
    #                     for character in search_key:
    #                         ActionChains(d).send_keys(character).perform()
                            
                            
    #                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[1]/div[1]/div/div/input")))
                        
    #                     pagination = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/div/div/div/nav")
    #                     ul = pagination.find_element(By.TAG_NAME, "ul")
    #                     li = ul.find_elements(By.TAG_NAME, "li")
    #                     li[1].click()

    #                     sleep(5)
                        
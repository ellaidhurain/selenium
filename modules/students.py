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

with open('config/students.json') as f:
    students = json.load(f)

class TestStudents(unittest.TestCase):

    def setUp(self):
        # Initialize the webdriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser
        self.driver.quit()
        
    def test_student_add(self):
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

                    with open('data/students.csv', 'r') as f:
                        reader = csv.reader(f)
                        # Skip the two header row
                        next(reader)
                        
                        for row in reader:
                            first_name = row[0]
                            middle_name = row[1]
                            last_name = row[2]
                            student_id = row[3]
                            aadhaar_no = row[4]
                            skills = row[5]
                            hobbies = row[6]
                            awards = row[7]
                            recognitions = row[8]
                            email = row[9]
                            mobile_no = row[10]
                            emergency_no = row[11]
                            scar = row[12]
                            mole = row[13]
                            medical_history = row[14]
                            temporary_address = row[15]
                            t_city = row[16]
                            t_state = row[17]
                            t_pincode = row[18]
                            perm_address = row[19]
                            p_city =row[20]
                            p_state =row[21]
                            p_pincode =row[22]
                            sibling_name =row[23]
                            sibling_education =row[24]
                 

                            for student_data in students["student_data"]:
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, student_data["student_module"])))
                                
                                calendar_module = d.find_element(By.XPATH, student_data["student_module"])
                                calendar_module.click()
                                sleep(2)
                                wait.until(EC.element_to_be_clickable((By.XPATH, student_data["add_new_student"])))
                                
                                add_new_student = d.find_element(By.XPATH, student_data["add_new_student"])
                                add_new_student.click()
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "First_name")))
                                first_name_input = d.find_element(By.NAME, "First_name")
                                
                                ActionChains(d).click(first_name_input).perform()
                                for character in first_name:
                                    ActionChains(d).send_keys(character).perform()
                             
                                wait.until(EC.element_to_be_clickable((By.NAME, "Middle_name")))
                                middle_name_input = d.find_element(By.NAME, "Middle_name")
                                
                                ActionChains(d).click(middle_name_input).perform()
                                for character in middle_name:
                                    ActionChains(d).send_keys(character).perform()
                             
                                wait.until(EC.element_to_be_clickable((By.NAME, "Last_name")))
                                last_name_input = d.find_element(By.NAME, "Last_name")
                                
                                ActionChains(d).click(last_name_input).perform()
                                for character in last_name:
                                    ActionChains(d).send_keys(character).perform()
                             
                                wait.until(EC.element_to_be_clickable((By.NAME, "Student_id")))
                                student_id_input = d.find_element(By.NAME, "Student_id")
                                
                                ActionChains(d).click(student_id_input).perform()
                                for character in student_id:
                                    ActionChains(d).send_keys(character).perform()
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "Dob")))
                                Dob_input = d.find_element(By.NAME, "Dob")
                                Dob_input.send_keys("07-04-2023")
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[8]/div/div/div")))
                                Dob_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[8]/div/div/div")
                                Dob_input.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
                                ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
                                li = ul.find_elements(By.TAG_NAME, "li")
                                
                                li[1].click()
                             
                                wait.until(EC.element_to_be_clickable((By.NAME, "Aadhaar_no")))
                                aadhaar_no_input = d.find_element(By.NAME, "Aadhaar_no")
                              
                                aadhaar_no_input.send_keys(aadhaar_no)
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "Skills")))
                                Skills_input = d.find_element(By.NAME, "Skills")
                              
                                Skills_input.send_keys(skills)
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "Hobbies")))
                                hobbies_input = d.find_element(By.NAME, "Hobbies")
                              
                                hobbies_input.send_keys(hobbies)
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "Awards")))
                                Awards_input = d.find_element(By.NAME, "Awards")
                              
                                Awards_input.send_keys(awards)
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "Recognitions")))
                                Recognitions_input = d.find_element(By.NAME, "Recognitions")
                              
                                Recognitions_input.send_keys(recognitions)
                               
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "Mail_id")))
                                Mail_id_input = d.find_element(By.NAME, "Mail_id")
                              
                                Mail_id_input.send_keys(email)
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "Mobile_no")))
                                Mobile_no_input = d.find_element(By.NAME, "Mobile_no")
                              
                                Mobile_no_input.send_keys(mobile_no)
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "Parent_mobile_no")))
                                emergency_mobile_no_input = d.find_element(By.NAME, "Parent_mobile_no")
                              
                                emergency_mobile_no_input.send_keys(emergency_no)
                                
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "Nationality")))
                                Nationality_input = d.find_element(By.NAME, "Nationality")
                              
                                Nationality_input.send_keys("india")
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "Religion")))
                                Religion_input = d.find_element(By.NAME, "Religion")
                              
                                Religion_input.send_keys("hinmuschrist")
                                
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[3]/div[2]/div/div/div/div/div/div[3]/div/div/div")))
                                caste_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[3]/div[2]/div/div/div/div/div/div[3]/div/div/div")
                              
                                caste_input.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
                                ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
                                li = ul.find_elements(By.TAG_NAME, "li")
                                
                                li[1].click()
                                
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "Community")))
                                Community_input = d.find_element(By.NAME, "Community")
                              
                                Community_input.send_keys("new")
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "Scar")))
                                Scar_input = d.find_element(By.NAME, "Scar")
                              
                                Scar_input.send_keys(scar)
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "Mole")))
                                Mole_input = d.find_element(By.NAME, "Mole")
                              
                                Mole_input.send_keys(mole)
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div")))
                                blood_group_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div")
                              
                                blood_group_input.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
                                ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
                                li = ul.find_elements(By.TAG_NAME, "li")
                                
                                li[1].click()
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "Medical_history")))
                                Medical_history_input = d.find_element(By.NAME, "Medical_history")
                              
                                Medical_history_input.send_keys(medical_history)
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[5]/div[2]/div/div/div/div/div/div[1]/div/div/div")))
                                language_known_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[5]/div[2]/div/div/div/div/div/div[1]/div/div/div")
                              
                                language_known_input.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
                                ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
                                li = ul.find_elements(By.TAG_NAME, "li")
                                
                                li[1].click()
                                
                                ul.send_keys(Keys.ESCAPE)
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[5]/div[2]/div/div/div/div/div/div[2]/div/div/div")))
                                mother_tongue = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[5]/div[2]/div/div/div/div/div/div[2]/div/div/div")
                              
                                mother_tongue.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
                                ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
                                li = ul.find_elements(By.TAG_NAME, "li")
                                
                                li[1].click()
                                
                                sleep(1)
                                wait.until(EC.element_to_be_clickable((By.NAME, "Address")))
                                t_address_input = d.find_element(By.NAME, "Address")
                                ActionChains(d).click(t_address_input).perform()
                                for character in temporary_address:
                                    ActionChains(d).send_keys(character).perform()

                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "City")))
                                t_city_input = d.find_element(By.NAME, "City")
                              
                                ActionChains(d).click(t_city_input).perform()
                                for character in t_city:
                                    ActionChains(d).send_keys(character).perform()
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "State")))
                                t_state_input = d.find_element(By.NAME, "State")
                                
                                ActionChains(d).click(t_state_input).perform()
                                for character in t_state:
                                    ActionChains(d).send_keys(character).perform()
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "Pincode")))
                                t_pincode_input = d.find_element(By.NAME, "Pincode")
                                
                                ActionChains(d).click(t_pincode_input).perform()
                                for character in t_pincode:
                                    ActionChains(d).send_keys(character).perform()
                                
                              
                                same_as_temp = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[2]/div[1]/div[2]/label/span[1]/input")
                                same_as_temp.click()

                                  
                                # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/input")))
                                # p_address_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/input")
                                
                                # ActionChains(d).click(p_address_input).perform()
                                # for character in perm_address:
                                #     ActionChains(d).send_keys(character).perform()

                                
                                # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/input")))
                                # p_city_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/input")
                              
                                # ActionChains(d).click(p_city_input).perform()
                                # for character in p_city:
                                #     ActionChains(d).send_keys(character).perform()
                                
                                # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/input")))
                                # p_state_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/input")
                                
                                # ActionChains(d).click(p_state_input).perform()
                                # for character in p_state:
                                #     ActionChains(d).send_keys(character).perform()
                                
                                # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/input")))
                                # p_pincode_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/input")
                                
                                # ActionChains(d).click(p_pincode_input).perform()
                                # for character in p_pincode:
                                #     ActionChains(d).send_keys(character).perform()
                                
                                # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[7]/div[2]/div/div/div/div/div/button")))
                                
                                # sibling = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[7]/div[2]/div/div/div/div/div/button")
                                # sibling.click()
                                
                                # wait.until(EC.element_to_be_clickable((By.NAME, "Sibling_name")))
                                # Sibling_name_input = d.find_element(By.NAME, "Sibling_name")
                                
                                # ActionChains(d).click(Sibling_name_input).perform()
                                # for character in sibling_name:
                                #     ActionChains(d).send_keys(character).perform()
                                    
                                # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[7]/div[2]/div/div/div/div/div[1]/div[2]/div/div/div")))
                                # sibling_relation_type = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[7]/div[2]/div/div/div/div/div[1]/div[2]/div/div/div")
                                # sibling_relation_type.click()
                                
                                # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
                                # ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
                                # li = ul.find_elements(By.TAG_NAME, "li")
                                
                                # li[1].click()
                                
                                
                                # wait.until(EC.element_to_be_clickable((By.NAME, "Sibling_edu")))
                                # Sibling_edu_input = d.find_element(By.NAME, "Sibling_edu")
                                
                                # ActionChains(d).click(Sibling_edu_input).perform()
                                # for character in sibling_education:
                                #     ActionChains(d).send_keys(character).perform()
                                    
                                # wait.until(EC.element_to_be_clickable((By.NAME, "Education_institute")))
                                # Education_institute_input = d.find_element(By.NAME, "Education_institute")
                                
                                # ActionChains(d).click(Education_institute_input).perform()
                                # for character in "anna univercity":
                                #     ActionChains(d).send_keys(character).perform()
                                
                                # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[1]/nav/a/button")))
                                # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[1]/nav/a/button")
                                # cancel_btn.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[2]/button")))
                                next_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[2]/button")
                                next_btn.click()
                                
                                #  --- education tab ----
                                # wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"MuiTab-root")))

                                # tabs = d.find_elements(By.CLASS_NAME,"MuiTab-root")

                                # edu_tab = tabs[1].click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/div/div/div[1]/div/div/div")))
                                standard_type = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/div/div/div[1]/div/div/div")
                                standard_type.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
                                ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
                                li = ul.find_elements(By.TAG_NAME, "li")
                                
                                li[1].click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div")))
                                medium_type = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div")
                                medium_type.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
                                ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
                                li = ul.find_elements(By.TAG_NAME, "li")
                                
                                li[1].click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/div/div/div[3]/div/div/div")))
                                student_type = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/div/div/div[3]/div/div/div")
                                student_type.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
                                ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
                                li = ul.find_elements(By.TAG_NAME, "li")
                                
                                li[1].click()
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "Date_of_joining")))
                                doj = d.find_element(By.NAME, "Date_of_joining")
                                
                                doj.send_keys("07-04-2023")
                                
                                wait.until(EC.element_to_be_clickable((By.NAME, "Admission_no")))
                                Sibling_edu_input = d.find_element(By.NAME, "Admission_no")
                                
                                ActionChains(d).click(Sibling_edu_input).perform()
                                for character in "ADMSN0012":
                                    ActionChains(d).send_keys(character).perform()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/div/div/div[6]/div/div/div")))
                                role = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/div/div/div[6]/div/div/div")
                                role.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
                                ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
                                li = ul.find_elements(By.TAG_NAME, "li")
                                
                                li[1].click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "//html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/div/div/div[7]/div/div/div")))
                                status_type = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/div/div/div[7]/div/div/div")
                                status_type.click()
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
                                ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
                                li = ul.find_elements(By.TAG_NAME, "li")
                                
                                li[0].click()
                                
                                # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[1]/nav/a/button")))
                                # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[1]/nav/a/button")
                                # cancel_btn.click()
                                
                                # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[2]/button")))
                                # back_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[2]/button")
                                # back_btn.click()
                                
                                
                                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[3]/button")))
                                next_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[3]/button")
                                next_btn.click()
                                
                                
                                #  --- family tab ----
                                # wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"MuiTab-root")))

                                # tabs = d.find_elements(By.CLASS_NAME,"MuiTab-root")

                                # family_tab = tabs[2].click()
                                
                                with open('data/students2.csv', 'r') as f:
                                    reader = csv.reader(f)
                                    # Skip the two header row
                                    next(reader)
                                    
                                    for row in reader:
                                        parent_id = row[1]
                                        annual_income = row[2]
                                        father_name = row[3]
                                        father_mobile = row[4]
                                        father_mail = row[5]
                                        father_education = row[6]
                                        father_occupation = row[7]
                                        mother_name = row[8]
                                        mother_mobile = row[9]
                                        mother_gmail = row[10]
                                        mother_education = row[11]
                                        mother_occupation = row[12]
                                        guardian_name = row[13]
                                        guardian_mobile = row[14]
                                        guardian_gmail = row[15]
                                        guardian_education = row[16]
                                        guardian_occupation = row[17]
                                        notes = row[18]
                                     
                                
                                
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Parent_id")))
                                        Parent_id = d.find_element(By.NAME, "Parent_id")
                                        
                                        ActionChains(d).click(Parent_id).perform()
                                        for character in parent_id:
                                            ActionChains(d).send_keys(character).perform()
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Annual_income")))
                                        Annual_income = d.find_element(By.NAME, "Annual_income")
                                        
                                        ActionChains(d).click(Annual_income).perform()
                                        for character in annual_income:
                                            ActionChains(d).send_keys(character).perform()
                                        
                                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div/div/div")))
                                        role_group = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div/div/div")
                                        role_group.click()
                                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
                                        ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
                                        li = ul.find_elements(By.TAG_NAME, "li")
                                        
                                        li[1].click()
                                        
                                        
                                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[4]/div/div/div")))
                                        status = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[4]/div/div/div")
                                        status.click()
                                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
                                        ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
                                        li = ul.find_elements(By.TAG_NAME, "li")
                                        
                                        li[0].click()
                                        
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "First_name")))
                                        first_name_new = d.find_element(By.NAME, "First_name")
                                        
                                        ActionChains(d).click(first_name_new).perform()
                                        for character in "jhon":
                                            ActionChains(d).send_keys(character).perform()
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Middle_name")))
                                        middle_name_new = d.find_element(By.NAME, "Middle_name")
                                        
                                        ActionChains(d).click(middle_name_new).perform()
                                        for character in "wick":
                                            ActionChains(d).send_keys(character).perform()
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Last_name")))
                                        last_name_new = d.find_element(By.NAME, "Last_name")
                                        
                                        ActionChains(d).click(last_name_new).perform()
                                        for character in "new":
                                            ActionChains(d).send_keys(character).perform()
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Father_name")))
                                        Father_name = d.find_element(By.NAME, "Father_name")
                                        
                                        ActionChains(d).click(Father_name).perform()
                                        for character in father_name:
                                            ActionChains(d).send_keys(character).perform()
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Father_dob")))
                                        Father_dob = d.find_element(By.NAME, "Father_dob")
                                            
                                        Father_dob.send_keys("01-02-2023")
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Father_mob_no")))
                                        Father_mob_no = d.find_element(By.NAME, "Father_mob_no")
                                        
                                        ActionChains(d).click(Father_mob_no).perform()
                                        for character in father_mobile:
                                            ActionChains(d).send_keys(character).perform()
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Father_mail")))
                                        Father_mail = d.find_element(By.NAME, "Father_mail")
                                        
                                        ActionChains(d).click(Father_mail).perform()
                                        for character in father_mail:
                                            ActionChains(d).send_keys(character).perform()
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Father_education")))
                                        Father_education = d.find_element(By.NAME, "Father_education")
                                        
                                        ActionChains(d).click(Father_education).perform()
                                        for character in father_education:
                                            ActionChains(d).send_keys(character).perform()
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Father_occupation")))
                                        Father_occupation = d.find_element(By.NAME, "Father_occupation")
                                        
                                        ActionChains(d).click(Father_occupation).perform()
                                        for character in father_occupation:
                                            ActionChains(d).send_keys(character).perform()
                                        
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Mother_name")))
                                        Mother_name = d.find_element(By.NAME, "Mother_name")
                                        
                                        ActionChains(d).click(Mother_name).perform()
                                        for character in mother_name:
                                            ActionChains(d).send_keys(character).perform()
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Mother_dob")))
                                        Mother_dob = d.find_element(By.NAME, "Mother_dob")
                                        Mother_dob.send_keys("01-02-2023")
                                                                               
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Mother_mob_no")))
                                        Mother_mob_no = d.find_element(By.NAME, "Mother_mob_no")
                                        
                                        ActionChains(d).click(Mother_mob_no).perform()
                                        for character in mother_mobile:
                                            ActionChains(d).send_keys(character).perform()
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Mother_mail")))
                                        Mother_mail = d.find_element(By.NAME, "Mother_mail")
                                        
                                        ActionChains(d).click(Mother_mail).perform()
                                        for character in mother_gmail:
                                            ActionChains(d).send_keys(character).perform()
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Mother_education")))
                                        Mother_education = d.find_element(By.NAME, "Mother_education")
                                        
                                        ActionChains(d).click(Mother_education).perform()
                                        for character in mother_education:
                                            ActionChains(d).send_keys(character).perform()
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Mother_occupation")))
                                        Mother_occupation = d.find_element(By.NAME, "Mother_occupation")
                                        
                                        ActionChains(d).click(Mother_occupation).perform()
                                        for character in mother_occupation:
                                            ActionChains(d).send_keys(character).perform()
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Guardian_name")))
                                        Guardian_name = d.find_element(By.NAME, "Guardian_name")
                                        
                                        ActionChains(d).click(Guardian_name).perform()
                                        for character in guardian_name:
                                            ActionChains(d).send_keys(character).perform()
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Guardian_dob")))
                                        Guardian_dob = d.find_element(By.NAME, "Guardian_dob")
                                        Guardian_dob.send_keys("02-02-2023")
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Gaurdian_mail")))
                                        Gaurdian_mail = d.find_element(By.NAME, "Gaurdian_mail")
                                        
                                        ActionChains(d).click(Gaurdian_mail).perform()
                                        for character in guardian_gmail:
                                            ActionChains(d).send_keys(character).perform()
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Guardian_mob_no")))
                                        Guardian_mob_no = d.find_element(By.NAME, "Guardian_mob_no")
                                        
                                        ActionChains(d).click(Guardian_mob_no).perform()
                                        for character in guardian_mobile:
                                            ActionChains(d).send_keys(character).perform()
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Guardian_relation")))
                                        Guardian_relation = d.find_element(By.NAME, "Guardian_relation")
                                        
                                        ActionChains(d).click(Guardian_relation).perform()
                                        for character in "uncle":
                                            ActionChains(d).send_keys(character).perform()
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Guardian_education")))
                                        Guardian_education = d.find_element(By.NAME, "Guardian_education")
                                        
                                        ActionChains(d).click(Guardian_education).perform()
                                        for character in guardian_education:
                                            ActionChains(d).send_keys(character).perform()
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Guardian_occupation")))
                                        Sibling_edu_input = d.find_element(By.NAME, "Guardian_occupation")
                                        
                                        ActionChains(d).click(Sibling_edu_input).perform()
                                        for character in guardian_occupation:
                                            ActionChains(d).send_keys(character).perform()
                                        
                                        wait.until(EC.element_to_be_clickable((By.NAME, "Notes")))
                                        Notes = d.find_element(By.NAME, "Notes")
                                        
                                        ActionChains(d).click(Notes).perform()
                                        for character in notes:
                                            ActionChains(d).send_keys(character).perform()
                                            
                                        # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[1]/nav/a/button")))
                                        # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[1]/nav/a/button")
                                        # cancel_btn.click()
                                        
                                        # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[2]/button")))
                                        # back_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[2]/button")
                                        # back_btn.click()
                                        
                                        # sleep(5)
                                        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[3]/button")))
                                        save_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[3]/button")
                                        save_btn.click()
                                                
                                        
                                        
                                
                                        sleep(2000)
                                        
    # def test_student_edit(self):
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

    #                 with open('data/students.csv', 'r') as f:
    #                     reader = csv.reader(f)
    #                     # Skip the two header row
    #                     next(reader)
                        
    #                     for row in reader:
    #                         first_name = row[0]
    #                         middle_name = row[1]
    #                         last_name = row[2]
    #                         student_id = row[3]
    #                         aadhaar_no = row[4]
    #                         skills = row[5]
    #                         hobbies = row[6]
    #                         awards = row[7]
    #                         recognitions = row[8]
    #                         email = row[9]
    #                         mobile_no = row[10]
    #                         emergency_no = row[11]
    #                         scar = row[12]
    #                         mole = row[13]
    #                         medical_history = row[14]
    #                         temporary_address = row[15]
    #                         t_city = row[16]
    #                         t_state = row[17]
    #                         t_pincode = row[18]
    #                         perm_address = row[19]
    #                         p_city =row[20]
    #                         p_state =row[21]
    #                         p_pincode =row[22]
    #                         sibling_name =row[23]
    #                         sibling_education =row[24]
                 

    #                         for student_data in students["student_data"]:
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, student_data["student_module"])))
                                
    #                             calendar_module = d.find_element(By.XPATH, student_data["student_module"])
    #                             calendar_module.click()
    #                             sleep(2)
                                                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/div/div/table/tbody")))
                                
    #                             edit_student = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/div/div/table/tbody")
    #                             li = edit_student.find_elements(By.TAG_NAME, "tr")
    #                             td = li[0].find_elements(By.TAG_NAME, "td")
                                
    #                             index = 0  # index of the button to select
   
    #                             button_elements = td[5].find_elements(By.TAG_NAME, "button")

    #                             if len(button_elements) > index:
    #                                 button_elements[0].click()
    #                             else:
    #                                 print(f"No button found at index {index}")
                                
                                
    #                             # wait.until(EC.element_to_be_clickable((By.NAME, "First_name")))
    #                             first_name_input = d.find_element(By.NAME, "First_name")
    #                             first_name_input.clear()
    #                             ActionChains(d).click(first_name_input).perform()
    #                             for character in first_name:
    #                                 ActionChains(d).send_keys(character).perform()
                             
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Middle_name")))
    #                             middle_name_input = d.find_element(By.NAME, "Middle_name")
    #                             middle_name_input.clear()
    #                             ActionChains(d).click(middle_name_input).perform()
    #                             for character in middle_name:
    #                                 ActionChains(d).send_keys(character).perform()
                             
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Last_name")))
    #                             last_name_input = d.find_element(By.NAME, "Last_name")
    #                             last_name_input.clear()
    #                             ActionChains(d).click(last_name_input).perform()
    #                             for character in last_name:
    #                                 ActionChains(d).send_keys(character).perform()
                             
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Student_id")))
    #                             student_id_input = d.find_element(By.NAME, "Student_id")
    #                             student_id_input.clear()
    #                             ActionChains(d).click(student_id_input).perform()
    #                             for character in student_id:
    #                                 ActionChains(d).send_keys(character).perform()
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Dob")))
    #                             Dob_input = d.find_element(By.NAME, "Dob")
    #                             Dob_input.clear()
    #                             Dob_input.send_keys("07-04-2023")
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[8]/div/div/div")))
    #                             Dob_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[8]/div/div/div")
    #                             Dob_input.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
    #                             ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                             li = ul.find_elements(By.TAG_NAME, "li")
                                
    #                             li[1].click()
                             
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Aadhaar_no")))
    #                             aadhaar_no_input = d.find_element(By.NAME, "Aadhaar_no")
    #                             aadhaar_no_input.clear()
    #                             aadhaar_no_input.send_keys(aadhaar_no)
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Skills")))
    #                             Skills_input = d.find_element(By.NAME, "Skills")
    #                             Skills_input.clear()
    #                             Skills_input.send_keys(skills)
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Hobbies")))
    #                             hobbies_input = d.find_element(By.NAME, "Hobbies")
    #                             hobbies_input.clear()
    #                             hobbies_input.send_keys(hobbies)
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Awards")))
    #                             Awards_input = d.find_element(By.NAME, "Awards")
    #                             Awards_input.clear()
    #                             Awards_input.send_keys(awards)
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Recognitions")))
    #                             Recognitions_input = d.find_element(By.NAME, "Recognitions")
    #                             Recognitions_input.clear()
    #                             Recognitions_input.send_keys(recognitions)
                               
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Mail_id")))
    #                             Mail_id_input = d.find_element(By.NAME, "Mail_id")
    #                             Mail_id_input.clear()
    #                             Mail_id_input.send_keys(email)
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Mobile_no")))
    #                             Mobile_no_input = d.find_element(By.NAME, "Mobile_no")
    #                             Mobile_no_input.clear()
    #                             Mobile_no_input.send_keys(mobile_no)
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Parent_mobile_no")))
    #                             emergency_mobile_no_input = d.find_element(By.NAME, "Parent_mobile_no")
    #                             emergency_mobile_no_input.clear()
    #                             emergency_mobile_no_input.send_keys(emergency_no)
                                
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Nationality")))
    #                             Nationality_input = d.find_element(By.NAME, "Nationality")
    #                             Nationality_input.clear()
    #                             Nationality_input.send_keys("india")
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Religion")))
    #                             Religion_input = d.find_element(By.NAME, "Religion")
    #                             Religion_input.clear()
    #                             Religion_input.send_keys("hinmuschrist")
                                
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[3]/div[2]/div/div/div/div/div/div[3]/div/div/div")))
    #                             caste_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[3]/div[2]/div/div/div/div/div/div[3]/div/div/div")
                               
    #                             caste_input.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
    #                             ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                             li = ul.find_elements(By.TAG_NAME, "li")
                                
    #                             li[1].click()
                                
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Community")))
    #                             Community_input = d.find_element(By.NAME, "Community")
    #                             Community_input.clear()
    #                             Community_input.send_keys("new")
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Scar")))
    #                             Scar_input = d.find_element(By.NAME, "Scar")
    #                             Scar_input.clear()
    #                             Scar_input.send_keys(scar)
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Mole")))
    #                             Mole_input = d.find_element(By.NAME, "Mole")
    #                             Mole_input.clear()
    #                             Mole_input.send_keys(mole)
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div")))
    #                             blood_group_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div")
                                
    #                             blood_group_input.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
    #                             ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                             li = ul.find_elements(By.TAG_NAME, "li")
                                
    #                             li[1].click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Medical_history")))
    #                             Medical_history_input = d.find_element(By.NAME, "Medical_history")
    #                             Medical_history_input.clear()
    #                             Medical_history_input.send_keys(medical_history)
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[5]/div[2]/div/div/div/div/div/div[1]/div/div/div")))
    #                             language_known_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[5]/div[2]/div/div/div/div/div/div[1]/div/div/div")
                              
    #                             language_known_input.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
    #                             ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                             li = ul.find_elements(By.TAG_NAME, "li")
                                
    #                             li[1].click()
                                
    #                             ul.send_keys(Keys.ESCAPE)
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[5]/div[2]/div/div/div/div/div/div[2]/div/div/div")))
    #                             mother_tongue = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[5]/div[2]/div/div/div/div/div/div[2]/div/div/div")
                              
    #                             mother_tongue.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
    #                             ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                             li = ul.find_elements(By.TAG_NAME, "li")
                                
    #                             li[1].click()
                                
    #                             sleep(1)
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Address")))
    #                             t_address_input = d.find_element(By.NAME, "Address")
    #                             t_address_input.click()
    #                             t_address_input.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             t_address_input.send_keys(Keys.BACKSPACE)
    #                             ActionChains(d).click(t_address_input).perform()
    #                             for character in temporary_address:
    #                                 ActionChains(d).send_keys(character).perform()

                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "City")))
    #                             t_city_input = d.find_element(By.NAME, "City")
    #                             t_city_input.click()
    #                             t_city_input.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             t_city_input.send_keys(Keys.BACKSPACE)
                               
    #                             ActionChains(d).click(t_city_input).perform()
    #                             for character in t_city:
    #                                 ActionChains(d).send_keys(character).perform()
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "State")))
    #                             t_state_input = d.find_element(By.NAME, "State")
    #                             t_state_input.click()
    #                             t_state_input.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             t_state_input.send_keys(Keys.BACKSPACE)
                                
    #                             ActionChains(d).click(t_state_input).perform()
    #                             for character in t_state:
    #                                 ActionChains(d).send_keys(character).perform()
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Pincode")))
    #                             t_pincode_input = d.find_element(By.NAME, "Pincode")
    #                             t_pincode_input.click()
    #                             t_pincode_input.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             t_pincode_input.send_keys(Keys.BACKSPACE)
                                
    #                             ActionChains(d).click(t_pincode_input).perform()
    #                             for character in t_pincode:
    #                                 ActionChains(d).send_keys(character).perform()
                                
                              
    #                             same_as_temp = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[2]/div[1]/div[2]/label/span[1]/input")
    #                             same_as_temp.click()

                                  
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/input")))
    #                             # p_address_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/input")
    #                             # p_address_input.click()
    #                             # p_address_input.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             # p_address_input.send_keys(Keys.BACKSPACE)
                                
    #                             # ActionChains(d).click(p_address_input).perform()
    #                             # for character in perm_address:
    #                             #     ActionChains(d).send_keys(character).perform()

                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/input")))
    #                             # p_city_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/input")
    #                             # p_city_input.click()
    #                             # p_city_input.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             # p_city_input.send_keys(Keys.BACKSPACE)
                                
    #                             # ActionChains(d).click(p_city_input).perform()
    #                             # for character in p_city:
    #                             #     ActionChains(d).send_keys(character).perform()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/input")))
    #                             # p_state_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/input")
    #                             # p_state_input.click()
    #                             # p_state_input.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             # p_state_input.send_keys(Keys.BACKSPACE)
                                
    #                             # ActionChains(d).click(p_state_input).perform()
    #                             # for character in p_state:
    #                             #     ActionChains(d).send_keys(character).perform()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/input")))
    #                             # p_pincode_input = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[6]/div[2]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/input")
    #                             # p_pincode_input.click()
    #                             # p_pincode_input.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             # p_pincode_input.send_keys(Keys.BACKSPACE)
                              
    #                             # ActionChains(d).click(p_pincode_input).perform()
    #                             # for character in p_pincode:
    #                             #     ActionChains(d).send_keys(character).perform()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[7]/div[2]/div/div/div/div/div/button")))
                                
    #                             # sibling = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[7]/div[2]/div/div/div/div/div/button")
    #                             # sibling.click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.NAME, "Sibling_name")))
    #                             # Sibling_name_input = d.find_element(By.NAME, "Sibling_name")
    #                             # Sibling_name_input.click()
    #                             # Sibling_name_input.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             # Sibling_name_input.send_keys(Keys.BACKSPACE)
                              
    #                             # ActionChains(d).click(Sibling_name_input).perform()
    #                             # for character in sibling_name:
    #                             #     ActionChains(d).send_keys(character).perform()
                                    
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[7]/div[2]/div/div/div/div/div[1]/div[2]/div/div/div")))
    #                             # sibling_relation_type = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[7]/div[2]/div/div/div/div/div[1]/div[2]/div/div/div")
    #                             # sibling_relation_type.click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
    #                             # ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                             # li = ul.find_elements(By.TAG_NAME, "li")
                                
    #                             # li[1].click()
                                
                                
    #                             # wait.until(EC.element_to_be_clickable((By.NAME, "Sibling_edu")))
    #                             # Sibling_edu_input = d.find_element(By.NAME, "Sibling_edu")
    #                             # Sibling_edu_input.click()
    #                             # Sibling_edu_input.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             # Sibling_edu_input.send_keys(Keys.BACKSPACE)
                              
    #                             # ActionChains(d).click(Sibling_edu_input).perform()
    #                             # for character in sibling_education:
    #                             #     ActionChains(d).send_keys(character).perform()
                                    
    #                             # wait.until(EC.element_to_be_clickable((By.NAME, "Education_institute")))
    #                             # Education_institute_input = d.find_element(By.NAME, "Education_institute")
    #                             # Education_institute_input.click()
    #                             # Education_institute_input.send_keys(Keys.CONTROL + "a")  # select all existing input
    #                             # Education_institute_input.send_keys(Keys.BACKSPACE)
                              
    #                             # ActionChains(d).click(Education_institute_input).perform()
    #                             # for character in "anna univercity":
    #                             #     ActionChains(d).send_keys(character).perform()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[1]/nav/a/button")))
    #                             # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[1]/nav/a/button")
    #                             # cancel_btn.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[2]/button")))
    #                             next_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[2]/button")
    #                             next_btn.click()
                                
    #                             #  --- education tab ----
    #                             # wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"MuiTab-root")))

    #                             # tabs = d.find_elements(By.CLASS_NAME,"MuiTab-root")

    #                             # edu_tab = tabs[1].click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/div/div/div[1]/div/div/div")))
    #                             standard_type = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/div/div/div[1]/div/div/div")
    #                             standard_type.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
    #                             ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                             li = ul.find_elements(By.TAG_NAME, "li")
                                
    #                             li[1].click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div")))
    #                             medium_type = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div")
    #                             medium_type.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
    #                             ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                             li = ul.find_elements(By.TAG_NAME, "li")
                                
    #                             li[1].click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/div/div/div[3]/div/div/div")))
    #                             student_type = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/div/div/div[3]/div/div/div")
    #                             student_type.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
    #                             ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                             li = ul.find_elements(By.TAG_NAME, "li")
                                
    #                             li[1].click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Date_of_joining")))
    #                             doj = d.find_element(By.NAME, "Date_of_joining")
    #                             doj.clear()
    #                             doj.send_keys("07-04-2023")
                                
    #                             wait.until(EC.element_to_be_clickable((By.NAME, "Admission_no")))
    #                             Sibling_edu_input = d.find_element(By.NAME, "Admission_no")
                                
    #                             ActionChains(d).click(Sibling_edu_input).perform()
    #                             for character in "ADMSN0012":
    #                                 ActionChains(d).send_keys(character).perform()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/div/div/div[6]/div/div/div")))
    #                             role = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/div/div/div[6]/div/div/div")
    #                             role.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
    #                             ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                             li = ul.find_elements(By.TAG_NAME, "li")
                                
    #                             li[1].click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "//html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/div/div/div[7]/div/div/div")))
    #                             status_type = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div/div[2]/div/div/div/div/div/div[7]/div/div/div")
    #                             status_type.click()
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
    #                             ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                             li = ul.find_elements(By.TAG_NAME, "li")
                                
    #                             li[0].click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[1]/nav/a/button")))
    #                             # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[1]/nav/a/button")
    #                             # cancel_btn.click()
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[2]/button")))
    #                             # back_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[2]/button")
    #                             # back_btn.click()
                                
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[3]/button")))
    #                             next_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[3]/button")
    #                             next_btn.click()
                                
                                
    #                             #  --- family tab ----
    #                             wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"MuiTab-root")))

    #                             tabs = d.find_elements(By.CLASS_NAME,"MuiTab-root")

    #                             family_tab = tabs[2].click()
                                
    #                             with open('data/students2.csv', 'r') as f:
    #                                 reader = csv.reader(f)
    #                                 # Skip the two header row
    #                                 next(reader)
                                    
    #                                 for row in reader:
    #                                     parent_id = row[1]
    #                                     annual_income = row[2]
    #                                     father_name = row[3]
    #                                     father_mobile = row[4]
    #                                     father_mail = row[5]
    #                                     father_education = row[6]
    #                                     father_occupation = row[7]
    #                                     mother_name = row[8]
    #                                     mother_mobile = row[9]
    #                                     mother_gmail = row[10]
    #                                     mother_education = row[11]
    #                                     mother_occupation = row[12]
    #                                     guardian_name = row[13]
    #                                     guardian_mobile = row[14]
    #                                     guardian_gmail = row[15]
    #                                     guardian_education = row[16]
    #                                     guardian_occupation = row[17]
    #                                     notes = row[18]
                                     
                                
                                
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Parent_id")))
    #                                     Parent_id = d.find_element(By.NAME, "Parent_id")
    #                                     Parent_id.clear()
    #                                     ActionChains(d).click(Parent_id).perform()
    #                                     for character in parent_id:
    #                                         ActionChains(d).send_keys(character).perform()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Annual_income")))
    #                                     Annual_income = d.find_element(By.NAME, "Annual_income")
    #                                     Annual_income.clear()
    #                                     ActionChains(d).click(Annual_income).perform()
    #                                     for character in annual_income:
    #                                         ActionChains(d).send_keys(character).perform()
                                        
                                       
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div/div/div")))
    #                                     role_group = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div/div/div")
    #                                     role_group.click()
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
    #                                     ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                                     li = ul.find_elements(By.TAG_NAME, "li")
                                        
    #                                     li[1].click()
                                        
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[4]/div/div/div")))
    #                                     status = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[4]/div/div/div")
    #                                     status.click()
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul")))
                                
    #                                     ul = d.find_element(By.XPATH, "/html/body/div[2]/div[3]/ul")
    #                                     li = ul.find_elements(By.TAG_NAME, "li")
                                        
    #                                     li[0].click()
                                        
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "First_name")))
    #                                     first_name_new = d.find_element(By.NAME, "First_name")
    #                                     first_name_new.clear()
    #                                     ActionChains(d).click(first_name_new).perform()
    #                                     for character in "jhon":
    #                                         ActionChains(d).send_keys(character).perform()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Middle_name")))
    #                                     middle_name_new = d.find_element(By.NAME, "Middle_name")
    #                                     middle_name_new.clear()
    #                                     ActionChains(d).click(middle_name_new).perform()
    #                                     for character in "wick":
    #                                         ActionChains(d).send_keys(character).perform()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Last_name")))
    #                                     last_name_new = d.find_element(By.NAME, "Last_name")
    #                                     last_name_new.clear()
    #                                     ActionChains(d).click(last_name_new).perform()
    #                                     for character in "new":
    #                                         ActionChains(d).send_keys(character).perform()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Father_name")))
    #                                     Father_name = d.find_element(By.NAME, "Father_name")
    #                                     Father_name.clear()
    #                                     ActionChains(d).click(Father_name).perform()
    #                                     for character in father_name:
    #                                         ActionChains(d).send_keys(character).perform()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Father_dob")))
    #                                     Father_dob = d.find_element(By.NAME, "Father_dob")
    #                                     Father_dob.clear()    
    #                                     Father_dob.send_keys("01-02-2023")
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Father_mob_no")))
    #                                     Father_mob_no = d.find_element(By.NAME, "Father_mob_no")
    #                                     Father_mob_no.clear()
    #                                     ActionChains(d).click(Father_mob_no).perform()
    #                                     for character in father_mobile:
    #                                         ActionChains(d).send_keys(character).perform()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Father_mail")))
    #                                     Father_mail = d.find_element(By.NAME, "Father_mail")
    #                                     Father_mail.clear()
    #                                     ActionChains(d).click(Father_mail).perform()
    #                                     for character in father_mail:
    #                                         ActionChains(d).send_keys(character).perform()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Father_education")))
    #                                     Father_education = d.find_element(By.NAME, "Father_education")
    #                                     Father_education.clear()
    #                                     ActionChains(d).click(Father_education).perform()
    #                                     for character in father_education:
    #                                         ActionChains(d).send_keys(character).perform()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Father_occupation")))
    #                                     Father_occupation = d.find_element(By.NAME, "Father_occupation")
    #                                     Father_occupation.clear()
    #                                     ActionChains(d).click(Father_occupation).perform()
    #                                     for character in father_occupation:
    #                                         ActionChains(d).send_keys(character).perform()
                                        
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Mother_name")))
    #                                     Mother_name = d.find_element(By.NAME, "Mother_name")
    #                                     Mother_name.clear()
    #                                     ActionChains(d).click(Mother_name).perform()
    #                                     for character in mother_name:
    #                                         ActionChains(d).send_keys(character).perform()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Mother_dob")))
    #                                     Mother_dob = d.find_element(By.NAME, "Mother_dob")
    #                                     Mother_dob.clear()
    #                                     Mother_dob.send_keys("01-02-2023")
                                                                               
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Mother_mob_no")))
    #                                     Mother_mob_no = d.find_element(By.NAME, "Mother_mob_no")
    #                                     Mother_mob_no.clear()
    #                                     ActionChains(d).click(Mother_mob_no).perform()
    #                                     for character in mother_mobile:
    #                                         ActionChains(d).send_keys(character).perform()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Mother_mail")))
    #                                     Mother_mail = d.find_element(By.NAME, "Mother_mail")
    #                                     Mother_mail.clear()
    #                                     ActionChains(d).click(Mother_mail).perform()
    #                                     for character in mother_gmail:
    #                                         ActionChains(d).send_keys(character).perform()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Mother_education")))
    #                                     Mother_education = d.find_element(By.NAME, "Mother_education")
    #                                     Mother_education.clear()
    #                                     ActionChains(d).click(Mother_education).perform()
    #                                     for character in mother_education:
    #                                         ActionChains(d).send_keys(character).perform()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Mother_occupation")))
    #                                     Mother_occupation = d.find_element(By.NAME, "Mother_occupation")
    #                                     Mother_occupation.clear()
    #                                     ActionChains(d).click(Mother_occupation).perform()
    #                                     for character in mother_occupation:
    #                                         ActionChains(d).send_keys(character).perform()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Guardian_name")))
    #                                     Guardian_name = d.find_element(By.NAME, "Guardian_name")
    #                                     Guardian_name.clear()
    #                                     ActionChains(d).click(Guardian_name).perform()
    #                                     for character in guardian_name:
    #                                         ActionChains(d).send_keys(character).perform()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Guardian_dob")))
    #                                     Guardian_dob = d.find_element(By.NAME, "Guardian_dob")
    #                                     Guardian_dob.send_keys("02-02-2023")
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Gaurdian_mail")))
    #                                     Gaurdian_mail = d.find_element(By.NAME, "Gaurdian_mail")
    #                                     Gaurdian_mail.clear()
    #                                     ActionChains(d).click(Gaurdian_mail).perform()
    #                                     for character in guardian_gmail:
    #                                         ActionChains(d).send_keys(character).perform()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Guardian_mob_no")))
    #                                     Guardian_mob_no = d.find_element(By.NAME, "Guardian_mob_no")
    #                                     Guardian_mob_no.clear()
    #                                     ActionChains(d).click(Guardian_mob_no).perform()
    #                                     for character in guardian_mobile:
    #                                         ActionChains(d).send_keys(character).perform()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Guardian_relation")))
    #                                     Guardian_relation = d.find_element(By.NAME, "Guardian_relation")
    #                                     Guardian_relation.clear()
    #                                     ActionChains(d).click(Guardian_relation).perform()
    #                                     for character in "uncle":
    #                                         ActionChains(d).send_keys(character).perform()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Guardian_education")))
    #                                     Guardian_education = d.find_element(By.NAME, "Guardian_education")
    #                                     Guardian_education.clear()
    #                                     ActionChains(d).click(Guardian_education).perform()
    #                                     for character in guardian_education:
    #                                         ActionChains(d).send_keys(character).perform()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Guardian_occupation")))
    #                                     Sibling_edu_input = d.find_element(By.NAME, "Guardian_occupation")
    #                                     Sibling_edu_input.clear()
    #                                     ActionChains(d).click(Sibling_edu_input).perform()
    #                                     for character in guardian_occupation:
    #                                         ActionChains(d).send_keys(character).perform()
                                        
    #                                     wait.until(EC.element_to_be_clickable((By.NAME, "Notes")))
    #                                     Notes = d.find_element(By.NAME, "Notes")
    #                                     Notes.clear()
    #                                     ActionChains(d).click(Notes).perform()
    #                                     for character in notes:
    #                                         ActionChains(d).send_keys(character).perform()
                                            
    #                                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[1]/nav/a/button")))
    #                                     # cancel_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[1]/nav/a/button")
    #                                     # cancel_btn.click()
                                        
    #                                     # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[2]/button")))
    #                                     # back_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[2]/button")
    #                                     # back_btn.click()
                                        
    #                                     # sleep(5)
    #                                     wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[3]/button")))
    #                                     save_btn = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div/form/div[2]/div[3]/button")
    #                                     save_btn.click()
                                                

    #                                     sleep(60)
    
    
    # def test_student_delete(self):
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

    #                 with open('data/students.csv', 'r') as f:
    #                     reader = csv.reader(f)
    #                     # Skip the two header row
    #                     next(reader)
                        
    #                     for row in reader:
    #                         first_name = row[0]
    #                         middle_name = row[1]
    #                         last_name = row[2]
    #                         student_id = row[3]
    #                         aadhaar_no = row[4]
    #                         skills = row[5]
    #                         hobbies = row[6]
    #                         awards = row[7]
    #                         recognitions = row[8]
    #                         email = row[9]
    #                         mobile_no = row[10]
    #                         emergency_no = row[11]
    #                         scar = row[12]
    #                         mole = row[13]
    #                         medical_history = row[14]
    #                         temporary_address = row[15]
    #                         t_city = row[16]
    #                         t_state = row[17]
    #                         t_pincode = row[18]
    #                         perm_address = row[19]
    #                         p_city =row[20]
    #                         p_state =row[21]
    #                         p_pincode =row[22]
    #                         sibling_name =row[23]
    #                         sibling_education =row[24]
                 

    #                         for student_data in students["student_data"]:
                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, student_data["student_module"])))
                                
    #                             calendar_module = d.find_element(By.XPATH, student_data["student_module"])
    #                             calendar_module.click()
    #                             sleep(2)
                                                                
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/div/div/table/tbody")))
                                
    #                             edit_student = d.find_element(By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/div/div/table/tbody")
    #                             li = edit_student.find_elements(By.TAG_NAME, "tr")
    #                             td = li[0].find_elements(By.TAG_NAME, "td")
                                
    #                             index = 0  # index of the button to select
   
    #                             button_elements = td[5].find_elements(By.TAG_NAME, "button")

    #                             if len(button_elements) > index:
    #                                 button_elements[1].click()
    #                             else:
    #                                 print(f"No button found at index {index}")
                                    
    #                             wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/div/button[1]")))
                        
    #                             # confirm_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/div/button[1]")
    #                             # confirm_btn.click()
                                
    #                             cancel_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/div/button[2]")
    #                             cancel_btn.click()
                                
    #                             sleep(5)
                                
                                                                                
    # def test_student_search(self):
        # d = self.driver
        
        # # open csv file
        # with open('data/login.csv', 'r') as f:
        #     # read data
        #     reader = csv.reader(f)
        #     # Skip the header row
        #     next(reader)
            
        #     # loop all values in sheet
        #     for row in reader:
        #         username = row[0]
        #         password = row[1]
                
        #         # loop all values in json
        #         for data in login["login_data"]:
        #             # time.sleep(10)
        #             # navigate to the home page and click login
        #             wait = WebDriverWait(d, timeout=10)
        #             time.sleep(1)
                  
        #             d.get(data['valid_home_link'])
                    
        #             d.find_element(By.LINK_TEXT, "Login").click()
                    
        #             # Wait for the login page to load
        #             wait.until(EC.url_matches(data["valid_login_link"]))

        #             # verify text with assert method
        #             act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
        #             exp_title = data["login_confirm_text"]

        #             self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

        #             # invalid login check
        #             d.find_element(By.NAME, "Username").send_keys(username)
        #             d.find_element(By.NAME, "Password").send_keys(password)
        #             d.find_element(By.XPATH, data["login_btn_locator"]).click()

        #             # time.sleep(2)
        #             # Wait for the page to load after login
        #             wait.until(EC.url_matches(data["valid_dashboard_link"]))
        #             wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
        #             # time.sleep(2)
        #             ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
        #             li_elements = ul_element.find_elements(By.TAG_NAME,"li")
        #             li_elements[0].click() 
                  
        #             wait.until(EC.url_matches(data["valid_dashboard_link"]),)
        #             act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

        #             exp_title = data["dashboard_confirm_text"]

        #             self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

        #             for student_data in students["student_data"]:
                        
        #                 wait.until(EC.element_to_be_clickable((By.XPATH, student_data["student_module"])))
                        
        #                 calendar_module = d.find_element(By.XPATH, student_data["student_module"])
        #                 calendar_module.click()
        #                 sleep(2)
                                                        
                        
        #                 # search_btn = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[1]/div[1]/div/div/input")
        #                 # search_key ="martin"
        #                 # ActionChains(d).click(search_btn).perform()
        #                 # for character in search_key:
        #                 #     ActionChains(d).send_keys(character).perform()
                            
                            
        #                 # wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div/div[1]/div[1]/div/div/input")))
                        
        #                 # pagination = d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div[2]/div/div/div[2]/div/div/div/nav")
        #                 # ul = pagination.find_element(By.TAG_NAME, "ul")
        #                 # li = ul.find_elements(By.TAG_NAME, "li")
        #                 # li[2].click()

        #                 # sleep(5)
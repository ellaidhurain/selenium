import json
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException


with open('config/login_data.json') as f:
    login = json.load(f)
    data = login['login_data']

# Read the JSON file
with open('config/regional_school.json') as f:
    data2 = json.load(f)

data = data2["regional_school_data"]

class TestRegionalSchool(unittest.TestCase):
    
    def setUp(self):
        # Initialize the webdriver
        chrome_options = Options()
        chrome_options.add_argument("--disable-javascript")

        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.maximize_window()
    
    def tearDown(self):
        # Close the browser
        self.driver.quit()
    
    def test_regional_school_update(self):
        d = self.driver
        with open('data/login.csv', 'r') as f:
            reader = csv.reader(f)
            # Skip the header row
            next(reader)
            for row in reader:
                username = row[0]
                password = row[1]
                
                for data in login["login_data"]:
                    # time.sleep(10)
                    # navigate to the home page and click login
                    d.get(data['valid_home_link'])
                    d.find_element(By.LINK_TEXT, "Login").click()
                    wait = WebDriverWait(d, 10)

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
                    li_element = ul_element.find_elements(By.TAG_NAME,"li")
                    li_element[0].click()

                    wait.until(EC.url_matches(data["valid_dashboard_link"]))
                    act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

                    exp_title = data["dashboard_confirm_text"]

                    self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

                    with open('data/regional_school.csv', 'r') as f:
                            reader = csv.reader(f)
                            # Skip the header row
                            next(reader)
                            for row in reader:
                                school_domain = row[0]
                                school_name = row[2]
                                address1 = row[3]
                                address2 = row[4]
                                taluk = row[5]
                                pincode = row[6]    
                                school_phone_no = row[7]
                                school_mail = row[8]
                                no_of_staff = row[9]
                                no_of_student = row[10]
                                
                                for regional_school in data2["regional_school_data"]:
                                    # logout menu
                                    wait.until(EC.visibility_of_all_elements_located((By.XPATH,regional_school["profile_menu_locator"])))
                                    wait.until(EC.element_to_be_clickable((By.XPATH,regional_school["profile_menu_locator"])))
                                    d.find_element(By.XPATH,regional_school["profile_menu_locator"]).click()
                                    
                                    # time.sleep(2)
                                    
                                    settings_ul_element = d.find_element(By.XPATH, regional_school["settings_ul_locator"]) 
                                    settings_li_element = settings_ul_element.find_elements(By.TAG_NAME,"li")
                                    
                                    settings_li_element[0].click()
                                    
                                    wait.until(EC.url_matches(regional_school["valid_profile_link"]))
                                    
                                    act_title = d.find_element(By.XPATH, regional_school["regional_school_confirm_text_locator"]).text
                                    exp_title = regional_school["confirm_text"]

                                    self.assertEqual(act_title, exp_title, f"regional_school view failed: expected '{exp_title}', but got '{act_title}'")
                                    
                                    
                                    wait.until(EC.element_to_be_clickable((By.XPATH,regional_school["regional_school_ul"])))
                                    ul_element = d.find_element(By.XPATH, regional_school["regional_school_ul"])
                                    li_element = ul_element.find_elements(By.TAG_NAME, "li")
                                    btn_element = li_element[1].find_elements(By.CSS_SELECTOR, "button")
                                    
                                    if len(li_element) > 0:
                                        btn_element[0].click()
                                    else:
                                        print("no more element")
                                    
                                    wait.until(EC.element_to_be_clickable((By.NAME, "Domain_name")))                                                                                                  
                                                     
                                    sd = d.find_element(By.NAME, "Domain_name")
                                   
                                    actions = ActionChains(d)
                                    actions.click(sd).perform()
                                    d.execute_script("arguments[0].value = arguments[1];", sd, school_domain)
                                    d.execute_script("arguments[0].dispatchEvent(new Event('change'));", sd)
                                    d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", sd, school_domain)            
                                   
                                    sn = d.find_element(By.NAME, "School_name")
                                    actions = ActionChains(d)
                                    actions.click(sn).perform()
                                    d.execute_script("arguments[0].value = arguments[1];", sn, school_name)
                                    d.execute_script("arguments[0].dispatchEvent(new Event('change'));", sn)
                                    d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", sn, school_name)
                                    
                                    ad1 = d.find_element(By.NAME, "address1")
                                    actions = ActionChains(d)
                                    actions.click(ad1).perform()
                                    d.execute_script("arguments[0].value = arguments[1];", ad1, address1)
                                    d.execute_script("arguments[0].dispatchEvent(new Event('change'));", ad1)
                                    d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", ad1, address1)
                                    

                                    ad2 = d.find_element(By.NAME, "address2")
                                    actions = ActionChains(d)
                                    actions.click(ad2).perform()
                                    d.execute_script("arguments[0].value = arguments[1];", ad2, address2)
                                    d.execute_script("arguments[0].dispatchEvent(new Event('change'));", ad2)
                                    d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", ad2, address2)
                                    
                                    
                                    tk = d.find_element(By.NAME,"Taluk")
                                    actions = ActionChains(d)
                                    actions.click(tk).perform()
                                    d.execute_script("arguments[0].value = arguments[1];", tk, taluk)
                                    d.execute_script("arguments[0].dispatchEvent(new Event('change'));", tk)
                                    d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", tk, taluk)
                                    
                                    
                                    wait.until(EC.element_to_be_clickable((By.XPATH,regional_school["school_state_input"])))
                                    state = d.find_element(By.XPATH, regional_school["school_state_input"])
                                    state.click()
                                    
                                    wait.until(EC.element_to_be_clickable((By.XPATH,regional_school["school_state_input_ul"])))
                                    ul_element = d.find_element(By.XPATH, regional_school["school_state_input_ul"])
                                    li_element = ul_element.find_elements(By.TAG_NAME, "li")
                                    li_element[0].click()
                                    
                                    wait.until(EC.element_to_be_clickable((By.XPATH,regional_school["school_district_input"])))
                                    
                                    district = d.find_element(By.XPATH, regional_school["school_district_input"])
                                    district.click()
                                    
                                    # time.sleep(10)
                                    wait.until(EC.element_to_be_clickable((By.XPATH,regional_school["school_district_input_ul"])))
                                    ul_element = d.find_element(By.XPATH, regional_school["school_district_input_ul"])
                                    li_element = ul_element.find_elements(By.TAG_NAME, "li")
                                    li_element[0].click()
                                                       
                                                         
                                    wait.until(EC.element_to_be_clickable((By.NAME, "Pincode")))                               
                                    pin = d.find_element(By.NAME, "Pincode")
                                    actions = ActionChains(d)
                                    actions.click(pin).perform()
                                    d.execute_script("arguments[0].value = arguments[1];", pin, pincode)
                                    d.execute_script("arguments[0].dispatchEvent(new Event('change'));", pin)
                                    d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", pin, pincode)
                                            
                                    # time.sleep(2)
                                    wait.until(EC.element_to_be_clickable((By.XPATH, regional_school["school_next_btn"])))
                                    d.find_element(By.XPATH, regional_school["school_next_btn"]).click()
                                                                                                      
                                    # d.find_element(By.XPATH, regional_school["school_cancel_btn"]).click()
                                    wait.until(EC.visibility_of_element_located((By.NAME, "School_mob_no")))                               
                                    
                                    ph = d.find_element(By.NAME, "School_mob_no")
                                    actions = ActionChains(d)
                                    actions.click(ph).perform()
                                    d.execute_script("arguments[0].value = arguments[1];", ph, school_phone_no)
                                    d.execute_script("arguments[0].dispatchEvent(new Event('change'));", ph)
                                    d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", ph, school_phone_no)
                                    
                                    
                                    mail = d.find_element(By.XPATH, regional_school["school_mail_input"])
                                    mail.clear()
                                    mail.send_keys(school_mail)
                                    # actions = ActionChains(d)
                                    # actions.click(mail).perform()
                                    # d.execute_script("arguments[0].value = arguments[1];", mail, school_mail)
                                    # d.execute_script("arguments[0].dispatchEvent(new Event('change'));", mail)
                                    # d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", mail, school_mail)
                                    
                                    # time.sleep(10)
                                    wait.until(EC.element_to_be_clickable((By.XPATH,regional_school["school_type_input"])))
                                    st = d.find_element(By.XPATH, regional_school["school_type_input"])
                                    st.click()
                                    
                                    ul_element = d.find_element(By.XPATH, regional_school["school_type_input_ul"])
                                    li_element = ul_element.find_elements(By.TAG_NAME, "li")
                                    li_element[0].click()
                                    
                                    wait.until(EC.element_to_be_clickable((By.XPATH,regional_school["school_governance_input"])))
                                    st = d.find_element(By.XPATH, regional_school["school_governance_input"])
                                    st.click()
                                    
                                   
                                    wait.until(EC.element_to_be_clickable((By.XPATH,regional_school["school_governance_input"])))
                                    ul_element = d.find_element(By.XPATH, regional_school["school_governance_input_ul"])
                                    li_element = ul_element.find_elements(By.TAG_NAME, "li")
                                    li_element[1].click()
                                    
                                    wait.until(EC.element_to_be_clickable((By.XPATH,regional_school["school_board_of_education_input"])))
                                    st = d.find_element(By.XPATH, regional_school["school_board_of_education_input"])
                                    st.click()
                                    
                                    wait.until(EC.element_to_be_clickable((By.XPATH,regional_school["school_board_of_education_input"])))
                                    ul_element = d.find_element(By.XPATH, regional_school["school_board_of_education_input_ul"])
                                    li_element = ul_element.find_elements(By.TAG_NAME, "li")
                                    li_element[1].click()
                                    
                                    wait.until(EC.element_to_be_clickable((By.XPATH,regional_school["school_gender_type_input"])))
                                    st = d.find_element(By.XPATH, regional_school["school_gender_type_input"])
                                    st.click()
                                    
                                    wait.until(EC.element_to_be_clickable((By.XPATH,regional_school["school_gender_type_input"])))
                                    ul_element = d.find_element(By.XPATH, regional_school["school_gender_type_input_ul"])
                                    li_element = ul_element.find_elements(By.TAG_NAME, "li")
                                    li_element[1].click()
                                    
                                    wait.until(EC.element_to_be_clickable((By.XPATH, regional_school["school_no_of_staff_input"] )))
                                    staff = d.find_element(By.XPATH, regional_school["school_no_of_staff_input"])
                                    staff.clear()
                                    staff.send_keys(no_of_staff)
                                    
                                    # actions = ActionChains(d)
                                    # actions.click(staff).perform()
                                    # d.execute_script("arguments[0].value = arguments[1];", staff, no_of_staff)
                                    # d.execute_script("arguments[0].dispatchEvent(new Event('change'));", staff)
                                    # d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", staff, no_of_staff)
                                    
                                    student = d.find_element(By.XPATH, regional_school["school_no_of_student_input"])
                                    # student.clear()
                                    # student.send_keys(no_of_student)
                                    actions = ActionChains(d)
                                    actions.click(student).perform()
                                    d.execute_script("arguments[0].value = arguments[1];", student, no_of_student)
                                    d.execute_script("arguments[0].dispatchEvent(new Event('change'));", student)
                                    d.execute_script("const el = arguments[0]; const clone = el.cloneNode(true); el.parentNode.replaceChild(clone, el); clone.value = arguments[1];", student, no_of_student)
                                    
                                    wait.until(EC.element_to_be_clickable((By.XPATH,regional_school["school_highest_standard_input"])))
                                    st = d.find_element(By.XPATH, regional_school["school_highest_standard_input"])
                                    st.click()
                                    
                                    wait.until(EC.element_to_be_clickable((By.XPATH,regional_school["school_highest_standard_input"])))
                                    ul_element = d.find_element(By.XPATH, regional_school["school_highest_standard_input_ul"])
                                    li_element = ul_element.find_elements(By.TAG_NAME, "li")
                                    li_element[1].click()
                                    
                                    # # time.sleep(5)
                                    wait.until(EC.element_to_be_clickable((By.XPATH, regional_school["school_save_btn"])))
                                    d.find_element(By.XPATH, regional_school["school_save_btn"]).click()
                                    
                                    # time.sleep(5)
                                    # wait.until(EC.element_to_be_clickable((By.XPATH, regional_school["school_back_btn"])))
                                    # d.find_element(By.XPATH, regional_school["school_back_btn"]).click()
                                    
                                    # wait.until(EC.visibility_of_element_located((By.XPATH, regional_school["school_cancel_btn"])))
                                    # d.find_element(By.XPATH, regional_school["school_cancel_btn"]).click()
                                    
    #                                 time.sleep(2)
                                    
    #                                 # # text = d.find_element(By.XPATH, regional_school["pop_up_locator"]).text
    #                                 # # d.find_element(By.XPATH, regional_school["pop_up_txt"])
                                    
                        
                        

#     # def test_regional_school_active(self):
#     #     d = self.driver
#     #     with open('data/login.csv', 'r') as f:
#     #         reader = csv.reader(f)
#     #         # Skip the header row
#     #         next(reader)
#     #         for row in reader:
#     #             username = row[0]
#     #             password = row[1]
                
#     #             for data in login["login_data"]:
#     #                 # time.sleep(10)
#     #                 # navigate to the home page and click login
#     #                 d.get(data['valid_home_link'])
#     #                 d.find_element(By.LINK_TEXT, "Login").click()
#     #                 wait = WebDriverWait(d, 10)

#     #                 # Wait for the login page to load
#     #                 wait.until(EC.url_matches(data["valid_login_link"]))

#     #                 # verify text with assert method
#     #                 act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
#     #                 exp_title = data["login_confirm_text"]

#     #                 self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

#     #                 # invalid login check
#     #                 d.find_element(By.NAME, "Username").send_keys(username)
#     #                 d.find_element(By.NAME, "Password").send_keys(password)
#     #                 d.find_element(By.XPATH, data["login_btn_locator"]).click()

#     #                 # time.sleep(2)
#     #                 # Wait for the page to load after login
#     #                 wait.until(EC.url_matches(data["valid_dashboard_link"]))
#     #                 wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
#     #                 # time.sleep(2)
#     #                 ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
#     #                 li_element = ul_element.find_elements(By.TAG_NAME,"li")
#     #                 li_element[0].click()

#     #                 wait.until(EC.url_matches(data["valid_dashboard_link"]))
#     #                 act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

#     #                 exp_title = data["dashboard_confirm_text"]

#     #                 self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

#     #                 for regional_school in data2["regional_school_data"]:
#     #                     wait.until(EC.visibility_of_all_elements_located((By.XPATH,regional_school["profile_menu_locator"])))
#     #                     wait.until(EC.element_to_be_clickable((By.XPATH,regional_school["profile_menu_locator"])))
#     #                     d.find_element(By.XPATH,regional_school["profile_menu_locator"]).click()
                        
#     #                     # time.sleep(2)
                        
#     #                     settings_ul_element = d.find_element(By.XPATH, regional_school["settings_ul_locator"]) 
#     #                     settings_li_element = settings_ul_element.find_elements(By.TAG_NAME,"li")
                        
#     #                     settings_li_element[0].click()
                        
#     #                     wait.until(EC.url_matches(regional_school["valid_profile_link"]))
                        
#     #                     act_title = d.find_element(By.XPATH, regional_school["regional_school_confirm_text_locator"]).text
#     #                     exp_title = regional_school["confirm_text"]

#     #                     self.assertEqual(act_title, exp_title, f"regional_school view failed: expected '{exp_title}', but got '{act_title}'")
                        
                        
#     #                     wait.until(EC.element_to_be_clickable((By.XPATH,regional_school["regional_school_ul"])))
#     #                     # Find the first li element
#     #                     ul_element = d.find_element(By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div/ul")
#     #                     li_element = ul_element.find_elements(By.TAG_NAME,"li")
                        
#     #                     # Find the last div element inside the li element
#     #                     div_elements = li_element[2].find_elements(By.TAG_NAME, "div")
#     #                     last_div_element = div_elements[-1]                                        
#     #                     last_div_element.click()
                        
#     #                     verify_school_txt = "Campuzone School"
#     #                     expected_school_txt = d.find_element(By.XPATH,"//*[@id='root']/div[2]/header/div/h6/p").text

                        
#     #                     self.assertEqual(verify_school_txt, expected_school_txt, f"dashboard page open failed: expected '{expected_school_txt}', but got '{verify_school_txt}'")

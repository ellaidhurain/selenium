import json
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

with open('config/login_data.json') as f:
    login = json.load(f)
    data = login['login_data']
    

# Read the JSON file
with open('config/profile_data.json') as f:
    data2 = json.load(f)

data = data2["profile_data"]

class TestProfile(unittest.TestCase):
    
    def setUp(self):
        # Initialize the webdriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    
    def tearDown(self):
        # Close the browser
        self.driver.quit()
    
    def test_profile(self):
        d = self.driver
        with open('data/login.csv', 'r') as f:
            reader = csv.reader(f)
            # Skip the header row
            next(reader)
            for row in reader:
                username = row[4]
                password = row[5]
                
                for data in login["login_data"]:
                    # time.sleep(10)
                    # navigate to the home page and click login
                    d.get(data['valid_home_link'])
                    d.find_element(By.LINK_TEXT, "Login").click()
                    wait = WebDriverWait(d, 10)

                    # Wait for the login page to load
                    wait.until(EC.url_matches(data["valid_login_link"]))

                    # verify text with assert method
                    # act_title = d.find_element(By.XPATH, data["login_confirm_text_locator"]).text
                    # exp_title = data["login_confirm_text"]

                    # self.assertEqual(act_title, exp_title, f"login page open failed: expected '{exp_title}', but got '{act_title}'")

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

                    # wait.until(EC.url_matches(data["valid_dashboard_link"]))
                    # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

                    # exp_title = data["dashboard_confirm_text"]

                    # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

                    with open('data/profile.csv', 'r') as f:
                            reader = csv.reader(f)
                            # Skip the header row
                            next(reader)
                            for row in reader:
                                first_name = row[0]
                                middle_name = row[1]
                                last_name = row[2]
                                aadhaar_no = row[3]
                                address = row[4]
                                
                                for profile in data2["profile_data"]:
                                    # logout menu
                                    wait.until(EC.visibility_of_all_elements_located((By.XPATH,profile["profile_menu_locator"])))
                                    d.find_element(By.XPATH,profile["profile_menu_locator"]).click()
                                    
                                    # time.sleep(2)
                                    
                                    settings_ul_element = d.find_element(By.XPATH, profile["settings_ul_locator"]) 
                                    settings_li_element = settings_ul_element.find_elements(By.TAG_NAME,"li")
                                    
                                    settings_li_element[0].click()
                                    
                                    wait.until(EC.url_matches(profile["valid_profile_link"]))
                                    
                                    act_title = d.find_element(By.XPATH, profile["profile_confirm_text_locator"]).text
                                    exp_title = profile["profile_confirm_text"]

                                    self.assertEqual(act_title, exp_title, f"profile view failed: expected '{exp_title}', but got '{act_title}'")

                                    # EDIT
                                    # wait.until(EC.element_to_be_clickable((By.XPATH,profile["profile_edit_button_locator"])))
                                    
                                    # d.find_element(By.XPATH,profile["profile_edit_button_locator"]).click()
                                    
                                    # ADD                               
                                    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div/ul/div[2]/div[2]/button")))
                                    
                                    d.find_element(By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div/ul/div[2]/div[2]/button").click()
                                                                    
                                    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div/div/ul/div[1]/div/div")))
                                                    
                                    act_text = d.find_element(By.XPATH,profile["profile_edit_page_text_locator"]).text
                                    exp_text = "Edit Your Details"
                                    
                                    self.assertEqual(act_text, exp_text, f"profile page edit open failed: expected '{exp_title}', but got '{act_title}'")
                                                
                                    wait.until(EC.visibility_of_all_elements_located((By.XPATH,"/html/body/div/div[2]/main/div[2]/div/div/ul/div[1]/div/div")))
                                    
                                    fn = d.find_element(By.NAME, "First_name")
                                    fn.click()
                                    fn.send_keys(Keys.CONTROL + "a")
                                    fn.send_keys(Keys.BACKSPACE)
                                    ActionChains(d).click(fn).perform()
                                    for character in first_name:
                                        ActionChains(d).send_keys(character).perform()
                            
                                    mn = d.find_element(By.NAME, "Middle_name")
                                    mn.click()
                                    mn.send_keys(Keys.CONTROL + "a")
                                    mn.send_keys(Keys.BACKSPACE)
                                    ActionChains(d).click(mn).perform()
                                    for character in middle_name:
                                        ActionChains(d).send_keys(character).perform()
                                  
                                    # time.sleep(2)
                                    ln = d.find_element(By.NAME, "Last_name")
                                    ln.click()
                                    ln.send_keys(Keys.CONTROL + "a")
                                    ln.send_keys(Keys.BACKSPACE)
                                    ActionChains(d).click(ln).perform()
                                    for character in last_name:
                                        ActionChains(d).send_keys(character).perform()
                                  
                                    aadhar = d.find_element(By.NAME, "Aadhaar_no")
                                    aadhar.click()
                                    aadhar.send_keys(Keys.CONTROL + "a")
                                    aadhar.send_keys(Keys.BACKSPACE)
                                    ActionChains(d).click(aadhar).perform()
                                    for character in aadhaar_no:
                                        ActionChains(d).send_keys(character).perform()
                                  
                                    addr = d.find_element(By.NAME, "Address")
                                    addr.click()
                                    addr.send_keys(Keys.CONTROL + "a")
                                    addr.send_keys(Keys.BACKSPACE)
                                    ActionChains(d).click(addr).perform()
                                    for character in address:
                                        ActionChains(d).send_keys(character).perform()
                                   
                                    wait.until(EC.element_to_be_clickable((By.XPATH, profile["save_btn_input"])))
                                    d.find_element(By.XPATH, profile["save_btn_input"]).click()
                                    
                                    
                                    time.sleep(20)
                                    # d.find_element(By.XPATH, profile["cancel_btn_input"]).click()
                                    
                                    # text = d.find_element(By.XPATH, profile["pop_up_locator"]).text
                                    # d.find_element(By.XPATH, profile["pop_up_txt"])
                                    
                                    
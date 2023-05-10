import json
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
import csv
from selenium.webdriver.common.keys import Keys

# Read the JSON file
with open('config/login_data.json') as f:
    login = json.load(f)
    data = login['login_data']
    
# Read the JSON file
with open('config/news_data.json') as f:
    news = json.load(f)

class TestNews(unittest.TestCase):
    
    def setUp(self):
        # Initialize the webdriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    
    def tearDown(self):
        # Close the browser
        self.driver.quit()
       
    # add news
    def test_add_news(self):
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
                    # wait.until(EC.visibility_of_all_elements_located((By.XPATH, data["school_list_ul_locator"])))
                    # # time.sleep(2)
                    # ul_element = d.find_element(By.XPATH,data["school_list_ul_locator"])
                    # li_element = ul_element.find_elements(By.TAG_NAME,"li")
                    # li_element[0].click()

                    # wait.until(EC.url_matches(data["valid_dashboard_link"]))
                    # act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

                    # exp_title = data["dashboard_confirm_text"]

                    # self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

                    # time.sleep(1)
                
                            
                    
                    for news_data in news['news_data']:        
                        # find dropdown menu
                        wait.until(EC.visibility_of_element_located((By.XPATH ,news_data["profile_menu_locator"])))
                        
                        d.find_element(By.XPATH,news_data["profile_menu_locator"]).click()
                        
                        time.sleep(1)
                        
                        settings_ul_element = d.find_element(By.XPATH, news_data["settings_ul_locator"]) 
                        settings_li_element = settings_ul_element.find_elements(By.TAG_NAME,"li")
                        
                        # click first index value in ul list
                        settings_li_element[1].click()
                        
                        wait.until(EC.visibility_of_element_located((By.XPATH, news_data["news_title_locator"])))
                        
                        act_title = d.find_element(By.XPATH, news_data["news_title_locator"]).text
                        exp_title = "News"

                        self.assertEqual(act_title, exp_title, f"news view failed: expected '{exp_title}', but got '{act_title}'")
                        
                        # verify news page text
                        element_locator = (By.XPATH, news_data["news_title_locator"])
                        
                        with open('data/news.csv', 'r') as f:
                            reader = csv.reader(f)
                            # Skip the header row
                            next(reader)
                            for row in reader:
                                news_title = row[0]
                                news_description = row[1]
                                start_date= row[2]
                                end_date= row[3]

                                wait.until(EC.visibility_of_all_elements_located(element_locator))
                                # click add news
                                d.find_element(By.XPATH, news_data["add_news_btn_locator"]).click()                
                                            
                                act_text = d.find_element(By.XPATH, news_data["news_confirm_txt_locator"]).text
                                exp_text = "Add News"
                                            
                                self.assertEqual(act_text, exp_text, f"News page edit open failed: expected '{exp_title}', but got '{act_title}'")
                                            
                                title = wait.until(EC.element_to_be_clickable((By.XPATH, news_data["news_title_input_locator"])))
                                title.send_keys(news_title)
                                            
                                description = wait.until(EC.element_to_be_clickable((By.XPATH, news_data["news_description_locator"])))
                                description.send_keys(news_description)
                                            
                                # start date end date
                                date1 = wait.until(EC.element_to_be_clickable((By.XPATH, news_data["start_date_locator"])))
                                date1.send_keys(start_date)
                                            
                                date2 = wait.until(EC.element_to_be_clickable((By.XPATH, news_data["end_date_locator"])))
                                date2.send_keys(end_date)
                                            
                                role_group = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/main/div[2]/div[2]/div[1]/div[4]/div/form/div[1]/div[5]/div/div/div")))
                                role_group.click()
                                            
                                role_group_ul = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[3]/ul")))
                                role_li_element = role_group_ul.find_elements(By.TAG_NAME,"li")
                                role_li_element[1].click()
                                role_li_element[3].click()
                                
                                role_group_ul.send_keys(Keys.ESCAPE)
                                    
                                # wait for the save button to become clickable
                                save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, news_data["news_save_btn_locator"])))
                                save_btn.click()
                                            
                                time.sleep(2)
                                # wait for success message
                                # success_message = wait.until(EC.visibility_of_element_located((By.XPATH, news_data["news_success_message_locator"])))
                                # assert success_message.text == "Successfully Added!"
                                
                                

    # search news
    # def test_search_news(self):
    #     d = self.driver
    #     with open('data/login.csv', 'r') as f:
    #         reader = csv.reader(f)
    #         # Skip the header row
    #         next(reader)
    #         for row in reader:
    #             username = row[0]
    #             password = row[1]
                
    #             for data in login["login_data"]:
    #                 # time.sleep(10)
    #                 # navigate to the home page and click login
    #                 d.get(data['valid_home_link'])
    #                 d.find_element(By.LINK_TEXT, "Login").click()
    #                 wait = WebDriverWait(d, 10)

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
    #                 li_element = ul_element.find_elements(By.TAG_NAME,"li")
    #                 li_element[0].click()

    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]))
    #                 act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 exp_title = data["dashboard_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 # time.sleep(1)
    #                 with open('data/news.csv', 'r') as f:
    #                     reader = csv.reader(f)
    #                     # Skip the header row
    #                     next(reader)
    #                     for row in reader:
    #                         search_keyword = row[4]
    #                         sort_by_start_date = row[5]
    #                         sort_by_end_date= row[6]
                    
    #                         for news_data in news['news_data']:        
    #                             # find dropdown menu
    #                             d.find_element(By.XPATH,news_data["profile_menu_locator"]).click()
                                
    #                             time.sleep(1)
                                
    #                             settings_ul_element = d.find_element(By.XPATH, news_data["settings_ul_locator"]) 
    #                             settings_li_element = settings_ul_element.find_elements(By.TAG_NAME,"li")
                                
    #                             # click first index value in ul list
    #                             settings_li_element[1].click()
                                
    #                             wait.until(EC.url_matches(news_data["valid_news_link"]))
                                
    #                             act_title = d.find_element(By.XPATH, news_data["news_title_locator"]).text
    #                             exp_title = "News"

    #                             self.assertEqual(act_title, exp_title, f"news view failed: expected '{exp_title}', but got '{act_title}'")
                                
    #                             # verify news page text
    #                             element_locator = (By.XPATH, news_data["news_title_locator"])

    #                             wait.until(EC.visibility_of_all_elements_located(element_locator))
                                
    #                             for search_data in news["search_news_data"]:
    #                                 search = d.find_element(By.XPATH, search_data["search_bar_locator"])
    #                                 # search.send_keys(search_keyword)
    #                                 # search.clear()
                                    
    #                                 wait.until(EC.visibility_of_element_located((By.XPATH, search_data["sort_by_start_date_locator"]))) 
                                    
    #                                 # time.sleep(2)
    #                                 start_date_input = d.find_element(By.XPATH, search_data["sort_by_start_date_locator"])
    #                                 start_date_input.send_keys(sort_by_start_date)
    #                                 start_date_input.clear()
                                    
    #                                 time.sleep(2)
    #                                 wait.until(EC.visibility_of_element_located((By.XPATH, search_data["sort_by_end_date_locator"]))) 
                                    
    #                                 end_date = d.find_element(By.XPATH, search_data["sort_by_end_date_locator"])
    #                                 end_date.send_keys(sort_by_end_date)
    #                                 start_date_input.clear()
                                                               
    # # update news
    # def test_update_news(self):
    #     d = self.driver
    #     with open('data/login.csv', 'r') as f:
    #         reader = csv.reader(f)
    #         # Skip the header row
    #         next(reader)
    #         for row in reader:
    #             username = row[0]
    #             password = row[1]
                
    #             for data in login["login_data"]:
    #                 # time.sleep(10)
    #                 # navigate to the home page and click login
                    
    #                 d.get(data['valid_home_link'])
    #                 d.find_element(By.LINK_TEXT, "Login").click()
    #                 wait = WebDriverWait(d, 10)

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
    #                 li_element = ul_element.find_elements(By.TAG_NAME,"li")
    #                 li_element[0].click()

    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]))
    #                 act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 exp_title = data["dashboard_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")

    #                 # time.sleep(1)
    #                 with open('data/news.csv', 'r') as f:
    #                     reader = csv.reader(f)
    #                     # Skip the header row
    #                     next(reader)
    #                     for row in reader:
    #                         news_title = row[0]
    #                         news_description = row[1]
    #                         start_date= row[2]
    #                         end_date= row[3]
                                    
    #                         for news_data in news['edit_news_data']:        
    #                             # find dropdown menu
    #                             d.find_element(By.XPATH,news_data["profile_menu_locator"]).click()
                                
    #                             time.sleep(1)
                                
    #                             settings_ul_element = d.find_element(By.XPATH, news_data["settings_ul_locator"]) 
    #                             settings_li_element = settings_ul_element.find_elements(By.TAG_NAME,"li")
                                
    #                             # click first index value in ul list
    #                             settings_li_element[1].click()
                                
    #                             wait.until(EC.url_matches(news_data["valid_news_link"]))
                                
    #                             act_title = d.find_element(By.XPATH, news_data["news_title_locator"]).text
    #                             exp_title = "News"

    #                             self.assertEqual(act_title, exp_title, f"news view failed: expected '{exp_title}', but got '{act_title}'")
                                
    #                             # verify news page text
    #                             element_locator = (By.XPATH, news_data["news_title_locator"])

    #                             wait.until(EC.visibility_of_all_elements_located(element_locator))
                                
    #                             news_ul_element = d.find_element(By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div[2]/div[1]/ul")
    #                             news_li_elements = news_ul_element.find_elements(By.TAG_NAME, "li")
    #                             button = news_li_elements[1].find_elements(By.CSS_SELECTOR,'button')[1]
    #                             button.click()
                                
                                            
    #                             act_text = d.find_element(By.XPATH, news_data["news_confirm_txt_locator"]).text
    #                             exp_text = "Edit News"
                                            
    #                             self.assertEqual(act_text, exp_text, f"News page edit open failed: expected '{exp_title}', but got '{act_title}'")
                                            
    #                             wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div[2]/div[1]/div[4]/div/form/div[1]")))
                                
    #                             # title
    #                             title =d.find_element(By.XPATH, news_data["news_title_input_locator"])
    #                             d.execute_script("arguments[0].value = arguments[1];", title, news_title)
                                
    #                             # description
                                
    #                             description = d.find_element(By.XPATH, news_data["news_description_locator"])
    #                             d.execute_script("arguments[0].value = arguments[1];", description, news_description)
                                
    #                             # start date 
    #                             date1 = d.find_element(By.XPATH, news_data["start_date_locator"])
    #                             d.execute_script("arguments[0].value = arguments[1];", date1, start_date)
                                
    #                             # end date
    #                             date2 = d.find_element(By.XPATH, news_data["end_date_locator"])
    #                             d.execute_script("arguments[0].value = arguments[1];", date2, end_date)
                                            
    #                             role_group = wait.until(EC.visibility_of_element_located((By.XPATH, news_data["role_group_locator"])))
    #                             role_group.click()
                                            
    #                             try:
    #                                 role_group_dt = wait.until(EC.visibility_of_element_located((By.XPATH, news_data["news_role_ul_list_locator"])))
    #                                 role_li_element = role_group_dt.find_elements(By.TAG_NAME, "li")

    #                                 if len(role_li_element) >= 4:
            
    #                                         role_li_element[0].click()
    #                                         role_li_element[2].click()
    #                                         role_li_element[3].click()
    #                                         role_li_element[4].click()
                                          
    #                                         time.sleep(2)
                                  
    #                                 else:
    #                                     print("Not enough elements in role_li_element list.")
    #                             except Exception as e:
    #                                 print(e)
                                
    #                             # time.sleep(1)          
                        
    #                             role_ok_btn = wait.until(EC.element_to_be_clickable((By.XPATH, news_data["news_role_ok_btn_locator"])))
    #                             role_ok_btn.click()
                                
    #                             time.sleep(2)
                                
    #                             # # file_btn = wait.until(EC.visibility_of_element_located((By.XPATH, news_data["choose_file_locator"])))
    #                             # # file_btn.click()    
                                
    #                             # time.sleep(1)  
    #                             # # wait for the save button to become clickable
    #                             save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, news_data["news_save_btn_locator"])))
    #                             save_btn.click()
                                
                                
    #                             # cancel_btn = wait.until(EC.element_to_be_clickable((By.XPATH, news_data["news_close_btn_locator"])))
    #                             # cancel_btn.click()
                                            
                                            
    #                             time.sleep(2)
    #                             # wait for success message
    #                             success_message = wait.until(EC.visibility_of_element_located((By.XPATH, news_data["news_success_message_locator"])))
    #                             assert success_message.text == "Successfully Updated!"
                                
    #                             # wait.until(EC.element_to_be_clickable((By.XPATH,news_data["pagination_btn_locator"])))
    #                             # ul_element = d.find_element(By.XPATH, news_data["pagination_btn_locator"])
    #                             # li_element = d.find_elements(By.TAG_NAME, "li")
                                
    #                             # if len(li_element) > 0:
    #                             #     li_element[1].click()
    #                             #     time.sleep(2)
    #                             # else:
    #                             #     print("no li element found!")
                                
    # delete news
    # def test_delete_news(self):
    #     d = self.driver
    #     with open('data/login.csv', 'r') as f:
    #         reader = csv.reader(f)
    #         # Skip the header row
    #         next(reader)
    #         for row in reader:
    #             username = row[0]
    #             password = row[1]
                
    #             for data in login["login_data"]:
    #                 # time.sleep(10)
    #                 # navigate to the home page and click login
                    
    #                 d.get(data['valid_home_link'])
    #                 d.find_element(By.LINK_TEXT, "Login").click()
    #                 wait = WebDriverWait(d, 10)

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
    #                 li_element = ul_element.find_elements(By.TAG_NAME,"li")
    #                 li_element[0].click()

    #                 wait.until(EC.url_matches(data["valid_dashboard_link"]))
    #                 act_title = d.find_element(By.XPATH, data["dashboard_confirm_text_locator"]).text

    #                 exp_title = data["dashboard_confirm_text"]

    #                 self.assertEqual(act_title, exp_title, f"dashboard page open failed: expected '{exp_title}', but got '{act_title}'")
                                    
    #                 for news_data in news['edit_news_data']:        
    #                     # find dropdown menu
    #                     d.find_element(By.XPATH,news_data["profile_menu_locator"]).click()
                        
    #                     # time.sleep(1)
                        
    #                     settings_ul_element = d.find_element(By.XPATH, news_data["settings_ul_locator"]) 
    #                     settings_li_element = settings_ul_element.find_elements(By.TAG_NAME,"li")
                        
    #                     # click first index value in ul list
    #                     settings_li_element[1].click()
                        
    #                     wait.until(EC.url_matches(news_data["valid_news_link"]))
                        
    #                     act_title = d.find_element(By.XPATH, news_data["news_title_locator"]).text
    #                     exp_title = "News"

    #                     self.assertEqual(act_title, exp_title, f"news view failed: expected '{exp_title}', but got '{act_title}'")
                        
    #                     # verify news page text
    #                     element_locator = (By.XPATH, news_data["news_title_locator"])

    #                     wait.until(EC.visibility_of_all_elements_located(element_locator))
                        
    #                     news_ul_element = d.find_element(By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div[2]/div[1]/ul")
    #                     news_li_elements = news_ul_element.find_elements(By.TAG_NAME, "li")
    #                     button = news_li_elements[1].find_elements(By.CSS_SELECTOR,'button')[0]
    #                     button.click()
                        
    #                     wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='root']/div[2]/main/div[2]/div[2]/div[1]/div[4]/div/form/h6")))
                        
    #                     for news_data in news['delete_news_data']:   
    #                         # d.find_element(By.XPATH, news_data["cancel_btn_locator"]).click()
    #                         d.find_element(By.XPATH, news_data["sure_btn_locator"]).click()
                            
    #                         time.sleep(5)
                            
    #                         success_message = wait.until(EC.visibility_of_element_located((By.XPATH, news_data["news_success_message_locator"])))
    #                         assert success_message.text == "Successfully Removed!"

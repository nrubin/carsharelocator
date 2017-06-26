import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from time import sleep

chrome_path = r"/Users/noam/Projects/carshare/scraping/chromedriver"
options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.geolocation" :2}
# options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_path,chrome_options=options)
driver.get("https://www.enterprisecarshare.com/us/en/login.html")

# Since we disabled automatic location, we should pick CA to get the San Francisco program
state_select = Select(driver.find_element_by_name("state"))
state_select.select_by_visible_text("California")
sleep(0.6)
program_select = Select(driver.find_element_by_name("program"))
program_select.select_by_visible_text("San Francisco")
sleep(2.5)
driver.find_element_by_id("program-continue-btn").click()

#login page
sleep(1.0)
username = "238390"
password = "icNk9GUpT#ksa2dDHPpHWhzc9"
driver.find_element_by_name("loginName").send_keys(username)
sleep(0.8)
driver.find_element_by_name("password").send_keys(password)
sleep(0.3)
driver.find_element_by_id("login-form-button-container").click()
sleep(10)

print "showing all results"
#after login, need to enable showing all results for proper crawling
driver.find_element_by_id("search_results_results_filter__show_everything_").click()
sleep(0.8)
driver.find_element_by_id("res_filter_search_button").click()
print "just clicked search button"

print "beginning to parse list pages"
page_count = 0
car_lists = []
next_button_appeared = True

while next_button_appeared:
    print "sleeping for 20 seconds "
    sleep(20)
    print "scraping this page"
    driver.execute_script(open("./list_parse.js","r").read())
    list_data = driver.execute_script("return data;")    
    car_lists.append(list_data)
    page_count += 1
    print "scraped %s pages of an estimated 17" % (page_count)
    print "trying to find next button"
    try:
        next_button = WebDriverWait(driver, 25).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "imageButton_next")))
        sleep(5) #the next button is css hidden once it loads, so we need to wait just a lil bit becofre clicking it
        next_button.click()
        print 'clicked next button'
    except:
        next_button_appeared = False

print car_lists

# sleep(1.3)

# set condition for next button appearing by timeout
# while loop while button keeps appearing
# when you hit the timeout set the while condition to false and print results

# map page
# next steps: none,really
# driver.find_element_by_css_selector("div#rightCol > div#header > ul > li > a[onclick*='map']").click()
# sleep(20)
# try:
#     driver.execute_script(open("./map_parse.js","r").read())
# except:
#     pass
# gps_data = driver.execute_script("return gps_data;")
# print gps_data
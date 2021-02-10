from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "E:/Python/WebDriver/chromedriver.exe"
firefox_driver_path = "E:/Python/WebDriver/geckodriver.exe"
opera_driver_path = "E:/Python/WebDriver/operadriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver = webdriver.Firefox(executable_path=firefox_driver_path)
driver = webdriver.Opera(executable_path=opera_driver_path)


# Test site
# =========
driver.get("https://secure-retreat-92358.herokuapp.com/")

# input_fname = driver.find_element_by_name("fName")
# input_lname = driver.find_element_by_name("lName")
# input_email = driver.find_element_by_name("email")
#
# input_fname.send_keys("John")
# input_lname.send_keys("Private")
# input_email.send_keys("jp@example.com")
# input_email.submit()

# driver.find_element_by_tag_name("button").click()
# driver.find_element_by_css_selector("form button").click()

input_details = driver.find_element_by_name("fName")
input_details.send_keys("John" + Keys.TAB + "Private" + Keys.TAB + "jp@example.com" + Keys.ENTER)

# Actual Newsletter Subscription
# ==============================
# driver.get("https://www.appbrewery.co/p/newsletter")
#
# input_email = driver.find_element_by_id("profile-form-fields").find_element_by_id("member_email")
# input_email.send_keys("jp@example.com")
# input_email.submit()
#
# # input_submit = driver.find_element_by_id("profile-form-fields").find_element_by_css_selector(".input-group-btn")
# # input_submit.click()



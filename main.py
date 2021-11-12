# import selenium  # used only to get selenium installed
from selenium import webdriver

chrome_driver_path = "E:/Python/WebDriver/chromedriver.exe"
firefox_driver_path = "E:/Python/WebDriver/geckodriver.exe"
opera_driver_path = "E:/Python/WebDriver/operadriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# TEST CODE
# =========

# find_element_by_id
# find_element_by_name
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector

# driver.get("https://www.amazon.co.uk/dp/B083KM6BZS?tag=camelproducts-21&linkCode=ogi&th=1&psc=1&language=en_GB")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)
#
driver.get("https://www.python.org")
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

logo = driver.find_element_by_class_name("python-logo")
print(logo.size)

exit()
# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)
#
# bug_link = documentation_link.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text, bug_link.get_attribute("href"))


# CHALLENGE
# =========
# Get Upcoming Events from python.org

driver.get("https://www.python.org")
list_time = driver.find_elements_by_css_selector(
    ".event-widget time")  # find all time tags inside event-widget class
list_name = driver.find_elements_by_css_selector(
    ".event-widget li a")  # find all a tags inside li tags inside event-widget class
events = {}
for index in range(len(list_time)):
    date = list_time[index].text
    name = list_name[index].text
    events[index] = {"time": date, "name": name}
print(events)
"""
{
  "0": {
    "time": "2021-02-19",
    "name": "PyCascades 2021"
  },
  "1": {
    "time": "2021-02-24",
    "name": "Careers with Python: Volume 0"
  },
  "2": {
    "time": "2021-03-18",
    "name": "PyCon Cameroon 2021"
  },
  "3": {
    "time": "2021-03-22",
    "name": "Python Web Conference 2021"
  },
  "4": {
    "time": "2021-04-22",
    "name": "GeoPython 2021"
  }
}
"""


# using list comprehension - solution by Armando
upcoming_events = driver.find_element_by_css_selector('.event-widget').find_elements_by_tag_name('li')
upcoming_events_dict = {
    index:
        {
            'time': key.find_element_by_tag_name('time').get_attribute('datetime').split('T')[0],
            'name': key.find_element_by_tag_name('a').text
        }
    for index, key in enumerate(upcoming_events)}
print(upcoming_events_dict)


# driver.close()  # Close the current browser tab
driver.quit()  # Close the entire browser

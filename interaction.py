from selenium import webdriver

chrome_driver_path = "E:/Python/WebDriver/chromedriver.exe"
firefox_driver_path = "E:/Python/WebDriver/geckodriver.exe"
opera_driver_path = "E:/Python/WebDriver/operadriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

"""
CSS Selectors
https://saucelabs.com/resources/articles/selenium-tips-css-selectors

'#' == '@id'     tag identifier      (e.g. “[@id='example']” in XPATH)
'=' == '//'      element type        (e.g. //div or //input in XPATH)
'>' == '/'       direct child        (e.g. //div/a in XPATH)
' ' == '//'      child or sub-child  (e.g. //div//a in XPATH) [whitespace] 
'.' == '@class'  tag class           (e.g. “[@class='example']” in XPATH)

'^=' == Match a prefix               (e.g. a[id^='id_prefix_'])
'$=' == Match a suffix               (e.g. a[id$='_id_suffix'])
'*=' == Match a substring            (e.g. a[id*='id_pattern']) 
"""

# stats = driver.find_element_by_id("articlecount").find_element_by_tag_name("a")
stats = driver.find_element_by_css_selector("#articlecount a")
print(int(stats.text.replace(",", "")))


driver.quit()  # Close the entire browser

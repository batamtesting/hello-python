from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = r"C:\SeleniumDrivers\chromedriver-v2.33_win32\chromedriver.exe"
#options = Options()
#options.binary_location = '/path/to/chrome'

#driver = webdriver.Chrome()
driver = webdriver.Chrome(chromedriver) #Optional, if not specified, WebDriver will search your path for chromedriver.
#driver = webdriver.Chrome(chromedriver, chrome_options=options)
driver.get("http://www.python.org")

#assert "Python" in driver.title

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

#assert "No results found." not in driver.page_source

#driver.quit()
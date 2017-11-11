from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

geckodriver = r"C:\SeleniumDrivers\geckodriver-v0.19.0-win64\geckodriver.exe"
binary = FirefoxBinary(r"C:\Browsers\Mozilla Firefox55.0.3-x64\firefox.exe")
fp = webdriver.FirefoxProfile()

driver = webdriver.Firefox(executable_path=geckodriver, firefox_binary=binary, firefox_profile=fp) #Optional, if not specified, WebDriver will search your path for geckodriver.
#driver = webdriver.Firefox()
driver.get("http://www.python.org")

#assert "Python" in driver.title

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

#assert "No results found." not in driver.page_source

#driver.quit()
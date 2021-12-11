"""
description: Script to invoke Chrome on a Macbook and invoke google search on a test string 
usage:
python3 p1
requirements:
Place the chromedriver in /usr/local/bin/chromedriver
"""

import os
import time
from selenium import webdriver
driver = webdriver.Chrome("/usr/local/bin/chromedriver")

print(driver)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.google.com/")
elem = driver.find_element_by_name("q")
time.sleep(2)
elem.send_keys("hello webdriver")
time.sleep(2)
elem.submit()
time.sleep(2)
driver.close()

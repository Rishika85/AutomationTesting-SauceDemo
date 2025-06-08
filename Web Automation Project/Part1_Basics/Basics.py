#import webdriver module from selenium package
from selenium import webdriver
import time

#instantiate webdriver and launch Chrome browser
driver = webdriver.Chrome()

#open google.com web page
driver.get("https://www.google.com")

time.sleep(2)

#open youtube
driver.get("https://www.youtube.com")

time.sleep(2)

#back to google
driver.back()

time.sleep(2)

#forward to youtube
driver.forward()

time.sleep(2)

#refresh the page
driver.refresh()

time.sleep(2)


#close the browser window
driver.quit()
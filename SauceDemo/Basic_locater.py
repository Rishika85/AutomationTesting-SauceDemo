#import webdriver module from selenium

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

'selenium.webdriver.common.by.By'

#instantiate webdriver and launch Chrome browser
driver = webdriver.Chrome()

#open google.com web page
driver.get("https://www.google.com")

driver.maximize_window()

time.sleep(2)

#Navigate to Saucedemo website
driver.get("https://www.saucedemo.com")

time.sleep(2)

#locate username web element
#username = driver.find_element(By.NAME, "user-name")

#locate username by relative xpath
#username = driver.find_element(By.XPATH,"//input[@id='user-name']")
#username = driver.find_element(By.XPATH,"//input[@id='user-name' and @type='text']")

#locate username by tag name
username = driver.find_element(By.TAG_NAME,"input")


#enter username
username.send_keys("standard_user")

#locate password web element
#password = driver.find_element(By.NAME, "password")

#locate password by relative xpath
#password = driver.find_element(By.XPATH,"//input[@name='password']")

#locate password by index method
password = driver.find_element(By.XPATH,"(//input)[2]")


#enter password
password.send_keys("secret_sauce")
time.sleep(5)

#locate login button
#loginBtn = driver.find_element(By.XPATH,"//input[@id='login-button']")
#loginBtn = driver.find_element(By.XPATH,"//input[@id='login-button' or @id='wrong-button']")

#locate login button by class name
loginBtn = driver.find_element(By.CLASS_NAME,"btn_action")
#click on login button
loginBtn.click()

time.sleep(5)

#locate add to cart button by contains method
addToCart = driver.find_element(By.XPATH,"//button[contains(@class,'btn_primary')]")
#click on add to cart button
addToCart.click()
time.sleep(5)

#locate web element sauce labs bolt tshirt by text method
#product = driver.find_element(By.XPATH,"//div[text()='Sauce Labs Bolt T-Shirt']")

#find product link for sauce labs bolt tshirt BY.LINK_TEXT
product = driver.find_element(By.LINK_TEXT,'Sauce Labs Bolt T-Shirt')
product.click()
time.sleep(5)

#find product link for sauce labs fleece jacket BY.PARTIAL_LINK_TEXT
#thing = driver.find_element(By.PARTIAL_LINK_TEXT,'Fleece Jacket')
#thing.click()
#time.sleep(5)


#locate web element sauce labs bike light by [contains(text)] method
#product = driver.find_element(By.XPATH,"//div[contains(text),'Bike Light']")
#product.click()


#close browser
driver.quit()
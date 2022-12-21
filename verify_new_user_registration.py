# IT CALLED RAW because its a standalone/no framework


from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
time.sleep(2)

url = 'http://demostore.supersqa.com/my-account/'
email_field_id = 'reg_email'
password_field_id = 'reg_password'
logout_btn_css = 'li.woocommerce-MyAccount-navigation-link--customer-logout a'

# Go to the URL
driver.get(url)
email_field = driver.find_element(By.ID, email_field_id)
password_field = driver.find_element(By.ID, password_field_id)

# Generate random email
letters = string.ascii_lowercase
rand_string = ''.join(random.choice(letters) for i in range(15))
rand_email = rand_string + '@raykamilah.com'

# Type in the email field
email_field.send_keys(rand_email)

# Find password field and enter password
password_field = driver.find_element(By.ID, password_field_id)
password_field.send_keys('abcd12342323!!!')                    #if its too weak, it wont click

time.sleep(2)

# Click on register button
reg_btn = driver.find_element(By.CSS_SELECTOR, '#customer_login > div.u-column2.col-2 > form > p:nth-child(4) > button').click()
# reg_btn = driver.find_element(By.CSS_SELECTOR, 'button[value="Register"]').click()

# Check if logged in + Catch 1
try:
    logout_btn = driver.find_element(By.CSS_SELECTOR, logout_btn_css)
except:
    raise Exception("User not logged in after registering")

# Catch 2
# if logout_btn.is_displayed():
#     print("PASS")
# else:
#     raise Exception("User not logged in after registering")









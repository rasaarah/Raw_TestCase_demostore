
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def add_1_item_to_cart():
    driver.find_element(By.CLASS_NAME, 'add_to_cart_button').click()         #walaupun banyak button, tapi makenya find_element jadi cuma akan kepilih yang pertama aja
    wait.until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="site-header-cart"]/li[1]/a/span[2]'), '1 item')
    )

def click_card_in_top_menu():
    driver.find_element(By.XPATH, '//*[@id="site-header-cart"]/li[1]/a').click()

def input_coupon_and_hit_enter(coupon_code):
    coupon_field = wait.until(
        EC.visibility_of_element_located((By.ID, 'coupon_code'))
    )
    # coupon_field = driver.find_element(By.ID, 'coupon_code') #same with above tp yg atas dia wait dulu
    coupon_field.send_keys(coupon_code)
    coupon_field.send_keys(Keys.ENTER)

def verify_total_is_0():
    wait.until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="post-7"]/div/div/div[2]/div/table/tbody/tr[3]/td/strong/span'), '$0.00')
    )


if __name__ == '__main__':

    coupon_code = 'SSQA100'

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    url = 'http://demostore.supersqa.com/'

    wait = WebDriverWait(driver, 10)

    driver.get(url)

    add_1_item_to_cart()
    click_card_in_top_menu()
    input_coupon_and_hit_enter(coupon_code)
    verify_total_is_0()
    print("PASS")
    driver.quit()




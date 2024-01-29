from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome browser
driver = webdriver.Chrome()

try:




    # Open Gmail
    driver.get('https://www.10fastfingers.com')
    time.sleep(3)
    cookies_button = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    cookies_button.click()
    time.sleep(2)
    start_button = driver.find_element(By.ID, 'typing-test')
    start_button.click()

    parent_div = driver.find_element(By.ID,'row1')
    input_field =  driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    # Find all span elements within the parent div
    span_elements = driver.find_elements(By.CSS_SELECTOR, 'span[wordnr]')

    input_field = driver.find_element(By.ID,'inputfield')
    try:

        target_wpm = 220 # give or take 20

        # Calculate the sleep time based on the target typing speed
        sleep_time = 60 / target_wpm
        i = 0
        while True:
            time.sleep(sleep_time)
            elements = driver.find_element(By.XPATH,"//span[@wordnr='" + str(i) + "']")
            print(elements.text)
            input_field.send_keys(elements.text)
            input_field.send_keys(" ")
            i += 1
    except:
        print("Words completed")

finally:
    # Close the browser
    time.sleep(60)
    driver.quit()

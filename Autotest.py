import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

def main():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com.ua")
    elem = driver.find_elements_by_name('q')
    elem.click()
    elem.send_keys('123')
    elem.send_keys(Keys.ENTER)

if __name__ == "__main__":
    main()



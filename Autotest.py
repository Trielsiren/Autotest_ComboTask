import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

def main():
    driver = webdriver.Chrome()
    driver.get("https://combotask.com.ua/performers?ordering=-rating_mark")
    elem = driver.find_elements_by_class_name(' form-input-grey ')
    elem.click()

if __name__ == "__main__":
    main()



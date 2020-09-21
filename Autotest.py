import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

class Combotask(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://combotask.com.ua/performers?ordering=-count_done_tasks")

    def test_01(self):
        driver = self.driver
        links_elem_1 = driver.find_element_by_class_name("create-link").click()

    def test_02 (self):
        driver = self.driver
        field_01 = driver.find_element_by_name("title").send_keys("Task_1")
        field_02 = driver.find_element_by_name("description").send_keys("Description_1")
        field_03 = driver.find_element_by_class_name("external-task-search").click()
        field_04 = driver.find_element_by_class_name("external-place-selected-text").click()
        field_05 = driver.find_element_by_class_name("c-4-center external-place-outer").click()
        field_06 = driver.find_element_by_class_name("Киев").click()
        field_07 = driver.find_element_by_name("street").send_keys("Street_1")
        field_08 = driver.find_element_by_name("home_number").send_keys("Home_1")
        field_09 = driver.find_element_by_name("flat_number").send_keys("flat_1")
        field_10 = driver.find_element_by_name("price").send_keys("12345")
        field_11 = driver.find_element_by_class_name("form-submit form-submit-desktop").click()

    def test_03 (self):
        driver = self.driver
        check_box_1 = driver.find_element_by_class_name("checkbox-custom").click()

    def test_04 (self):
        driver = self.driver
        elem_1 = driver.find_element_by_link_text('/faq').click()

    def test_05 (self):
        driver = self.driver
        elem_2 = driver.find_element_by_class_name('lang-icon ru').click()

    def test_06 (self):
        driver = self.driver
        elem_3 = driver.find_element_by_class_name('sort-button').click()

    def test_07 (self):
        driver = self.driver
        elem_4 = driver.find_element_by_class_name('external-price-wrap-heading').click()

if __name__ == '__main__':
    unittest.main()

        #for elem in links_elem:
           # lang_link = (elem.get_attribute('href'))
           # print (lang_link)

            #if self.lang in lang_link:

        #click_element_1 = driver.find_element_by_tag_name("a").click(self)
        #click_element_1.send_keys('')


#def main():
   # driver = webdriver.Chrome()
   # driver.get("https://www.google.com.ua")
    #element = driver.find_element_by_name("q")
   # element.click()
    #time.sleep(1)
    #element.send_keys('123')
    #element.send_keys(Keys.ENTER)

#if __name__ == "__main__":
    #main()



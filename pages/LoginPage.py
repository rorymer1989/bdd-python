from selenium import webdriver
import time

def open_browser(self):
  self.driver = webdriver.Chrome('chromedriver.exe')
  self.driver.get('http://automationpractice.com/index.php')
  self.driver.find_element_by_id('search_query_top').send_keys('Hola')
  self.driver.find_element_by_name('submit_search').click()
  time.sleep(5)

def valid_message(self):
  return  self.driver.find_element_by_xpath('//*[@id="center_column"]/p').text

def close_browser(self):
  self.driver.close()
  self.driver.quit()
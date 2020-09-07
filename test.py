import time
import unittest
from selenium import webdriver

tc = unittest.TestCase('__init__')
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://automationpractice.com/index.php')
driver.find_element_by_id('search_query_top').send_keys('Hola')
driver.find_element_by_name('submit_search').click()
time.sleep(5)
text = driver.find_element_by_xpath('//*[@id="center_column"]/p').text
print(text)
tc.assertEqual('No results were found for your search "Hola"',text)

driver.close()
driver.quit()
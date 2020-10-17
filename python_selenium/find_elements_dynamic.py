import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/natemac/Documents/Repo/chromedriver')
driver.get('https://www.rahulshettyacademy.com/dropdownsPractise/')

driver.find_element_by_id('autosuggest').send_keys('ind')
# enter the letter 'i' in the dynamic dropdown search

time.sleep(2)
# do not use these in real development

countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print('Amount of countries: ' + str(len(countries)))
for country in countries:
    if country.text == "India":
        country.click()
        break
# put the returned country options into a list and iterate through to click on the matching country
assert driver.find_element_by_id('autosuggest').get_attribute('value') == 'India'
# verify that the correct option was selected (test passes)
# get_attribute retrieves 'value' stored after dom has loaded,
#  but the input has generated new page data

driver.close()

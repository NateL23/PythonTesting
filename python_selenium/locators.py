from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='/Users/natemac/Documents/Repo/chromedriver')
driver.get('https://www.rahulshettyacademy.com/angularpractice/')

driver.find_element_by_id('exampleCheck1').click()
# id
driver.find_element_by_name('email').send_keys('nathanael.lemay23@gmail.com')
# name
driver.find_element_by_css_selector("input[name='name']").send_keys('Nate')
# css

dropdown = Select(driver.find_element_by_id('exampleFormControlSelect1'))
# Select() provides methods to handle dropdown options
dropdown.select_by_visible_text("Male")
# select "Male" by visible text
dropdown.select_by_index(1)
# select 'Female' option using index
# $ dropdown.select_by_value()
# select using 'value' attribute

# $ driver.find_element_by_xpath("//input[@type='submit']").click()
driver.find_element_by_xpath("//*[contains(@type, 'submit')]").click()
# xpath, click submit button as specific element, or using 'contains'
# avoid xpath if possible, much slower than css

# $ print(driver.find_element_by_class_name('alert-success').text)
print(driver.find_element_by_css_selector("[class*='alert-success']").text)
# print text displayed inside the element with class name 'alert-success'
# use '*' as 'contains()'

driver.close()

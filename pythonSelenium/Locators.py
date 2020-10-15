from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/natemac/Documents/Repo/chromedriver')
driver.get('https://www.rahulshettyacademy.com/angularpractice/')

driver.find_element_by_id('exampleCheck1').click()
# id
driver.find_element_by_name('email').send_keys('nathanael.lemay23@gmail.com')
# name
driver.find_element_by_css_selector("input[name='name']").send_keys('Nate')
# css

# $ driver.find_element_by_xpath("//input[@type='submit']").click()
driver.find_element_by_xpath("//*[contains(@type, 'submit')]").click()
# xpath, click submit button as specific element, or using 'contains'

# $ print(driver.find_element_by_class_name('alert-success').text)
print(driver.find_element_by_css_selector("[class*='alert-success']").text)
# print text displayed inside the element with class name 'alert-success'
# use '*' as 'contains()'

driver.close()

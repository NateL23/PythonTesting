from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/natemac/Documents/Repo/chromedriver')
driver.get('https://www.rahulshettyacademy.com/angularpractice/')

# driver.find_element_by_name('name').send_keys('Rahul')
driver.find_element_by_id('exampleCheck1').click()
driver.find_element_by_css_selector("input[name='name']").send_keys('rahul')
driver.find_element_by_name('email').send_keys('Shetty')
# css
driver.find_element_by_xpath("//input[@type='submit']").click()
# xpath

driver.close()


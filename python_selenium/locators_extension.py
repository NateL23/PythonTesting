from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/natemac/Documents/Repo/chromedriver')
driver.get('https://login.salesforce.com')

driver.find_element_by_css_selector('#username').send_keys('nate')
# css id
driver.find_element_by_css_selector('.password').send_keys('password1')
# css class
driver.find_element_by_css_selector('.password').clear()
# clear field
driver.find_element_by_link_text('Forgot Your Password?').click()
# css link text
driver.find_element_by_xpath("//a[text() = 'Cancel']").click()
# using 'a' as tagname (tagname is the first word in the DOM structure('a', 'input', 'button', etc.)

print(driver.find_element_by_xpath("//form[@name = 'login']/div[1]/label").text)
# xpath parent/child tags used to print text above Username field
print(driver.find_element_by_css_selector("form[name = 'login'] label:nth-child(3)").text)
# css parent/child tags used to print text above Password field

driver.close()

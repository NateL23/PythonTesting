from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/natemac/Documents/Repo/chromedriver')
driver.get('https://www.makemytrip.com')

driver.find_element_by_id('fromCity').click()
driver.find_element_by_css_selector("input[placeholder = 'From']").send_keys('del')

cities = driver.find_element_by_css_selector("p[class* = 'blackText]")
print('Amount of cities: ' + len(cities))

for city in cities:
    if city.text == 'Del Rio, United States':
        city.click()

driver.find_element_by_css_selector("p[text = 'Delhi, India']").click()

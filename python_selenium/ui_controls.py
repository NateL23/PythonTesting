from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/natemac/Documents/Repo/chromedriver')
driver.get('https://www.rahulshettyacademy.com/AutomationPractice')

checkboxes = driver.find_elements_by_xpath("//input[@type = 'checkbox']")

print('Count of checkboxes: ' + str(len(checkboxes)))

for box in checkboxes:
    box .click()
    assert box.is_selected()
# validate the checkbox has been checked after checking all checkboxes

driver.close()

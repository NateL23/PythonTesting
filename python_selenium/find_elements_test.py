from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='/Users/natemac/Documents/Repo/chromedriver')
driver.get('https://www.makemytrip.com/')

driver.find_element_by_css_selector('li[data-cy = "account"]').click()
driver.find_element_by_css_selector('body[class = "desktop in"]').click()
# had to hack this together because there is a silly login popup that happens

from_city_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'fromCity'))
)
# remade this one with explicit waits, I am personally not a fan of using
# $ time.wait(x)
from_city_element.click()

driver.find_element_by_css_selector("input[placeholder = 'From']").send_keys('del')
# send "del" keys into the "From" dropdown

cities = WebDriverWait(driver, 3).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'p[class*="blackText"]'))
)
# get all cities that pop up in the dynamic dropdown after entering "del"
# print('Amount of cities: ' + str(len(cities)))
for city in cities:
    if city.get_attribute('text') == 'Del Rio, United States':
        city.click()
        break
# break inside the if block to kill the loop when the option is found
# in this example, the option we are looking for is intentionally not on the list

real_city_to_click = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.XPATH, '//p[text() = "Delhi, India"]'))
)
if real_city_to_click.text == 'Delhi, India':
    real_city_to_click.click()
# select a real option from the list,added if to prevent incorrect cities selected
if driver.find_element_by_css_selector('p[title*="DEL,"]').is_displayed():
    assert driver.find_element_by_css_selector('p[title*="DEL,"]').is_displayed()
    print("Test passed!")
# passing condition
driver.close()

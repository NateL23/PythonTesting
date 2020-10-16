from selenium import webdriver
# browser exposes an executable file, invoke file through selenium test

# driver = webdriver.Chrome(executable_path='/Users/natemac/Documents/Repo/chromedriver')
driver = webdriver.Firefox(executable_path='/Users/natemac/Documents/Repo/geckodriver')
driver.get('https://www.rahulshettyacademy.com')
driver.maximize_window()
# in case window loads minimized
print(driver.title)
print(driver.current_url)
driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
driver.minimize_window()
# to minimize window again
driver.back()
# hit back button in browser
driver.refresh()
# reloads page
driver.close()
# closes all windows, $ driver.quit() closes single window

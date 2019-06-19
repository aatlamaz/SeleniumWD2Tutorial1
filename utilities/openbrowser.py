from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title

try:
    elem = browser.find_element_by_name('p')  # Find the search box
    elem.send_keys('seleniumhq', Keys.RETURN)

except:
    print("Element not found")
#browser.quit()
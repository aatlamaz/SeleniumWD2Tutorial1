from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class ChangeToCapital():

    def test1(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        element =driver.find_element_by_id("name")


        driver.find_element_by_id("name").send_keys(Keys.SHIFT, 'ahmet')
        driver.find_elements(By.TAG_NAME("a")).size()

aa = ChangeToCapital()
aa.test1()

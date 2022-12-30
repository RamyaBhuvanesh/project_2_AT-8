import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


"""


test-5 
     1. login
     2. fill out the dependants details
     3. save

"""


@pytest.fixture()
def setUP():
        global driver
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)

        user_name = driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Admin")
        time.sleep(3)
        print("user name is correct")

        password = driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("admin123")
        time.sleep(5)
        print("password is correct")

        login = driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(5)

def test_orangeHRM(setUP):

    admin = driver.find_element(By.XPATH, '//a[@href="/web/index.php/admin/viewAdminModule"]').click()
    time.sleep(4)

    usermanagement = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]').click()
    time.sleep(4)

    users = driver.find_element(By.XPATH, '//a[@href="#"]').click()
    time.sleep(3)

    userrole = driver.find_element(By.XPATH, '//label[text()="User Role"]/following::div[3]').click()
    time.sleep(3)

    drpadmin = driver.find_element(By.XPATH, '//div[@role="listbox"]//span[text()="Admin"]').click()
    time.sleep(3)

    status = driver.find_element(By.XPATH, '//label[text()="Status"]/following::div[3]').click()
    time.sleep(3)

    drpenabled = driver.find_element(By.XPATH, '//div[@role="listbox"]//span[text()="Enabled"]').click()
    time.sleep(3)

    userrole = driver.find_element(By.XPATH, '//label[text()="User Role"]/following::div[3]').click()
    time.sleep(3)

    ESS = driver.find_element(By.XPATH, '//div[@role="listbox"]//span[text()="ESS"]').click()
    time.sleep(3)
    status = driver.find_element(By.XPATH, '//label[text()="Status"]/following::div[3]').click()
    time.sleep(3)

    drpdisabled = driver.find_element(By.XPATH, '//div[@role="listbox"]//span[text()="Disabled"]').click()
    time.sleep(3)



def teardowm ():
        driver.close()
        driver.quite()
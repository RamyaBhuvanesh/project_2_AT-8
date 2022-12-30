import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

"""
test-11
     1.login
     2.job details
     3.activate employee
     4.job activated
     

"""


class Successful_Employee_Login():
    def login_test():
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)

        username = driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Admin")
        time.sleep(3)

        password = driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("admin123")
        time.sleep(3)

        submit = driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(5)

        enter_pim = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]').click()
        time.sleep(2)

        emp_list = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a').click()
        time.sleep(3)

        # emp_info = driver.find_element(By.XPATH, '//button[@type="button"][@class="oxd-icon-button"]/*[@class="oxd-icon bi-caret-down-fill"]').send_keys(Keys.ENTER)
        # time.sleep(3)

        employee_name = driver.find_element(By.XPATH, '//input[@placeholder="Type for hints..."][1]').send_keys("Aaliyah Haq")
        time.sleep(3)

        save = driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(7)

        # choose = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div/div/div/div[1]/div[1]/div/div').click()
        # time.sleep(3)

        job = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a').click()
        time.sleep(3)

        terminated = driver.find_element(By.XPATH,'//button[@type="button"][@class="oxd-button oxd-button--medium oxd-button--label-danger --termination-button"]').click()
        time.sleep(3)

        termination_date = driver.find_element(By.XPATH,'//label[text()="Termination Date"]/following::div[3]').send_keys('2022-11-16')
        time.sleep(3)

        termination_reason = driver.find_element(By.XPATH,'//label[text()="Termination Reason"]/following::div[3]').click()
        time.sleep(3)

        termination_reason_1 = driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Contract Not Renewed"]').click()
        time.sleep(3)

        note = driver.find_element(By.XPATH, '//textarea[@placeholder="Type here"]').send_keys('he have to renew the contract, to continue his job... ')


get_it = Successful_Employee_Login
get_it.login_test()










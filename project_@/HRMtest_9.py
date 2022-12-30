import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from self import self

"""
test-9
     1.login
     2.job details
     3.add
     4.details
     5.employee contract details
     6.details
     7.save
"""
class Successful_Employee_Login():
    def login_test():
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)

        # xpath to username
        username = driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Admin")
        time.sleep(3)

        # xpath to password
        password = driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("admin123")
        time.sleep(3)

        # xpath to login button
        submit = driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(5)

        enter_pim = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]').click()
        time.sleep(2)

        add_button = driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]').click()
        time.sleep(2)

        first_name = driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys("Ramya")
        time.sleep(2)

        middle_name = driver.find_element(By.XPATH, '//input[@name="middleName"]').send_keys("Chandrasekaran")
        time.sleep(2)

        last_name = driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys("B")
        time.sleep(2)

        save_data = driver.find_element(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]').click()
        time.sleep(7)

        job = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a').click()
        time.sleep(3)

        joined_date = driver.find_element(By.XPATH, '//input[@placeholder="yyyy-mm-dd"]').send_keys("1997-02-27")
        time.sleep(3)

        job_tit = driver.find_element(By.XPATH, '//label[text()="Job Title"]/following::div[3]').click()
        time.sleep(3)

        job_title = driver.find_element(By.XPATH, '//div[@role="listbox"]//span[text()="tester 123"]').click()
        time.sleep(5)

        job_cat = driver.find_element(By.XPATH, '//label[text()="Job Category"]/following::div[3]').click()
        time.sleep(3)

        job_category = driver.find_element(By.XPATH, '//div[@role="listbox"]//span[text()="Professionals"]').click()
        time.sleep(3)

        subunit = driver.find_element(By.XPATH, '//label[text()="Sub Unit"]/following::div[3]').click()
        time.sleep(3)

        sub_unit = driver.find_element(By.XPATH, '//div[@role="listbox"]//span[text()="Engineering"]').click()
        time.sleep(3)

        location = driver.find_element(By.XPATH, '//label[text()="Location"]/following::div[4]').click()
        time.sleep(3)

        location_1 = driver.find_element(By.XPATH, '//div[@role="listbox"]//span[text()="Canadian Regional HQ"]').click()
        time.sleep(3)

        employment_status = driver.find_element(By.XPATH, '//label[text()="Employment Status"]/following::div[4]').click()
        time.sleep(3)

        employment_status_1 = driver.find_element(By.XPATH, '//div[@role="listbox"]//span[text()="Full-Time Permanent"]').click()
        time.sleep(3)

        contract_details = driver.find_element(By.XPATH, '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]').click()
        time.sleep(3)

        contract_start_date = driver.find_element(By.XPATH, '//label[text()="Contract Start Date"]/following::input[@class="oxd-input oxd-input--active"][1]').send_keys('2019-12-09')
        time.sleep(2)

        contract_end_date = driver.find_element(By.XPATH, '//label[text()="Contract End Date"]/following::input[@placeholder="yyyy-mm-dd"]').send_keys('2021-10-23')
        time.sleep(2)

        save = driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(3)










get_it = Successful_Employee_Login
get_it.login_test()



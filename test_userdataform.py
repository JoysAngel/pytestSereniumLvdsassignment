from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest


@pytest.fixture
def setUp():
    global name,address,pincode,mobile,emailid,password,confirmpassword,driver
    name=input("Enter the user name :")
    address=input("Enter the user address:")
    pincode=int(input("Enter the user pincode:"))
    mobile=int(input("Enter the user mobile number:"))
    emailid=input("Enter the user email id:")
    password=input("Enter the password:")
    confirmpassword=input("confirm the password")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(10)
    driver.close()

def test_form(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/userdata.php")
    time.sleep(2)
    driver.find_element_by_name("name").send_keys("Joys Angel M")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input[2]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[3]/td[2]/select/option[1]").click()
    time.sleep(2)
    driver.find_element_by_name("Address").send_keys("K.R.Puram Bangalore")
    time.sleep(2)
    driver.find_element_by_name("Pincode").send_keys("560036")
    time.sleep(2)
    driver.find_element_by_name("Mobile").send_keys("9901711257")
    time.sleep(2)
    driver.find_element_by_name("Email").send_keys("joysangelm@gmail.com")
    time.sleep(2)
    driver.find_element_by_name("pass").send_keys("Almightygod@111")
    time.sleep(2)
    driver.find_element_by_name("cnfpass").send_keys("Almightygod@111")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[10]/td[2]/div/input").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[11]/td[2]/button").click()
    time.sleep(5)



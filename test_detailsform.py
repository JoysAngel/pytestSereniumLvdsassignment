from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

@pytest.fixture
def setUp():
    global name,driver
    name =input("enter the name")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(10)
    driver.close()

def test_form(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/")
    time.sleep(2)
    driver.find_element_by_name("name").send_keys("Joys Angel M")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input[2]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[3]/td[2]/select/option[1]").click()
    time.sleep(1)
    driver.find_element_by_name("fcheckbox").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[5]/td[2]/button").click()
    time.sleep(3)

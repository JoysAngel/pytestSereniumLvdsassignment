from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest


@pytest.fixture
def setUp():
    global moviename,year,directorname,distributer,producer,driver
    moviename = input("Enter the movie name :")
    year = int(input("Enter the year :"))
    directorname = input("Enter the director name :")
    distributer = input("Enter the distributer :")
    producer = input("Enter the producer :")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(10)
    driver.close()

def test_form(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    time.sleep(2)
    driver.find_element_by_name("mname").send_keys("Titanic")
    time.sleep(2)
    driver.find_element_by_name("myear").send_keys("1992")
    time.sleep(2)
    driver.find_element_by_name("mdirector").send_keys("James Cameron")
    time.sleep(2)
    driver.find_element_by_name("mdist").send_keys("20th Century studios")
    time.sleep(2)
    driver.find_element_by_name("mproducer").send_keys("jon landau")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[3]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[7]/td[2]/button").click()
    time.sleep(4)

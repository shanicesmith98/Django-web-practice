from selenium import webdriver
import time

def test_opening_webdriver_instance():
    driver = webdriver.Chrome()
    driver.get("http://www.google.com")
    time.sleep(3)
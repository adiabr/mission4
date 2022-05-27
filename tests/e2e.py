from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def test_score_service(url):
    val = False
    my_driver = webdriver.Chrome(executable_path='C:/Windows/System32/chromedriver.exe')
    my_driver.get(url)
    actual_site_name = my_driver.find_element(By.ID, "score").text
    if 1 <= int(actual_site_name) <= 1000:
        val = True
    else:
        val = False

    my_driver.close()
    return val

def main_function():
    val = test_score_service("http://10.100.102.6:5001/")
    if val:
        return 0
    else:
        return -1
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome("C:\\Users\\brik7\\PycharmProjects\\Hackathon 2019\\chromedriver.exe")
browser.get("http://www.youtube.com")
browser.maximize_window()

while 1 :
    currentURL = browser.current_url
    print (currentURL)
    try:
        wait = WebDriverWait(browser, 3)
        wait.until_not(EC.url_equals(currentURL))
        currentURL = browser.current_url
        print ("Different page has been detected")
    except TimeoutException:
        print("SAME PAGE")
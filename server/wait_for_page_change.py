from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome("C:\\Users\\brik7\\PycharmProjects\\Hackathon 2019\\chromedriver.exe")
browser.get("http://www.youtube.com")
browser.maximize_window()

while 1 :
    currentURL = browser.current_url
    try:
        wait = WebDriverWait(browser, 2)
        wait.until(EC.url_changes(currentURL))
        currentURL = browser.current_url
        if "watch?" in currentURL :
            print ("Youtube video detected")
            print (currentURL)
        print ("Different page has been detected")
    except TimeoutException:
        print("SAME PAGE")
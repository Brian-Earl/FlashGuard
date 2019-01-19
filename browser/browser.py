import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome(executable_path = "/Users/JeffHarnois/Downloads/hackathon/upgraded-guacamole/browser/chromedriver")
browser.get("https://www.youtube.com/")
browser.maximize_window()
while 1 :
    currentURL = browser.current_url
    try:
        wait = WebDriverWait(browser, 2)
        wait.until(EC.url_changes(currentURL))
        currentURL = browser.current_url
        if "watch?" in currentURL:
            video = browser.find_element_by_id("movie_player")
            print ("Youtube video detected")
            print (currentURL)
            time.sleep(1)
            video.click()
            time.sleep(2)
            browser.execute_script("alert('This video is paused because you might die. DO NOT WATCH. Killing myself now');")
            time.sleep(3)
            browser.close()
            exit()
        print ("Different page has been detected")
    except TimeoutException:
        print("SAME PAGE")

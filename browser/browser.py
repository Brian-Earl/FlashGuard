import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import client


alert_script = "var r = confirm(\"WARNING\\nPart of this video could induce an epileptic seizure\\nPress the OK button to be redirected to the YouTube home page\\nor cancel to override\"); if (r == true) {window.location.replace(\"http://www.youtube.com\")};"
browser = webdriver.Chrome(executable_path="/Users/JeffHarnois/Downloads/hackathon/upgraded-guacamole/browser/chromedriver")
youtube = "https://www.youtube.com/"
browser.get(youtube)
browser.maximize_window()


def pause_vid():
    browser.execute_script(alert_script)
    while 1:
        try:
            WebDriverWait(browser, 3).until(EC.alert_is_present())
            print("alert is here!")
        except TimeoutException:
            time.sleep(1)
            print("alert is no longer here!")
            break


def browserScraper():
    while 1:
        currentURL = browser.current_url
        try:
            wait = WebDriverWait(browser, 2)
            wait.until(EC.url_changes(currentURL))
            currentURL = browser.current_url
            if "watch?" in currentURL:
                try:
                    video = browser.find_element_by_id("movie_player")
                except WebDriverException:
                    video = browser.find_element_by_id("player")
                if(client.client_sock(currentURL) == 1):
                    time.sleep(1)
                    video.click()
                    time.sleep(1)
                    pause_vid()
            print ("Different page has been detected")
        except TimeoutException:
            print("SAME PAGE")

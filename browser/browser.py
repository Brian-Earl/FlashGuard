import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

alert_script = "var r = confirm(\"Press a button!\"); if (r == true) { window.location.replace(\"http://www.youtube.com\") } else { ; }; console.log(txt);"

def browserScraper():
    browser = webdriver.Chrome(executable_path = "/Users/JeffHarnois/Downloads/hackathon/upgraded-guacamole/browser/chromedriver")
    youtube = "https://www.youtube.com/"
    browser.get(youtube)
    browser.maximize_window()
    while 1 :
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
                print ("Youtube video detected")
                print (currentURL)
                time.sleep(1)
                video.click()
                time.sleep(1)
                browser.execute_script(alert_script)
            print ("Different page has been detected")
        except TimeoutException:
            print("SAME PAGE")

browserScraper()

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
browser = webdriver.Chrome(executable_path = "/Users/JeffHarnois/Downloads/hackathon/upgraded-guacamole/browser/chromedriver")
browser.get("https://www.youtube.com/watch?v=ltBPDI1omgo")
video = browser.find_element_by_id("movie_player")
time.sleep(1)
video.click()
time.sleep(2)
browser.execute_script("alert('This video is paused because you might die. DO NOT WATCH. Killing myself now');")
time.sleep(3)
browser.close()

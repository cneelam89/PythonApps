# download chromedriver of the same version as your browser
#pip install selenium
#import webdriver
from selenium import webdriver

# print(dir(webdriver))
# import Keys
from selenium.webdriver.common.keys import Keys

# import time
import time

browser = webdriver.Chrome(executable_path="C:\\Users\\WHGNR-1398\\chromedriver")
website = "https://www.youtube.com"
browser.maximize_window()
browser.get(website)
time.sleep(5)
search_box = browser.find_element_by_xpath('//input[@id="search"]')
print("search box found")
search_box.send_keys("numb")
search_box.send_keys(Keys.ENTER)
time.sleep(5)
songs = browser.find_elements_by_xpath('//*[@id="video-title"]/yt-formatted-string')
print(songs)
mysong = songs[0]
print(mysong)
mysong.click()
time.sleep(15)
browser.find_element_by_xpath('//*[@id="skip-button:5"]/span/button/span').click()
print("clicked")
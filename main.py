from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
from selenium.webdriver.chrome.options import Options
import time
import random
import pandas as pd
import datetime


options = Options()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
driver_path = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(options = options, executable_path=r'./chromedriver')

driver.get('https://www.instagram.com')
driver.maximize_window()

def url_name(url):
    driver.get(url)
    time.sleep(2)


def login(username,password):
    time.sleep(2)
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys('bappy3a')
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click()

username = "allrafi@hishabee.io"
password = "Sonatola123"

login(username,password)

def send_message():
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[1]/div/div[3]/div/div[2]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a').click()
    message= driver.find_element_by_xpath('iv[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys('Happy Birthday bro')
    message.sendKeys(Keys.RETURN)

send_message()

def birthdaycheck():
    bday=pd.read_excel('birthday.xlsx')
    bday['month']=pd.DatetimeIndex(bday['birthday']).month
    bday['day']=pd.DatetimeIndex(bday['birthday']).day
    name=list(bday['name'])

import csv
import os
import json
import requests
from os import path
from auth import auth, password
from os import path
from configparser import ConfigParser
from time import sleep
from contextlib import suppress

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("user-data-dir=/Users/mouradmarzouk/Library/Application Support/Google/Chrome/")


def fetch_element(driver: WebDriver, selector: str, strategy: str = By.CSS_SELECTOR, timeout: int = 10) -> WebElement:
    with suppress(Exception):
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((strategy, selector)))


fileName = "new2"
if not path.exists('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), fileName)):
    print("Sorry that file name doesn't exist, try again")
    quit()

list = list(range(0, 3165))
oldString = []
issueid = []
type = []
parent = []
with open('/Users/{}/Desktop/{}.csv'.format(os.getlogin(), fileName), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for t in csv_reader:
        oldString.append(t["oldstring"])
        issueid.append(t["issueid"])
        type.append(t["type"])
        parent.append(t["parentkey"])

x = 0

with Chrome(chrome_options=options) as driver:
    for i in list:
        if type[x] == 'Sub-task':
            driver.get(f"https://lucidmotors.atlassian.net/secure/ConvertIssue.jspa?id={issueid[x]}")
            if fetch_element(driver, '#username'):
                fetch_element(driver, '#username').send_keys('mouradmarzouk@lucidmotors.com')
                fetch_element(driver, '#login-submit').click()
                fetch_element(driver, '#okta-signin-username').send_keys('mouradmarzouk')
                fetch_element(driver, '#okta-signin-password').send_keys(password)
                fetch_element(driver, '#okta-signin-submit').click()
                fetch_element(driver, 'input[value="Send Push"]').click()
                sleep(3)
            fetch_element(driver, '#parentIssueKey').send_keys(f'YTSJY-{parent[x]}')
            sleep(2)
            fetch_element(driver, '#parentIssueKey').send_keys(Keys.ENTER)
            sleep(2)
            fetch_element(driver, '#next_submit').click()
            sleep(2)
            fetch_element(driver, '#finish_submit').click()
        x += 1
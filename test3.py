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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("user-data-dir=/Users/mouradmarzouk/Library/Application Support/Google/Chrome/")


def fetch_element(driver: WebDriver, selector: str, strategy: str = By.CSS_SELECTOR, timeout: int = 10) -> WebElement:
    with suppress(Exception):
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((strategy, selector)))


with Chrome(chrome_options=options) as driver:
    driver.get("https://lucidmotors.atlassian.net/secure/MoveIssue!default.jspa?id=358759")
    if fetch_element(driver, 'log in', By.LINK_TEXT):
        fetch_element(driver, 'log in', By.LINK_TEXT).click()
        fetch_element(driver, '#username').send_keys('mouradmarzouk@lucidmotors.com')
        fetch_element(driver, '#login-submit').click()
        fetch_element(driver, '#okta-signin-username').send_keys('mouradmarzouk')
        fetch_element(driver, '#okta-signin-password').send_keys(password)
        fetch_element(driver, '#okta-signin-submit').click()
        fetch_element(driver, 'input[value="Send Push"]').click()
        sleep(3)
    fetch_element(driver, '#project-field').send_keys(Keys.DELETE)
    fetch_element(driver, '#project-field').send_keys('atlas')
    sleep(3)
    fetch_element(driver, '#project-field').send_keys(Keys.ENTER)
    sleep(2)
    fetch_element(driver, '#next_submit').click()
    sleep(9000)

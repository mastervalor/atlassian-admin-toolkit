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

path = '//*[@id="jira"]/div[17]/div[15]/div/div/div[2]/div/div/div[2]/span'
button = '//*[@id="jira-issue-header-actions"]/div/div/div[1]/div/div/button/span/span'
with Chrome(chrome_options=options) as driver:
    driver.get("https://lucidmotors.atlassian.net/browse/GAR-200")
    if fetch_element(driver, '#username'):
        fetch_element(driver, '#username').send_keys('mouradmarzouk@lucidmotors.com')
        fetch_element(driver, '#login-submit').click()
        fetch_element(driver, '#okta-signin-username').send_keys('mouradmarzouk')
        fetch_element(driver, '#okta-signin-password').send_keys(password)
        fetch_element(driver, '#okta-signin-submit').click()
        fetch_element(driver, 'input[value="Send Push"]').click()
        sleep(3)

    driver.find_element_by_xpath(button).click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, path)))
    driver.find_element_by_xpath(path).click()
    sleep(100)
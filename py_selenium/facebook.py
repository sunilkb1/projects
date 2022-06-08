"""
description: Script to login to facebook, print hello <user> and logout via UI automation.
usage:
python3 facebook_login.py -u/--username <username> --p
requirements:
Place the compatible chromedriver in /usr/local/bin/chromedriver
"""

import os
import time
import argparse
import re
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Facebook:

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-u", "--username", help="Login user", required=True)
        parser.add_argument("-p", "--password", help="Login Password", required=True)
        self.args = parser.parse_args()
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--incognito")
        options.add_argument("start-maximized")
        s = Service("/usr/local/bin/chromedriver")
        self.driver = webdriver.Chrome(service=s, options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get("https://www.facebook.com/")
        self.title = self.driver.title

    def login(self):
        username = self.driver.find_element(By.ID, "email")
        password = self.driver.find_element(By.ID, "pass")
        login = self.driver.find_element(By.NAME, "login")
        username.send_keys(self.args.username)
        password.send_keys(self.args.password)
        login.click()
        WebDriverWait(self.driver, 30).until_not(EC.title_is(self.title))
        self.title = self.driver.title

    def print_info(self):
        print("----------------------------------------------------------------------")
        user = re.search(r'What\'s on your mind,(.*?)\?', self.driver.page_source).group(1)
        print("Hello {}".format(user))
        birthday = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                       '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div/div[1]/div/div[2]/div/a/div[1]/div[2]/div/div/div')))
        print("Please note: {}".format(birthday.text))
        print("----------------------------------------------------------------------")

    def logout(self):
        drop_down = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/span/div')))
        drop_down.click()
        logout = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                  '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[5]/div/div[1]')))
        logout.click()
        WebDriverWait(self.driver, 30).until_not(EC.title_is(self.title))

    def cleanup(self):
        self.driver.close()


# Main
if __name__ == '__main__':
    f = Facebook()
    f.login()
    f.print_info()
    f.logout()
    f.cleanup()

import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from helper import helper

global config

def hackerrank(task_config):
    global config
    config=task_config
    url=task_config['url']
    
    #navigate to hackerrank
    helper.get_request(url)

    #login in hackerrank
    login()

    #naviagate to problem
    navigate_problem(config['tutorial'][0])
    
def login():
    #click login button
    helper.xpath_click(".//button[@class='hrds-btn login-btn']")

    #click github button
    helper.xpath_click("(.//img[@class='social-btn-icon'])[4]")

    #get windows details [0]:hackerrank, [1]:github
    # window=helper.get_window_handle()

    # #switch to github login window
    # helper.switch_window(window[1])

    # #enter credential
    # helper.xpath_send_key("", ".//input[contains(@name,'login')]")
    # helper.xpath_send_key("", ".//input[contains(@name,'password')]")
    # helper.xpath_click(".//input[contains(@name,'commit')]")

    # #switch to hackerrank window
    # helper.switch_window(window[0],len(window))

    #wait for manual login in github
    helper.hit_xpath_time(".//img[contains(@alt, 'mritunjaysri28')]", 1500)


def navigate_problem(task):
    url=task['tutorialUrl']
    sub_drictory=task['subDirectory']
    tutorial_name=task['tutorialName']
    
    #navigate to tutorial
    helper.get_request(url)

    #scroll all record
    helper.xpath_click(".//input[contains(@value,'solved')]")
    helper.dynamic_scrolling()

def scrap_code():
    elements=helper.get_elements(".//span[text()='Solved']")
    print(elements)
import os
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = None


def get_driver():
    '''return driver object'''
    global driver
    return driver

def start_driver(browser):
    '''Launch browser'''

    global driver

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61"
    browser_path = os.path.join(os.getcwd(), 'driver', browser['driver'])
    service = Service(browser_path)

    options = Options()
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("start-maximized")
    options.add_experimental_option("detach", True)

    try:
        if browser['browser'] == 'edge':
            driver = webdriver.Edge(service=service, options=options, keep_alive=True)
    except:
        print(">>> Failed to launch browser")
        return

def close_driver():
    '''close browser'''
    global driver
    driver.quit()

def get_request(url):
    '''Hit the URL'''
    global driver
    try:
        driver.get(url)
    except:
        print(">>> Failed to hit url ", url)

def hit_xpath(xpath, return_flag=False):

    global driver
    try:
        elements = driver.find_elements(By.XPATH, xpath)                    
    except:
        print(">>> xpath not found ", xpath)
    
    return elements

def xpath_send_key(text, xpath):
    elements=hit_xpath(xpath=xpath)
    for element in elements:
        element.send_keys(text)

def xpath_click(xpath):
    elements=hit_xpath(xpath)
    for element in elements:
        element.click()

def dynamic_scrolling():
    xpath_click(".//input[contains(@value, 'solved')]")
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        element = driver.find_element(
            By.XPATH, ".//footer[@class='community-footer']")

        # Scroll down to bottom
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(30)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height

def new_tab():
    global driver

    # get current url
    current_url = driver.current_url

    # create new tab
    driver.switch_to.new_window('tab')

    # get tab details
    tab = driver.window_handles

    get_request(current_url)       

def hit_xpath_time(xpath, time):
    
    global driver

    try:
        WebDriverWait(driver, time).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    except:
        print(">>> Timeout to hit xpath")

def get_elements(xpath):
    return hit_xpath(xpath)
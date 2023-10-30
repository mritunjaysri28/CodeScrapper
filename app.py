from utils import utils
from helper import helper
import hackerrank

if __name__ == "__main__":

    # read config file
    browser = utils.read_json('./config/config.json')
    task_config = utils.read_json(browser['task_config'])

    task_name = browser['task_name']

    # start browser
    helper.start_driver(browser['browser'])

    if task_name == 'hackerrank':
        hackerrank.hackerrank(task_config)

    # close webdriver
    helper.close_driver()

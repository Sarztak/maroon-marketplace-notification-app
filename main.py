# This project is still work in progress

import logging.config
from re import I
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from scrapy import Selector
import time
import logging


def get_browser():
    '''
    Function to start the browser in headless mode
    '''
    logging.info("Opening connection...") 
    driver_path = r".\chromedriver.exe"
    try:
        service = Service(driver_path)
        option = webdriver.ChromeOptions()
        option.add_argument("--headless=new")
    except Exception as e:
        logging.info('e')
    
    return webdriver.Chrome(service=service, options=option)

def print_titles(browser, url):
    '''
    Basic function to print the title for checking purpose
    '''
    logging.info("Printing Titles...")

    try:
        logging.info("Started Parsing")
        browser.get(url)
        _class = "text-lg font-medium text-gray-900 hover:text-gray-600"
        time.sleep(2) # need to wait until page loads completely
        new_selector = Selector(text=browser.page_source)
        titles = new_selector.xpath(f"//h2[@class='{_class}']/text()").getall()
        logging.info(f'Parsing {titles}') 
        print(titles)
    except Exception as e:
        logging.debug(e)
    finally:
        browser.close()
        logging.info('closing browser')



def main():
    logging.info("Start")
    browser = get_browser()
    url = "https://marketplace.chicagomaroon.com/category/for-sale/computers" 
    print_titles(browser, url)

if __name__ == "__main__":
    logging.basicConfig(level='DEBUG')
    main()

   
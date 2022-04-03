#import required library
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import bs4
import time
import sqlite3
import pandas as pd
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import os

def download_files():
    '''
    this function will download both csv files
    '''
    # installing driver
    path = os.getcwd()
    print(path)
    chrome_options = webdriver.ChromeOptions()
    pref =  {"download.default_directory":path,"safebrowsing.enabled":"false"}
    chrome_options.add_experimental_option("prefs",pref)
    desired_capabilities= DesiredCapabilities.CHROME.copy()
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=chrome_options,desired_capabilities=desired_capabilities)

    #fetch “Securities available for Equity segment (.csv)” file
    driver.get('https://www.nseindia.com/market-data/securities-available-for-trading')
    # click on csv to download
    driver.find_element_by_xpath('/html/body/div[8]/div/section/div/div/div/div/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div/p[1]/a').click()
    print('Securities available for Equity segment (.csv) file downloaded')
    time.sleep(5)
    # get the latest “bhavcopy” csv file
    driver.get('https://www.nseindia.com/all-reports')
    # get search field
    search = driver.find_element_by_xpath('//*[@id="crEquityDailySearch"]')
    # search bhavcopy file
    search.send_keys("bhavcopy")
    # click on file
    driver.find_element_by_xpath('//*[@id="cr_equity_daily_Current"]/div/div[26]/div/div/span[3]/a').click()

    print('bhavcopy csv file downloded')

def insert_data():


    connection = sqlite3.connect('database.db')

    with open('schema.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()
    securities_data = pd.read_csv('E')
    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                ('First Post', 'Content for the first post')
                )

    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                ('Second Post', 'Content for the second post')
                )

    connection.commit()
    connection.close()

if __name__ == '__main__':
    download_files()
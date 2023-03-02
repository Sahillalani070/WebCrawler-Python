"""
------------------------------------------------------------------------
[Crawler]
------------------------------------------------------------------------
Author(s): Sahil Lalani
File Name: crawler.py
Updated: 2021-07-21
------------------------------------------------------------------------
Notes:
------------------------------------------------------------------------
"""

# Import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import random
import time
from bs4 import BeautifulSoup


# Constants
CAT_DIR = "Categories\\"
SEARCH = "http://www.duckduckgo.com/?q="


"""
------------------------------------------------------------------------
Initialize Web Driver
------------------------------------------------------------------------
"""

options = Options()
# options.headless = True
options.add_argument("--log-level=3")
options.add_argument("--ignore-certificate-errors-spki-list")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
options.add_argument("start-maximized")


"""
------------------------------------------------------------------------
Run
------------------------------------------------------------------------
"""


print("Initializing Directories...")

if not os.path.exists("Categories"):
    print("\n'Categories' directory does not exists.")
    print("Creating directory...")
    os.mkdir("Categories")
    print("Done.\n")
else:
    print("\n'Categories' directory exists.\n")


"""
========================================================================
Step 1: Get Category List
========================================================================
"""

cat = "0"
cat_list = []

while cat != "":
    cat = input("Enter a category (press enter to end): ")
    if cat != "":
        cat_list.append(cat)


sample_size = int(input("\nEnter sample size: "))


"""
========================================================================
Step 2: Crawl
========================================================================
"""

print("-_"*30)

print("\n\nOpening Browser...")
driver = webdriver.Chrome(r'C:\Users\sahil\Downloads\chromedriver_win32\chromedriver.exe')

# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
wait = WebDriverWait(driver, 45)

for category in cat_list:
    print(f"\n:: Accessing Category ~ [{category}] ::")

    try:
        if not os.path.exists(CAT_DIR + str(category)):
            os.mkdir(CAT_DIR + str(category))

        url = SEARCH + \
            category.replace(" ", "+").replace("&", "+").replace("-", "+")
        driver.get(url)
        random_wait = random.randint(0, 20)
        time.sleep(random_wait)

        for n in range(1, sample_size+1):
            driver.find_element_by_xpath(
                f'/html/body/div[2]/div[5]/div[3]/div/div[1]/div[5]/div[{n}]/div/h2/a[1]').click()

            #======================================================================
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            text = soup.find_all(text=True)

            output = ''
            blacklist = [
                '[document]',
                'noscript',
                'header',
                'html',
                'meta',
                'head',
                'input',
                'script',
                # there may be more elements you don't want, such as "style", etc.
            ]

            for t in text:
                if t.parent.name not in blacklist:
                    output += '{} '.format(t)

            print(output)
            #======================================================================


            time.sleep(2)


            driver.execute_script("window.history.go(-1)")




    except:
        print("Unable to process this category")


# try:
#     driver.find_element_by_xpath().click()
#     random_wait = random.randint(0,5)
#     time.sleep(random_wait)
# except:
#     print("Automation Detected!")

print("-_"*30)
# driver.close()
print("\nBrowser Closed.")
print("\nScript Ended.")

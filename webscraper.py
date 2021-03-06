from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import csv
import time
import os

def runWebscraper(userInput):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    toolNum = userInput
    url = 'https://nocodefamily.com/tools'
    browser = webdriver.Chrome(executable_path="./chromedriver.exe",chrome_options=options)
    browser.get(url)
    siteTools = []
    siteName = ""
    toolURL = ""
    links = ""
    csvBody = []
    csvRow = []

    # Loads entire webpage
    for i in range(0, 16):
        browser.find_element(By.XPATH, '//body').send_keys(Keys.CONTROL + Keys.END)
        time.sleep(2)

    # Goes through all links of each tool in website and put them inside a list
    for i in range(1, toolNum + 1):
        links = browser.find_element(By.XPATH, f"/html/body/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div[1]/div[not(contains(@class, 'list-dummy'))][{i}]/div/div/div/div/div/a")
        if "https://nocodefamily.com/tool/" not in links.get_attribute("href"):
            siteTools.append("External link")
        else:
            siteTools.append(links.get_attribute("href"))

    # For each tool in list, gathers all user reviews and puts them on a list
    for i in range(toolNum):
        if siteTools[i] == "External link":
            csvBody.append(["Site leads to external link", "Could not obtain reviews."])
            continue
        browser.get(siteTools[i])
        time.sleep(5)
        siteName = browser.find_element(By.XPATH, f'//*[@id="no-translate"]').get_attribute("innerText")
        browser.find_element(By.XPATH, f'//*[@id="index"]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div').click()
        revTab = browser.find_element(By.XPATH, f'//*[@id="menu_1"]/div[2]') # XPATH for review tab

        time.sleep(3)
        browser.find_element(By.XPATH, '//body').send_keys(Keys.PAGE_DOWN) 
        browser.find_element(By.XPATH, '//body').send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        revPro = browser.find_elements(By.XPATH, f'//*[@id="index"]/div/div[3]/div[2]/div[3]/div/div[1]/div[2]/div[not(contains(@style, "display: none"))]/div/div[1]/div[1]') # XPATH for pro tool reviews

        if len(revPro) != 0:
            for p in revPro:
                print(p.get_attribute("innerHTML"))
                csvRow.append(siteName)
                csvRow.append(p.get_attribute("innerHTML"))
                csvBody.append(csvRow)
                csvRow = []

        else:
            print("No positive reviews")

        revCon = browser.find_elements(By.XPATH, f'//*[@id="index"]/div/div[3]/div[2]/div[3]/div/div[2]/div[2]/div[not(contains(@style, "display: none"))]/div/div[1]/div[1]') # XPATH for con tool reviews

        if len(revCon) != 0:
            for c in revCon:
                print(c.get_attribute("innerHTML")) 
                csvRow.append(siteName)
                csvRow.append(c.get_attribute("innerHTML"))
                csvBody.append(csvRow)
                csvRow = []
        else:
            print("No negative reviews")

        if len(revCon) == 0 and len(revPro) == 0:
            csvRow.append(siteName)
            csvRow.append("No reviews")
            csvBody.append(csvRow)
            csvRow = []

    print(csvBody)

    if not os.path.exists("reviewScraper.csv"):
        # create csv file
        with open("reviewScraper.csv", "x", encoding="utf-8"):
            print("File created")
                
    with open("reviewScraper.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerows(csvBody)
        print("File written") 



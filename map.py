from selenium import webdriver
import pandas as pd
import html5lib
import re
import numpy as np
from os import access, path, mkdir
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException


print(f"{open('extra/welcome.txt', encoding='UTF-8').read()}\n\n") #Welcomes user.

veto = []
bans = []
picks = []

options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)



teamId = input("Enter TeamID from VLR.GG: ")


driver.get("https://www.vlr.gg/team/matches/" + teamId)


wait = WebDriverWait(driver, 30)

teamNametoShow = driver.find_element(By.XPATH, "//*[@id='wrapper']/div[1]/div/div[1]/div[1]/div[2]/div/div[1]/h1").text
teamName= driver.find_element(By.XPATH, "//*[@id='wrapper']/div[1]/div/div[1]/div[1]/div[2]/div/div[1]/h2").text
print("Getting " + teamNametoShow + " first map bans & picks... this might take a bit.")

print("Note: this will scrape recent 25 games, max is 50 using the open source file")



i=0

def doForEachGame(i): 
    btn = driver.find_element(By.XPATH, f"//*[@id='wrapper']/div[1]/div/div[3]/div[{i}]/a/div[1]").click()
    try:
      element = driver.find_element(By.XPATH, "//*[@id='wrapper']/div[1]/div[3]/div[1]/div[3]")
      
      
      if teamName +' ban' in element.text:
       mapBanned= element.text.split(teamName +' ban')[1].split()[0]
       mapBanC = mapBanned.replace(";", "")
       bans.append(mapBanC)


      if teamName +' pick' in element.text:
       mapPicked= element.text.split(teamName +' pick')[1].split()[0]
       mapPickC = mapPicked.replace(";", "")
       picks.append(mapPickC)




      #veto.append(element.text)
    except NoSuchElementException:
       print("Found a game with no veto, proceeding to next game...")
     
    driver.back()
 
while i < 26: #Change this to 50 if you'd like to do recent 50, DO NOT GO BEYOND 50.
    i = i + 1
    doForEachGame(i)



finalBans = {}

for b in bans:
    finalBans[b] = bans.count(b)

BansDF = pd.DataFrame(finalBans.items(), columns=['Maps', 'First Bans Amount'])



finalPicks = {}

for p in picks:
    finalPicks[p] = picks.count(p)

PicksDF = pd.DataFrame(finalPicks.items(), columns=['Maps', 'First Picks Amount'])


result = pd.concat([BansDF, PicksDF], axis=1)

finalResult = result.replace(np.nan, '', regex=True)

print(finalResult)


finalResult.to_csv(teamName + " Veto.csv", encoding='utf-8', index=False)
print("A csv file has been exported, close now...")
    
    


driver.quit()






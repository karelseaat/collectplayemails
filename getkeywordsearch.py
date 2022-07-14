#!/usr/bin/env python

import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from models import App

from config import make_session


options = Options()
options.add_argument("--headless")

dbsession = make_session()

SCROLL_PAUSE_TIME = 3

def get_list_of_ids(listofsearch):
    """get a list of app ides with the search tags we are looking for"""
    allresults = []

    for toseach in listofsearch:
        driver = webdriver.Firefox(
            executable_path= r"./geckodriver", options=options
        )
        driver.get(f'https://play.google.com/store/search?q={toseach}&c=apps')

        last_height = driver.execute_script(
            "return document.body.scrollHeight"
        )

        while True:
            # Scroll down to bottom
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script(
                "return document.body.scrollHeight"
            )
            if new_height == last_height:
                break
            last_height = new_height

        klont = driver.find_element_by_class_name("Ktdaqe").find_elements_by_tag_name('c-wiz')
        for ele in klont:
            alla = ele.find_elements_by_tag_name('a')
            if len(alla) >= 4:
                allresults.append(alla[0].get_attribute('href').split("=")[1])

        driver.quit()
    return allresults


allids =  get_list_of_ids(['mesenger', 'display', 'screen', 'android', 'lingo', 'painter', 'printer', 'color', 'learn', 'daily', 'sky', 'note', 'power', 'interior', 'blog', 'player', 'running', 'design', 'stream', 'family', 'browser', 'share', 'music'])
# allids = get_list_of_ids(['surver', 'survers', 'bride', 'princess', 'Airplane game', 'farm game', 'saga game', 'ball game', 'pool game', 'Crossword', 'brawl game', 'magic game', 'tile game', 'build game', 'storys', 'shooter game', 'bubble game', 'network tool', 'wifi', 'editor', 'sound', 'car game'])
# allids = get_list_of_ids(['cars', 'car', 'house', 'finder', 'trees', 'party', 'searcher', 'animal', 'airplane', 'shopper', 'shop', 'walk', 'speed', 'energy', 'power'])
# allids = get_list_of_ids(['altitude meter', 'romantic dice', 'camera gps', 'tank game', 'dice 3D', 'dating', 'recepie app', 'live wallpaper', 'food games', 'local area', 'story', 'sound recorder', 'spirit level', 'singing app', 'photo effects', 'pictures', 'funny', 'spot', 'match', 'tracker', 'ruler', 'scanner', 'star', 'brain', 'learn', 'table', 'lessons', 'daily', 'commics', 'compass', 'radar', 'rpg', 'trails', 'view'])
# allids = get_list_of_ids(['daily', 'commics'])


print("allids:" + str(len(allids)))

double = 0

for aid in allids:

    aApp = App()
    aApp.appid = aid

    count = dbsession.query(App).filter(App.appid == aid).count()
    if count == 0:
        dbsession.add(aApp)
        dbsession.commit()
    else:
        double += 1

print("double:" + str(double))
dbsession.close()

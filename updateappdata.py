#!/usr/bin/env python

import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from models import App
from config import make_session

options = Options()
options.add_argument("--headless")

dbsession = make_session()

result = dbsession.query(App).filter(App.email.is_(None)).all()

for ares in result:
    print(f"Starting: {ares.appid} nr {result.index(ares)} of {len(result)}")
    driver = webdriver.Firefox(
        executable_path= r"/home/aat/Desktop/geckodriver", options=options
    )
    driver.get(f'https://play.google.com/store/apps/details?id={ares.appid}')

    try:
        tempo = driver.find_element_by_tag_name("main").find_elements_by_class_name("hAyfc")
    except Exception as e:
        tempo = []

    nogbeter = []

    if tempo:
        try:
            rest = tempo[0].find_elements_by_tag_name('span')[-1].get_attribute('innerHTML')
            something = datetime.datetime.strptime(rest, "%B %d, %Y").date()
        except Exception as e:
            print(e, ares.appid)
            something = None

        try:
            anothersomething = int(
                tempo[2].
                find_elements_by_tag_name('span')[-1].
                get_attribute('innerHTML')[:-1].
                replace(',', '')
            )
        except Exception as e:
            print(e, ares.appid)
            anothersomething = None

        ass = tempo[-1].find_elements_by_tag_name('a')
        lel = [a.get_attribute('href') for a in ass]

        nogbeter = [a for a in lel if a and 'mailto' in a]

    if nogbeter:
        mail = nogbeter[0].split(":")[1]
        ares.email = mail
        if something:
            ares.lastupdate = something
        if anothersomething:
            ares.installs = anothersomething

        dbsession.commit()

    driver.quit()


dbsession.close()

#!/usr/bin/env python

import datetime
from models import App

from config import make_session


dbsession = make_session()

now = datetime.datetime.now()
sixmonthsago = now - datetime.timedelta(days=128)

result = dbsession.query(App).filter(App.installs > 50).filter(App.id > 11493).filter(App.installs < 500).filter(App.lastupdate > sixmonthsago).distinct(App.email).all()

for res in result:
    print(res.email, res.appid)

#!/usr/bin/env python

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *
import datetime

from config import (
    make_session
)

dbsession = make_session()

now = datetime.datetime.now()
sixmonthsago = now - datetime.timedelta(days=128)

result = dbsession.query(App).filter(App.installs > 50).filter(App.installs < 500).filter(App.lastupdate > sixmonthsago).all()

for res in result:
    print(res.email, res.appid)

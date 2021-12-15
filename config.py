
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models import Base
import os


CONNECTIONURI = "sqlite:////{}/appstomail.sqlite".format(os.path.dirname(__file__))


def make_session():
    engine = create_engine(CONNECTIONURI, echo=False, connect_args={'check_same_thread': False})
    dbsession = scoped_session(sessionmaker(bind=engine))
    Base.metadata.create_all(engine)
    return dbsession()

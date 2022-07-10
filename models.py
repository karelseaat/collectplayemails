from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Boolean, Date
from sqlalchemy_utils import get_hybrid_properties


Base = declarative_base(name="Base")
metadata = Base.metadata

class DictSerializableMixin(Base):
    __abstract__ = True

    def _asdict(self):
        """will return a query and its props in dict form"""
        result = {}

        for key in self.__mapper__.c.keys() + list(get_hybrid_properties(self).keys()):
            result[key] = getattr(self, key)
        return result

    def _asattrs(self, adict, afilter):
        """will return a query and its props as attrs ?"""
        for key, val in adict.items():
            if hasattr(self, key) and key in afilter:
                setattr(self, key, val)

class App(DictSerializableMixin):
    """Users with names emails google ids etc"""
    __tablename__ = 'app'

    id = Column(Integer, primary_key=True)
    appid = Column(String(128))
    email = Column(String(128))
    # companyname = Column(String(128))
    installs = Column(Integer)
    lastupdate = Column(Date, nullable=True)
    sendemail = Column(Boolean, default=False)

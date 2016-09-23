from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import basedir
import os

engine = create_engine('sqlite:///' + os.path.join(basedir, 'alumni.db'), echo=True, convert_unicode=True)
metadata = MetaData(bind=engine)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = session.query_property()

def create_session():
	import alumni.models
	Base.metadata.reflect(engine)
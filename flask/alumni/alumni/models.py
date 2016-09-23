from alumni import db, app
from alumni.database import Base, session
from sqlalchemy import Column, Text, Integer, Float


class Alum(Base):
	__tablename__ = 'alums'
	__searchable__ = ['zipcode']
	first_name = Column(Text)
	last_name = Column(Text)
	id = Column(Integer, primary_key=True)
	zipcode = Column(Text)
	lat = Column(Float)
	lon = Column(Float)

	def __repr__(self):
		return '<Alumni %r>' % (self.id)

	def serialize(self):
		return {
			'first_name': self.first_name,
			'last_name':self.last_name,
			'id': self.id,
			'zipcode': self.zipcode,
			'lat': self.lat,
			'lon': self.lon
		}

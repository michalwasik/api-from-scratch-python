from sqlalchemy import create_engine,Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///racetrack.db', connect_args={'check_same_thread': False})
Base = declarative_base()




class Track(Base):
    __tablename__ = 'track'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    slugname = Column(String)
    stuff = relationship('Data', backref='track')


class Data(Base):
    __tablename__ = 'data'

    id = Column(Integer, primary_key=True)
    driver = Column(String)
    time = Column(Float)
    car = Column(String)
    added = Column(String)
    track_id = Column(Integer, ForeignKey('track.id'))

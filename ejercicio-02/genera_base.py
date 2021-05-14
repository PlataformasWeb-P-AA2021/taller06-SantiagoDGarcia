from sqlalchemy import create_engine

engine = create_engine('sqlite:///pais.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Pais(Base):
    __tablename__ = 'Pais'
    
    id = Column(Integer, primary_key=True)
    pais = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geoname_id = Column(String)
    itu = Column(String)
    lenguajes = Column(String)
    independiente = Column(String)

    def __repr__(self):
        return "Nombre Pais:%s || Capital:%s || Continente:%s || Dial:%s || Geoname ID:%s || ITU:%s || Lenguajes:%s || Es independiente:%s ||\n" % (
                          self.pais, 
                          self.capital, 
                          self.continente, 
                          self.dial, 
                          self.geoname_id, 
                          self.itu,
                          self.lenguajes,
                          self.independiente)

Base.metadata.create_all(engine)


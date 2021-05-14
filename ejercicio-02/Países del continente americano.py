from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from genera_base import Pais 

engine = create_engine('sqlite:///pais.db')
Session = sessionmaker(bind=engine)
session = Session()

continente_americano = session.query(Pais).filter(or_(Pais.continente=="SA", Pais.continente=="NA")).all()
print(continente_americano)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from genera_base import Pais 

engine = create_engine('sqlite:///pais.db')
Session = sessionmaker(bind=engine)
session = Session()

paises_europa = session.query(Pais).filter(Pais.continente=="EU").order_by(Pais.capital).all()
print(paises_europa)

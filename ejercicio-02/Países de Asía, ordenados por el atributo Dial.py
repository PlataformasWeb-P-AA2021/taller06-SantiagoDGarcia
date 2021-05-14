from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from genera_base import Pais 

engine = create_engine('sqlite:///pais.db')
Session = sessionmaker(bind=engine)
session = Session()

paises_asia = session.query(Pais).filter(Pais.continente=="AS").order_by(Pais.dial).all()
print(paises_asia)

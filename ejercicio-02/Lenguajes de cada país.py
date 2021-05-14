from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from genera_base import Pais 

engine = create_engine('sqlite:///pais.db')
Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Pais).all()

for s in paises:
    print("Nombre Pais: %s  Lenguajes:%s" % (s.pais, s.lenguajes))


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from genera_base import Pais 

engine = create_engine('sqlite:///pais.db')
Session = sessionmaker(bind=engine)
session = Session()

paises_cadena =  session.query(Pais).filter(or_(Pais.pais.like("%uador%"), Pais.capital.like("%ito%"))).all()  
print(paises_cadena)
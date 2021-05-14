from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_base import Pais
import requests
import json

engine = create_engine('sqlite:///pais.db')
Session = sessionmaker(bind=engine)
session = Session()

archivo = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json", "r")
datos_json = archivo.json()

for d in datos_json:
	session.add(Pais(pais=d['CLDR display name'], capital=d['Capital'], continente=d['Continent'], dial=d['Dial'], geoname_id=d['Geoname ID'], itu=d['ITU'], lenguajes=d['Languages'], independiente=d['is_independent']))

session.commit()
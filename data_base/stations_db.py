from sqlalchemy import Table, Column, Integer, String, Date, MetaData, ForeignKey
from sqlalchemy import create_engine
import csv
import os

db_file = 'stations.db'

# For demo purposes always create a data base from scratch.
if os.path.exists(db_file):
    os.remove(db_file)

engine = create_engine(f'sqlite:///{db_file}', echo = True)

meta = MetaData()
countries = Table(
    'countries', meta,
    Column('code', String(2), primary_key = True),
    Column('name', String)
)
states = Table(
    'states', meta,
    Column('code', String(2), primary_key = True),
    Column('country_code', String(2), ForeignKey('countries.code')),
    Column('name', String)
)
meta.create_all(engine)

with open('clean_stations.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    print(reader.fieldnames)


from sqlalchemy import Table, Column, Integer, SmallInteger, String, Date, Float, MetaData, ForeignKey
from sqlalchemy import create_engine
from datetime import date
import csv
import os

db_file = 'stations.db'

# For demo purposes always create a data base from scratch.
if os.path.exists(db_file):
    os.remove(db_file)

engine = create_engine(f'sqlite:///{db_file}')

meta = MetaData()
countries = Table(
    'countries', meta,
    Column('code', String(2), primary_key = True),
    Column('name', String)
)
states = Table(
    'states', meta,
    Column('code', String(2), primary_key = True),
    Column('country', String(2), ForeignKey('countries.code')),
    Column('name', String)
)
stations = Table(
    'stations', meta,
    Column('station', String(11), primary_key = True),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('elevation', Float),
    Column('name', String),
    Column('country', String(2), ForeignKey('countries.code')),
    Column('state', String(2), ForeignKey('states.code'))
)
measures = Table(
    'measures', meta,
    Column('id', Integer, primary_key = True, autoincrement = True),
    Column('station', Integer, ForeignKey('stations.station')),
    Column('date', Date),
    Column('precip', Float),
    Column('tobs', SmallInteger)
)
meta.create_all(engine)

conn = engine.connect()
conn.execute(countries.insert().values(code = 'US', name = 'United States of America'))
conn.execute(states.insert().values(code = 'HI', country = 'US', name = 'Hawaii'))

with open('clean_stations.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    ins = stations.insert()
    conn.execute(ins, list(reader))

with open('clean_measure.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    ins = measures.insert()
    for row in reader:
        conn.execute(ins.values(station = row['station'], date = date.fromisoformat(row['date']), precip = row['precip'], tobs = row['tobs']))

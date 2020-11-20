from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, String, Table, MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser
import os

config = configparser.ConfigParser()
config.read('config.ini')
user = config.get('MYSQL', 'USER')
try:
    passwd = config.get('MYSQL', 'PASSWD')
except:
    passwd = None
host = config.get('MYSQL', 'HOST')
database = config.get('MYSQL', 'DATABASE')


languages = {}
strings = {}
new_str = {}

d = config.get('DEFAULT', 'strings_location')

for fn in os.listdir(d):
    if fn.startswith('strings_'):
        with open(d + fn, 'r', encoding='utf-8') as f:
            a = f.read()

            lang_strings = eval(a)

            strings[fn[8:10]] = lang_strings

            languages[lang_strings['__full__']] = fn[8:10]

for language, s in strings.items():
    out = {}
    for key, value in s.items():
        if isinstance(value, str):
            out[key] = value

        elif isinstance(value, dict):
            for key2, value2 in value.items():
                out['{}/{}'.format(key, key2)] = value2

    new_str[language] = out

print('Languages enabled: ' + str(languages))


if passwd:
    engine = create_engine('mysql+pymysql://{user}:{passwd}@{host}/{db}?charset=utf8mb4'.format(user=user, passwd=passwd, host=host, db=database))
else:
    engine = create_engine('mysql+pymysql://{user}@{host}/{db}?charset=utf8mb4'.format(user=user, host=host, db=database))

Base = declarative_base()


class Languages(Base):
    __tablename__ = 'languages'

    id = Column(Integer, primary_key=True)
    name = Column( String(20), nullable=False )
    code = Column( String(2), nullable=False )


Base.metadata.bind = engine

Session = sessionmaker(bind=engine)
session = Session()

strings_table = Table('strings', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', Text),
    Column('language', Text),
    Column('value', Text),
)

inserted = []

try:
    strings_table.drop()
except:
    pass

strings_table.create()

session.query(Languages).delete(synchronize_session='fetch')

lang_orms = [Languages(code=code, name=name) for name, code in languages.items()]
[session.add(x) for x in lang_orms]

for lang, strings in new_str.items():
    for key, value in strings.items():
        session.execute('''INSERT INTO strings (name, language, value) VALUES (:name, :lang, :val)''', {"name": key, "lang": lang, "val": value})

session.commit()

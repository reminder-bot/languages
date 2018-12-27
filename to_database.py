from sqlalchemy import Column, Integer, Text, Table, MetaData
from sqlalchemy import create_engine
import configparser
import os

config = configparser.SafeConfigParser()
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

d = config.get('DEFAULT', 'strings_location')

for fn in os.listdir(d):
    if fn.startswith('strings_'):
        with open(d + fn, 'r', encoding='utf-8') as f:
            a = f.read()
            strings[fn[8:10]] = eval(a)

            languages[a.split('\n')[0].strip('#:\n ')] = fn[8:10]

for language, s in strings.items():
    pass

print('Languages enabled: ' + str(languages))


if passwd:
    engine = create_engine('mysql+pymysql://{user}:{passwd}@{host}/{db}?charset=utf8mb4'.format(user=user, passwd=passwd, host=host, db=database))
else:
    engine = create_engine('mysql+pymysql://{user}@{host}/{db}?charset=utf8mb4'.format(user=user, host=host, db=database))

meta = MetaData(bind=engine)

strings_table = Table('strings', meta,
    Column('id', Integer, primary_key=True),
    Column('name', Text),
    *(
        Column('value_{}'.format(lang), Text) for lang in languages.values()
    )
)

strings_table.drop()
strings_table.create()

engine.execute()

import psycopg2
import json

connection = psycopg2.connect(
  user = 'postgres',
  password = '1234',
  host = '127.0.0.1',
  port = '5432',
  database = 'fifa'
)

with open('data/nation.json', 'r') as jsonfile:
  data = jsonfile.read()

obj = json.loads(data)

cursor = connection.cursor()

create_nation_table_query = '''CREATE TABLE recap
  (
    ID INT PRIMARY KEY      NOT NULL,
    COUNTRY         TEXT    NOT NULL,
    APR_04_2019     INT     NULL,
    FEB_07_2019     INT     NULL,
    DEC_20_2018     INT     NULL,
    NOV_29_2018     INT     NULL,
    OCT_25_2018     INT     NULL,
    SEP_20_2018     INT     NULL,
    AUG_16_2018     INT     NULL,
    JUNE_07_2018    INT     NULL,
    MAY_17_2018     INT     NULL,
    APR_12_2018     INT     NULL
  );'''
cursor.execute(create_nation_table_query)

i = 0
for data in obj['data']:
  postgres_insert_query = """INSERT INTO recap (ID, COUNTRY) VALUES (%s,%s)"""
  record_to_insert = (i, data['name'])
  cursor.execute(postgres_insert_query, record_to_insert)
  i += 1
  postgres_update_query = """
    UPDATE recap
    SET
    APR_04_2019 = %s,
    FEB_07_2019 = %s,
    DEC_20_2018 = %s,
    NOV_29_2018 = %s,
    OCT_25_2018 = %s,
    SEP_20_2018 = %s,
    AUG_16_2018 = %s,
    JUNE_07_2018 = %s,
    MAY_17_2018 = %s,
    APR_12_2018 = %s
    WHERE COUNTRY = %s;
    """
  record_to_update = (
    data['recap'][0]['point'],
    data['recap'][1]['point'],
    data['recap'][2]['point'],
    data['recap'][3]['point'],
    data['recap'][4]['point'],
    data['recap'][5]['point'],
    data['recap'][6]['point'],
    data['recap'][7]['point'],
    data['recap'][8]['point'],
    data['recap'][9]['point'],
    data['name']
  )
  cursor.execute(postgres_update_query, record_to_update)

connection.commit()

cursor.close()
connection.close()
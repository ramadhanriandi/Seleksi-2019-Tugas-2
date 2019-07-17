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

# create_nation_table_query = '''CREATE TABLE nation
#   (ID INT PRIMARY KEY   NOT NULL,
#   NAME        TEXT      NOT NULL);'''
# cursor.execute(create_nation_table_query)

i = 0
for data in obj['data']:
  postgres_insert_query = """INSERT INTO nation (ID, NAME) VALUES (%s,%s)"""
  record_to_insert = (i, data['name'])
  cursor.execute(postgres_insert_query, record_to_insert)
  i += 1

connection.commit()

cursor.close()
connection.close()
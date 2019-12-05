import xml.etree.ElementTree
import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# Создание таблицы
# cursor.execute("""CREATE TABLE users
#                   (id INTEGER,
#                   user_id INTEGER,
#                     timestamp text,
#                    lat DOUBLE,
#                    lon DOUBLE)
#                """);

# получим элементы
e = xml.etree.ElementTree.parse('map.osm').getroot()

id = []
user_id = []
timestamp = []
lat = []
lon = []
for atype in e.findall('node'):
    id.append(atype.get('id'))
    user_id.append(atype.get('uid'))
    timestamp.append(atype.get('timestamp'))
    lat.append(atype.get('lat'))
    lon.append(atype.get('lon'))
    # print(atype.get('user'))

# users = list(users)
# print(users)

# Сохраняем изменения
for i in range(len(id)):
    cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (id[i], user_id[i], timestamp[i], lat[i], lon[i]))

for row in cursor.execute("SELECT * FROM users"):
    print(row)
# print(cursor.fetchall())

conn.commit()
conn.close()


import sqlite3

database = sqlite3.connect('db_test.db')
cursor = database.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS weather(
    weather_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    temp TEXT,
    wind TEXT,
    sunrise TEXT,
    sunset TEXT 
);
''')

database.commit()
database.close()
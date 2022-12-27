import sqlite3

database = sqlite3.connect('bot.db')
cursor = database.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS history(
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id BIGINT,
    city TEXT,
    temperature FLOAT,
    windspeed FLOAT,
    sunrise DATETIME,
    sunset DATETIME
);
''')

database.commit()
database.close()

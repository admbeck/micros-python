import psycopg2

database = psycopg2.connect(
    dbname='chetverg15',
    host='localhost',
    user='postgres',
    password='123456'
)

cursor = database.cursor()
cursor.execute('''
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(60),
    username VARCHAR(30),
    email  VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS posts(
    user_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title TEXT,
    body TEXT,
    userid INTEGER REFERENCES users(user_id) 
);
''')

database.commit()
database.close()
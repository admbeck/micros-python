import psycopg2
import requests

database = psycopg2.connect(
    dbname='chetverg15',
    host='localhost',
    user='postgres',
    password='123456'
)

cursor = database.cursor()

users = requests.get('https://jsonplaceholder.typicode.com/users').json()
posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()


for user in users:
    name = user['name']
    username = user['username']
    email = user['email']
    cursor.execute('''
    INSERT INTO users(name, username, email) VALUES (%s, %s, %s)
    ''', (name, username, email))
    database.commit()


for post in posts:
    title = post['title']
    body = post['body']
    userid = post['userId']
    cursor.execute('''
    INSERT INTO posts(title, body, userid) VALUES (%s, %s, %s)
    ''', (title, body, userid))
    database.commit()

database.close()

















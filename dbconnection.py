#!/usr/bin/python3
print('Content-Type: text/html; charset=utf-8 \r\n')
print('<h1>Подключение к БД PostgreSQL</h1>')
import psycopg2 as pgsql
from psycopg2 import OperationalError
try:
    connection = pgsql.connect(database='telega', user='bot', password='dh15975346', host='localhost', port='5432')
    print('<h2>Подключение к базе данных выполнено успешно</h2>')
    connection.close()
except OperationalError as error:
    print(f'<h2>Ошибка подключения к БД: {error} </h2>')
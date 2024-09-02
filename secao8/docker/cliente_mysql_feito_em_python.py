# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import pymysql
import dotenv
import os

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_ROOT_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            """
            create table if not exists customers(
            id int not null auto_increment,
            nome varchar(50) not null,
            idade int not null,
            primary key (id))
            """
        )
        connection.commit()
        print(cursor)
        
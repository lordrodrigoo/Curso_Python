import pymysql
import dotenv
import os
dotenv.load_dotenv()

TABLE_NAME = 'customers'

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_ROOT_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f"""
            create table if not exists {TABLE_NAME} (
                id int not null auto_increment,
                nome varchar(50) not null,
                idade int not null,
                primary key (id)
            );
            """
        )
        cursor.execute(f'truncate table {TABLE_NAME}')  # CUIDADO isso Limpa a tabela 
    connection.commit()
        

    with connection.cursor() as cursor:
        result = cursor.execute(
            f"""
            insert into {TABLE_NAME} (nome, idade)
            values ('Luiz', 25)
            """
        )
        print(result)
    connection.commit()
        
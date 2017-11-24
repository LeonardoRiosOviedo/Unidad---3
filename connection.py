"""Leonardo Rios Oviedo   23/11/2017
create the connection with the database Postgresql """

import psycopg2
from config import config

def connect():
    """Conect to the Postgresql database server"""
    conn = None

    try:
        params = config()

        print('Connecting to the Postgresql database')
        conn = psycopg2.connect(**params)
        print('Connecting')

        #create cursor
        cursor = conn.cursor()

        print('Postgresql database version:')
        cursor.execute('SELECT version()')

        #display the Postgresql database server version
        db_version = cursor.fetchone()
        print(db_version)

        #close the commication with the Postgresql
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


connect()






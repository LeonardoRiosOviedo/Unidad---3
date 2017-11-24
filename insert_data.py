"""Leonardo Rios Oviedo   23/11/2017
Insert a new vendor into the table if the vendors """
import psycopg2
from config import config



def insert_vendor(vendor_name):
    """Insert a new vendor into the table """
    sql = """INSERT INTO vendors(vendor_name)
             VALUES (%s) RETURNING vendor_id;"""
    connection = None
    vendor_id = None
    try:
        #read database cofiguration
        params = config()
        # connect to the PostgreSQL database
        connection = psycopg2.connect(**params)
        #create to new cursor
        cursor = connection.cursor()
        #execute the INSERT statement
        cursor.execute(sql, (vendor_name,))
        #get the generated id back
        vendor_id = cursor.fetchone()[0]
        # commit the changes to the database
        connection.commit()
        #close the communication width the database
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return vendor_id

def insert_vendor_list(vendor_list):
    """ insert multiple vendors into vendor table"""
    sql = "INSERT INTO vendors(vendor_name) VALUES (%s)"
    connection = None
    try:
        #read database configuration
        params = config()
        # connect to the PostgreSQL database
        connection = psycopg2.connect(**params)
        #create a new cursor
        cursor= connection.cursor()
        #execute the INSERT statement
        cursor.executemany(sql, vendor_list)
        # commit the changes to the database
        connection.commit()
        #close communication with the database
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
if __name__=='__main__':
    # insert one vendor
    # print(insert_vendor('3m Co.'))
    insert_vendor_list([('AKM Semiconductor Inc.',),
                      ('Asahi Glass Co Ltd.',),
                      ('Daikin Industries Ltd.',),
                      ('Dynacast International Inc.',),
                      ('Foster Electric Co. Ltd.',),
                      ('Murata Manufacturing Co. Ltd.',)])
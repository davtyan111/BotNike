# database/db.py

import mysql.connector
from config import MYSQL_CONFIG

def insert_photo(drive_file_id, tariff, location, subcode):
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor()
    
    query = """
        INSERT INTO photos (drive_file_id, tariff, location, subcode)
        VALUES (%s, %s, %s, %s)
    """
    values = (drive_file_id, tariff, location, subcode)
    cursor.execute(query, values)
    conn.commit()
    
    cursor.close()
    conn.close()
def get_all_locations():
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM locations")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_all_subcodes():
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM subcodes")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def add_subcode(name):
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO subcodes (name) VALUES (%s)", (name,))
    conn.commit()
    cursor.close()
    conn.close()

def delete_subcode(subcode_id):
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM subcodes WHERE id = %s", (subcode_id,))
    conn.commit()
    cursor.close()
    conn.close()



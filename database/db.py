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


def find_photo_by_filters(tariff, subcode, location):
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT drive_file_id FROM photos
        WHERE tariff = %s AND subcode = %s AND location = %s
        LIMIT 1
    """
    cursor.execute(query, (tariff, subcode, location))
    result = cursor.fetchone()

    cursor.close()
    conn.close()
    return result

# database/db.py

import mysql.connector
from config import MYSQL_CONFIG

def get_all_tariffs():
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tariffs")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_all_locations():
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM locations")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_all_subcodes():
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM subcodes")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result



# database/db.py

import mysql.connector
from config import MYSQL_CONFIG

# --- Добавление тарифа ---
def add_tariff(name):
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tariffs (name) VALUES (%s)", (name,))
    conn.commit()
    cursor.close()
    conn.close()

# --- Удаление тарифа ---
def delete_tariff(tariff_id):
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tariffs WHERE id = %s", (tariff_id,))
    conn.commit()
    cursor.close()
    conn.close()


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

def add_location(name):
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO locations (name) VALUES (%s)", (name,))
    conn.commit()
    cursor.close()
    conn.close()

def delete_location(location_id):
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM locations WHERE id = %s", (location_id,))
    conn.commit()
    cursor.close()
    conn.close()



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


def save_order(user_id, tariff, subcode, location):
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor()
    query = """
        INSERT INTO orders (user_id, tariff, subcode, location)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (user_id, tariff, subcode, location))
    conn.commit()
    cursor.close()
    conn.close()

def get_user_orders(user_id):
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT tariff, subcode, location, created_at
        FROM orders WHERE user_id = %s
        ORDER BY created_at DESC LIMIT 10
    """
    cursor.execute(query, (user_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


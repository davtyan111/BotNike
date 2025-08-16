# database/init.py

import mysql.connector
from config import MYSQL_CONFIG

def init_db():
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS photos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            drive_file_id VARCHAR(255) NOT NULL,
            tariff VARCHAR(50),
            location VARCHAR(50),
            subcode VARCHAR(50),
            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

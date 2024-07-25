import time
import psycopg2
from psycopg2 import OperationalError

def wait_for_psql():
    while True:
        try:
            conn = psycopg2.connect(
                dbname="postgres",
                user="odoo",
                password="odoo",
                host="db"
            )
            conn.close()
            break
        except OperationalError:
            print("PostgreSQL no está listo, esperando...")
            time.sleep(2)

wait_for_psql()

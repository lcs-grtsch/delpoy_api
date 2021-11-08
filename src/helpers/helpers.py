import psycopg2
import os


def get_value_from_db():
    try:
        conn = psycopg2.connect(
            host=os.environ['DB_HOST'],
            database=os.environ['DB_DATABASE'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'])
        sql = "SELECT to_regclass('schema_name.table_name');"
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        conn.close()
        if str(result) == '[(None,)]':
            return 'Connection successful!!!'
    except Exception as e:
        return str(e)


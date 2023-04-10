import psycopg2
conn = None
cur = None
try:
    conn = psycopg2.connect(
        host="localhost",
        database="suppliers",
        user="postgres",
        password="123456",
        port = "5432")

    cur = conn.cursor()
    create_script = ''' DROP TABLE IF EXISTS imdb '''

    cur.execute(create_script)
    conn.commit()
except Exception as error:
    print("error")
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
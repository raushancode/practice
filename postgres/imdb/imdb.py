import pandas as pd
import psycopg2
import csv

conn = psycopg2.connect(
        host="localhost",
                database="suppliers",
                user="postgres",
                password="123456",
                port = "5432"
)
cur = conn.cursor()
with open(r'C:\Users\Raushan\codes\postgres\imdb\imdb.csv', 'r') as file:
        contents = csv.reader(file)
        # remove 1st row as header
        next(contents, None)

        insert_records = '''INSERT INTO imdb (movie, year, certificate, "genre.1", "genre.2", "genre.3", imdb_rating, metascore, time_minute, vote, gross_earning) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

        cur.executemany(insert_records, contents)
conn.commit()
cur.close()
conn.close()
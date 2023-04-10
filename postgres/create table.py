import psycopg2
cur = None
conn =None
try:
    conn = psycopg2.connect(
        host="localhost",
                database="suppliers",
                user="postgres",
                password="123456",
                port = "5432"
    )
    cur = conn.cursor()
    cur.execute('''DROP TABLE IF EXISTS imdb''')
    create_script = ''' CREATE TABLE IF NOT EXISTS imdb (
                                        ID SERIAL	PRIMARY KEY NOT NULL
                                        , movie         varchar
                                        , year          varchar
                                        , certificate   varchar
                                        , "genre.1"     varchar
                                        , "genre.2"     varchar
                                        , "genre.3"     varchar
                                        , imdb_rating   varchar
                                        , metascore     varchar
                                        , time_minute   varchar
                                        , vote          varchar
                                        , gross_earning varchar
                                        ) '''
    cur.execute(create_script)
    conn.commit()
    print("Table Created")
except Exception as error:
    print("error")
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

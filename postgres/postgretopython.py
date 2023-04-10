import psycopg2
conn = None
cur = None
try:
    with psycopg2.connect(
            host="localhost",
            database="suppliers",
            user="postgres",
            password="123456",
            port = "5432") as conn:

        with conn.cursor() as cur:
            cur.execute('DROP TABLE IF EXISTS employee')
            create_script = ''' CREATE TABLE IF NOT EXISTS employee (
                                    ID SERIAL	PRIMARY KEY NOT NULL
                                    , NAME			VARCHAR(40)				NOT NULL
                                    , SALARY        INT
                                    , DEPT_ID VARCHAR(30)
                                    ) '''

            cur.execute(create_script)
            insert_script = ''' INSERT INTO employee(NAME, SALARY, DEPT_ID)
                            VALUES ('RAUSHAN', 1000, 'KIG'),
                                    ('mohan', 2000, 'kig'),
                                    ('gargi', 3000, 'mig') '''
            cur.execute(insert_script)
            cur.execute('select * from employee')
            for record in cur.fetchall():
                print(record[1], record[2], record[3])
                # print(record)
            conn.commit()
            print("table created")
except Exception as error:
    print("error")
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
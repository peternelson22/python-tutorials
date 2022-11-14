import psycopg2 as pg

con = pg.connect(host='localhost', user='postgres',
                       password='1234', database='nelson')
                # change the password and db name
cur = con.cursor()

try:
    # TRY AND EXECUTE ALL
    # cur.execute('CREATE TABLE jae(id int primary key, name varchar(100), email varchar(255))')
    # cur.execute('INSERT INTO jae VALUES(1, "jae", "jae@gmail.com")')
    # cur.execute("SELECT * FROM jae")
    # cur.execute("SELECT name, email FROM jae WHERE id = 1")
    # result = cur.fetchone()
    # cur.execute("UPDATE jae SET name = 'NELSON' WHERE id = 1")
    cur.execute("DELETE FROM jae WHERE id = 2")
    con.commit()
    # con.commit() # use commit when modifying the table like create, insert, update, delete
    # when reading, you don't have to use commit
    # for i in result:
    #   print(i)
except:
    print('Something went wrong')
    con.rollback()
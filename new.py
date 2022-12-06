import psycopg2 as p

con = p.connect(host = 'localhost', user = 'postgres', password = '1234', database = 'python')
cursor = con.cursor()


class New:

    # @staticmethod
    # def save():
    #
    #     sql = "INSERT INTO nelson (firstname, lastname) VALUES (%s, %s)"
    #     firstname = input("Enter firstname: ")
    #     lastname = input("Enter lastname: ")
    #     val = (firstname, lastname)
    #
    #     try:
    #         cursor.execute(sql, val)
    #         con.commit()
    #
    #         print('Worked')
    #     except p.DatabaseError:
    #         raise p.DatabaseError('Something went wrong')

    @staticmethod
    def readme():
        sql = "SELECT firstname FROM nelson"

        try:
            cursor.execute(sql)
            y = cursor.fetchall()
            for z in y:
                print(z)

        except Exception:
            print('Something went wrong')


x = New()
x.readme()
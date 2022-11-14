import logging
from utils import *

import psycopg2 as pg
from datetime import datetime


class MaverickVault:

    @staticmethod
    def add_names():
        sql = """INSERT INTO payroll(first_name,last_name,company_id,position,salary,register_date)
              VALUES(%s,%s,%s,%s,%s,%s)"""
        first_name = input('First Name: ')
        last_name = input('Last Name: ')
        company_id = input('Company Id: ')
        position = input('Position: ')
        salary = int(input('Salary: '))
        register_date = date

        val = (first_name, last_name, company_id, position, salary, register_date)

        try:
            cursor.execute(sql, val)
            con.commit()
            print(f'Successfully added {first_name}')
        except pg.DataError as err:
            print('SOMETHING WENT WRONG', err)
            con.rollback()
        con.close()

    @staticmethod
    def view_names():
        try:
            cursor.execute('SELECT * FROM payroll')
            details = cursor.fetchall()
            for detail in details:
                print(detail)
        except pg.OperationalError as err:
            print('SOMETHING WENT WRONG', err)
            con.rollback()
        con.close()

    @staticmethod
    def view_name(id_db):
        try:
            cursor.execute(f'SELECT * FROM payroll WHERE id = {id_db}')
            details = cursor.fetchone()
            print(details)
        except pg.DatabaseError as err:
            print('SOMETHING WENT WRONG', err)
            con.rollback()
        con.close()

    @staticmethod
    def update():
        print('Check the row number before updating' + '\nThese are the column names you can update:'.upper())
        print('first_name')
        print('last_name')
        print('company_id')
        print('position')
        print('salary')
        print('\t')
        id_db = input('ID: ')
        column = input('Enter column: ')
        if column == 'salary':
            print('Pls make sure your enter integer values')
        update = input('Enter update: ')
        try:
            cursor.execute(f"UPDATE payroll SET {column}='{update}' WHERE id={id_db}")
            con.commit()
            print(f'Successful operation on {column}')
        except pg.IntegrityError as err:
            print('SOMETHING WENT WRONG', err)
            con.rollback()
        con.close()

    @staticmethod
    def delete(id_db):
        try:
            cursor.execute(f'DELETE FROM payroll WHERE id = {id_db}')
            con.commit()
            print('Successfully deleted')
        except pg.IntegrityError as err:
            print('SOMETHING WENT WRONG', err)
            con.rollback()
        con.close()


du = keygen.decrypt(eu).decode()
dp = keygen.decrypt(ep).decode()

prompt_1 = input('Enter username: ')
prompt_2 = input('Enter password: ')

while True:
    con = pg.connect(host='localhost', user='postgres', password='1234', database='nelson')
    cursor = con.cursor()
    now = datetime.now()
    date = now.strftime('%d-%m-%Y %H:%M:%S')

    nelson = MaverickVault()

    if dp == prompt_2 and du == prompt_1:
        print('\t')
        print(f'Welcome to {name} ❤😎💙 {du.upper()} 🎁☀(❁´◡`❁)')
        logging.info(f'Access granted to {du}')
        print('\t')
        print('1.Save Data')
        print('2.Get All Data')
        print('3.Get Data By Id')
        print('4.Update Data By Column Name')
        print('5.Delete Data By Id')
        print('\t')
        key = int(input('Enter Option: '))

        if key == 1:
            print('\t')
            nelson.add_names()
        if key == 2:
            print('\t')
            nelson.view_names()
        if key == 3:
            print('\t')
            id_no = int(input('Enter Id: '))
            print('\t')
            nelson.view_name(id_no)
        if key == 4:
            print('\t')
            nelson.update()
        if key == 5:
            print('\t')
            id_no = int(input('Enter Id: '))
            nelson.delete(id_no)

        print('\nDo you want to continue? y/n')
        answer = input().lower()
        if answer == 'y':
            pass
        else:
            print(f'GOOD BYE {owner}')
            break
    else:
        print('\t\tBad Credentials')
        break




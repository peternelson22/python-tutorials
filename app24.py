print('Welcome to employee data')

data = []

def add():
    info = {}
    info['Name'] = input('Enter name ')
    info['Position'] = input('Enter position ')
    info['Age'] = int(input('Enter age '))
    info['Salary'] = int(input('Enter salary '))
    data.append(info)

def view():
    for detail in data:
        print(detail)

def delete(i):
    del data[i]

while True:
    print('1.Add')
    print('2.View')
    print('3.Remove')

    choice = input('Enter choice ')

    if choice == '1':
        add()
    elif choice == '2':
        view()
    elif choice == '3':
        index = int(input('Enter index '))
        delete(index)
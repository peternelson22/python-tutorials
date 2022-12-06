print('Welcome to public register')

names = []

def add(name):
    names.append(name)

def view():
    for name in names:
        print(name)

def delete(name):
    names.remove(name)

while True:
    print('1 Add')
    print('2. View')
    print('3. remove')

    choice = input('Enter your choice ')

    if choice == '1':
        input_in = input('Enter your data: ')
        add(input_in)

    elif choice == '2':
        view()

    elif choice == '3':
        input_remove = input('Enter the name you want to remove: ')
        delete(input_remove)
    else:
        break
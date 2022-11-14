print('Welcome to my register')
names = []

def add(input_):
    names.append(input_)

def read():
    for name in names:
        print(name)

def delete(item):
    names.remove(item)

while True:
    print('1. Add name ')
    print('2. view ')
    print('3. remove ')
    print('4. exit ')

    user_input = input('Enter your choice ')
    if user_input == '1':
        add_name = input('Enter your name ')
        add(add_name)
    elif user_input == '2':
        read()
    elif user_input == '3':
        remove_name = input('Enter the name you want to remove ')
        delete(remove_name)
    elif user_input == '4':
        break
    else:
        print('something went wrong')






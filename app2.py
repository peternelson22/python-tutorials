def add(x, y):
    answer = x + y
    print(f'Answer = {answer}\n')


def sub(x, y):
    answer = x - y
    print(f'Answer = {answer}\n')


def multi(x, y):
    answer = x * y
    print(f'Answer = {answer}\n')


def div(x, y):
    answer = x / y
    print(f'Answer = {answer}\n')


def mod(x, y):
    answer = x % y
    print(f'Answer = {answer}\n')


while True:
    print('Welcome to mycalc')
    print('1 Addition')
    print('2 Subtraction')
    print('3 Multiplication')
    print('4 Division')
    print('5 Modulus')
    print('6 Exit')

    choice = int(input('Enter Your choice: '))

    if choice == 1:
        print('Addition')
        a = int(input('Enter number: '))
        b = int(input('Enter number: '))
        add(a, b)
    elif choice == 2:
        print('Subtraction')
        a = int(input('Enter number: '))
        b = int(input('Enter number: '))
        sub(a, b)
    elif choice == 3:
        print('Multiplication')
        a = int(input('Enter number: '))
        b = int(input('Enter number: '))
        multi(a, b)
    elif choice == 4:
        print('Division')
        a = int(input('Enter number: '))
        b = int(input('Enter number: '))
        div(a, b)
    elif choice == 5:
        print('Modulus')
        a = int(input('Enter number: '))
        b = int(input('Enter number: '))
        mod(a, b)
    elif choice == 6:
        exit()
    else:
        print("Pls enter a valid number")
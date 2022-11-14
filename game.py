going = False

while True:
    command = input('+ ').lower()
    print('')
    if command == 'go':
        if going:
            print('I am already going')
        else:
            going = True
            print('I am going')
    elif command == 'stop':
        if not going:
            print('I have already stop')
        else:
            going = False
            print('I have stop')
    elif command == 'quit':
        break


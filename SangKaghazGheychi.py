import random

a = 'sang'
b = 'kaghaz'
c = 'gheychi'
machine = [a, b, c]

while True:
    print(machine)
    machine_select = random.choice(machine)
    User_Entry = input('Enter your thought:').lower()

    if User_Entry == 'sang' or User_Entry == 'kaghaz' or User_Entry == 'gheychi':
        if User_Entry == machine_select:
            print("Mosavi")
            print('To gofti     >>>', User_Entry)
            print('Manam goftam >>>', machine_select)
        elif (User_Entry == 'sang' and machine_select == 'gheychi') or \
                (User_Entry == 'kaghaz' and machine_select == 'sang') or \
                (User_Entry == 'gheychi' and machine_select == 'kaghaz'):
            print('To Bordi ! :((')
            print('To gofti   >>>', User_Entry)
            print('Man goftam >>>', machine_select)
        else:
            print('Bakhti :))')
            print('To gofti   >>>', User_Entry)
            print('Man goftam >>>', machine_select)
    elif User_Entry == '0':
        print('Khosh Gozasht, Bye Bye ...')
        break
    else:
        print('Eshtebah vared kardi ke, sang kaghaz gheychi vared kon')
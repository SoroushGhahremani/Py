age = input('How old are you? ')
sex = input('Male or Female? ').lower()
nationality = input('Enter your country name\nAttention >> Only Iran, America, China, Russia, Other: ').lower()

if not age.isdigit():
    print('Please insert only a number for age')
else:
    age = int(age)
    if sex != 'male' and sex != 'female':
        print('Invalid Sex')
    elif nationality == 'iran':
        if sex == 'male':
            if age <= 50:
                print('Sino')
            else:
                print('Astra')
        elif sex == 'female':
            if age <= 50:
                print('Sput')
            else:
                print('Barekat')
    elif nationality == 'america':
        if sex == 'male':
            if age <= 50:
                print('Moderna')
            else:
                print('Pfizer')
        else:
            if age <= 50:
                print('Pfizer')
            else:
                print('Moderna')
    elif nationality == 'china':
        if sex == 'male':
            print('There is no Vaccine for you')
        elif sex == 'female':
            print('Sino')
    elif nationality == 'russia':
        if sex == 'male':
            print('Sput')
        elif sex == 'female':
            print('Pfizer')
    elif nationality == 'other':
        if age <= 50:
            print('Pfizer')
        else:
            print('Moderna')
    else:
        print('Invalid nationality')
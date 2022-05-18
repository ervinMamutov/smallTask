birthdays = {'John': 'June 1', 'Jason': 'Jan 1',
             'Laura': 'Apr 1'}

while True:
    print('enter name (press <Enter for the escape) : ')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(name + ': birhdays - ' + birthdays[name])
    else:
        print("I don't know when birthdays is " + name)
        print("When is person's a birthdays? ")
        bday = input()
        birthdays[name] = bday
        print ('Update birthdays information.')

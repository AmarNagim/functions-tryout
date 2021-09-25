# Amar Nagim
# F1.5.01.L3 - Tri-Tryout


import sys
import time

def naamEnLeeftijd():
    name = input('Vul hier uw naam in: ')
    age = input('Vul hier uw leeftijd in: ')
    while name == name:  
        print('')
        print(f'Hallo {name}, je leeftijd is {age}.')
        print('')
        continueOrNot = input('Druk enter als u door wilt gaan, en typ \'stop\' als u wilt stoppen: ').lower()
        if continueOrNot == 'stop':
            print('')
            print('Fijne dag nog!')
            time.sleep(1)
            sys.exit(0)
        name = input('Vul hier uw naam in: ')
        age = input('Vul hier uw leeftijd in: ')

naamEnLeeftijd()
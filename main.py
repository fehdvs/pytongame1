import random

HERO = {
    'Name':'',
    'Health':100,
    'Invetory':{
                'Sword':25,
                'Health Flask':30
    },
    'Armor':25,
    'Model':'😈',
    'Base damage':20,
    'Luck':random.randint(0,3),
    'Posishen' :[0,0],
}
ENEMY = {
    'Health':125,
    'Invetory':{
        'бейджик':35,
        'Health Flask':30,
                 },
    'Armor':10,
    'Model':'💀',
    'Base damage':25,
}
HERO['Name'] = input('веите имя героя ->')
#start igru
HELTH_HERO = HERO['Health'] + (HERO['Armor']*0.25)
DAMAGE_HERO = HERO['Invetory']['Sword'] + HERO['Base damage']

HELTH_ENAMY = ENEMY['Health'] + (ENEMY['Armor']*0.25)
DAMAGE_ENAMY = ENEMY['Invetory']['бейджик']+ENEMY['Base damage']

if random.randint(1,6) in [6,1,1]:
    ENEMY['Health'] -= DAMAGE_HERO
    ENEMY['Armor'] = ENEMY['Armor'] - ENEMY['Armor']*0.25
else:
    HERO['Health'] -= DAMAGE_ENAMY
    HERO['Armor'] = HERO['Armor'] - HERO['Armor'] * 0.25

model_health = "▌"
HELTH_BAR_HERO = HERO['Health']//10
HELTH_BAR_ENEMY = ENEMY['Health']//10
BAR_HERO = f'{HERO["Name"]}\n{HELTH_BAR_HERO*model_health}\n'
BAR_ENEMY = f'ENEMY\n{HELTH_BAR_ENEMY*model_health}\n'
print(BAR_ENEMY,BAR_HERO)

MAP = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]
counter_hero =0
counter_enemy = 0
while counter_hero !=1 and counter_enemy != 3:
    for y in range(5):
        for x in range(5):
            if random.randint(1,50) in [10,25,50,20,30,35]:
                if random.randint(0,1) == 1:
                    if counter_hero < 1:
                        MAP[y][x] = HERO['Model']
                        HERO['Posishen'] = [y,x]
                        counter_hero+=1
                else:
                    if counter_enemy < 4:
                        MAP[y][x] = ENEMY['Model']
                        counter_enemy+=1
while True :
    for i in MAP:
        print('\n')
        for j in i:
            print(''.join(str(j)), end='\t')
    print(HERO['Posishen'])
    move = input('\nвыберете действие!:\n1)сходить налево\n2)сходить направо\n3)сходить вниз\n4)сходить вверх\n--> ')
    if move == '1':
        temp = HERO['Posishen']
        if temp[1] >0:
            MAP[temp[0]][temp[1]] = 0
            MAP[temp[0]][temp[1] - 1] = HERO['Model']
            HERO['Posishen'] = [temp[0], temp[1] - 1]

    elif move == '2':
        temp = HERO['Posishen']
        if temp[1] < 4:
            MAP[temp[0]][temp[1]] = 0
            MAP[temp[0]][temp[1]+1] = HERO['Model']
            HERO['Posishen'] = [temp[0], temp[1] + 1]

    elif move == '3':
        temp = HERO['Posishen']
        if temp[0] <4:
            MAP[temp[0]][temp[1]] = 0
            MAP[temp[0] + 1][temp[1]] = HERO['Model']
            HERO['Posishen'] = [temp[0] + 1, temp[1]]

    elif move == '4':
        temp = HERO['Posishen']
        if temp[0] > 0:
            MAP[temp[0]][temp[1]] = 0
            MAP[temp[0] - 1][temp[1]] = HERO['Model']
            HERO['Posishen'] = [temp[0] - 1, temp[1]]


        print(HERO['Posishen'])
        govno = ENEMY['Posishen']
        vataka = input('')
        if HERO['Posishen'] == govno:







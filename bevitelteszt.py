import random

num = 0
f = open('log.txt', 'w')
result1 = ''
result2 = ''
result3 = ''
rossz = 0

def valaszt():
    global num
    global f
    global rossz
    while True:
        if num == 1:
            try:
                result1 = input('Írj be egy számot: ')
            except:
                pass
            if result1 == 'exit':
                exit()
            if result1.isnumeric() == False:
                f.write('szám: ' + result1 + '\trossz\n')
                print('Ez nem jó')
                rossz += 1
                if rossz >= 3:
                    print('Hülye vagy?')
                    exit()
            else:
                f.write('szám: ' + str(result1) + '\tjó\n')
                print('jó')
                result1 = ''
                num = 0
                rossz = 0
                break
            
        if num == 2:
            try:
                result2 = input('Írj be egy szöveget: ')
            except:
                pass
            if result2 == 'exit':
                exit()
            elif len(result2) == 0:
                f.write('szöveg: ' + result2 + '\trossz\n')
                print('Ez üres')
                rossz += 1
                if rossz >= 3:
                    print('Hülye vagy?')
                    exit()
            elif len(result2) == 1 or result2.isnumeric():
                f.write('szöveg: ' + result2 + '\trossz\n')
                print('Ez nem jó')
                rossz += 1
                if rossz >= 3:
                    print('Hülye vagy?')
                    exit()
            else:
                f.write('szöveg: ' + str(result2) + '\tjó\n')
                print('jó')
                result2 = ''
                num = 0
                rossz = 0
                break
            
        if num == 3:
            try:
                result3 = input('Írj be egy betűt: ')
            except:
                pass
            if result3 == 'exit':
                exit()
            elif len(result3) == 0:
                f.write('betű: ' + result3 + '\trossz\n')
                print('Ez üres')
                rossz += 1
                if rossz >= 3:
                    print('Hülye vagy?')
                    exit()
            elif result3.isnumeric() or len(result3) > 1:
                f.write('betű: ' + result3 + '\trossz\n')
                print('Ez nem jó')
                rossz += 1
                if rossz >= 3:
                    print('Hülye vagy?')
                    exit()
            else:
                f.write('betű: ' + str(result3) + '\tjó\n')
                print('jó')
                result3 = ''
                num = 0
                rossz = 0
                break
            
while True:
    num = random.randint(1,3)
    valaszt()

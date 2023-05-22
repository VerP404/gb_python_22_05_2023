flag = True
while flag:    
    juravliki = int(input('введи число:'))
    if juravliki % 2 == 0:
        katya = int(juravliki/2)
        petya = serioja = int(katya/2)
        print(f'{juravliki} -> {petya} {katya} {serioja}')
        flag = False
    else:
        print('Число не удовлетворяет условиям')

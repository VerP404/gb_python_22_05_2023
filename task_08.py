def check(x, y, k):
    while x > 0:
        a = x * y
        x = x - 1
        if a == k:
            x = 0
            return True
    return False

print('Введите размер шоколадки')
n = int(input('Сторона 1: '))
m = int(input('Сторона 2: '))
k = int(input('Количество долек, которые нужно отломить: '))

if n*m > k-1:
    if check(n,m,k) or check(m,n,k):
        print(f'{k} -> yes')
    else:
        print(f'{k} -> no')   
else:
    print(f'Число долек {k}, которое нужно отломить, больше количества долек в шоколадке {n*m}')

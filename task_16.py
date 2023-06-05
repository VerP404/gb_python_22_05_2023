N = int(input())
print('\t', end='')
A = list(map(int, input().split()))
while len(A) != N:
    print("Количество элементов в массиве не соответствует заданному размеру.")
    A = list(map(int, input().split()))
X = int(input('\t'))
count = 0
for i in A:
    if i == X:
        count += 1
print(f'\t-> {count}')

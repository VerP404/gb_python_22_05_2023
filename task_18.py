N = int(input())
print('\t', end='')
A = list(map(int, input().split()))
while len(A) != N:
    print("Количество элементов в массиве не соответствует заданному размеру.")
    N = int(input())
    print('\t', end='')
    A = list(map(int, input().split()))
X = int(input('\t'))

raznitsa = []
for i in A:
    raznitsa.append(abs(X-i))

min = raznitsa[0]

for y in range(len(raznitsa)):
    if raznitsa[y] < min:
        min=raznitsa[y]
        index = y
print(raznitsa)
print(f'\t-> {A[index]}')

def summa(a, b, sum_a=0, sum_b=0, sum = 0):
    if sum_a < a:
        sum_a = sum_a + 1
        sum = sum + 1
    elif sum_b < b:
        sum_b = sum_b + 1
        sum = sum + 1
    else:
        return sum
    return summa(a, b, sum_a, sum_b, sum)

num_1 = int(input("Число 1 = "))
num_2 = int(input("Число 2 = "))
print(summa(num_1,num_2))

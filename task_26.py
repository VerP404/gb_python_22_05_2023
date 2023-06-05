def exponentiation(a, b, num=1):
    num = num * a
    b = b - 1
    if b == 0:
        return num
    return exponentiation(a, b, num)


num_a = int(input("A = "))
num_b = int(input("B = "))
print(f"A = {num_a}; B = {num_b} -> {exponentiation(num_a, num_b)}")

flag = True
while flag:
    input_text = input('Введите число: ')
    if input_text.isdigit():
        
        count = 0
        for i in range(len(input_text)):
            count = count + int(input_text[i])
        print(f'Сумма цифр числа {input_text} -> {count}')
        flag = False
    else:
        print('введено не число')
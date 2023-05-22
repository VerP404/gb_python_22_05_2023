flag = True
while flag:
    ticket = input('Введите номер билета: ')
    if len(ticket) == 6 and ticket.isdigit():
        flag = False
    else:
        print('Введен не номер билета')
count1 = count2 = 0    
for i in range(3):
    count1 = count1 + int(ticket[i])
for i in range(3,6):
    count2 = count2 + int(ticket[i])    
if count1 == count2:
    print(f'{ticket} -> yes')
else:
    print(f'{ticket} -> no')

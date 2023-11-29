def create_phone_number(n):
    err ='wrong data format'
    phone_number = '('


    for i in range (3):
        phone_number = phone_number + str(n[i])
    phone_number= phone_number + ') '
    for i in range (3,6):
        phone_number = phone_number + str(n[i])
    phone_number = phone_number + '-'
    for i in range (6,10):
        phone_number = phone_number + str(n[i])



        # phone_number = phone_number + str(i)

    return phone_number



create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
# n=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(len(n))
# if i >= 0 and i <= 9 and type(i) == int() :
# if len(n) == 10:
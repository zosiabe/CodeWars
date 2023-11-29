def alphabet_position(text):
    lower_text=text.lower()
    position=str()


    for i in lower_text:
        number = ord(i)
        if number > 96 and number < 123:
            if position:
                position = position + ' ' + str(number-96)
            else:
                position = str(number - 96)

    return position
a = alphabet_position("The sunset sets at twelve o' clock.")
# a = alphabet_position('abc')

print(a)

# 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11
# A-65
# Z-90
# a-97
# z-122


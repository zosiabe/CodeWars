# Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.
#
# For example:
#
# nextSmaller(21) == 12
# nextSmaller(531) == 513
# nextSmaller(2071) == 2017
# Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.
#
# nextSmaller(9) == -1
# nextSmaller(111) == -1
# nextSmaller(135) == -1
# nextSmaller(1027) == -1 // 0721 is out since we don't write numbers with leading zeros
# some tests will include very large numbers.
# test data only employs positive integers.


def next_smaller(n):
    text=str(n)
    tab1=[]
    tab2=[]
    is_bigger= False
    size=len(str(n))
    change_possition=1
    maxtab2=0
    possition_tab2 = 0
    result = -1
    sresult = ''
    change_value = 1
    for i in range (0,size):
        number=int(text[i])
        tab1.append (number)
    if size == 1:
        return -1
    else:
        for i in range(size - 1, 0, -1):

            if tab1[i] < tab1[i - 1]:

                is_bigger = True
                change_possition = i - 1
                change_value = tab1[change_possition]
                tab2.append(tab1[i])
                break
            else:
                tab2.append(tab1[i])
        tab2.sort(reverse=True)
        for i in range(0, len(tab2)):

            if tab2[i] < tab1[change_possition]:
                maxtab2 = tab2[i]
                possition_tab2 = i
                break

        tab1[change_possition] = maxtab2
        tab2[possition_tab2] = change_value

        for i in range(0, change_possition + 1):
            sresult = sresult + str(tab1[i])
        for i in tab2:
            sresult = sresult + str(i)
        result = int(sresult)
        if tab1[0] == 0 or is_bigger==False:
            result = -1


        return result

print(next_smaller(1))


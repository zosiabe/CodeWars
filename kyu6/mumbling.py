def accum(s):
    result=''
    for i in range(1, len(s) + 1):
        k = 0
        for j in range(i):
            if k == 0:
                result = result + s[i - 1].upper()
            else:
                result = result + s[i - 1].lower()
            k += 1
        result=result+'-'
    # slice(result[len(result)-1])
    return result[0:len(result)-1]




print(accum('ngvhjg'))



    # print (i)
    # print (text[i-1])
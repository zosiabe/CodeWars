def dig_pow(n, p):

# n=3
# p=114
    str_p=str(p)
    digits=len(str_p)
    l1=[]
    sum=0
    result=-1
    print (result)
    m=1
    print(p)
    print(str_p)
    for i in str_p:
        l1.append(int(i))

    for i in l1:
        sum=i**n+sum
        n+=1
    temp=p
    # m=0
    # m+=1
    print(l1)

    while temp <= sum:

        temp = p * m
        if temp == sum:

            result = m
            # return m-1
            break
            print('jestem')
        else:

            # temp = p * m

            m=m+1
            result=-1
            # multiplier += 1
    # print (result)
    print('result=', result)
    return result



print (dig_pow(1,92))
# p=695
# print(len(695))
# Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.
# https://www.codewars.com/kata/5629db57620258aa9d000014

import operator
def mix(s1,s2):
    leters1=""
    leters2=""
    common={}
    s1count=[]
    s2count=[]
    answear=''
    com=""
    anstab=[]
    anstab2=[]
    result=''
    listalist=[]

    for i in s1:
        if ord(i) >=97 and ord(i) <= 122:
            leters1 = leters1 + i
    leters1= set(leters1)

    for i in s2:
        if ord(i) >= 97 and ord(i) <= 122:
            leters2 = leters2 + i

    leters2= set(leters2)

    common = leters1 | leters2
    for i in common:

        s1count.append(str(s1.count(i)))

        s2count.append(str(s2.count(i)))
        com=com+i

    for i in range (0,len(common)):
        print('i:',com[i])
        if s1count[i] > s2count[i] and int(s1count[i]) > 1 :
            answear = answear + "1:" + int(s1count[i]) * com[i]+'/'
            print(answear)
            anstab.append(answear[0:len(answear) - 1])
            anstab.append(int(s1count[i])*-1)
            anstab.append(1)
            anstab.append(ord(answear[2]))
            listalist.append(anstab)

        elif s1count[i] < s2count[i]  and int(s2count[i]) > 1:
            answear = answear + "2:" + int(s2count[i]) * com[i]+'/'
            print(answear)
            anstab.append(answear[0:len(answear) - 1])
            anstab.append(int(s2count[i]) *-1)
            anstab.append(2)
            anstab.append(ord(answear[2]))
            listalist.append(anstab)
        elif int(s1count[i]) > 1:
            answear = answear + "=:" + int(s1count[i]) * com[i]+"/"
            print(answear)
            anstab.append(answear[0:len(answear)-1])
            anstab.append(int(s1count[i]) * -1)
            anstab.append(3)
            anstab.append(ord(answear[2]))
            listalist.append(anstab)
        answear=""
        anstab=[]

        listalist = sorted (listalist,key=operator.itemgetter(1,2,3))

    for i in listalist:
        result = result + i[0] +'/'
    return result[0:len(result)-1]


s1="Sadus:cpms>orqn3zecwGvnznSgacs"
s2="MynwdKizfd$lvse+gnbaGydxyXzayp"
print(mix(s1,s2))


# a-97
# z-122


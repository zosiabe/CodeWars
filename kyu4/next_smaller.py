def next_smaller(n):
    text=str(n)
    tab1=[]
    tab2=[]
    z=0
    s=''
    for i in range (0,len(str(n))):
        number=int(text[i])
        if number != 0:
            tab1.append (number)
            tab2.append (number)
        else:
            z+=1
    tab2.sort()
    s=str(tab2[0])
    for i in range(z):
        s = s + '0'
    for i in range (1,len(tab2)):
        s=s+str(tab2[i])

    smallest=int(s)
    if smallest == n:
        return -1
    else:
       return smallest





print (next_smaller (90706778))
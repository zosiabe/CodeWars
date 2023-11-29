def score(dice):

    sum=0
    numbers= [1,2,3,4,5,6]
    count = [0,0,0,0,0,0]
    for i in dice:
        count[i-1]=count[i-1]+1

    for i in range (0,6):
        if i != 0 and i != 4:
            if count [i] >=3:
                sum = sum +  (i+1) * 100
        elif i == 0:
            if count [i] >= 3:
                sum = sum + 1000 + (count [i] - 3) * 100
            else:
                sum = sum + count [i] * 100
        elif i == 4:
            if count[i] >= 3:
                sum = sum + 500 + (count[i] - 3) * 50
            else:
                sum = sum + count [i] * 50




    return sum

print (score([6,6,6,6,6]))


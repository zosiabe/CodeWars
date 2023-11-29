def solution(number):
    multiples=[]
    multiples_sum=0
    if number <= 0:
        return 0
    else:
        for i in range(1,number):
            if i%3==0 or i%5==0:
                multiples.append(i)
    for i in multiples:
        multiples_sum=multiples_sum+i
    return multiples_sum

print(solution(10))

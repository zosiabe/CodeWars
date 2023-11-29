def sum_two_smallest_numbers(numbers):
    sum=min(numbers)
    numbers.remove(sum)
    sum=sum+min(numbers)
    return sum

tab = [1,2,3,4]
print(sum_two_smallest_numbers(tab))

print(tab)
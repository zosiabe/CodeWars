# Given a positive integral number n, return a strictly increasing sequence (list/array/string depending on the language) of numbers, so that the sum of the squares is equal to n².
#
# If there are multiple solutions (and there will be), return as far as possible the result with the largest possible values:
#
# Examples
# decompose(11) must return [1,2,4,10]. Note that there are actually two ways to decompose 11², 11² = 121 = 1 + 4 + 16 + 100 = 1² + 2² + 4² + 10² but don't return [2,6,9], since 9 is smaller than 10.
#
# For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49] since [1, 1, 4, 9, 49] doesn't form a strictly increasing sequence.

def decompose(n, a=None):
    if a == None: a = n*n
    if a == 0: return []
    for m in range(min(n-1, int(a ** .5)), 0, -1):
        sub = decompose(m, a - m*m)
        if sub != None: return sub + [m]

    # for i in range (1,sqrt(n)-1):
print (decompose(25))
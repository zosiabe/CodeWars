# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.
#
# Example:
#
# Given an input string of:
#
# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:
#
# apples, pears
# grapes
# bananas

import re


def strip_comments(string, markers):
    def solution(string, markers):
        parts = string.split('\n')
        for s in markers:
            parts = [v.split(s)[0].rstrip() for v in parts]
        return '\n'.join(parts)

    return k


# result = strip_comments("apples, pears # and bananas\ngrapes\nbananas ! apples", ["#", "!"])
# print(result)
String = '- pears avocados\ncherries ! strawberries\ncherries bananas . watermelons @\nwatermelons cherries # lemons strawberries\n. watermelons bananas'
Markers= ['-', '.', '!', "'", '=', '?']
print(strip_comments(String,Markers))
# String: '\t^ # lemons apples =\noranges apples ?\nwatermelons bananas ! , .\nlemons strawberries avocados bananas @ watermelons\n@ # @ cherries watermelons'
# Markers: []


# s="apples, pears # and bananas\ngrapes\nbananas !apples"

# s=s.replace('!','#')

# for i in range(s.count('#')):
# l = s.split(r'[# |!|]')
# print(l)
# k=''
# for i in l:
#     if l.index(i) == 0:
#         k = k+i
#     elif '\n' in i :
#         k=k+i[i.index('\n'):len(i)]
# # s = s[0:s.index('#')-1] + s[s.index('\n'):len(s)]
# print(k)
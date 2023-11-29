def solution(s):

    no_camel=""

    for i in s:
        if ord (i) > 64 and ord(i) < 90:
            no_camel = no_camel + " " + i
        else:
            no_camel = no_camel + i
    return no_camel


print (solution ('breakCamelCase'))
# a=97
# z=122
# A=65
# Z=90
# " "=32

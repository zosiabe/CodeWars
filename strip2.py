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
def strip_comments(string, markers):
    l = []
    k = ''
    res = ''
    if len(string) == 0 or string == ' ':
        return ''
    else:
        if string[0] == '\t' and string[1] == '\n' or string[0] == ' ' and string[1] == '\n':
            string = string[1:len(string) - 1]

    if len(markers) == 1:
        l = string.split(markers[0])
    elif len(markers) >= 1:
        for i in range(1, len(markers)):
            string = string.replace(markers[i], markers[0])
        l = string.split(markers[0])
    elif len(markers) == 0:
        l.append(string)
    string = string.strip()

    for i in l:
        if l.index(i) == 0:
            i.rstrip()
            k = k + i
        elif '\n' in i:
            i.strip()
            k = k + i[i.index('\n'):len(i)]
    l = []
    l = k.split('\n')
    for i in l:
        if len(i) > 1:
            if i[len(i) - 1] == ' ':
                while i[len(i) - 1] == ' ':
                    i = i[0:len(i) - 1]
                    if len(i) - 1 < 1:
                        break
            if i[0] == ' ':
                if i.count(' ') == len(i):
                    i = ''
        else:
            if i == ' ':
                i = ''

        res = res + i + '\n'

    if res[len(res) - 1] == '\n' and string.strip()[len(string) - 1] != '\n':
        res = res[0:len(res) - 1]

    return res


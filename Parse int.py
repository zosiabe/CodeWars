# In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.
#
# Examples:
#
# "one" => 1
# "twenty" => 20
# "two hundred forty-six" => 246
# "seven hundred eighty-three thousand nine hundred and nineteen" => 783919
# Additional Notes:
#
# The minimum number is "zero" (inclusively)
# The maximum number, which must be supported is 1 million (inclusively)
# The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
# All tested numbers are valid, you don't need to validate them
# PARSINGSTRINGSALGORITHMS

def parse_int(string):
    unity = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
            'nineteen']
    ty = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    big = ['hundred', 100, 'thousand', 1000, 'million', 1000000]

    number = []
    string = string.lower()
    number = string.split()
    intnumber = []
    temp = []
    if "million" in string:
        return 1000000
    if len(number) == 1:
        if string in unity:
            return unity.index(string)
        elif string in teen:
            return teen.index(string) + 10
        elif string in ty:
            return (ty.index(string) + 2) * 10
        elif '-' in string:
            temp = string.split('-')
            return (ty.index(temp[0]) + 2) * 10 + unity.index(temp[1])
        elif string in big:
            return big[big.index(string) + 1]

    else:
        for i in number:
            if '-' in i:
                temp = i.split('-')
                intnumber.append((ty.index(temp[0]) + 2) * 10 + unity.index(temp[1]))
                temp = []
            elif i in big:
                intnumber.append(big[big.index(i) + 1])
            elif i in unity:
                intnumber.append(unity.index(i))
            elif i in teen:
                intnumber.append(teen.index(i) + 10)
            elif i in ty:
                intnumber.append((ty.index(i) + 2) * 10)

        for i in range(2):
            if 100 in intnumber and i == 0:
                for j in range(intnumber.count(100)):
                    hu = intnumber.index(100)
                    if hu - 1 != -1 and intnumber[hu - 1] < 100:
                        intnumber[hu - 1] = 100 * intnumber[hu - 1]
                        intnumber.remove(intnumber[hu])
                        hu = hu - 1
                        if len(intnumber) == 1:
                            return (intnumber[0])
                    if hu + 1 > len(intnumber) - 1:
                        intnumber[hu] = intnumber[hu]
                    elif hu + 1 <= len(intnumber) and intnumber[hu + 1] < 100:
                        if (hu + 2 <= len(intnumber) and [hu + 2] != 1000) or (hu + 2 > len(intnumber)):
                            intnumber[hu + 1] = intnumber[hu] + intnumber[hu + 1]
                            intnumber.remove(intnumber[hu])
                            if len(intnumber) == 1:
                                return (intnumber[0])

            if 1000 in intnumber and i == 1:
                th = intnumber.index(1000)
                if th - 1 != -1:
                    intnumber[th - 1] = 1000 * intnumber[th - 1]
                    intnumber.remove(intnumber[th])
                    th = th - 1
                    if len(intnumber) == 1:
                        return (intnumber[0])
                if th + 1 <= len(intnumber):
                    intnumber[th + 1] = intnumber[th] + intnumber[th + 1]
                    intnumber.remove(intnumber[th])
                    if len(intnumber) == 1:
                        return (intnumber[0])

print (parse_int("five hundred thousand three hundred"))
# print (parse_int("thirty-eight thousand two hundred thirty-eight"))
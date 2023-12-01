# Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be tested for each function.
#
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
#
# Input range : 1 <= n < 4000
#
# In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

class RomanNumerals:
    def __init__(self):
        self.chars = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        self.numbers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

    def to_roman(self,val:int)->str:
        self.val=val
        temp=self.val
        done=0
        s=''
        # if temp == 0:
        #     return to_roman (temp)
        while temp > 0:
            for i in range (len(self.numbers)):
                if temp >= self.numbers[i]:
                    done = temp // self.numbers[i]
                    s = s + str (done * self.chars [i])
                    temp = temp - done * self.numbers[i]
                    done = 0
                    for j in range (len(self.numbers)):
                        if temp == self.numbers [j]:
                            done = self.numbers [j]
                            s = s + self.chars [j]
                            temp = temp - done * self.numbers[j]
                            break
        return (s)


    def from_roman(self,roman_num):
        self.roman_num = roman_num
        s=''
        res = 0
        bo = False
        k=0
        for i in range (len(self.chars)):
            if roman_num == self.chars[i]:
                return self.numbers[i]
        # for i in range(len(self.roman_num)):
        while k <= len(self.roman_num):
            if k != len(self.roman_num)-1:
                s = roman_num[k] + roman_num[k+1]
            else:
                s = roman_num[k]
            bo = False
            for j in range (len(self.chars)):
                if s == self.chars[j]:
                    res = res + self.numbers[j]
                    bo = True
                    k +=1
                    if k == len(self.roman_num)-1:
                        return res
                    break
            if bo == False:
                for j in range(len(self.chars)):
                    if roman_num[k] == self.chars[j]:
                        res = res + self.numbers[j]
                        print ('i',self.numbers[k])
                        break
            k+=1

        return res


    #     return 0

roman_numerals = RomanNumerals()
# print(roman_numerals.to_roman(1666))
print(roman_numerals.from_roman('MMCDXXXVII'))
print(roman_numerals.from_roman('IV'))

# print(to_roman(1666))
# print(from_roman(to_roman(1666)))

# class RomanNumerals:
#     @staticmethod
#     def to_roman(val : int) -> str:
#         return ''
# #
#     @staticmethod
#     def from_roman(roman_num : str) -> int:
#         return 0

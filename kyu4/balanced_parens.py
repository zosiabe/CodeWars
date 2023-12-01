# Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses
#
# Examples
# balancedParens 0 -> [""]
# balancedParens 1 -> ["()"]
# balancedParens 2 -> ["()()","(())"]
# balancedParens 3 -> ["()()()","(())()","()(())","(()())","((()))"]
def balanced_parens(n):
    ret = []

    def generate(parans, openings, closings):
        if openings == 0 and closings == 0:
            ret.append(parans)
            return
        elif openings == 0:
            ret.append(parans + ")" * closings)
            return
        if openings < closings:
            generate(parans + ")", openings, closings - 1)
        generate(parans + "(", openings - 1, closings)

    generate("", n, n)
    return ret

print(balanced_parens(3))
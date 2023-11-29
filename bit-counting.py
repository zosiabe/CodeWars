def count_bits(n):
    binary_rep=bin(n)
    string_rep= str(binary_rep)
    one_bits= binary_rep.count("1")
    return (one_bits)

number=int(input())

print(count_bits(number))
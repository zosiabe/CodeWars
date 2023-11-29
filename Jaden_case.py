def to_jaden_case(string):

    jaden = " "
    j=32
    for i in string:
        if j != 32:
            jaden = jaden + i
        else:
            jaden = jaden + i.upper()

        j=ord(i)




    return jaden


text= to_jaden_case("can mirrors be real if our eyes aren't real")
te="uhuih"
print(te[0])
print(text)

# " "=32
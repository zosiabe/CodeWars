def narcissistic( value ):
    text_value=str(value)
    power=len(text_value)
    n_value=0
    for i in text_value:
        n_value = n_value + int(i) ** power
    return n_value

print (narcissistic(1652))

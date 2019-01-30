
def is_palindrome(number):
    number_string = str(number)
    if (number_string == number_string[::-1]):
        return True
    else:
        return False
def oposite_number(number):
    number_string = str(number)
    return int(number_string[::-1])

#print(oposite_number(123455))

def is_Lychrel(number):
    is_Lychrel = True
    for iterations in range(1,51):
        number = number + oposite_number(number)
        if (is_palindrome(number)):
            is_Lychrel = False
            return is_Lychrel
    return is_Lychrel

#print(is_Lychrel(349))



def number_Lychrel_below(number):
    Lychrel = []
    for i in range(0,number):
        if is_Lychrel(i):
            Lychrel.append(i)

    return len(Lychrel)

print number_Lychrel_below(10000)





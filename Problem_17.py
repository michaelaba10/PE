import inflect
p = inflect.engine()
str =""
for i in range(1,1001):
    number = p.number_to_words(i)
    number = number.replace('-', "")
    number = number.replace(' ', '')
    str = str+number
print(len(str))
from tictoc import tic, toc
def next_in_chain(number):
    number_list = [int(i) for i in str(number)]
    number_list_suqarted = [i**2 for i in number_list]
    return sum(number_list_suqarted)

def chain_arrives_eighty_nine(number):
    while (number != 1) and (number != 89):
        number = next_in_chain(number)
    if (number == 1):
        return False
    else:
        return True
chain_arrives_eighty_nine(89)

good_numbers = []
tic()
for i in range(1,10000000):
    if chain_arrives_eighty_nine(i):
        good_numbers.append(i)
print(len(good_numbers))
toc()
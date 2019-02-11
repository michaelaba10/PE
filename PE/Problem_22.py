'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing 
over five-thousand first names, begin by sorting it into alphabetical order.
 Then working out the alphabetical value for each name, multiply this value by its 
 alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
 So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

from tictoc import tic,toc

with open('names.txt', 'r') as myfile:
  names = myfile.read()
 
    
names = names.replace('"', "")
names = names.split(',')
names.sort()

characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]



def numerical_value_string(string):
    value_string = 0
    for letter in string:
        index = characters.index(letter)
        value_string = value_string + numbers[index]
    return value_string
 
    
tic()
i = 1
total_value = 0
for name in names:
    total_value = total_value + i* numerical_value_string(name)
    i = i+1


print(total_value)
toc()    

myfile.close()

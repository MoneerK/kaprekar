# kaprekar.py
# order descending 
# reverse
# subtract
# repeat until 6174

def get_input():
    return str(input("Enter your value: "))
def reorder(num, rev = False):
    return sorted(num, reverse=rev)
def list_to_string(list):
    return ''.join(list)
def string_to_int(num):
    return int(num)
def get_diff(num1, num2):
    return num1 - num2

# num = '8512'
num = get_input()
desNum = reorder(num, True)
ascNum = reorder(num, False)
print (desNum, ascNum)
desNum =list_to_string(desNum)
ascNum =list_to_string(ascNum)
desNumInt = string_to_int(desNum)
ascNumInt = string_to_int(ascNum)
print(desNumInt,ascNumInt)
diffNum = get_diff(desNumInt, ascNumInt)
print('diffNum = ', diffNum)

# desNum = sorted(num, reverse=True)
# ascNum = sorted(num, reverse=False)
# print (desNum, ascNum)
# desNum =''.join(desNum)
# ascNum =''.join(ascNum)
# desNumInt = int(desNum)
# ascNumInt = int(ascNum)
# print(desNumInt,ascNumInt)

# diffNum = desNumInt-ascNumInt
# print('diffNum = ', diffNum)

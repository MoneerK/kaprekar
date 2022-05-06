# kaprekar.py
# order descending 
# reverse
# subtract
# repeat until 6174

def get_input():
    return str(input('Enter a number of exactly 4 digits, with at least 2 different digits: '))
def reorder(num, rev = False):
    return sorted(num, reverse=rev)
def list_to_string(list):
    return ''.join(list)
def string_to_int(num):
    return int(num)
def get_diff(num1, num2):
    return num1 - num2

num = get_input()
diff_num = 0
iterations = 0

while diff_num != 6174:
    if iterations >= 10:
        break
    des_num = reorder(num, True)
    asc_num = reorder(num, False)
    # print ('des_num:',des_num, 'asc_num',asc_num)
    des_num_str =list_to_string(des_num)
    asc_num_str =list_to_string(asc_num)
    des_num_int = string_to_int(des_num_str)
    asc_num_int = string_to_int(asc_num_str)
    # print(des_num_int,asc_num_int)
    diff_num = get_diff(des_num_int, asc_num_int)
    # print('diff_num = ', diff_num)
    if diff_num != 6174:
        num = str(diff_num)
        if len(num)<4:
            num = ''.join(['0',num])
        iterations += 1
final_num = num
print('final_num:', final_num, ', number of iterations: ', iterations)
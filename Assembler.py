from helper import helper
from helper import *
from encoding import *
# address = 0
import sys
def filter(inp):
    lst = inp.strip().split(" ")
    ls1 = []
    ls2 = []
    for i in lst:
        if "," in i:
            ls1 = i.split(",")
        else:
            ls2.append(i)

        lst = []
        lst = ls2 + ls1
    output = ""
    if ":" in lst[0]:
        lst.pop(0)
    return lst
# Using readlines()

input_file = sys.argv[1]
output_file = sys.argv[2]


res= open(output_file, 'w')
test = open(input_file ,'r')
lines = test.readlines()
Program_counter = -4
count = 0
label_dict={}
halt = ['beq', 'zero','zero','0']
linez = []
for i in lines:
    linez.append(filter(i))
print(linez)
if halt in linez and linez.index(halt) == len(lines)-1:
    for inp in lines:
        lst = inp.strip().split(" ")  # Split the input string by spaces and store it in a list
        ls1 = []
        ls2 = []
        for i in lst:
            if "," in i:
                ls1 = i.split(",")
            else:
                ls2.append(i)

            lst = []
            lst = ls2+ls1

        result = ""
        if ":" in lst[0]:
            label = lst[0]
            lst.pop(0)
            if  helper(lst, result):
                label_dict.update({label[:-1]: Program_counter+4})

        Program_counter+= 4
        count += 1

    else:
        c = 0
        Program_counter = 0
        for inp in lines:
            lst = filter(inp)
            output = ""
            try:
                if registers.type_of_ins(lst[0])[0] in ["B","J"] and lst[len(lst)-1] in label_dict:
                    lst[len(lst)-1] = label_dict[lst[len(lst)-1]] - Program_counter
            except TypeError:
                res.write('Invalid instruction or typo in ' + lst[0] + '\n')
                break
            try:
                final = helper(lst,output)

                res.write(final)
                res.write("\n")
            except TypeError:
                print('INVALID REGISTERS OR TYPO'+ ' at line'+ ' '+str(c+1)+'\n')
                print(lst[len(lst)-1].isnumeric())
                break
            c += 1
            Program_counter+=4
elif halt in linez and linez.index(halt)+1 != len(lines)-1:
    print(linez.index(halt), len(lines)-1)
    print('HALT AT WRONG PLACE!')
elif halt not in linez:
    print('HALT MISSING')









# start: lui t0,100
#     addi t1,t0,-50
#     bge t1,zero,end
#     bltu t2,t1,start
#     addi t2,t1,20
#     add t3,t1,t2
#     jal gp,-512
#     jalr t4,t0,0
# end: beq zero,zero,0


# 00000000000000000000001010110111
# 11111100111000101000001100010011
# 11111110000000110101010011100011
# 00000000011000111110011001100011
# 00000001010000110000001110010011
# 00000000011100110000111000110011
# 11100000000111111111000111101111
# 00000000000000101000111011100111
# 00000000000000000000000001100011


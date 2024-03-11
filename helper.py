import sys
from encoding import *  
def helper(lst,result):
    opcode = registers.func(lst[0])[0]
    result = result + opcode

    type_of_instruction = registers.type_of_ins(lst[0])[0]

    try:

        if type_of_instruction == "R":
            rd = registers.regis_binary(lst[1])
            func3 = registers.func(lst[0])[1]
            rs1 = registers.regis_binary(lst[2])
            rs2 = registers.regis_binary(lst[3])
            func7 = registers.func(lst[0])[2]
            result = func7 + rs2 + rs1 + func3 + rd + result

        elif type_of_instruction == "I":
            if registers.type_of_ins(lst[0])[1] == "lw" :
                rd = registers.regis_binary(lst[1])
                func3 = registers.func(lst[0])[1]
                rs1 = registers.regis_binary(lst[2][-3:-1])
                rs2 = registers.regis_binary(lst[1])
                imm = registers.sext_binary(lst[2][0:-4])
                result = imm + rs1 + func3 + rd + result

            else:
                rd = registers.regis_binary(lst[1])
                func3 = registers.func(lst[0])[1]
                rs1 = registers.regis_binary(lst[2])
                imm = registers.sext_binary(lst[3])
                result = imm + rs1 + func3 + rd + result

                print(lst[2][-3:-1])
                print(lst[2][0:2])

        elif type_of_instruction == "S":
             imm1 = registers.sext_binary(lst[2][0:-4])[7:12]
             func3 = registers.func(lst[0])[1]
             rs1 = registers.regis_binary(lst[2][-3:-1])
             rs2 = registers.regis_binary(lst[1])
             imm2 = registers.sext_binary(lst[2][0:-4])[0:7]
             result = imm2+rs2+rs1+func3+imm1+result
             print(lst[2][0:-4])
             print(imm1)
             print(imm2)

        elif type_of_instruction == "B":

            imm = registers.sext_binary_B(lst[3])
            imm1 = imm[8:12] + imm[1]
            func3 = registers.func(lst[0])[1]
            rs1 = registers.regis_binary(lst[1])
            rs2 = registers.regis_binary(lst[2])
            imm2 = imm[0] + imm[2:8]
            result = imm2 + rs2 + rs1 +func3 + imm1 + result


        elif type_of_instruction == "U":
            rd = registers.regis_binary(lst[1])
            imm = registers.sext_binary_U(lst[2])[0:20]
            result = imm + rd + result

        elif type_of_instruction == "J":
            rd = registers.regis_binary(lst[1])
            imm1 = registers.sext_binary_J(lst[2])
            # imm[20 | 10: 1 | 11 | 19: 12]
            imm = imm1[0] + imm1[10:20] + imm1[9] + imm1[1:9]
            result = imm + rd + result
            print(lst[2])
            print(imm)
    except ValueError:
        print("Wrong register names \n")

    return result
    


#Corrected B-Type intructions.

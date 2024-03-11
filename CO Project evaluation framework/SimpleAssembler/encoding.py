import sys
# import numpy
# from manim import *

# res= open('result.txt', 'w')
class registers:
    # def __init__(self, regis, abi):

    def regis_binary(abi):
        register_encoding = {
                # Zero register, always returns 0
            "00000": ["x0", "zero", "0"],
                # Return address register, used for storing the return address of a function
            "00001": ["x1", "ra", "0"],
                # Stack pointer, points to the top of the stack
            "00010": ["x2", "sp", "0"],
                # Global pointer, points to the global data area
            "00011": ["x3", "gp", "0"],
                # Thread pointer, points to the current thread's local storage
            "00100": ["x4", "tp", "0"],
                # Temporary/alternate link register
            "00101": ["x5", "t0", "0"],
                # Temporaries for caller
                "00110": ["x6", "t1", "0"],
                "00111": ["x7", "t2", "0"],
                # Saved register/frame pointer
                "01000": ["x8", "s0", "fp"],
                # Saved register
                "01001": ["x9", "s1", "0"],
                # Function arguments/return values for caller
                "01010": ["x10", "a0", "0"],
                "01011": ["x11", "a1", "0"],
                # Function arguments for caller
                "01100": ["x12", "a2", "0"],
                "01101": ["x13", "a3", "0"],
                "01110": ["x14", "a4", "0"],
                "01111": ["x15", "a5", "0"],
                "10000": ["x16", "a6", "0"],
                "10001": ["x17", "a7", "0"],
                # Saved registers for caller
                "10010": ["x18", "s2", "0"],
                "10011": ["x19", "s3", "0"],
                "10100": ["x20", "s4", "0"],
                "10101": ["x21", "s5", "0"],
                "10110": ["x22", "s6", "0"],
                "10111": ["x23", "s7", "0"],
                "11000": ["x24", "s8", "0"],
                "11001": ["x25", "s9", "0"],
                "11010": ["x26", "s10", "0"],
                "11011": ["x27", "s11", "0"],
                # Temporaries for caller
                "11100": ["x28", "t3", "0"],
                "11101": ["x29", "t4", "0"],
                "11110": ["x30", "t5", "0"],
                "11111": ["x31", "t6", "0"]
            }

        for key, values in register_encoding.items():
            i, j = values[1], values[2]
            if i == abi or j == abi:
                return key



    @staticmethod
    def type_of_ins(instruction):
        type_dict = {
            "R": ["add", "sub", "slt", "sltu", "xor", "sll", "srl", "or", "and"],
            "I": ["lw", "addi", "sltiu", "jalr"],
            "S": ["sw"],
            "B": ["beq", "bne", "bge", "bgeu", "blt", "bltu"],
            "U": ["auipc", "lui"],
            "J": ["jal"],
            "BONUS": ["mull", "rst", "halt", "rvrs"]
        }

        for keys, values in type_dict.items():
            if instruction in values:
                return [keys, instruction]

        return False


    def func(instruction):
        inc_type = registers.type_of_ins(instruction)[0]
        inc = registers.type_of_ins(instruction)[1]
        if inc_type == "R":
            # "Instruction" : ["opcode" , "func3" , "func7"]

            dict1 = {
                "add": ["0110011", "000", "0000000"],
                "sub": ["0110011", "000", "0100000"],
                "sll": ["0110011", "001", "0000000"],
                "slt": ["0110011", "010", "0000000"],
                "sltu": ["0110011", "011", "0000000"],
                "xor": ["0110011", "100", "0000000"],
                "srl": ["0110011", "101", "0000000"],
                "or": ["0110011", "110", "0000000"],
                "and": ["0110011", "111", "0000000"],
            }

            for i in dict1.keys():
                if i == inc:
                    return dict1[inc]

        elif inc_type == "I":
            # "Instruction" : ["opcode" , "func3"]
            dict1 = {
                "lw": ["0000011", "010"],
                "addi": ["0010011", "000"],
                "sltiu": ["0010011", "011"],
                "jalr": ["1100111", "000"],
            }

            for i in dict1.keys():
                if i == inc:
                    return dict1[inc]

        elif inc_type == "S":
            # "Instruction" : ["opcode" , "func3"]
            dict1 = {
                "sw": ["0100011", "010"]
            }
            for i in dict1.keys():
                if i == inc:
                    return dict1[inc]

        elif inc_type == "B":
            # "Instruction" : ["opcode" , "func3"]
            dict1 = {
                "beq": ["1100011", "000"],
                "bne": ["1100011", "001"],
                "blt": ["1100011", "100"],
                "bge": ["1100011", "101"],
                "bltu": ["1100011", "110"],
                "bgeu": ["1100011", "111"]
            }
            for i in dict1.keys():
                if i == inc:
                    return dict1[inc]

        elif inc_type == "U":
            # "Instruction" : ["opcode"]
            dict1 = {
                "lui": ["0110111"],
                "auipc": ["0010111"]
            }
            for i in dict1.keys():
                if i == inc:
                    return dict1[inc]


        elif inc_type == "J":
            # "Instruction" : ["opcode"]
            dict1 = {
                "jal": ["1101111"]
            }
            for i in dict1.keys():
                if i == inc:
                    return dict1[inc]

        return False

    def sext_binary(decimal):
        try:
            decimal = int(decimal)
            if decimal >= 0:
                imm = format(decimal, "012b")
                return imm
            else:
                imm = format(2 ** 12 + decimal, "012b")
                return imm
        except ValueError:
            print(" Given is not valid immediate \n ")
            print(decimal)
        return False

    def sext_binary_B(decimal):

        try:
            decimal = int(decimal)
            if decimal >= 0:
                imm = format(decimal, "013b")
                return imm
            else:
                imm = format(2 ** 13 + decimal, "013b")
                return imm
        except ValueError:
            print(" Given is not valid immediate \n ")

        return False
    def sext_binary_J(decimal):

        try:
            decimal = int(decimal)
            if decimal >= 0:
                imm = format(decimal, "021b")
                return imm

            else:
                imm = format(2 ** 21 + decimal, "021b")
                return imm
        except ValueError:
            print(" Given is not valid immediate \n")

        return False

    def sext_binary_U(decimal):
        try:
            decimal = int(decimal)
            if decimal >= 0:
                imm = format(decimal, "032b")
                return imm
            else:
                imm = format(2 ** 32 + decimal, "032b")
                return imm
        except ValueError:
            print(" Given is not valid immediate \n ")
        return False









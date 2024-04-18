
from encoding import *

def extend_to_32_bits(binary_value):
    num_zeros = 32 - len(binary_value)
    extended_binary = '0' * num_zeros + binary_value
    return extended_binary

def binary_to_decimal_signed(binary):
    is_negative = str(binary)[0] == '1'
    if is_negative:
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in binary)
        inverted_binary = bin(int(inverted_binary, 2) + 1)[2:].zfill(32)
        binary = inverted_binary
    # print(binary)
    decimal = int(binary, 2)
    if is_negative:
        decimal = -decimal
    return decimal

def binary_to_decimal_unsigned(binary):
    decimal = int(binary, 2)
    return decimal

class function:
    @staticmethod
    def add(rs2, rs1):
        s1 = binary_to_decimal_signed(rs1)
        s2 = binary_to_decimal_signed(rs2)
        result = s1 + s2
        result = registers.sext_binary_U(result)
        return str(result)

    @staticmethod
    def sub(x0, rs):
        s1 = binary_to_decimal_signed(x0)
        s2 = binary_to_decimal_signed(rs)
        result = s1 - s2
        result = registers.sext_binary_U(result)
        return str(result)

    @staticmethod
    def slt(rs1, rs2, rd):
        r1 = binary_to_decimal_signed(rs1)
        r2 = binary_to_decimal_signed(rs2)
        if r1 < r2:
            rd = registers.sext_binary_U(1)
        return rd

    @staticmethod
    def sltu(rs1, rs2, rd):
        r1 = binary_to_decimal_unsigned(rs1)
        r2 = binary_to_decimal_unsigned(rs2)
        if r1 < r2:
            rd = registers.sext_binary_U(1)
        return rd

    @staticmethod
    def xor(rs1, rs2, rd):
        s1 = int(rs1[-1])
        s2 = int(rs2[-1])
        result = s1 ^ s2
        result = registers.sext_binary_U(result)
        return str(result)

    @staticmethod
    def sll(rs1, rs2, rd):
        shift_amount = rs2[-1:-6:-1]
        shift_amount_int = binary_to_decimal_signed(shift_amount)
        result = int(rs1) << shift_amount_int
        result = registers.sext_binary_U(result)
        return str(result)

    @staticmethod
    def srl(rs1, rs2, rd):
        rs1 = extend_to_32_bits(rs1)
        rs2 = extend_to_32_bits(rs2)
        shift_amount = rs2[-1:-6:-1]
        shift_amount_int = binary_to_decimal_signed(shift_amount)
        result = int(rs1) >> shift_amount_int
        result = registers.sext_binary_U(result)
        return str(result)

    @staticmethod
    def bitwise_or(rs1, rs2, rd):
        r1 = int(rs1[-1])
        r2 = int(rs2[-1])
        result = r1 | r2
        result = registers.sext_binary_U(result)
        return str(result)

    @staticmethod
    def bitwise_and(rs1, rs2, rd):
        r1 = int(rs1[-1])
        r2 = int(rs2[-1])
        result = r1 & r2
        result = registers.sext_binary_U(result)
        return str(result)

    @staticmethod
    def lw(imm, rs1):
        s1 = binary_to_decimal_signed(rs1)
        s2 = binary_to_decimal_signed(imm)
        result = s1 + s2
        result = registers.sext_binary_U(result)
        return str(result)

    @staticmethod
    def stliu(imm, rs, rd):
        r1 = extend_to_32_bits(rs)
        r2 = extend_to_32_bits(imm)
        rs_unsigned = binary_to_decimal_unsigned(r1)
        imm_unsigned = binary_to_decimal_unsigned(r2)
        if rs_unsigned < imm_unsigned:
            rd = extend_to_32_bits("1")
        return rd

    @staticmethod
    def jalr(x6, offset, pc, rd):
        r1 = extend_to_32_bits(x6)
        r2 = extend_to_32_bits(offset)
        offset_new = r2[-1:-12:-1]
        offset_decimal = binary_to_decimal_signed(offset_new)
        x6_decimal = binary_to_decimal_signed(x6)
        rd = pc + 4
        rd = registers.sext_binary_U(pc)
        pc = x6_decimal + offset_decimal
        pc = registers.sext_binary_U(pc)
        return [rd, pc]

    @staticmethod
    def sw(rs1, imm):
        s1 = binary_to_decimal_signed(rs1)
        imm1 = binary_to_decimal_signed(imm)
        s2 = imm1 + s1
        rs2 = registers.sext_binary_U(s2)
        return rs2

    @staticmethod
    def addi(imm, rs):
        r1 = extend_to_32_bits(rs)
        imm = extend_to_32_bits(imm)
        r1_int = binary_to_decimal_signed(r1)
        imm_int = binary_to_decimal_signed(imm[-1:-12:-1])
        rd = r1_int + imm_int
        rd = registers.sext_binary_U(rd)
        return rd

    @staticmethod
    def beq(rs2, rs1, imm, pc):
        prog = registers.sext_binary_U(pc)
        if binary_to_decimal_signed(rs1) == binary_to_decimal_signed(rs2):
            prog = pc + binary_to_decimal_signed(imm)
            prog = registers.sext_binary_U(prog)
        return prog

    @staticmethod
    def bne(rs2, rs1, imm, pc):
        prog = registers.sext_binary_U(pc)
        if binary_to_decimal_signed(rs1) != binary_to_decimal_signed(rs2):
            prog = pc + binary_to_decimal_signed(imm)
            prog = registers.sext_binary_U(prog)
        return prog


    @staticmethod
    def bge(rs2, rs1, imm, pc):
        prog = registers.sext_binary_U(pc)
        if binary_to_decimal_signed(rs1) >= binary_to_decimal_signed(rs2):
            prog = pc + binary_to_decimal_signed(imm)
            prog = registers.sext_binary_U(prog)
        return prog

    @staticmethod
    def bgeu(rs2, rs1, imm, pc):
        prog = registers.sext_binary_U(pc)
        if binary_to_decimal_unsigned(rs1) >= binary_to_decimal_unsigned(rs2):
            prog = pc + binary_to_decimal_signed(imm)
            prog = registers.sext_binary_U(prog)
        return prog

    @staticmethod
    def blt(rs2, rs1, imm, pc):
        prog = registers.sext_binary_U(pc)
        if binary_to_decimal_signed(rs1) < binary_to_decimal_signed(rs2):
            prog = pc + binary_to_decimal_signed(imm)
            prog = registers.sext_binary_U(prog)
        return prog

    @staticmethod
    def btlu(rs2, rs1, imm, pc):
        prog = registers.sext_binary_U(pc)
        if binary_to_decimal_unsigned(rs1) < binary_to_decimal_unsigned(rs2):
            prog = pc + binary_to_decimal_signed(imm)
            prog = registers.sext_binary_U(prog)
        return prog

    @staticmethod
    def auipc(rd, pc, imm):
        imm = extend_to_32_bits(imm)[-32:-12]
        rd = pc + binary_to_decimal_signed(imm)
        return rd

    @staticmethod
    def lui(imm, pc):
        imm = extend_to_32_bits(imm)[-32:-12]
        rd = binary_to_decimal_signed(imm) 
        return rd

    @staticmethod
    def jal(rd, pc, imm):
        pc = pc + 4
        rd = registers.sext_binary_U(pc)
        imm1_decimal = binary_to_decimal_signed(imm)
        pc = pc + imm1_decimal
        pc = registers.sext_binary_U(pc)
        return [rd,pc]
    





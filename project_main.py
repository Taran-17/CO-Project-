

from encoding import regs

def assemble_instruction(instruction):
    parts = instruction.split()
    opcode = {
        "add": "0110011",
        "jalr": "1100111",
        "lw": "0000011",
        "sw": "0100011",
        "blt": "1100011",
        "auipc": "0010111",
        "jal": "1101111"
    }[parts[0]]

    if parts[0] == "add":
        funct7 = "0000000"
        funct3 = "000"
        rd = regs[format(int(parts[1][1:]), '05b')]
        rs1 = regs[format(int(parts[2][1:]), '05b')]
        rs2 = regs[format(int(parts[3][1:]), '05b')]
        return f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}"

    if parts[0] == "jalr":
        imm = format(int(parts[3]), '012b')
        funct3 = "000"
        rd = regs[format(int(parts[1][1:]), '05b')]
        rs1 = regs[format(int(parts[2][1:]), '05b')]
        return f"{imm}{rs1}{funct3}{rd}{opcode}"

    if parts[0] == "lw" or parts[0] == "sw":
        offset = parts[2].split("(")
        imm = format(int(offset[0]), '012b')
        funct3 = {
            "lw": "010",
            "sw": "010"
        }[parts[0]]
        rd = regs[format(int(parts[1][1:]), '05b')]
        rs1 = regs[format(int(offset[1][1:-1]), '05b')]
        return f"{imm}{rs1}{funct3}{rd}{opcode}"

    if parts[0] == "blt":
        imm = format(int(parts[3]) - 1, '013b')[::-1]
        funct3 = "100"
        rs1 = format(int(parts[1][1:]), '05b')
        rs2 = format(int(parts[2][1:]), '05b')
        imm = imm[:5] + imm[6:]  # rearranging imm for B-type instruction
        return f"{imm}{rs2}{rs1}{funct3}{opcode}"

    if parts[0] == "auipc":
        imm = format(int(parts[2]), '020b')
        rd = regs[format(int(parts[1][1:]), '05b')]
        return f"{imm}{rd}{opcode}"

    if parts[0] == "jal":
        imm = format(int(parts[2]) - 1, '021b')[::-1]
        rd = regs[format(int(parts[1][1:]), '05b')]
        imm = imm[:1] + imm[11:] + imm[1:11]  # rearranging imm for J-type instruction
        return f"{imm}{rd}{opcode}"


if __name__ == "__main__":
    for line in sys.stdin:
        assembly_instruction = line.strip()
        if not assembly_instruction:
            break
        machine_code = assemble_instruction(assembly_instruction)
        print(machine_code)

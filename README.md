# CO-Project-

Members:<br />
Tushita Kapoor 2023562 <br />
Rahul Agarwal 2023418  <br />
Tarandeep Singh 2023553  <br />
Pranshu Ranga 2023386  <br />

-> Process to run the code:-
a) Download the repository and open the Assembler.py file. Now run the Assembler.py file in the terminal.
b) To check for the testcases, run it in the cmd/terminal.
c) The result/output will show as to how many of the tescases worked and passes.

-> Assembler file: https://github.com/naiverahul/CO-Project-/blob/main/Assembler.py
The above is the link for the main assembler, which converts assembly program into binary and further lets us check for the tescases. It contains the program counter, which helps to handle labels and instructions related to it efficinetly. It also consists of a filter function to filter and append the required output of segregated instructions. Also, we have used is-else and try-except blocks to ensure the smooth and efficient functioning of our code.

The labels and the immediates have been implemented in such a way, that whenever encountered by an invalid opcode, out of range immediate value, or register, it stops working and throws an error.

-> Encoding file: https://github.com/naiverahul/CO-Project-/blob/main/encoding.py
This file consists of the register class, which defines methods for encoding RISC-V assembly instructions into binary machine code. It consists of methods for encoding different types of instructions(like R,I,S,B,J,U).It consists of a function named: 'regis_binary', which is used for register encoding. The function: 'type_of_ins' comsists of all the types of instructions of different types. The function 'func' consists of all the operations with their details in binary format,like opcode,function code(of each type like R,J,U,etc). The functions 'sext_binary','sext_binary_B','sext_binary_J', 'sext_binary_U' are used to take the immediate values and convert them properly.

-> Helper file: https://github.com/naiverahul/CO-Project-/blob/main/helper.py
This file contains a helper function, used in the main script to process attain the output in binary of the segregated instructions.




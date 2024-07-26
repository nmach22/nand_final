from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List


def get_a_instr(curr_instruction: str, symbol_table: dict[str, int]) -> str:
    bin_num = "0"
    if curr_instruction[1:].isnumeric():
        bin_num += "{:015b}".format(int(curr_instruction[1:]))
    else:
        bin_num += "{:015b}".format(symbol_table[curr_instruction[1:]])
    return bin_num


def get_destination_binary_code(dest: str) -> str:
    if not dest:
        return "000"
    result = ""
    if "A" in dest:
        result += "1"
    else:
        result += "0"

    if "D" in dest:
        result += "1"
    else:
        result += "0"
    if "M" in dest:
        result += "1"
    else:
        result += "0"
    return result


def get_computation_binary(comp: str) -> str:
    result = "0"
    if "M" in comp:
        result = "1"

    if comp == "0":
        result += "101010"
    elif comp == "1":
        result += "111111"
    elif comp == "-1":
        result += "111010"
    elif comp == "D":
        result += "001100"
    elif comp == "A" or comp == "M":
        result += "110000"
    elif comp == "!D":
        result += "001101"
    elif comp == "!A" or comp == "!M":
        result += "110001"
    elif comp == "-D":
        result += "001111"
    elif comp == "-A" or comp == "-M":
        result += "110011"
    elif comp == "D+1":
        result += "011111"
    elif comp == "D-1":
        result += "001110"
    elif comp == "A+1" or comp == "M+1":
        result += "110111"
    elif comp == "A-1" or comp == "M-1":
        result += "110010"
    elif comp == "D+A" or comp == "D+M" or comp == "A+D" or comp == "M+D":
        result += "000010"
    elif comp == "D-A" or comp == "D-M":
        result += "010011"
    elif comp == "A-D" or comp == "M-D":
        result += "000111"
    elif comp == "D&A" or comp == "D&M":
        result += "000000"
    elif comp == "D|A" or comp == "D|M":
        result += "010101"
    return result


def get_jump_binary(jump: str) -> str:
    result = "000"
    if jump == "JGT":
        result = "001"
    if jump == "JEQ":
        result = "010"
    if jump == "JGE":
        result = "011"
    if jump == "JLT":
        result = "100"
    if jump == "JNE":
        result = "101"
    if jump == "JLE":
        result = "110"
    if jump == "JMP":
        result = "111"
    return result


def get_c_instr(instruction: str) -> str:
    # tmp_instr = instruction
    dest, comp, jump = "", "", ""
    if "=" in instruction:
        dest = instruction[: instruction.find("=")]
        instruction = instruction[instruction.find("=") + 1:]

    if ";" in instruction:
        comp = instruction[: instruction.find(";")]
        instruction = instruction[instruction.find(";") + 1:]
        jump = instruction
    else:
        comp = instruction

    # print(tmp_instr, "dest", dest, "comp", comp, "jump", jump)

    # destination
    dest = get_destination_binary_code(dest)

    # computation
    comp = get_computation_binary(comp)

    # Jump
    jump = get_jump_binary(jump)

    c_instruction = "111" + comp + dest + jump

    return c_instruction


@dataclass
class Assembler:
    @classmethod
    def create(cls) -> Assembler:
        return cls()

    # Add the predefined symbols to the symbol_table.
    def generate_symbol_table(self) -> dict[str, int]:
        symbol_table = {
            "SCREEN": 16384,
            "KBD": 24576,
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,
        }
        # Fill the symbol table with R0 to R15
        for i in range(16):
            symbol_table[f"R{i}"] = i
        return symbol_table

    # Remove comments and white spaces from the code.
    def remove_comments_and_spaces(self, assembly: Iterable[str]) -> List[str]:
        cleaned_assembly = []
        for line in assembly:
            # Remove comments starting with "//" and strip white spaces
            if "//" in line:
                start_index = line.find("//")
                line = line[:start_index]

            if not line.strip():
                continue
            cleaned_line = line.strip().replace(" ", "")
            cleaned_assembly.append(cleaned_line)
        return cleaned_assembly

    def assemble(self, assembly: Iterable[str]) -> Iterable[str]:
        # Call the function to remove comments and white spaces
        cleaned_code = self.remove_comments_and_spaces(assembly)

        # Fill the symbol table
        symbol_table = self.generate_symbol_table()

        # Iterate over the assembly instructions and
        # fill the dictionary with variables and labels.
        instructions = []
        address = 0
        for code in cleaned_code:
            if code[0] == "(" and code[-1] == ")":
                label = code[1:-1]
                if label not in symbol_table:
                    symbol_table[label] = address
            else:
                instructions.append(code)
                address += 1

        # Variables start from address 16. (First 15 addresses
        # are special and predefined that we've already added into the dict)
        index = 16
        for curr_instruction in instructions:
            if curr_instruction[0] == "@":
                # If A instruction contains number after '@'
                # we shouldn't add it to the symbol_table
                if not curr_instruction[1:].isnumeric():
                    # If instruction doesn't appear in dictionary,
                    # it is a variable, and we need to save it in dict.
                    if curr_instruction[1:] not in symbol_table:
                        symbol_table[curr_instruction[1:]] = index
                        index += 1
        result = []

        for i, curr_instruction in enumerate(instructions):
            # print(i, curr_instruction)
            # if curr_instruction == "M=-1":
            #     print(curr_instruction)
            # instruction_to_binary = ""
            if curr_instruction[0] == "@":
                # 'A' Instruction: binary code is: 0 and
                # binary representation of address (15 bits)
                instruction_to_binary = get_a_instr(curr_instruction, symbol_table)
            else:
                # Handle 'C' Instruction
                instruction_to_binary = get_c_instr(curr_instruction)
            result.append(instruction_to_binary)

        return result

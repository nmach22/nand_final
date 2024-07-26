from typing import Iterable


class Memory:
    def __init__(self, size: int) -> None:
        self.memory = [0] * size
        self.used_indices: set[int] = set()

    def set(self, index: int, value: int) -> None:
        self.memory[index] = value
        self.used_indices.add(index)

    def get(self, index: int) -> int:
        return self.memory[index]

    def dump_to_dict(self) -> dict[int, int]:
        result: dict[int, int] = dict()
        for i in self.used_indices:
            result[i] = self.memory[i]
        return result

    def __getitem__(self, index: int) -> int:
        return self.get(index)

    def __setitem__(self, index: int, value: int) -> None:
        self.set(index, value)

    def __len__(self) -> int:
        return len(self.memory)


class HackComputer:
    def __init__(self) -> None:
        self.RAM = Memory(32768)  # 32K RAM
        self.ROM = [0] * 32768  # 32K RAM
        self.PC = 0  # Program Counter
        self.registers = {'A': 0, 'D': 0}

    def load_program(self, hack_instructions: Iterable[str]) -> None:
        for i, instruction in enumerate(hack_instructions):
            self.ROM[i] = int(instruction, 2)

    def execute(self, cycles: int) -> None:
        for _ in range(cycles):
            if self.PC >= len(self.RAM):
                raise RuntimeError(f'PC {self.PC} out of range')
            instruction = self.ROM[self.PC]
            self.execute_instruction(instruction)

    def execute_instruction(self, instruction: int) -> None:
        binary_str = f"{instruction:016b}"

        # 'A' Instruction
        if binary_str[0] == '0':
            binary_value = binary_str[1:]
            value = int(binary_value, 2)
            self.registers['A'] = value
        # C Instruction
        else:
            # 111accccccdddjjj
            a = binary_str[3]  # Addressing mode
            c = binary_str[4:10]  # Computation part
            d = binary_str[10:13]  # Destination part

            comp_result = self.compute(c, a)

            if d[2] == '1':  # Destination M
                self.RAM[self.registers['A']] = comp_result
            if d[1] == '1':  # Destination D
                self.registers['D'] = comp_result
            if d[0] == '1':  # Destination A
                self.registers['A'] = comp_result

        # Update the Program Counter (PC) based on the jump part
        if binary_str[0] == '1' and self.should_jump(binary_str[13:16]):
            self.PC = self.registers['A']
        else:
            self.PC += 1

    def compute(self, comp_bits: str, a: str) -> int:
        # Decode the computation part
        if comp_bits == '101010':  # 0
            return 0
        elif comp_bits == '111111':  # 1
            return 1
        elif comp_bits == '111010':  # -1
            return -1
        elif comp_bits == '001100':  # D
            return self.registers['D']

        elif a == '0' and comp_bits == '110000':  # A
            return self.registers['A']
        elif a == '1' and comp_bits == '110000':  # M
            return self.RAM[self.registers['A']]

        elif comp_bits == '001101':  # !D
            return ~self.registers['D']

        elif a == '0' and comp_bits == '110001':  # !A
            return ~self.registers['A']
        elif a == '1' and comp_bits == '110001':  # !M
            return ~self.RAM[self.registers['A']]

        elif comp_bits == '001101':  # -D
            return -self.registers['D']

        elif a == '0' and comp_bits == '110011':  # -A
            return -self.registers['A']
        elif a == '1' and comp_bits == '110011':  # -M
            return -self.RAM[self.registers['A']]

        elif comp_bits == '011111':  # D+1
            return self.registers['D'] + 1

        elif a == '0' and comp_bits == '110111':  # A+1
            return self.registers['A'] + 1
        elif a == '1' and comp_bits == '110111':  # M+1
            return self.RAM[self.registers['A']] + 1
        elif comp_bits == '001110':  # D-1
            return self.registers['D'] - 1

        elif a == '0' and comp_bits == '110010':  # A-1
            return self.registers['A'] - 1
        elif a == '1' and comp_bits == '110010':  # M-1
            return self.RAM[self.registers['A']] - 1

        elif a == '0' and comp_bits == '000010':  # D+A
            return self.registers['D'] + self.registers['A']
        elif a == '1' and comp_bits == '000010':  # D+M
            return self.registers['D'] + self.RAM[self.registers['A']]

        elif a == '0' and comp_bits == '010011':  # D-A
            return self.registers['D'] - self.registers['A']
        elif a == '1' and comp_bits == '010011':  # D-M
            return self.registers['D'] - self.RAM[self.registers['A']]

        elif a == '0' and comp_bits == '000111':  # A-D
            return self.registers['A'] - self.registers['D']
        elif a == '1' and comp_bits == '000111':  # M-D
            return self.RAM[self.registers['A']] - self.registers['D']

        elif a == '0' and comp_bits == '000000':  # D&A
            return self.registers['D'] & self.registers['A']
        elif a == '1' and comp_bits == '000000':  # D&M
            return self.registers['D'] & self.RAM[self.registers['A']]

        elif a == '0' and comp_bits == '001100':  # D|A
            return self.registers['D'] | self.registers['A']
        elif a == '1' and comp_bits == '001100':  # D|M
            return self.registers['D'] | self.RAM[self.registers['A']]

        else:
            raise ValueError(f"Invalid computation bits: {comp_bits}")

    def should_jump(self, jump_bits: str) -> bool:
        # Decode the jump part
        comp_result = self.registers['D']
        if jump_bits == '000':  # null
            return False
        elif jump_bits == '001':  # JGT
            return comp_result > 0
        elif jump_bits == '010':  # JEQ
            return comp_result == 0
        elif jump_bits == '011':  # JGE
            return comp_result >= 0
        elif jump_bits == '100':  # JLT
            return comp_result < 0
        elif jump_bits == '101':  # JNE
            return comp_result != 0
        elif jump_bits == '110':  # JLE
            return comp_result <= 0
        elif jump_bits == '111':  # JMP
            return True
        else:
            raise ValueError(f"Invalid jump bits: {jump_bits}")

    def dump_ram(self) -> dict[int, int]:
        return self.RAM.dump_to_dict()

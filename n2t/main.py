import argparse
import json
import os
from typing import Iterable

from n2t.HackComputer import HackComputer
from n2t.home_works.assembler import Assembler


def main() -> None:
    parser = argparse.ArgumentParser(description='Hack Simulator')
    parser.add_argument('operation_name', type=str, help='operation name (execute)', choices=['execute'])
    parser.add_argument('file_path', type=str, help='Path to the .hack or .asm file')
    parser.add_argument('--cycles', type=int, default=10000, help='Number of cycles to execute')
    args = parser.parse_args()

    file_path = args.file_path
    cycles = args.cycles

    if file_path.endswith('.asm'):
        hack_instructions = parse_asm(file_path)
        file_path = write_hack(file_path, hack_instructions)

    with open(file_path, 'r') as f:
        hack_instructions = [line.strip() for line in f.readlines()]

    computer = HackComputer()
    computer.load_program(hack_instructions)
    computer.execute(cycles)

    ram_state = computer.dump_ram()
    json_output = {
        "RAM": ram_state
    }
    file_suffix = "_generated.hack" if file_path.endswith("_generated.hack") else ".hack"
    json_file = file_path.replace(file_suffix, '.json')
    with open(json_file, 'w') as f:
        json.dump(json_output, f, indent=4)

    if file_path.endswith('_generated.hack'):
        os.remove(file_path)


if __name__ == "__main__":
    main()


def parse_asm(file_path: str) -> Iterable[str]:
    assembler = Assembler.create()
    # Assembler logic to convert .asm to .hack
    with open(file_path, 'r') as f:
        assembly_instr = f.readlines()

    clean_assembly = assembler.remove_comments_and_spaces(assembly_instr)
    return assembler.assemble(clean_assembly)


def write_hack(file_path: str, hack_instructions: Iterable[str]) -> str:
    hack_file = file_path.replace('.asm', '_generated.hack')
    with open(hack_file, 'w') as f:
        for instruction in hack_instructions:
            f.write(instruction + '\n')
    return hack_file

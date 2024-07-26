import subprocess
from compare_json import compare_json_files


def execute_test(asm_file: str) -> int:
    cmd = ["python", "-m", "n2t", "execute",
           asm_file, "--cycles",
           "10000"]
    exit_code = subprocess.check_call(cmd)
    if exit_code != 0:
        print(exit_code)
        return 1
    file1_path = asm_file.replace('.asm', '.json')
    file2_path = asm_file.replace('.asm', '_comp.json')

    assert compare_json_files(file1_path, file2_path)
    return 0


def main() -> None:
    tests = ["./t1/Add.asm", "./t2/Sub.asm", "./t3/Copy.asm", "./t4/Loop.asm", "./t5/Jump.asm",
             "./t6/FibonacciElement.asm"]
    for test in tests:
        execute_test(test)


if __name__ == '__main__':
    main()

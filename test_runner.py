import itertools
import pathlib
import subprocess

from compare_json import compare_json_files

PROJECT_ROOT = pathlib.Path(__file__).parent


def execute_test(asm_file: pathlib.Path) -> int:
    cmd = ["python", "-m", "n2t", "execute",
           asm_file, "--cycles",
           "10000"]
    exit_code = subprocess.check_call(cmd, cwd=PROJECT_ROOT)
    if exit_code != 0:
        print(exit_code)
        return 1

    file1_path = asm_file.with_suffix(".json")
    ext = asm_file.suffix
    file2_path = asm_file.with_name(asm_file.name.replace(ext, '_comp.json'))

    assert compare_json_files(file1_path, file2_path)
    return 0


def main() -> None:
    tests_dir = PROJECT_ROOT / "files" / "tests"
    tests = itertools.chain(tests_dir.rglob("*.asm"), tests_dir.rglob("*.hack"))

    for test in tests:
        res = execute_test(test)

        if res == 0:
            print(f"executed {test} successfully")
        else:
            print(f"executed {test} failed: {res}")


if __name__ == '__main__':
    main()

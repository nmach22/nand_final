import json
from typing import Any, Dict, cast


def load_json(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        return cast(Dict[str, Any], json.load(file))


def is_subset(superset: Dict[str, Any], subset: Dict[str, Any]) -> bool:
    for key, value in subset.items():
        if key not in superset or superset[key] != value:
            return False
    return True


def compare_json_files(file1: str, file2: str) -> bool:
    json1 = load_json(file1)
    json2 = load_json(file2)

    if 'RAM' in json1 and 'RAM' in json2:
        subset_result = is_subset(json1['RAM'], json2['RAM'])
    else:
        subset_result = False

    return subset_result


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Compare two JSON files.")
    parser.add_argument("file1", help="Path to the first JSON file.")
    parser.add_argument("file2", help="Path to the second JSON file.")

    args = parser.parse_args()

    compare_json_files(args.file1, args.file2)

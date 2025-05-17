import re


def main(input_str):
    pattern = r'store\s+([a-zA-Z0-9_]+)\s*:\s*(-?\d+)'
    matches = re.findall(pattern, input_str)
    result = {}
    for match in matches:
        key = match[0]
        value = int(match[1])
        result[key] = value
    return result


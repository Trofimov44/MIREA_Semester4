def main(_str):
    num = int(_str)
    n1 = (num >> 0) & 0b1
    n2 = (num >> 1) & 0b111111111
    n3 = (num >> 10) & 0b11

    result = 0
    result |= (n3 << 14)
    result |= (n2 << 5)
    result |= (n1 << 0)

    hex_str = hex(result)

    return hex_str

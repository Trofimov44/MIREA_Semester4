import numpy as np
def handle_metal(x):
    if x[4] == 'MASK':
        if x[1] == 1973:
            return 0
        elif x[1] == 1987:
            return 1
        elif x[1] == 1978:
            return 2
    if x[4] == 'JAVA':
        return 3
    if x[4] == 'CHUCK':
        return 4


def handle_hlsl(x):
    # Handle MASK conditions separately
    if x[4] == 'MASK':
        return handle_mask(x)

    # Handle JAVA conditions
    if x[4] == 'JAVA':
        return handle_java(x)

    # Handle CHUCK condition
    if x[4] == 'CHUCK':
        return 10


def handle_mask(x):
    if x[0] == 1982:
        if x[2] == 'CSS':
            return 5
        else:
            return 6
    elif x[0] == 1967:
        return 7


def handle_java(x):
    if x[0] == 1982:
        return 8
    else:
        return 9


def main(x):
    if x[3] == 'METAL':
        return handle_metal(x)
    if x[3] == 'X10':
        return 11
    if x[3] == 'HLSL':
        return handle_hlsl(x)

# Проверка примеров
examples = [
    ([1982, 1978, 'GLYPH', 'METAL', 'JAVA'], 3),
    ([1967, 1987, 'GLYPH', 'X10', 'MASK'], 11),
    ([1982, 1987, 'GLYPH', 'METAL', 'MASK'], 1),
    ([1967, 1978, 'GLYPH', 'METAL', 'CHUCK'], 4),
    ([1982, 1978, 'GLYPH', 'HLSL', 'JAVA'], 8)
]

for inp, expected in examples:
    result = main(inp)
    print(f"main({inp}) = {result}, expected = {expected}")

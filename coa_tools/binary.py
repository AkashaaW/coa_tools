def to_binary(number):
    return bin(number)[2:]


def twos_complement(number, bits=8):
    minimum = -(2 ** (bits - 1))
    maximum = 2 ** (bits - 1) - 1

    if number < minimum or number > maximum:
        raise ValueError("Number does not fit in the selected bit width")

    if number < 0:
        number = (2 ** bits) + number

    return format(number, f"0{bits}b")

def from_binary(binary_text, signed=False):
    if not binary_text or any(bit not in "01" for bit in binary_text):
        raise ValueError("Enter only binary digits 0 and 1")

    number = int(binary_text, 2)

    if signed and binary_text[0] == "1":
        number = number - (2 ** len(binary_text))

    return number
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

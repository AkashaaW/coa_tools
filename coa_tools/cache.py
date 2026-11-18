def split_address(address, cache_size=16, block_size=4):
    number_of_lines = cache_size // block_size
    block_number = address // block_size

    index = block_number % number_of_lines
    tag = block_number // number_of_lines
    offset = address % block_size

    return tag, index, offset


def access_cache(address, cache_lines):
    tag, index, offset = split_address(address)

    if cache_lines[index] == tag:
        return "HIT"

    cache_lines[index] = tag
    return "MISS"
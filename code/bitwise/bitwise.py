
def swap_even_odd_bits(n: int) -> int:
    even_bits_shifted_left = _clear_odd_bits(n) << 1
    odd_bits_shifted_right = _clear_even_bits(n) >> 1
    
    return even_bits_shifted_left | odd_bits_shifted_right


def _clear_odd_bits(n: int) -> int:
    return n & int("01010101010101010101010101010101", base=2)


def _clear_even_bits(n: int) -> int:
    return n & int("10101010101010101010101010101010", base=2)

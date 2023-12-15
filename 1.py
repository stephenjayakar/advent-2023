from typing import Tuple

# assumes that there is at least one digit in calibration_value
def get_digits(calibration_value: str) -> Tuple[str, str]:
    first_digit = None
    last_digit = None
    for c in calibration_value:
        if c.isdigit():
            if first_digit == None:
                first_digit = c
            last_digit = c
    assert(not (first_digit == None or last_digit == None))
    return first_digit, last_digit

def soln():
    with open('inputs/1', 'r') as file:
        contents = file.readlines()
    total = 0
    for line in contents:
        digits = get_digits(line)
        number = int(''.join(digits))
        total += number
    return total

def test():
    tcs = {
    "1abc2": ('1', '2'),
    "pqr3stu8vwx": ('3', '8'),
    "a1b2c3d4e5f": ('1', '5'),
    "treb7uchet": ('7', '7'),
    }
    for x, expected in tcs.items():
        actual1, actual2 = get_digits(x)
        assert(actual1 == expected[0] and actual2 == expected[1])

if __name__ == '__main__':
    test()
    print(soln())

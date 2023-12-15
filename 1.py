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

number_strs = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]
def get_digits2(calibration_value: str) -> int:
    first_digit = None
    last_digit = None
    for i, c in enumerate(calibration_value):
        possibleVal = None
        if c.isdigit():
            possibleVal = c
        else:
            for j, number_str in enumerate(number_strs):
                actual_number = str(j + 1)
                if calibration_value[i:i+len(number_str)] == number_str:
                    possibleVal = actual_number
        if possibleVal:
            if first_digit == None:
                first_digit = possibleVal
            last_digit = possibleVal
    assert(not (first_digit == None or last_digit == None))
    return int(f'{first_digit}{last_digit}')

def soln2():
    with open('inputs/1', 'r') as file:
        contents = file.readlines()
    total = 0
    for line in contents:
        number = get_digits2(line)
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

def test2():
    tcs = {
        'two1nine': 29,
        'eightwothree': 83,
        'abcone2threexyz': 13,
        'xtwone3four': 24,
        '4nineeightseven2': 42,
        'zoneight234': 14,
        '7pqrstsixteen': 76,
    }
    for x, expected in tcs.items():
        actual = get_digits2(x)
        assert(expected == actual)

if __name__ == '__main__':
    test()
    print(soln())
    test2()
    print(soln2())

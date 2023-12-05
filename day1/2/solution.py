import re

DIGIT_MAP = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def replace_inline(line):
    for spelled, digit in DIGIT_MAP.items():
        line = re.sub(rf'{spelled}', f'{spelled}{digit}{spelled}', line)

    return line


def cast_to_digits(line):
    integers_line = replace_inline(line)
    return re.findall(r'\d', integers_line)


def get_number(line):
    digits = cast_to_digits(line)

    first = digits[0]
    last = digits[-1]
    number = int(f'{first}{last}')

    return number


def main():
    total = 0

    with open('sample_input.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            number = get_number(line)

            print(f'{line} [number: {number}]')

            total += number

    print(f'Total: {total}')

if __name__ == "__main__":
    main()

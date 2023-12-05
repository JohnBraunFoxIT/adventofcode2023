import re

def retrieve_digits_from_string(input):
    return re.findall(r'\d', input)


def get_number(matches):
    first = matches[0]
    last = matches[-1]

    number = int(f'{first}{last}')

    return number


def main():
    total = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            matches = retrieve_digits_from_string(line)
            number = get_number(matches)
            print(f'Found number: {number}')
            total += number 

    print(f'Total: {total}')
        

if __name__ == "__main__":
    main()

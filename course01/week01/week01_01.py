import sys
digit_string = sys.argv[1]

if digit_string.isdigit():
    print(sum(map(int, digit_string)))
else:
    print('value is not digit')

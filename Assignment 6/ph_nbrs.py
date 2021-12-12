import sys
import re

file_name = sys.argv[1]

ptrn1 = '(\([2-9][0-8][0-9]\)) ([2-9][0-9]{2})-(\d{4})'
ptrn2 = '([2-9][0-8][0-9])-([2-9][0-9]{2})-(\d{4})'
ptrn3 = '([2-9][0-8][0-9]).([2-9][0-9]{2}).(\d{4})'
ptrn4 = '([2-9][0-8][0-9]) ([2-9][0-9]{2}) (\d{4})'
ptrn5 = '([2-9][0-8][0-9])([2-9][0-9]{2})(\d{4})'

pattern_list = [ptrn1, ptrn2, ptrn3, ptrn4, ptrn5]

with open(file_name) as f:
    for line in f:
        number = line[:-1]
        for ptrn in pattern_list:
            regex = re.compile(ptrn)
            match = regex.search(number)
            if match:
                if match.group(2)[1:] == '11':
                    print(f'[ERROR] {number} is an invalid phone number')
                    print(
                        "        2nd and 3rd digits in the Exchange Code can't be 1 at the same time")
                    break
                else:
                    international_format = f'+1{match.group(1)}{match.group(2)}{match.group(3)}'
                    print(f'{number} is a valid phone number')
                    print(
                        f'{"*"*len(number)} International-formatted phone number is {international_format}')
                    break
        else:
            print(f'[ERROR] {number} has an invalid format / digits')

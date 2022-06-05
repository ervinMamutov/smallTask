#! usr/bin python3
"""
n2w: module for converting numbers into verbal description
contains num2words function
Can also be run as a script.
Use as a script: n2w num #  Usage Help; includes example
(Converts a number to its description in English)
num: an integer in the range 0 to 999,999,999,999,999
(commas are optional)
example: n2w 10,003,103
for 10,003,103, say: ten million three thousand one hundred three

"""
import argparse
import sys

_1to9dict = {'0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
             '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
_10to19dict = {'0': 'ten', '1': 'eleven', '2': 'twelve', '3': 'thirteen', '4': 'fourteen',
               '5': 'fifteen', '6': 'sexteen', '7': 'seventeen', '8': 'eighteen',
               '9': 'nineteen'}
_20to90dict = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty',
               '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}
_magnitude_list = [(0, ''), (3, 'thousand '), (6, 'million '),
                   (9, 'billion'), (12, 'trillion'), (15, '')]


def num2words(num_string):
    """num2words(num_string): convert number to English words"""
    if num_string == '0':  # Handles special cases (number is 0 or too large)
        return 'zero'
    num_string = num_string.replace(',', '')  # Removes commas from numbers
    num_length = len(num_string)
    max_digits = _magnitude_list[-1][0]
    if num_length > max_digits:
        return 'Sorry, cant handle numbers with more than   ' \
               '{0} digits'.format(max_digits)
    num_string = '00' + num_string  # Pads number with spaces on the left
    # creates a string with a number
    word_string = ''  # Initializes a string to describe
    for mag, name in _magnitude_list:
        if mag >= num_length:
            return word_string
        else:
            hundreds, tens, ones = num_string[-mag - 3], \
                                   num_string[-mag - 2], num_string[-mag - 1]
            if not (hundreds == tens == ones == '0'):
                word_string = _handle1to999(hundreds, tens, ones) + \
                              name + word_string


def _handle1to999(hundreds, tens, ones):
    if hundreds == '0':
        return _handle1to99(tens, ones)
    else:
        return _1to9dict[hundreds] + 'hundred' + _handle1to99(tens, ones)


def _handle1to99(tens, ones):
    if tens == '0':
        return _1to9dict[ones]
    elif tens == '1':
        return _10to19dict[ones]
    else:
        return _20to90dict[tens] + ' ' + _1to9dict[ones]


def test():  # Function for module test mode
    values = sys.stdin.read().split()
    for val in values:
        print('{0} = {1}'.format(val, num2words(val)))


def main():
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument('num', nargs='*')  # Gathers all values in this argument into a list
    parser.add_argument('-t', '--test', dest='test',
                        action='store_true', default=False,
                        help='Test mode: reads from stdin')
    args = parser.parse_args()
    if args.test:  # Runs in test mode if the test variable is set
        test()
    else:
        try:
            result = num2words(args.num[0])
        except KeyError:
            parser.error('argument contains non-digits')
        else:
            print('For {0}, say: {1}'.format(args.num[0], result))


if __name__ == '__main__':
    main()
else:
    print('n2w loaded as a module')

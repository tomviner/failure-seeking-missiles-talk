import re
import pytest
from nose.tools import assert_equal

def compress_string(string):
    if string is None or len(string) == 0:
        return string

    # Calculate the size of the compressed string
    size = 0
    last_char = string[0]
    for char in string:
        if char != last_char:
            size += 2
            last_char = char
    size += 2

    # If the compressed string size is greater than
    # or equal to string size, return original string
    if size >= len(string):
        return string

    # Create compressed_string
    compressed_string = list()
    count = 0
    last_char = string[0]
    for char in string:
        if char == last_char:
            count += 1
        else:
            compressed_string.append(last_char)
            compressed_string.append(str(count))
            count = 1
            last_char = char
    compressed_string.append(last_char)
    compressed_string.append(str(count))

    # Convert the characters in the list to a string
    return "".join(compressed_string)

def expand_string(s):
    part_re = r'(?:^\w+|\d+\w+|\w+\d+|\w+|\d+)'
    res = ''
    letter = ''
    for part in re.findall(part_re, s):
        if part.isdigit():
            res += int(part) * letter
        else:
            res += part[:-1]
            letter = part[-1]
    return res


@pytest.mark.parametrize('s', ('AABBCC', 'AAABCCDDDD'))
def test_compress_expand(s):
    assert expand_string(compress_string(s)) == s

class TestCompress(object):

    def test_compress(self, func=compress_string):
        assert_equal(func(None), None)
        assert_equal(func(''), '')
        assert_equal(func('AABBCC'), 'AABBCC')
        assert_equal(func('AAABCCDDDD'), 'A3B1C2D4')
        print('Success: test_compress')

# integers().map(text(alphabet=string.upper), lambda n, x: n*x)

def main():
    test = TestCompress()
    test.test_compress()

if __name__ == '__main__':
    main()

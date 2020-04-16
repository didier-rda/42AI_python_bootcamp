"""
This module returns params values in reverse order with reverse case
Classes: None
Functions: reverse(text)
"""

import sys


def ft_reverse(text):
    """Return the reverse words with reversed case"""
    reverse_text = text[::-1]
    reverse_case = map(lambda l: l.upper() if l.isupper() else l.lower(), reverse_text)
    return ''.join(list(reverse_case))


if __name__ == '__main__':
    print(ft_reverse(' '.join(sys.argv[1:])))

from hypothesis import given, assume
import hypothesis.strategies as st

from hypothesis.settings import Settings

Settings.max_examples = 999999

@given(st.integers())
def two_is_bad(n):
    print n
    if n == 999:
        raise ReferenceError
    return n

if __name__ == '__main__':
    two_is_bad()

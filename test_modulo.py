"""
https://twitter.com/raymondh/status/617049150606028801
#python tip:  The modulo operation x % y gives a result with the same sign as y and with abs(result) < abs(y):
>>> 11 % 7
4
>>> 11 % -7
-3
"""
import math
from hypothesis import given, assume
import hypothesis.strategies as st

def same_sign(a, b):
    return (a * b) >= 0

@given(st.integers(), st.integers())
def test_int_mod_properties(x, y):
    # can't divide by 0
    assume(y != 0)

    result = x % y
    assert abs(result) < abs(y)
    assert same_sign(result, y)

@given(
    (st.integers() | st.floats()),
    (st.integers() | st.floats())
)
def test_int_float_mod_properties(x, y):
    # infinity can't be divided by anything
    assume(not math.isinf(x))
    # can't divide by 0
    assume(y != 0)
    # tiny x gives result that's equal not less than y
    # >>> (-1e-17 % 1.0) < 1.0
    # False
    assume(1e-15 < abs(x))
    # large y gives result that's equal not less than y
    # >>> abs(1 % -1e16) < abs(-1e16)
    # False
    assume(abs(y) < 1e15)

    result = x % y
    assert abs(result) < abs(y)
    assert same_sign(result, y)

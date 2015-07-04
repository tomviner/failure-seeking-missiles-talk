import pytest
import itertools
from hypothesis import given, assume
import hypothesis.strategies as st

import change_count

against_all_version = pytest.mark.parametrize('func', (
    pytest.mark.xfail(
        change_count.make_change_v1, reason='basic'),
    change_count.make_change_v2,
    change_count.make_change_v3
))

@against_all_version
@given(st.integers())
def test_type_returned(func, total):
    assume(0 <= total <= 999999)
    coins = func(total)
    assert isinstance(coins, list)

@against_all_version
@given(st.integers())
def test_sum(func, total):
    assume(0 <= total <= 999999)
    coins = func(total)
    assert sum(coins) == total

# amended from https://docs.python.org/2/library/itertools.html#recipes
def powerset(iterable, min_len):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(
        itertools.combinations(s, r)
        for r in range(min_len, len(s)+1))

# @against_all_version
func = change_count.make_change_v3
@given(st.integers())
def test_minimal_choice(total):
    assume(0 <= total <= 999)
    coins = func(total)
    for subset in powerset(coins, min_len=2):
        assert sum(subset) not in change_count.COINS

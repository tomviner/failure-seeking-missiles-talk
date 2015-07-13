from hypothesis import given
import hypothesis.strategies as st


def reverse(ls):
    return list(reversed(ls))

@given(
    st.lists(st.integers()),
    st.lists(st.integers()),
)
def test_reverse(xs, ys):
    """
    prop_revapp :: [Int] -> [Int] -> Bool
    prop_revapp xs ys = reverse (xs++ys) == reverse xs ++ reverse ys
    """
    print xs
    print ys
    print reverse(xs + ys) == reverse(xs) + reverse(ys)
    print
    assert reverse(xs + ys) == reverse(xs) + reverse(ys)


if __name__ == '__main__':
    # main = quickCheck prop_revapp
    test_reverse()

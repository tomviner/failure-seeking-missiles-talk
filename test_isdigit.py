# -*- coding: utf-8 -*-
# import itertools
import re
# import matplotlib
# matplotlib.use('Agg')

# import pylab as plt
# from matplotlib_venn import venn3, venn3_circles
# import pytest
from hypothesis import given, assume, find
import hypothesis.strategies as st
from hypothesis import Settings, Verbosity
from hypothesis.errors import NoSuchExample, Unsatisfiable


# @pytest.mark.skipif
# @given(st.text(), settings=Settings(max_examples=100099))
# def test_digit_int(s):
#     if s.isdigit():
#         int(s)

# @given(st.text(max_size=3), settings=Settings(max_examples=1000000099, verbosity=Verbosity.normal))
# def test_cast_regex(s):
#     assume(re.match(r'^-?\d+\Z', s))
#     try:
#         int(s.strip())
#     except (ValueError, TypeError):
#         # print(s)
#         pass
#     # else:

def isdigit(s):
    return s.isdigit()

def cast(s):
    try:
        int(s.strip())
    except (ValueError, TypeError):
        return False
    except:
        return False
    else:
        return True

def cast_blows_up(s):
    try:
        int(s)
    except (ValueError, TypeError):
        return False
    except:
        return True
    else:
        return False

def regex(s):
    return bool(re.match(r'^-?\d+\Z', s))

funcs = [isdigit, cast, regex]

def search(bs, vs):
    def cond(s):
        r0 = funcs[0](s)
        r1 = funcs[1](s)
        r2 = funcs[2](s)
        assume(r0 == bs[0])
        assume(r1 == bs[1])
        assume(s not in vs)
        return r2 == bs[2]

    try:
        return find(st.text(max_size=3), cond, settings=Settings(max_examples=1000))
    except (NoSuchExample, Unsatisfiable):
        return


# bs = [bs for bs in itertools.product(*3*((False, True),))]
bs = [map(str.isupper, tr) for tr in 'Abc, aBc, ABc, abC, AbC, aBC, ABC'.split(', ')]
print 'val\t', '\t'.join(f.__name__ for f in funcs)
args = []
vs = [u"६"]
for i in range(5):
    for b in bs:
        v = search(b, vs)
        # print(b, v)
        if v is None:
            print '-', '\t',
            print '\t'.join(map(str, b))
            args.append(0)
        else:
            print v or repr(v), '\t',
            vs.append(v)
            print '\t'.join(str(f(v)) for f in funcs)
            args.append(1)
        # else:

# venn = venn3(subsets=args)
# sets = [set(filter(lambda v: f(v), vs)) for f in funcs]
# venn = venn3(sets, [u', '.join(map(unicode, s)) for s in sets])
# plt.title("Sample Venn diagram")
# plt.plot([1,2,3])
# plt.show()
for f in funcs:
    print f.__name__
    for v in sorted(vs):
        if f(v):
            print v,
    print

# print cast_blows_up.__name__
# print find(st.text(max_size=1), cast_blows_up, settings=Settings(max_examples=1000909))
#
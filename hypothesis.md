# QuickCheck

From 1999
https://www.fpcomplete.com/user/pbv/an-introduction-to-quickcheck-testing

Imperative programming to a haskell person is like this:
![dognap][https://s3.amazonaws.com/lyah/dognap.png] ([src](http://learnyouahaskell.com/input-and-output))

From http://learnyouahaskell.com/input-and-output:

"In an imperative language, you have no guarantee that a simple function that should just crunch some numbers won't burn down your house, kidnap your dog and scratch your car with a potato while crunching those numbers.""

# Hypothosis

Pythonic implementation and update of QuickCheck

## Hypothesis

bidict
    basic:
        [code]
    advanced:
        Rule based state machines

how could this be working?
    formal proof - like a mathematical proof
        even in maths this is cutting edge
    so that leaves us: trying a load of examples

property based testing
    you specify a property of your code that must hold
    Hypothesis does its best to find a counterexample
    random = messy and hard to readthedocs
    shrinking

examples:
    change counting
    modulo tweet

components:
    strategy
        >>> import hypothesis.strategies as st
        >>> st.integers()
        RandomGeometricIntStrategy() | WideRangeIntStrategy()
        >>> st.floats()
        WrapperFloatStrategy(GaussianFloatStrategy() | BoundedFloatStrategy() | ExponentialFloatStrategy() | JustIntFloats() | SampledFromStrategy(
        (0.0, sys.float_info.min, -sys.float_info.min, -sys.float_info.max,
        sys.float_info.max,, inf, -inf, nan)) | FullRangeFloats())
        NastyFloats

    .example

how does it do it:
    templates:
        https://hypothesis.readthedocs.org/en/latest/internals.html
        pick interesting cases
    database of failing examples

Django

Reruns test many times
remembers failing cases
Dial down number of runs in dev
Django support

raymond tweet
forcing you to consider edge cases
    - valuable for security
    - consider browser security



## Conclusion

TOC? - smooth beginning

Take points from talk desc
    two approaches that have been around for a while have new libraries

Why more low level libs important for python
Preview afl to python
Don't repeat afl stuff (eg standard fuzzer)

Py.test runner hyp
Anecdote from Johnathon

Check wording / minimise

Advanced features
Not a silver bullets
Testing appropriate for your code eg django cats

Reread to do
push with notes off

Todo:

Python-AFL
Fuzzing JSON
Maze
    Depth of progression
    Filtered out
Add photo

Rest:

Choosing data, examples

feedback:

less haskell
AFL
    isn't Python
    specialises in security and binary formats
Notes were distracting me
Genetic Algorthm implies search and time
Agile Test Quadrant
Strategies as probability distributions

More jokes


todo:

randomesque
exhaustive
testing like your
thinking at the edges



old:

attention seeking missile
tidy intro

Sketch
can't draw a diagram of all the problems with *this* (funny photo)

model mommy: non-adversarial data. literally randint(-10000, 10000)


Why we test:
- work out what our code does
- ensure it doesn't do anything else
- define its properties
- ensure it meets its contracts
How we test:
- run the code
- manually interact



Scaling the random

- blind boxing
-

Testing with purely random data on it's own doesn't get you very far. But
two approaches that have been around for a while have new libraries that
help you generate random input, that homes in on failing testcases.


We don't let developers manually test, We hire QAs to manually test our code, why let them choose test inputs?
Softballing, unimaginitive, non-adversarial


Softball interview
Aggressive interview


Heat seeking missile (joke)



---

bidict
    basic:
        [code]
    advanced:
        Rule based state machines

examples:
    bidict
    change counting
    raymond modulo tweet


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



Django

Reruns test many times
remembers failing cases
Dial down number of runs in dev
Django support


forcing you to consider edge cases
    - valuable for security
    - consider browser security



code coverage - value coverage
choosing values to increase code coverage!
timeout (hangs), default 5*average

features:

    gnuplot
    dictionary of input keywords
    crash explorer
    minimise result

how it works:
    genetic algorithms

usage:
    stdin or filename
    fuzzing by script

sql bugs found

265 w:
    took 11 mins
    total execs: 3M (10^6)
    dumb search: 10^440
    http://manpages.ubuntu.com/manpages/hardy/man7/signal.7.html
    SIGFPE        8       Core    Floating point exception

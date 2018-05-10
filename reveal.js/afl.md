## American fuzzy lop (afl)

![afl-rabbit](images/rabbit.jpg)

- Michal Zalewski - 2014
- Written in C

Note: - bunny-the-fuzzer from 2007
- Specialises in security and binary formats
- Low level libs are essential to everything we do
- We'll get on to Python-AFL in a minute


## Fuzz Testing

- firing data at a program
- attempting to crash it
    - unhandled errors
    - memory leaks

Note: - Moving on from *property based testing*
- More about crashes than checking properties


## Workflow

- leave running (for days, weeks or more)
- speed very important

Note: - needs to cover a lot of ground

---

## Types of Fuzz Testing

- traditional "brute-force" e.g. *zzuf*
- feedback guided fuzzing i.e. *afl*


## Traditional fuzzing isn't dead

- *FFmpeg and a **thousand** fixes*
    - input media samples
    - simple mutation algorithms
    - 500-2000 cores over 2 years
- src: [google online security blog](http://googleonlinesecurity.blogspot.co.uk/2014/01/ffmpeg-and-thousand-fixes.html)

Note: - video processing lib
- wide used (Chrome, MPlayer, VLC)
- feedbackless fuzzing, just mutating sample data
- but with enough resourses can make great progress...


## Killer quote:

*Our personal feeling is between 10% and 20% of the problems could be considered easily exploitable security issues*

Note: - 100 to 200 zero-day exploits!

---

## AFL: traditional fuzzing
## + a special technique

- compile-time instrumentation
- drop-in replacement for gcc or clang

Note: - Speed
- Reliability
- Simplicity
- Traditional fuzzing techniques: input mutation strategies
- (next)
- maps out networks of code paths


## Usage:
<!-- . -->
    $ afl-gcc -o stdin_foo.afl stdin_foo.c

<!-- . -->
    $ afl-fuzz -i testcase_dir -o findings_dir ./stdin_foo.afl
<!-- -- class="fragment" -->

---

Running:

![afl-running](images/foo.png)

Note: - total paths / uniq crashes
- fuzzing strategy yields
- almost a million runs in 2.5 minutes


## impressive trophy case of bug discoveries

![afl-bugs](images/afl-bugs.png)

Note: - that's only about a quarter of them!

---

## How it works

- be a great traditional fuzzer
- search for inputs that span different code paths
- genetic algorithms for mashing examples together

---

## Python AFL

- Uses Cython
- Connects instrumentation to Python interpreter
    - sys.settrace
- Converts unhandled exceptions to SIGUSR1

<!-- . -->
    py-afl-fuzz -i in -o out -- python pafl_fuzz.py


### Fuzzing signature decoding

    import sys

    import afl

    from cryptography.hazmat.primitives.asymmetric.utils import (
        decode_rfc6979_signature
    )

    afl.start()

    try:
        decode_rfc6979_signature(sys.stdin.read())
    except ValueError:
        pass

From https://alexgaynor.net/2015/apr/13/introduction-to-fuzzing-in-python-with-afl/

Update: real issues found
https://github.com/pyca/cryptography/issues/1838

Note: - bugs found!


### Fuzzing layer 2 networking

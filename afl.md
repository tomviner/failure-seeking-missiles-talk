## Fuzz Testing

- firing data at a program
- attempting to crash it
    - unhandled errors
    - memory leaks

Note: - Moving on from *property based testing*
- Generic failures


## American fuzzy lop

![afl-rabbit](images/rabbit.jpg)
- By Michal Zalewski

Note: - bunny-the-fuzzer from 2007
- Released 2014
- Written in C


## Types of Fuzz Testing

- traditional "brute-force"
- AFL: feedback guided fuzzing

<!-- Note: -->


## Traditional fuzzing isn't dead

- *FFmpeg and a thousand fixes*
    - input media samples
    - simple mutation algorithms
    - 500-2000 cores over 2 years
- src: [google online security blog](http://googleonlinesecurity.blogspot.co.uk/2014/01/ffmpeg-and-thousand-fixes.html)

Note: - video processing lib
- wide used (Chrome, MPlayer, VLC)
- feedbackless fuzzing, just mutating sample data
- but with enough resourses can make great progress...


## Types of bugs found

- NULL pointer dereferences
- Invalid pointer arithmetic
- Out-of-bounds reads and writes
- Use of uninitialized memory
- Division errors
- Assertion failures

*Our personal feeling is between 10% and 20% of the problems could be considered easily exploitable security issues*

Note: - lots of memory mgmt bugs
    - self-managed for speed
- 100 to 200 zero-day exploits!


## AFL's secret

- compile-time instrumentation
- drop-in replacement for gcc or clang

<!-- . -->
    $ CC=/path/to/afl/afl-gcc ./configure
    $ make


## Toy example

Crash upon *foo!*

    char buf[100];
    read(0, buf, 100);

    if (buf[0] == 'f') {
      if (buf[1] == 'o') {
        if (buf[2] == 'o') {
          if (buf[3] == '!') {
            abort();
    }}}}


## Manual test of fail

    afl-gcc -o stdin_foo.afl stdin_foo.c

    $ echo "foo!" | ./stdin_foo.afl
    one
    two
    three
    four
    Aborted

Note: - no configure or make, just compile


Let's try it:

    afl-fuzz -i testcase_dir -o findings_dir ./stdin_foo.afl

Note: - really basic example in testcase_dir


Running:

![afl-running](images/foo.png)


code coverage - value coverage
choosing values to increase code coverage!
speed very important
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

## Fuzz Testing

- firing data at a program
- attempting to crash it
    - unhandled errors
    - memory leaks

Note: - Moving on from *property based testing*
- Generic failures


## Workflow

- leave running (for days or weeks)
- speed very important

Note: - needs to cover a lot of ground

---

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

---

## AFL's goals

- Speed
- Reliability
- Simplicity (little setup required)
- Traditional fuzzing techniques: input mutation strategies
- Plus...


## AFL's secret

- compile-time instrumentation
- drop-in replacement for gcc or clang

<!-- . -->
    $ CC=/path/to/afl/afl-gcc ./configure
    $ make

Note: - maps out networks of code paths

---

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

    # compile adding instrumentation
    $ afl-gcc -o stdin_foo.afl stdin_foo.c

    $ echo "foo!" | ./stdin_foo.afl
    one
    two
    three
    four
    Aborted

Note: - no configure or make, just compile


Let's try it:

    $ afl-fuzz -i testcase_dir -o findings_dir ./stdin_foo.afl

Note: - really basic example in testcase_dir
- stdin or filename
- use RAM disk if SSD


Running:

![afl-running](images/foo.png)

Note: - total paths / uniq crashes
- fuzzing strategy yields
- almost a million runs in 2.5 minutes


## Findings

`queue/`:
- `.`
- `fýç↡`
- `foý↡`
- `fooÿ`

`crashes/`:
- `foo!`

Note: numbered files


Filename:

    crashes/id:000000,sig:06,src:000003,op:arith8,pos:3,val:+34

- `sig:06`: SIGABRT (Abort signal)
- based on `queue/000003` (`fooÿ`)
- operation: 8-bit arithmetics
- position 3, value +34


## impressive trophy case of bug discoveries

![afl-bugs](images/afl-bugs.png)

Note: - that's only about a third of them!

---

<!-- http://lcamtuf.blogspot.co.uk/2015/04/finding-bugs-in-sqlite-easy-way.html -->
## Specific example: sql bugs found


## Approach

- dictionary of SQL keywords
    - `ALTER, SELECT, COLUMN` etc
- a single simple testcase:

<!-- . -->
    create table t1(one smallint);
    insert into t1 values(1);
    select * from t1;

---

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

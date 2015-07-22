Code from https://hg.python.org/cpython

    hg clone https://hg.python.org/cpython

Adapt instructions from https://docs.python.org/devguide/

(I couldn't see how to use afl-clang-fast)

    CC=path/to/afl-clang ./configure --with-pydebug && make -j2


path/to/afl-fuzz -i in -o out ./python fuzz_json.py

where fuzz_json.py is Jakub's script from above.

But I never get any new paths found, here's the strace from doing:

    strace -s 99999 -f -o log path/to/afl-fuzz -i in -o /run/shm/fuzz/current ./python fuzz_json.py

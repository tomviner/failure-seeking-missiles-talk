Code from https://hg.python.org/cpython

    hg clone https://hg.python.org/cpython

Adapt instructions from https://docs.python.org/devguide/

(I couldn't see how to use afl-clang-fast)

    CC=path/to/afl-clang ./configure --with-pydebug && make -j2


path/to/afl-fuzz -i in -o out ./python fuzz_json.py

where fuzz_json.py is Jakub's script from above.
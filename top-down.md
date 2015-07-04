## Intro

Why we test:
- work out what our code does
- ensure it doesn't do anything else
- define its properties
- ensure it meets its contracts

How we test:
- run the code
- manually interact
- unittest by passing in hardcoded values
- unittest by firing a failure seeking missile???

Bug space
- Map of all the different types of bugs
- Thorough testing (over the whole dev life cycle) is about reaching as many parts of bugspace as possible
- Risk of over testing certain parts of bug space, and under testing others e.g.
    - testing text inputs with ascii instead of unicode
    - passing low positive integers, when large / negative / floats would find extra bugs

Schetch
can't draw a diagram of all the problems with *this* (funny photo)

Reproducibility
- Pro: consistent pass or fail
- Con: find more bugs!
- Legitimate debate


Testing with purely random data on it's own doesn't get you very far. But
two approaches that have been around for a while have new libraries that
help you generate random input, that homes in on failing testcases.

## Hypothesis

## American fuzzy lop

## Conclusion

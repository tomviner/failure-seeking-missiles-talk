## Testing with two failure seeking missiles:
## fuzzing and
## property based testing
##### A EuroPython 2015 Talk by @tomviner

---

I'm here to challenge how you test your code


Audience starting point?
- done unittesting / integration testing / end-to-end
- but always with hard coded values?

Note: - who's only used hard coded values?
- who's used some form of random data


I ask you:
- are you testing your code hard enough?
- stretching it?
- asking it questions it wasn't expecting?
- are you a softball interviewer?


## Coverage
- code coverage
    - line
    - branch
- value coverage?


Why we test:
- work out what our code does
- ensure it doesn't do anything else
- define its properties
- ensure it meets its contracts


How we test:
- run the code
- manually interact
- test by passing in hardcoded values
- test by firing a failure seeking missile???

[missile image]


## Bug space
- Map of all the different types of bugs
- Thorough testing (over the whole dev life cycle) is about reaching as many parts of bugspace as possible
- Risk of over testing certain parts of bugspace, and under testing others e.g.
    - testing text inputs with ascii instead of unicode
    - passing low positive integers, when large / negative / floats would find extra bugs


Sketch
can't draw a diagram of all the problems with *this* (funny photo)


model mommy: non-adversarial data. literally randint(-10000, 10000)


Testing with purely random data on it's own doesn't get you very far. But
two approaches that have been around for a while have new libraries that
help you generate random input, that homes in on failing testcases.


We don't let developers manually test, why let them choose test inputs?
Softballing, unimaginitive, non-adversarial


Softball interview
Aggressive interview


Heat seeking missile (joke)

## Testing with two failure seeking missiles:
## fuzzing and
## property based testing
##### A EuroPython 2015 Talk by @tomviner

---

I'm here to challenge how you test your code


Audience starting point?
- you've written tests...
- but always with hard coded example values?

Note: - who's only used hard coded values?
- who's used some form of random data


I ask you:
- are you testing your code hard enough?

Note: - stretching it?
- asking it questions it wasn't expecting?
- are you an aggressive interviewer?
- or are you a softball interviewer who asks easy questions?


## Coverage
- code coverage
    - line
    - branch
    - loop counts
- value coverage?
<!-- -- class="fragment" -->


## Input space

![graph](images/graph.jpg)
- Map of all possible inputs
- All data related bugs have a point on here

Note: - which type of points do you pick when testing?
- where would adversarial approach take you?


## Artist's reconstruction of edge cases
![shamrock](images/shamrock.png)

Note: - reaching as many parts of input space as possible
- over testing simple cases
- under testing
    - ascii instead of unicode
    - empty list / strings
    - passing low positive integers, when large / negative / floats would find extra bugs


## So how to create test data?

- hand write hardcoded values
<!-- -- class="fragment" -->
- import random or model_mommy
<!-- -- class="fragment" -->
- OR... by firing a failure seeking missile???
<!-- -- class="fragment" -->
![missile](images/missile.jpg)
<!-- -- class="fragment" -->

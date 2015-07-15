## Interesting questions raised


## Reproducibility / non-deterministic
- Pro: consistent pass or fail
<!-- -- class="fragment" -->
- Con: find more bugs!
<!-- -- class="fragment" -->
- Find failing cases and add them to your deterministic test pack
<!-- -- class="fragment" -->


### Getting the balance right
- unittests should be fast but with adversarial data
<!-- -- class="fragment" -->
- purely random data is too naive, makes shallow progress
<!-- -- class="fragment" -->
- but exhaustively enumerating possibilities takes too long
<!-- -- class="fragment" -->
- mutate too conservatively: less novel outcomes
<!-- -- class="fragment" -->
- use the tools available like Hypothesis and AFL to find more bugs
<!-- -- class="fragment" -->


## In Conclusion

We've seen two styles of coming up with test data today

- Humans are bad at picking random examples
<!-- -- class="fragment" -->
- Developers are bad at being adversarial
<!-- -- class="fragment" -->
- Computers are fast, let them play (break) your code
<!-- -- class="fragment" -->
- Find the bugs before your customer/secret service does
<!-- -- class="fragment" -->


## Let me end by saying

Note: - Don't interrogate your code like it's a cat stuck up a tree...
- Fire a guided missile, blow the fucking tree up and clear up the mess!


![ray-hyp](images/ray-hyp.png)


Other talks you may find interesting:
- Hypothesis talk by someone else


Thanks to my company for sponsoring my conference trip!
![hogarth-logo](images/hogarth-logo.png)

## Any questions?

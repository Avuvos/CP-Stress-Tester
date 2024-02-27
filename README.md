# Competitive-Programming-Stress-Tester
Stress Tester for Competitive Programming

# Instructions
- put the correct (but slow) brute force solution on ``brute_sol``
- put the optimal (but wrong) solution on ``optimal_sol``
- go to the ``testcase_generator`` and print the testcases according to the question
- on your terminal run ``./tester.sh 20`` for example to run 20 testcases

# Example
Imagine the following simple and silly problem: <br>
Given some ``n``, print ``n`` if ``n <= 20`` and otherwise print ``-1``. <br>
If for example our wrong code always outputs ``n`` no matter what, this is what will happen: <br>
<br>
![image](https://github.com/Avuvos/CP-Stress-Tester/assets/92464368/723615c5-129a-41e4-ab67-6f7be2e7c0c2)
<br>
<br>
However if everything is working correctly, it will always look like this: <br>
![image](https://github.com/Avuvos/CP-Stress-Tester/assets/92464368/04c8a22b-60d1-463a-accc-0329e4972e5d)


# nose-random

`nose-random` is designed to facilitate "Monte-Carlo style" unit testing. The idea is that instead of running your tests with only one input set, or against an explicitly defined list of input sets, you use a random number generator to generate a larger number of input scenarios and run the test on each of those input scenarios. This means you test your code against a wider range of possible inputs.

Adding randomness potentially leads to the disadvantage tests fail or succeed randomly, i.e. non-reproducibly, which means it's harder to
* know if you've fixed a failing test
* know if an test fails only on some machines or configurations and not others
* debug a failing test

`nose-random` avoids these problems because it 
* uses a fixed seed so that each test run is identical
* tells you which scenario caused a test to fail
* lets you to run the test only on a specific scenario to facilitate debugging

## Installation

    pip install git+https://github.com/ZoomerAnalytics/nose-random.git
    
or clone the repo and run `python setup.py install`.
    
## Usage


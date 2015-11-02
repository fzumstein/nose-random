import unittest

from nose_random import randomize

class RandomTestCase(unittest.TestCase):
    
    def generate_scenario(self, rng):
        return rng.random(), 10 * rng.random()
        
    @randomize(1000, generate_scenario)
    def failing_test(self, scenario):
        x, y = scenario
        self.assertLess(x, y)

    @randomize(1000, generate_scenario)
    def passing_test(self, scenario):
        x, y = scenario
        self.assertLess(x, y + 1)
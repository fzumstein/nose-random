__version__ = '0.0.1'

from nose.plugins import Plugin
import os


seed = None


class NoseRandomPlugin(Plugin):
    def options(self, parser, env=os.environ):
        parser.add_option('--scenario', type='int',
                          dest='scenario',
                          help="Specify the scenario seed for debugging random tests.")

    def configure(self, options, conf):
        global seed
        seed = getattr(options, 'scenario', None)



def randomize(n, scenario_generator, seed=12038728732):
    def decorator(test):
        def randomized_test(self):
            from random import Random
            import nose_random
            nseeds = n
            if nose_random.seed is not None:
                nseeds = 1
                seeds = [nose_random.seed]
            else:
                rng_seed = Random(seed)
                nseeds = n
                seeds = (rng_seed.getrandbits(32) for i in range(n))
            for i, rseed in enumerate(seeds):
                rng = Random(rseed)
                scenario = scenario_generator(self, rng)
                try:
                    test(self, scenario)
                except Exception as e:
                    import sys
                    raise type(e), type(e)('%s with scenario %i (%i of %i)' % (e.message, rseed, i+1, nseeds)), sys.exc_info()[2]
        return randomized_test
    return decorator
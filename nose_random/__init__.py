__version__ = '0.0.1'

from nose.plugins import Plugin
import os

from random import Random


_missing = object()


class NoseRandomConfig(object):
    def __init__(self):
        self.is_nose_plugin = False
        self._scenario = _missing

    @property
    def scenario(self):
        if self._scenario is _missing:
            import sys
            for arg in sys.argv:
                if arg.startswith('--scenario='):
                    self._scenario = arg[len('--scenario='):]
        return self._scenario

    @scenario.setter
    def scenario(self, value):
        self._scenario = value


config = NoseRandomConfig()


class NoseRandomPlugin(Plugin):
    def options(self, parser, env=os.environ):
        parser.add_option('--scenario', type='str',
                          dest='scenario',
                          help="Specify the scenario seed for debugging random tests.")

    def configure(self, options, conf):
        config.scenario = getattr(options, 'scenario', None)


def _generate_tag(n, rng):
    return ''.join(rng.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(n))


def randomize(n, scenario_generator, seed=12038728732):
    def decorator(test):
        def randomized_test(self):
            if config.scenario is not None:
                nseeds = 1
                seeds = [config.scenario]
            else:
                rng_seed = Random(seed)
                nseeds = n
                seeds = (_generate_tag(12, rng_seed) for i in range(n)) # (rng_seed.getrandbits(32) for i in range(n))
            for i, rseed in enumerate(seeds):
                rng = Random(rseed)
                scenario = scenario_generator(self, rng)
                try:
                    test(self, scenario)
                except Exception as e:
                    import sys
                    raise type(e), type(e)('%s with scenario %s (%i of %i)' % (e.message, rseed, i+1, nseeds)), sys.exc_info()[2]
        return randomized_test
    return decorator
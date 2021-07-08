import ctypes as ct
import os
import unittest
import pystable

LIBSTABLE_PATH = 'libstable/stable/libs/libstable.so'


class TestPystable(unittest.TestCase):

    def setUp(self):
        self.lib = pystable.load_libstable(self.libpath())

    def libpath(self) -> str:
        path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.abspath(os.path.join(path, os.pardir))
        return os.path.abspath(os.path.join(path, LIBSTABLE_PATH))

    def test_version(self):
        assert pystable.__version__ == '0.1.0'

    def test_load_libstable(self):
        path = self.libpath()
        lib = pystable.load_libstable(path)
        self.assertIsInstance(lib, ct.CDLL)

    def test_stable_dist_struct(self):
        pass

    def test_wrap_function(self):
        pass

    def test_c_stable_create(self):
        pass

    def test_stable_create(self):
        dist_params = {
                'alpha': 1.3278285879842862,
                'beta': 0.0816835526225623,
                'mu': -0.0000252748167384907,  # loc
                'sigma': 0.0006409442772706084,  # scale
                'parameterization': 1,
            }
        actual = pystable.stable_create(self.lib, dist_params)
        try:
            actual = {
                    'alpha': actual.contents.alpha,
                    'beta': actual.contents.beta,
                    'sigma': actual.contents.sigma,
                    'mu_0': actual.contents.mu_0,
                    'mu_1': actual.contents.mu_1
                }

        except Exception:
            print("ERROR")

        expected = {
                'alpha': 1.3278285879842862,
                'beta': 0.0816835526225623,
                'sigma': 0.0006409442772706084,
                'mu_0': -0.00011779403879895914,
                'mu_1': -2.52748167384907e-05
            }

        self.assertDictEqual(actual, expected)

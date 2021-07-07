import ctypes as ct
import os
import unittest
import pystable

LIBSTABLE_PATH = 'libstable/stable/libs/libstable.so'


class TestPystable(unittest.TestCase):

    def get_lib(self) -> str:
        path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.abspath(os.path.join(path, os.pardir))
        return os.path.abspath(os.path.join(path, LIBSTABLE_PATH))

    def test_version(self):
        assert pystable.__version__ == '0.1.0'

    def test_load_libstable(self):
        path = self.get_lib()
        lib = pystable.load_libstable(path)
        self.assertIsInstance(lib, ct.CDLL)

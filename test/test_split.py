import logging
import unittest
import os
import glob

from gpx_split.split import Splitter
from gpx_split.writer import Writer

OUT = 'test/out/'
FILE = 'test.gpx'

class TestSplitter(unittest.TestCase):

    def __path(self, name):
        f = 'test/resources/' + name
        return os.path.realpath(f)

    def __files(self):
        return glob.glob(OUT + '*')

    def setUp(self):
        writer = Writer(OUT)
        self.splitter = Splitter(writer)
        self.splitter.logger.setLevel(logging.DEBUG)

    def tearDown(self):
        for f in self.__files():
            os.remove(f)

    def test_split_into_one(self):
        self.splitter.split(self.__path(FILE))
        self.assertEqual(1, len(self.__files()))

    def test_split_into_two(self):
        self.splitter.split(self.__path(FILE), 30)
        self.assertEqual(2, len(self.__files()))


if __name__ == '__main__':
    unittest.main()
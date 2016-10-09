import tict
import unittest


class BaseTests(unittest.TestCase):
    def setUp(self):
        self.t = tict.TictDict()

    def test_stop_key_error(self):
        with self.assertRaises(KeyError) as context:
            self.t.stop('foobar')

    def test_start(self):
        self.t.start('foobar')
        self.assertTrue('foobar' in self.t)

    def test_no_key_start(self):
        key = self.t.start()
        self.assertTrue(key in self.t)

    def test_total_time(self):
        self.t.start('foobar')
        self.t.stop('foobar')
        self.assertTrue(self.t['foobar'] != None)

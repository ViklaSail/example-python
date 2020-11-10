import unittest

import awesome
import example_pkg


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(awesome.smile(), ":)")
  
    def test_anotherOne(self):
        foores = example_pkg.foo_func()
        barres = example_pkg.bar_func()
        bazres = example_pkg.baz_func()
        self.assertRegexpMatches(barres,".*bar.*")


if __name__ == '__main__':
    unittest.main()

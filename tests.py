import unittest

import awesome
import example_pkg
import pipeLine

 url = 'http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json'

class TestMethods(unittest.TestCase):
    def test_add(self):
        # call to function changing some "global" data structure 
        # assert function is checking that the change you expected happens properly. 
        self.assertEqual(awesome.smile(), ":)")
  
    def test_anotherOne(self):
        foores = example_pkg.foo_func()
        barres = example_pkg.bar_func()
        bazres = example_pkg.baz_func()
        self.assertRegexpMatches(barres,".*bar.*")

    def test_pipeline(self):
        result = pipeLine.getData(url)
        self.assertRegexpMatches(barres,".*bar.*")


if __name__ == '__main__':
    unittest.main()

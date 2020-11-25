import unittest
from mock import patch

import awesome
# import example_pkg
# 12.1.2020 something close to functional programming
# map, reduce and filter operations
# https://stackoverflow.com/questions/31127824/what-are-pythons-equivalent-of-javascripts-reduce-map-and-filter
# for dataframe there is this functionality build in 
# DataFrame.apply, DataFrame.applymap
# datasets for cleaning exercises: https://makingnoiseandhearingthings.com/2018/04/19/datasets-for-data-cleaning-practice/
# 11.1.2020 utest and related. 
# from app.mocking import test_method
# for mocking to work you need to import the function to be tested to the same namespace with unit tests!!!
# this is wy below from-sentences  are made.
# that is my understanding, untested.
from example_pkg import laughingChain
from example_pkg import laughingChainPara
from example_pkg import funcSameNameSpace
# if testing a function in the same namespace, it does not work!!! trying to find solution...
# https://stackoverflow.com/questions/46464947/python-function-not-using-the-mocked-object
# possible solution maybe here https://docs.python.org/3/library/unittest.mock.html#where-to-patch
from example_pkg import foo_func
from example_pkg import bar_func

# import pipeLine

url = 'http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json'

class TestMethods(unittest.TestCase):
    def test_add(self):
        # call to function changing some "global" data structure 
        # assert function is checking that the change you expected happens properly. 
        self.assertEqual(awesome.smile(), ":)")
  
    def test_anotherOne(self):
        barres = bar_func()
        self.assertRegexpMatches(barres,".*bar.*")
    
    #def test_pipeline(self):
    #    result = pipeLine.getData(url)
    #    self.assertRegexpMatches(result,".*bar.*")

    def test_laugh(self):
        reslau = awesome.laughing()
        self.assertEqual(reslau, ":D")

    # function to be mocked in patch macro
    # seems to be so that patched function can not be in the same namespace (package) as the one calling it. 
    @patch('awesome.laughing')
    def test_modulefunction(self,test_patch):
        test_patch.return_value = 1
        result = laughingChain()
        self.assertEqual(result,2)

    @patch('awesome.laughingPara')
    def test_parameterfunc(self, test_para):
        test_para.return_value = "HUI"
        result  = laughingChainPara()
        self.assertEqual(result,"testausta")

    @patch('example_pkg.foo_func')
    def test_samemodule(self, test_para):
        test_para.return_value = "SAME NAMESPACE"
        result  = funcSameNameSpace()
        self.assertEqual(result,"testausta")

    def test_playdata(self):
        #https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas first version
        # 
        from functools import reduce
        import pandas as pd
        import numpy as np
        df = pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 110, 120]})
        for index, row in df.iterrows():
            print(row['c1'], row['c2'])

if __name__ == '__main__':
    unittest.main()

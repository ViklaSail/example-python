import unittest
from mock import patch

import awesome
from example_pkg import laughingChain
from example_pkg import laughingChainPara
from example_pkg import funcSameNameSpace
# if patching a function in the same package, mocking/patching does not work!!! You will have to test the whole function chain
# https://stackoverflow.com/questions/46464947/python-function-not-using-the-mocked-object
# possible solution maybe here https://docs.python.org/3/library/unittest.mock.html#where-to-patch
from example_pkg import foo_func
from example_pkg import bar_func
from dataTransforming import transformationForData
from dataTransforming import transformationTestingWithApply
from dataTransforming import transformFoo

from functools import reduce
import pandas as pd
import numpy as np

url = 'http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json'

class TestMethods_live(unittest.TestCase):
    def test_transformation(self):
        # call to function changing some "global" data structure 
        # assert function is checking that the change you expected happens properly. 
        result = transformFoo()
        self.assertEqual("foo", result)
        self.assertEqual(awesome.smile(), ":)")

    def test_assertion_1(self):
        # call to function changing some "global" data structure 
        # assert function is checking that the change you expected happens properly. 
        self.assertEqual(awesome.smile(), ":)")
  
    def test_assertion_2(self):
        barres = bar_func()
        self.assertRegexpMatches(barres,".*bar.*")


    def test_assertion_3(self):
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
        self.assertEqual(result,"testing")

    @patch('example_pkg.foo_func')
    def test_samemodule(self, test_para):
        test_para.return_value = "SAME NAMESPACE"
        result  = funcSameNameSpace()
        self.assertEqual(result,"testing")

    def test_framingApply(self):
        #https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas first version
        df = pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 110, 120]})
        for row in df.iterrows():
            print(row['c1'], row['c2'])
        
        df.apply(transformationForData, axis=0, raw=False, result_type=None, args=())
        #DataFrame.apply(func, axis=0, raw=False, result_type=None, args=(), **kwds)

    def test_exploringFunctionChain(self):
        # preparing data for exploring
        df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
        # exploring
        print(df)
        print(df.apply(np.sqrt))
        print("after sqrt, apply-function returns changed copy of the dataFrame")
        print("testing imported function")
        print(df.apply(transformationTestingWithApply))
        print("after apply")


if __name__ == '__main__':
    unittest.main()

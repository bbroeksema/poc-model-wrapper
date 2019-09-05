import unittest
import pandas as pd

from modelwrapper import model

class TestModelMethods(unittest.TestCase):

    def test_predict(self):
        df = pd.DataFrame([
            {'x1':  1 }, 
            {'x1':  2 }, 
            {'x1':  3 }, 
            {'x1':  4 }, 
            {'x1':  5 }, 
            {'x1':  6 }, 
            {'x1':  7 }, 
            {'x1':  8 }, 
            {'x1':  9 },
            {'x1': 10 }
         ])
        
        model.load()
        model.predict(df)
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()

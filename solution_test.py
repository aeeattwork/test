#!/usr/bin/python3
import solution
import unittest

class Testsolution(unittest.TestCase):
    def test_unique_values(self):
        popu,matches,unique_values = solution.controller()
        all_values = []
        no_duplicates = False
        for u in unique_values:
            for el in u:
                all_values.append(el)
        if (len(all_values) == len(set(all_values))):
            no_duplicates = True
        self.assertTrue(no_duplicates)
 
 
if __name__ == '__main__':
    unittest.main()

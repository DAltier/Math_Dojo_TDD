class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums) :
        self.result += num
        for var in nums :
            self.result += var
        return self
    def subtract(self, num, *nums) :
        self.result -= num
        for var in nums :
            self.result -= var
        return self

import unittest

class mathTests(unittest.TestCase) :
    def setUp(self):
        self.md = MathDojo() #creating MathDojo object

    def testAdd(self) :
        self.assertEqual(self.md.add(2,5,1,7).result, 15)

    def testSubtract(self) :
        self.assertEqual(self.md.subtract(7,2,5).result, -14)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
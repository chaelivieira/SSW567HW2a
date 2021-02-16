# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(5,4,3),'Right','5,4,3 is a Right triangle')
        
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self): 
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral','2,2,2 should be equilateral')

    def testIsocelesA(self): 
        self.assertEqual(classifyTriangle(1,2,2),'Isoceles','1,2,2 should be isoceles')

    def testIsocelesB(self): 
        self.assertEqual(classifyTriangle(2,2,1),'Isoceles','2,2,1 should be isoceles')

    def testIsocelesC(self): 
        self.assertEqual(classifyTriangle(3,2,2),'Isoceles','3,2,2 should be isoceles')

    def testNotATriangleA(self): 
        self.assertEqual(classifyTriangle(1,2,1),'NotATriangle','1,2,1 should be NotATriangle')
    
    def testNotATriangleB(self): 
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','1,2,3 should be NotATriangle')

    def testNotATriangleC(self): 
        self.assertEqual(classifyTriangle(10,20,30),'NotATriangle','10,20,30 should be NotATriangle')
    
    def testScaleneA(self): 
        self.assertEqual(classifyTriangle(7,9,8),'Scalene','7,9,8 should be scalene')

    def testScaleneB(self): 
        self.assertEqual(classifyTriangle(7,8,9),'Scalene','7,8,9 should be scalene')

    def testScaleneC(self): 
        self.assertEqual(classifyTriangle(9,8,7),'Scalene','9,8,7 should be scalene')

    def testBadInputA(self): 
        self.assertEqual(classifyTriangle("a","a","a"),'InvalidInput','a,a,a should be InvalidInput')
    
    def testBadInputB(self): 
        self.assertEqual(classifyTriangle(-1,-1,-1),'InvalidInput','-1,-1,-1 should be InvalidInput')
    
    def testBadInputC(self): 
        self.assertEqual(classifyTriangle(200,201,200),'InvalidInput','200,201,200 should be InvalidInput')

    def testBadInputD(self): 
        self.assertEqual(classifyTriangle(100,"a",100),'InvalidInput','100,a,100 should be InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    
    print (classifyTriangle(3,4,5))
    print (classifyTriangle(5,3,4))
    print (classifyTriangle(5,4,3))
    print (classifyTriangle(1,1,1))
    print (classifyTriangle(2,2,2))
    print (classifyTriangle(1,2,2))
    print (classifyTriangle(2,2,1))
    print (classifyTriangle(3,2,2))
    print (classifyTriangle(1,2,1))
    print (classifyTriangle(1,2,3))
    print (classifyTriangle(10,20,30))
    print (classifyTriangle(7,9,8))
    print (classifyTriangle(7,8,9))
    print (classifyTriangle(9,8,7))
    print (classifyTriangle("a","a","a"))
    print (classifyTriangle(-1,-1,-1))
    print (classifyTriangle(200,201,200))
    print (classifyTriangle(100,"a",100))
    unittest.main()


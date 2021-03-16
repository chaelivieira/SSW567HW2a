# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle
from math import sqrt

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    """
    Testing classify_triangle
    """

    def test_right_triangle_a(self):
        self.assertEqual(classify_triangle(3,4,5),'Right Scalene','3,4,5 is a Right triangle')

    def test_right_triangle_b(self):
        self.assertEqual(classify_triangle(5,3,4),'Right Scalene','5,3,4 is a Right triangle')

    def test_right_triangle_c(self):
        self.assertEqual(classify_triangle(5,4,3),'Right Scalene','5,4,3 is a Right triangle')

    def test_right_triangle_d(self):
        self.assertEqual(classify_triangle(8,8,sqrt(128)),'Right Isoceles','8,8,11.313 : Right triangle')

    def test_equilateral_triangles_a(self):
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def test_equilateral_triangles_b(self):
        self.assertEqual(classify_triangle(2,2,2),'Equilateral','2,2,2 should be equilateral')

    def test_isoceles_a(self):
        self.assertEqual(classify_triangle(1,2,2),'Isoceles','1,2,2 should be isoceles')

    def test_isoceles_b(self):
        self.assertEqual(classify_triangle(2,2,1),'Isoceles','2,2,1 should be isoceles')

    def test_isoceles_c(self):
        self.assertEqual(classify_triangle(3,2,2),'Isoceles','3,2,2 should be isoceles')

    def test_not_a_triangle_a(self):
        self.assertEqual(classify_triangle(1,2,1),'NotATriangle','1,2,1 should be NotATriangle')

    def test_not_a_triangle_b(self):
        self.assertEqual(classify_triangle(1,2,3),'NotATriangle','1,2,3 should be NotATriangle')

    def test_not_a_triangle_c(self):
        self.assertEqual(classify_triangle(10,20,30),'NotATriangle','10,20,30 : NotATriangle')

    def test_scalene_a(self):
        self.assertEqual(classify_triangle(7,9,8),'Scalene','7,9,8 should be scalene')

    def test_scalene_b(self):
        self.assertEqual(classify_triangle(7,8,9),'Scalene','7,8,9 should be scalene')

    def test_scalene_c(self):
        self.assertEqual(classify_triangle(9,8,7),'Scalene','9,8,7 should be scalene')

    def test_bad_input_a(self):
        self.assertEqual(classify_triangle("a","a","a"),'InvalidInput','a,a,a : InvalidInput')

    def test_bad_input_b(self):
        self.assertEqual(classify_triangle(-1,-1,-1),'InvalidInput','-1,-1,-1 : InvalidInput')

    def test_bad_input_c(self):
        self.assertEqual(classify_triangle(200,201,200),'InvalidInput','200,201,200 : InvalidInput')

    def test_bad_input_d(self):
        self.assertEqual(classify_triangle(100,"a",100),'InvalidInput','100,a,100 : InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
    
import data
import lab5
import unittest
from data import (Time)
from data import Point

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.


    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add(self):
        time1 = Time(5, 55, 10)
        time2 = Time(6, 10, 59)
        result = lab5.time_add(time1, time2)
        expected = Time(12, 6, 9)
        self.assertEqual(expected, result)

    def test_time_add(self):
        time1 = Time(5, 15,3)
        time2 = Time(6, 10, 2)
        result = lab5.time_add(time1, time2)
        expected = Time(11, 25, 5)
        self.assertEqual(expected, result)

    # Part 4
    def test_is_descending(self):
        list1 = [5,1,10,9,15]
        list_descending = lab5.is_descending(list1)
        expected = True
        self.assertEqual(expected, list_descending)

    def test_is_descending(self):
        list2 = [5,4,3,10,100]
        list_descending = lab5.is_descending(list2)
        expected = True
        self.assertEqual(expected, list_descending)

    # Part 5
    def test_largest_between(self):
        list1 = [5, 3, 10, 21, 0]
        result = lab5.largest_between(list1, 0, 4)
        expected = 3
        self.assertEqual(expected, result)


    def test_largest_between(self):
        list1 = [1, 5, 10, 2, 10]
        result = lab5.largest_between(list1, 0, 10)
        expected = 2
        self.assertEqual(expected, result)




    # Part 6
    def test_furthest_from_origin(self):
        list1 = [Point(9,10), Point(1,1), Point(2,7), Point(0,0)]
        result = lab5.furthest_from_origin(list1)
        expected = 0
        self.assertEqual(expected, result)

    def test_furthest_from_origin(self):
        list1 = []
        result = lab5.furthest_from_origin(list1)
        expected = None
        self.assertEqual(expected, result)






if __name__ == '__main__':
    unittest.main()

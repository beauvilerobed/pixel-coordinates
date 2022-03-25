from django.test import TestCase
from django.http import QueryDict
import numpy as np
from app.views import is_valid
from calc_pixel.calculate import get_coordinates, get_points


class UserInputValidation(TestCase):
    """ Test module for validating user input """

    def test_is_valid(self):
        query1 = QueryDict('tocken=hello&=(1,2)&secondcoord=(1,2)&thirdcoord=(1,2)&fourthcoord=(1,2)&height=1&width=1')
        query2 = QueryDict('tocken=hello&=&secondcoord=(1,2)&thirdcoord=(1,2)&fourthcoord=(1,2)&height=1&width=1')
        query3 = QueryDict('tocken=hello&=(1  ,  2)&secondcoord=(1.   ,2)&thirdcoord=(  1,  2 )&fourthcoord=(  1,2)&height=1.0&width=2.1')
        query4 = QueryDict('tocken=hello&=(... 1,2)&secondcoord=(1,2)&thirdcoord=(1,2)&fourthcoord=(1,2)&height=1&width=1')
        query5 = QueryDict('tocken=hello&=(1,2)&secondcoord=(1,2)&thirdcoord=(1,2)&fourthcoord=(1,2)&height=(1,2)&width=1')

        self.assertEqual(is_valid(query1), True)
        self.assertEqual(is_valid(query2), False)
        self.assertEqual(is_valid(query3), False)
        self.assertEqual(is_valid(query4), False)
        self.assertEqual(is_valid(query5), False)


class Calculate(TestCase):
    """ Test module for calculation functionality """

    def test_get_points(self):
        input = [
            (1.0, 3.0), (3.0, 3.0),
            (1.0, 1.0), (3.0, 1.0)
        ]

        input2 = [
            (1.0, 1.0), (3.0, 3.0),
            (1.0, 3.0), (3.0, 1.0)
        ]

        expected = np.array([
            [1.0, 3.0], [3.0, 1.0]
        ])

        expected2 = np.array([
            [1.0, 1.0], [3.0, 3.0]
        ])

        actual = get_points(input)
        actual2 = get_points(input2)

        self.assertTrue(np.alltrue(expected == actual))
        self.assertTrue(np.alltrue(expected2 == actual2))


    def test_get_coordinates(self):
        input = QueryDict('tocken=hello&=(1,1)&secondcoord=(3,1)&thirdcoord=(1,3)&fourthcoord=(3,3)&height=3&width=3')
        solution = [
            [[1.0, 3.0], [2.0, 3.0], [3.0, 3.0]],
            [[1.0, 2.0], [2.0, 2.0], [3.0, 2.0]],
            [[1.0, 1.0], [2.0, 1.0], [3.0, 1.0]]
        ]
        actual = np.array(get_coordinates(input))
        expected = np.array(solution)
        self.assertTrue(np.alltrue(expected == actual))


        input2 = QueryDict('tocken=hello&=(1,1)&secondcoord=(3,1)&thirdcoord=(1,3)&fourthcoord=(3,3)&height=3&width=3')
        solution2 = [
            [[1.0, 3.0], [3.0, 3.0], [3.0, 3.0]],
            [[1.0, 2.0], [2.0, 2.0], [3.0, 2.0]],
            [[1.0, 1.0], [2.0, 1.0], [3.0, 1.0]]
        ]
        actual = np.array(get_coordinates(input2))
        expected = np.array(solution2)
        self.assertFalse(np.alltrue(expected == actual))

        input3 = QueryDict('tocken=hello&=(1,1)&secondcoord=(0,0)&thirdcoord=(1,0)&fourthcoord=(0,1)&height=3&width=2')
        solution3 = [
            [[1.0, 0.0], [1.0, 1.0]],
            [[0.5, 0.0], [0.5, 1.0]],
            [[0.0, 0.0], [0.0, 1.0]]
        ]
        actual = np.array(get_coordinates(input3))
        expected = np.array(solution3)
        self.assertFalse(np.alltrue(expected == actual))
    
        input4 = QueryDict('tocken=hello&=(0,0)&secondcoord=(1,1)&thirdcoord=(1,0)&fourthcoord=(0,1)&height=3&width=2')
        solution4 = [
            [[1.0, 0.0], [1.0, 1.0]],
            [[0.5, 0.0], [0.5, 1.0]],
            [[0.0, 0.0], [0.0, 1.0]]
        ]
        actual = np.array(get_coordinates(input4))
        expected = np.array(solution4)
        self.assertFalse(np.alltrue(expected == actual))
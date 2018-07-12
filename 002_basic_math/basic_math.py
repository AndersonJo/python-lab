# -*- coding:utf-8 -*-


import yourtest
import unittest


class BasicBoolean(unittest.TestCase):
    """
    기본적인 산수
    """
    def test_machine_check(self):
        """
        두수의 합을 구하는 함수를 만들자
        """
        self.assertEqual(2, yourtest.plus(1, 1))
        self.assertEqual(6, yourtest.plus(2, 4))
        self.assertEqual(1, yourtest.plus(0, 1))
        self.assertEqual(0, yourtest.plus(0, 0))
        self.assertEqual(0, yourtest.plus(-1, 1))
        self.assertEqual(9, yourtest.plus(-31, 40))
        self.assertEqual(6.2, yourtest.plus(2.0, 4.2))
    
    def test_square(self):
        """
        제곱을 하는 함수를 만들자
        첫번째는 숫자, 두번째는 제곱근
        """
        self.assertEqual(1, yourtest.square(1))
        self.assertEqual(4, yourtest.square(2))
        self.assertEqual(0, yourtest.square(0))
        self.assertEqual(10000, yourtest.square(100))
        self.assertEqual(361, yourtest.square(19))
        self.assertEqual(16, yourtest.square(-4))
    
    def test_cube(self):
        """
        세제곱을 하는 함수를 만들자
        """
        self.assertEqual(1, yourtest.cube(1))
        self.assertEqual(8, yourtest.cube(2))
        self.assertEqual(4096, yourtest.cube(16))
        self.assertEqual(42875000, yourtest.cube(350))
        self.assertEqual(-8, yourtest.cube(-2))
        self.assertEqual(0, yourtest.cube(0))
        self.assertEqual(-920031709176, yourtest.cube(-9726))
        
    def test_make_float(self):
        """
        주어진 정수를 floating-point number 로 만들자
        float 을 사용하자
        """
        self.assertEqual(1.0, yourtest.make_float(1))
        self.assertEqual(5.0, yourtest.make_float(5))
        self.assertEqual(-14.0, yourtest.make_float(-14))
        self.assertEqual(0.0, yourtest.make_float(0))
        
    def test_make_int(self):
        """
        floating-point number를 정수로 만들자
        int 를 사용하자
        """
        self.assertEqual(1, yourtest.make_int(1.0))
        self.assertEqual(4, yourtest.make_int(4.5))
        self.assertEqual(4, yourtest.make_int(4.94))
        self.assertEqual(2, yourtest.make_int(2.4548))
        self.assertEqual(1569846312845, yourtest.make_int(1569846312845.0488454))
        self.assertEqual(-34, yourtest.make_int(-34.111))
    
    def test_abs(self):
        """
        절대값을 리턴시키자
        abs 함수 사용
        """
        self.assertEqual(1, yourtest.make_abs(1))
        self.assertEqual(23, yourtest.make_abs(23))
        self.assertEqual(14, yourtest.make_abs(-14))
        self.assertEqual(111100, yourtest.make_abs(-111100))
        self.assertEqual(0, yourtest.make_abs(0))
        self.assertEqual(123123234234123123, yourtest.make_abs(123123234234123123))
        
if __name__ == "__main__":
    unittest.main()

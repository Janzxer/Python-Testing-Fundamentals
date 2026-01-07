import unittest
import TriangleUtils
    # JANNE VILJANEN TKM24
class TriangleTests(unittest.TestCase):
    def test_CheckIsTheTriangleValid(self):
        a = 2 #1,2
        b = 2
        c = 3

        result = TriangleUtils.triangleInspector(a,b,c)

        self.assertEqual(result, "The triangle is not valid")

    def test_CheckIsTheInputZeroOrLess(self):
        a = 3
        b = 3
        c = 1 #0,1

        result = TriangleUtils.triangleInspector(a,b,c)

        self.assertEqual(result, "While it's possible to draw negative triangles on the x and y axis, here it is not.")

    def test_CheckIsTheTriangleEquilateral(self):
        a = 2 #3,2
        b = 3
        c = 3

        result = TriangleUtils.triangleInspector(a,b,c)

        self.assertEqual(result, "Triangle is equilateral")

    def test_CheckIsTheTriangleIsosceles(self):
        a = 1 #2,1
        b = 2
        c = 3

        result = TriangleUtils.triangleInspector(a,b,c)

        self.assertEqual(result, "The triangle is isosceles")

    def test_CheckIsTheTriangleScalene(self):
        a = 7 #5,7
        b = 7
        c = 9

        result = TriangleUtils.triangleInspector(a,b,c)

        self.assertEqual(result, "The triangle is scalene")

    def test_CheckIsTheInputInteger(self):
        a = 1
        b = 1
        c = 1
        
        result = TriangleUtils.triangleInspector(a,b,c)

        self.assertEqual(result, "All of the inputs must be integers.")

if __name__ == "__main__":
    unittest.main()
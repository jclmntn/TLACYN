import math
import random
from algorithms.BinarySearch import binary_search
from algorithms.LinearSearch import linear_search
from algorithms.TwoCrystalBalls import two_crystal_balls

class TestLinearSearch:
    test = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
 
    def test_one(self):
        assert linear_search(self.test, 69) == True   

    def test_two(self):
        assert linear_search(self.test, 1336) == False

    def test_three(self):
        assert linear_search(self.test, 69420) == True

    def test_four(self):
        assert linear_search(self.test, 69421) == False

    def test_five(self):
        assert linear_search(self.test, 1) == True

    def test_six(self):
        assert linear_search(self.test, 0) == False


class TestBinarySearch:
    test = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
 
    def test_one(self):
        assert binary_search(self.test, 69) == True   

    def test_two(self):
        assert binary_search(self.test, 1336) == False

    def test_three(self):
        assert binary_search(self.test, 69420) == True

    def test_four(self):
        assert binary_search(self.test, 69421) == False

    def test_five(self):
        assert binary_search(self.test, 1) == True

    def test_six(self):
        assert binary_search(self.test, 0) == False

class TestBalls:
    idx = math.floor(random.random() * 10000)
    data = [False] * 10000

    for i in range(idx, 10000):
        data[i] = True
    
    def test_one(self):
        assert two_crystal_balls(self.data) == self.idx
        assert two_crystal_balls([False] * 821) == -1
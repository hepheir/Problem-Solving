import unittest


class Problem1(unittest.TestCase):
    def setUp(self) -> None:
        from .prob1 import solution
        self.solution = solution
        return super().setUp()

    def tearDown(self) -> None:
        self.assertEqual(self.solution(*self.args), self.ans)
        return super().tearDown()

    def test_1(self):
        self.args = (
            [[1,0],[35,0],[1,0],[100,1],[35,1],[100,1],[35,0],[1,1],[1,1]],
        )
        self.ans = 2

    def test_2(self):
        self.args = (
            [[1,0],[2,0],[3,0],[1,0],[2,0],[1,0],[1,1],[2,0],[2,0],[2,1],[1,0],[1,1],[3,0],[3,0],[1,1]],
        )
        self.ans = 4

    def test_3(self):
        self.args = (
            [[1,0],[2,0],[3,0]],
        )
        self.ans = 0


class Problem2(unittest.TestCase):
    def setUp(self) -> None:
        from .prob2 import solution
        self.solution = solution
        return super().setUp()

    def tearDown(self) -> None:
        self.assertEqual(self.solution(*self.args), self.ans)
        return super().tearDown()

    def test_1(self):
        self.args = (
            [ [1, 2], [3, 4] ],
        )
        self.ans = 7

    def test_2(self):
        self.args = (
            [ [1, 8, 3, 2], [7, 4, 6, 5] ],
        )
        self.ans = 19


class Problem3(unittest.TestCase):
    def setUp(self) -> None:
        from .prob3 import solution
        self.solution = solution
        return super().setUp()

    def tearDown(self) -> None:
        self.assertEqual(self.solution(*self.args), self.ans)
        return super().tearDown()

    def test_1(self):
        self.args = (
            [4,5,2,3,1],
            2,
        )
        self.ans = 4

    def test_2(self):
        self.args = (
            [5,4,3,2,1],
            4,
        )
        self.ans = 2

    def test_3(self):
        self.args = (
            [5,4,3,2,1],
            2,
        )
        self.ans = 3

if __name__ == '__main__':
    unittest.main()
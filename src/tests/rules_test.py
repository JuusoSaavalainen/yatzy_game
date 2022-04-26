import unittest
from src.rules import Checkrules

class TestLogik(unittest.TestCase):
    def setUp(self):
        self.rules = Checkrules()
        self.done_score = [False]*13
        self.scoredfh = [1, 2, 1, 2, 1]
        self.scoredts = [5, 5, 3, 2, 5]
        self.scoredfs = [3, 3, 6, 3, 3]
        self.scoredyz = [1, 1, 1, 1, 1]

    def test_right_possibility(self):
        helper_a = self.rules.possibility_all(self.done_score, self.scoredfh)
        self.assertTrue(helper_a[0])
        self.assertTrue(helper_a[8])

    def test_points_right(self):
        fullhouse = self.rules.points(self.scoredfh, 8)
        treesame = self.rules.points(self.scoredts, 6)
        foursame = self.rules.points(self.scoredfs, 7)
        yatzy = self.rules.points(self.scoredyz, 11)
        change = self.rules.points(self.scoredfh, 12)

        self.assertEqual(fullhouse, 25)
        self.assertEqual(treesame, 15)
        self.assertEqual(foursame, 12)
        self.assertEqual(yatzy, 50)
        self.assertEqual(change, 7)

from src.logik import Draw
import unittest

class TestLogik(unittest.TestCase):
    def setUp(self):
        self.draw = Draw(1000)

    def test_init_right(self):
        self.assertEqual(len(self.draw.dices),6)

    def test_all_sprites(self):
        self.assertEqual(len(self.draw.all_sprites),8)

    def test_roll_dice(self):
        og = [sprite.number for sprite in self.draw.dices]
        self.draw.roll_dice(755,1)
        self.assertNotEqual([sprite.number for sprite in self.draw.dices],og)

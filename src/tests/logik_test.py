from src.logik import Draw
import unittest


#En ole vielä keksinyt miten voin testata kohtia joissa tarvitaan fonttia. Herjaa -> pygame.error: font not initialized
class TestLogik(unittest.TestCase):
    def setUp(self):
        self.draw = Draw(1000)

    def test_init_right(self):
        self.assertEqual(len(self.draw.dices),5)

    def test_all_sprites(self):
        self.assertEqual(len(self.draw.all_sprites),14)

    def test_roll_dice(self):
        og = [sprite.number for sprite in self.draw.dices]
        self.draw.first_roll()
        self.assertNotEqual([sprite.number for sprite in self.draw.dices],og)

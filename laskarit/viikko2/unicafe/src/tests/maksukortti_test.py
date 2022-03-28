import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_lataus_onnistuu(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")
    
    def test_rahan_ottaminen_toimii(self):
        x = self.maksukortti.ota_rahaa(15)
        y = self.maksukortti.ota_rahaa(9)
        self.assertEqual(x,False)
        self.assertEqual(y,True)
        self.assertEqual(str(self.maksukortti), "saldo: 0.01")
        

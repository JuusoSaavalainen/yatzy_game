import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_rahan_maara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kassapaate.maukkaat,0)
    
    def test_syo_edullisesti_kateinen_riittävä(self):
        x = self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(x,0)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100240)
        self.assertEqual(self.kassapaate.edulliset,1)

    def test_syo_edullisesti_kateinen_eiriittava(self):
        x = self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(x,230)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.edulliset,0)

    def test_syo_maukkaasti_kateinen_riittava(self):
        x = self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(x,0)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100400)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_syo_maukkaasti_kateinen_eiriittävä(self):
        x = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(x,200)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.maukkaat,0)

    def test_korttiosto_maukas_eitoimiva(self):
        self.apukortti = Maksukortti(200)
        x = self.kassapaate.syo_maukkaasti_kortilla(self.apukortti)
        self.assertEqual(self.apukortti.saldo,200)
        self.assertEqual(x,False)
        self.assertEqual(self.kassapaate.maukkaat,0)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_korttiosto_maukas_toimiva(self):
        self.apukortti = Maksukortti(450)
        x = self.kassapaate.syo_maukkaasti_kortilla(self.apukortti)
        self.assertEqual(self.apukortti.saldo,50)
        self.assertEqual(x,True)
        self.assertEqual(self.kassapaate.maukkaat,1)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_korttiosto_edullinen_eitoimiva(self):
        self.apukortti = Maksukortti(200)
        x = self.kassapaate.syo_edullisesti_kortilla(self.apukortti)
        self.assertEqual(self.apukortti.saldo,200)
        self.assertEqual(x,False)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_korttiosto_edullinen_toimiva(self):
        self.apukortti = Maksukortti(250)
        x = self.kassapaate.syo_edullisesti_kortilla(self.apukortti)
        self.assertEqual(self.apukortti.saldo,10)
        self.assertEqual(x,True)
        self.assertEqual(self.kassapaate.edulliset,1)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_lataus_kortille(self):
        self.apukortti = Maksukortti(250)
        self.kassapaate.lataa_rahaa_kortille(self.apukortti,250)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100250)
        self.assertEqual(self.apukortti.saldo,500)
        
    def test_lataus_kortille_neg(self):
        self.apukortti = Maksukortti(250)
        x = self.kassapaate.lataa_rahaa_kortille(self.apukortti,-250)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(x,None)

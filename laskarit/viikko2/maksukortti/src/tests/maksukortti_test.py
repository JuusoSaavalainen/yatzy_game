import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(10)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.5 euroa")

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6 euroa")


    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.kortti.syo_edullisesti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(25)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35 euroa")

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
    	self.kortti.lataa_rahaa(200)
    	self.assertEqual(str(self.kortti), "Kortilla on rahaa 150 euroa")

    def test_maukkaan_lounaan_syominen_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti.syo_edullisesti()
        self.kortti.syo_edullisesti()
        self.kortti.syo_edullisesti()
        self.kortti.syo_maukkaasti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2.5 euroa")

    def test_neg_lataus_ei_muuta_saldoa(self):
	    self.kortti.lataa_rahaa(-20)
	    self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")

    def test_edullisen_syominen_kun_saldo_tasn_sen_hinta(self):
        self.kortti2 = Maksukortti(2.5)
        self.kortti2.syo_edullisesti()
        self.assertEqual(str(self.kortti2), "Kortilla on rahaa 0.0 euroa")

    def test_maukkaan_lounaan_syominen_kun_saldo_4(self):
        self.kortti3 = Maksukortti(4)
        self.kortti3.syo_maukkaasti()
        self.assertEqual(str(self.kortti3), "Kortilla on rahaa 0 euroa")

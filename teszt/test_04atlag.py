from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import atlag

class TestAtlag(TestCase):
    def test_feladat04_atlag(self):
        aktualis = atlag.feladat04_osszeg()
        elvart = 5.2
        self.assertEqual(elvart, aktualis, "Az átlagot helytelenül határozta meg!")



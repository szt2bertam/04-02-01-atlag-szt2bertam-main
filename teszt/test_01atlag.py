from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import atlag

class TestAtlag(TestCase):
    def test_feladat01_atlag(self):
        aktualis = atlag.feladat01_atlag()
        elvart = 2.1875
        self.assertEqual(elvart, aktualis, "Az átlagot helytelenül határozta meg!")


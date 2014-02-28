import unittest
from unittest.mock import Mock
from fournisseur_meteo import FournisseurMeteo
from canal_meteo import CanalMeteo


class CanalMeteoTest(unittest.TestCase):
    TEMPERATURE_ELEVEE = 50
    TEMPERATURE_BASSE = -30
    TEMPERATURE_TROP_BASSE = -60

    def setUp(self):
        self.fournisseur_de_salut_bonjour = FournisseurMeteo()
        self.salut_bonjour = CanalMeteo(self.fournisseur_de_salut_bonjour)

    def test_temperature_elevee_soleil_lunettes(self):
        #given
        self.fournisseur_de_salut_bonjour.get_temperature = Mock(return_value=self.TEMPERATURE_ELEVEE)

        #when
        affichage = self.salut_bonjour.affiche_image()

        #then
        self.assertEquals("Soleil avec lunettes", affichage)

    def test_temperature_froide_flocons(self):
        #given
        self.fournisseur_de_salut_bonjour.get_temperature = Mock(return_value=self.TEMPERATURE_BASSE)

        #when
        affichage = self.salut_bonjour.affiche_image()

        #then
        self.assertEquals("Flocon", affichage)

    def test_temperature_trop_froide_erreur(self):
        #given
        self.fournisseur_de_salut_bonjour.get_temperature = Mock(return_value=self.TEMPERATURE_TROP_BASSE)

        #then
        self.assertRaises(NotImplementedError, self.salut_bonjour.affiche_image)
"""Test non fonctionnel minimal de performance pour la page de rendez-vous."""
import time

from django.test import TestCase


class PerformanceFormulaireTest(TestCase):
    def test_formulaire_repond_rapidement(self):
        debut = time.perf_counter()
        reponse = self.client.get("/rendezvous/")
        duree = time.perf_counter() - debut

        self.assertEqual(reponse.status_code, 200)
        self.assertLess(
            duree,
            1.0,
            f"La page de rendez-vous a répondu en {duree:.3f} seconde(s)",
        )

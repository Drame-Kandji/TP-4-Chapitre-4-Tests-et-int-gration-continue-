from django.test import TestCase

from patients.models import Patient

from .models import TypeConsultation


class ParcoursCompletRendezVousTest(TestCase):
    def test_parcours_complet_de_la_prise_de_rendez_vous_a_la_facture(self):
        patient = Patient.objects.create(
            nom="Ndiaye",
            prenom="Awa",
            email="awa@example.com",
        )

        formulaire = self.client.get("/rendezvous/")
        self.assertEqual(formulaire.status_code, 200)
        self.assertContains(formulaire, "Awa Ndiaye")

        reponse = self.client.post(
            "/rendezvous/",
            {
                "patient": patient.id,
                "type_consultation": TypeConsultation.GENERALISTE,
                "date": "2026-07-21",
                "notes": "Consultation de suivi",
            },
        )
        self.assertRedirects(reponse, "/rendezvous/")

        facture = self.client.get(f"/rendezvous/facture/{patient.id}/")
        self.assertEqual(facture.status_code, 200)
        self.assertContains(facture, "Total :")
        self.assertContains(facture, "5000 FCFA")

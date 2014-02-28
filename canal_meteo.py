class CanalMeteo:
    def __init__(self, fournisseur_meteo):
        self.fournisseur_meteo = fournisseur_meteo

    def affiche_image(self):
        temperature = self.fournisseur_meteo.get_temperature()

        if temperature > 30:
            return "Soleil avec lunettes"
        elif temperature > 10:
            return "Soleil"
        elif temperature > -10:
            return "Nuage"
        elif temperature > -40:
            return "Flocon"
        else:
            raise NotImplementedError
from canal_meteo import CanalMeteo
from fournisseur_meteo import FournisseurMeteo

EnvironnementCanada = FournisseurMeteo()
MeteoMedia = CanalMeteo(EnvironnementCanada)

print(MeteoMedia.affiche_image())
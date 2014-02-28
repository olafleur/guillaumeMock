import time
import random


class FournisseurMeteo:
    def get_temperature(self):
        element1 = self.consulte_expert()
        element2 = self.fais_calculs_complexes()

        return element1 + element2

    @staticmethod
    def consulte_expert():
        time.sleep(10)
        return random.randrange(-20, 10)

    @staticmethod
    def fais_calculs_complexes():
        time.sleep(5)
        return random.randrange(-30, 50)

# Euer github-Repository: https://github.com/SunSharks/World2Mathesis2022

# https://github.com/cvanwynsberghe/pyworld3/blob/main/pyworld3/population.py
# GIT für windows: https://git-scm.com/download/win
# SSH-Key für git auf Windows: https://medium.com/devops-with-valentine/2021-how-to-set-up-your-ssh-key-for-github-on-windows-10-afe6e729a3c0
from table import Table
legende = {"P": "Population", "PI" : "Population Initial",
}

class world():

    def __init__ (self, startjahr, endjahr):
        self.zeitraum=endjahr-startjahr
        self.PI = 1.65e9
        self.BRN = 0.04

    def zeitschritt(self):
        self.birthrate()
        self.getpopulation()

    def getpopulation (self):
        P[k]= P[k-1]+DT*(self.BR-self.DR)

    def birthrate (self, k):
        '''berechnet zum Zeitpunkt k die Geburtenrate für den nächsten Zeitraum'''
        self.BR= P[k]*self.clip(BRN, BRN1, SWT, k)*

    def deathrate (self, k):
        '''Berechnet die Todesrate am Zeitpunkt k.'''
        self.DR = P[k]*self.clip(DRN, DRN1, SWT3, k)*DRMM[k]*

    def clip (self, vgl1, vgl2, SWT, k):
        '''Wählt je nach Zeit eine von zwei Raten (vgl1 und vgl 2)
        aus und gibt sie zurück, wenn ein bestimmter
        Zeitpunkt SWT überschritten wurde'''
        if k< SWT:
            return vgl1
        else:
            return vgl2

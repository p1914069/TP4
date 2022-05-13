#################################################################################
# Écrit par     : Arnaud MORMONT                                                #
# Me contacter  : arnaud.mormont@etu.univ-lyon1.fr                              #
# Objectif      : Fichier contenant la classe du joueur                         #
# Version       : 0.1                                                           #
#################################################################################

import core
import random

class Joueur():
    def __init__(self):
        self.rayon = 15
        self.x = random.randint(0, core.WINDOW_SIZE[0] - self.rayon)
        self.y = random.randint(0, core.WINDOW_SIZE[1] - self.rayon)
        self.couleur = (255, 255, 255)

    def show(self):
        core.Draw.circle(self.couleur, [self.x, self.y], self.rayon)

    def move(self):
        if core.getKeyPressList("z"):
            self.y = self.y - 25
        if core.getKeyPressList("s"):
            self.y = self.y + 25
        if core.getKeyPressList("q"):
            self.x = self.x - 25
        if core.getKeyPressList("d"):
            self.x = self.x + 25

        self.edge()

    def edge(self):
        if self.x - self.rayon <= 0:
            self.x = self.rayon
        if self.x + self.rayon >= core.WINDOW_SIZE[0]:
            self.x = core.WINDOW_SIZE[0] - self.rayon
        if self.y - self.rayon <= 0:
            self.y = self.rayon
        if self.y + self.rayon >= core.WINDOW_SIZE[1]:
            self.y = core.WINDOW_SIZE[1] - self.rayon
#################################################################################
# Écrit par     : Arnaud MORMONT                                                #
# Me contacter  : arnaud.mormont@etu.univ-lyon1.fr                              #
# Objectif      : Fichier contenant la classe de la balle                       #
# Version       : 0.1                                                           #
#################################################################################
from pygame import Vector2

import core
import random


class Ball:
    def __init__(self):
        self.rayon = 10
        self.x = random.randint(0, core.WINDOW_SIZE[0]-self.rayon)
        self.y = random.randint(0, core.WINDOW_SIZE[1]-self.rayon)
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 100))

        self.acc = Vector2(0,0)
        self.vel = [0, 0]
        self.maxVel = 1

    def show(self):
        core.Draw.circle(self.couleur, [self.x, self.y], self.rayon)

    def move(self):
        if core.getKeyPressList("z"):
            self.y = self.y - 1
        if core.getKeyPressList("s"):
            self.y = self.y + 1
        if core.getKeyPressList("q"):
            self.x = self.x - 1
        if core.getKeyPressList("d"):
            self.x = self.x + 1

        self.edge()

    def randomMove(self):

        self.acc = Vector2(random.uniform(-3,3),  random.uniform(-3,3))

        self.vel = self.vel + self.acc

        if self.vel.length() > self.maxVel:
            self.vel.scale_to_length(self.maxVel)

        self.y = self.vel.y + self.y
        self.x = self.vel.x + self.x

        self.edge()

    def edge(self):
        if self.x - self.rayon <= 0:
            self.x = self.rayon
        if self.x + self.rayon >= core.WINDOW_SIZE[0]:
            self.x=core.WINDOW_SIZE[0] - self.rayon
        if self.y - self.rayon <= 0:
            self.y = self.rayon
        if self.y + self.rayon >= core.WINDOW_SIZE[1]:
            self.y = core.WINDOW_SIZE[1] - self.rayon

    def collision(self, joueur):
        dist = Vector2(self.x, self.y).distance_to(Vector2(joueur.x, joueur.y))
        sommerayons = self.rayon + joueur.rayon

        if sommerayons >= dist:
            return True
        else:
            return False
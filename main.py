#################################################################################
# Écrit par     : Arnaud MORMONT                                                #
# Me contacter  : arnaud.mormont@etu.univ-lyon1.fr                              #
# Objectif      : Fichier de travail du TP4                                     #
# Version       : 0.1                                                           #
#################################################################################

import core

from ball import Ball
from joueur import Joueur


def setup():
    print("setup")
    core.WINDOW_SIZE = [1080, 720]
    core.fps = 60

    nb_balles = 100
    core.memory("tab_balles", [])

    j = Joueur()
    core.memory("Joueur", j)

    core.memory("score", 0)

    core.memory("gameOver", False)

    for i in range(0, nb_balles):
        b = Ball()
        core.memory("tab_balles").append(b)


def run():
    core.cleanScreen()
    if not core.memory("gameOver"):
        core.memory("score", core.memory("score") + 1/core.fps)

        for i in core.memory("tab_balles"):
            i.show()
            i.randomMove()
            gameOver = i.collision(core.memory("Joueur"))
            if gameOver:
                core.memory("gameOver", True)

        if not gameOver :
            core.memory("Joueur").show()
            core.memory("Joueur").move()

    else:
        core.Draw.text((255,0,0), f'GameOver : {core.memory("score")}', [10, 10])

if __name__ == '__main__':
    core.main(setup, run)

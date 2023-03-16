import math

import arcade
import random

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

#Liste des couleurs disponible
COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
          arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]

def collisiondetection(cercle, x, y):
    # return True si une coordonée a l'interieur du périmètre d'un cercle.
    # Sinon, il retourne false
    maxposX = cercle.x + cercle.rayon
    maxposY = cercle.y + cercle.rayon

    minposX = cercle.x - cercle.rayon
    minposY = cercle.y - cercle.rayon

    if maxposX > x > minposX and maxposY > y > minposY:
        return True
    else:
        return False

class Cercle():
    """Classe qui crée des objects Cercle"""
    def __init__(self, x, y, rayon, color):
        self.rayon = rayon
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        # Fonction qui dessine l'objet cercle
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)


class MyGame(arcade.Window):
    """Classe représentant le jeu, hérite des fonctions du module Arcade"""
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_cercles = []

    def setup(self):
        # remplir la liste de cercle avec 20 objets de type Cercle
        # On génère la position et la couleur des cercle aléatoirement
        for _ in range(20):
            rayon = random.randint(10, 30)
            center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
            center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
            color = random.choice(COLORS)
            cercleObject = Cercle(center_x, center_y, rayon, color)
            self.liste_cercles.append(cercleObject)

    def on_draw(self):
        # Active la fonction "draw" de chaque cercle présent dans la liste chaque frame
        arcade.start_render()

        for cercle in self.liste_cercles:
            cercle.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        # function qui est activé a chaque click, on regarde si la position du cuseur touche un cercle
        # button = 1 si click gauche
        # button = 4 si click droit
        for cercle in self.liste_cercles:
            if collisiondetection(cercle, x, y):
                if button == 1:
                    # Si l'utilisateur click gauche, on enlève le cercle de la liste qui va être dessiner
                    self.liste_cercles.remove(cercle)
                elif button == 4:
                    # Si l'utilisateur click droit, on assigne une couleur aléatoire au cercle
                    cercle.color = random.choice(COLORS)

def main():
    #Initialize la classe du jeu
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()

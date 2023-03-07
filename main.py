import math

import arcade
import random

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
          arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]

def collisiondetection(cercle, x, y):
    maxposX = cercle.x + cercle.rayon
    maxposY = cercle.y + cercle.rayon

    minposX = cercle.x - cercle.rayon
    minposY = cercle.y - cercle.rayon

    if maxposX > x > minposX and maxposY > y > minposY:
        return True
    else:
        return False

class Cercle():
    def __init__(self, x, y, rayon, change_x, change_y, color):
        self.rayon = rayon
        self.x = x
        self.y = y
        self.color = color

    def update(self):
        pass

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_cercles = []

    def setup(self):
        # remplir la liste avec 20 objets de type Cercle
        for _ in range(20):
            rayon = random.randint(10, 30)
            center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
            center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
            color = random.choice(COLORS)
            cercleObject = Cercle(center_x, center_y, rayon, random.randint(-10, 10), random.randint(-10, 10), color)
            self.liste_cercles.append(cercleObject)

    def on_draw(self):
        arcade.start_render()

        for cercle in self.liste_cercles:
            cercle.update()
            cercle.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):

        for cercle in self.liste_cercles:
            if collisiondetection(cercle, x, y):
                if button == 1:
                    self.liste_cercles.remove(cercle)
                elif button == 4:
                    cercle.color = random.choice(COLORS)

def collisiondetection(cercle, x, y):
    #Fonction qui return True si une position x,y est dans un cercle
    maxposX = cercle.x + cercle.rayon
    maxposY = cercle.y + cercle.rayon

    minposX = cercle.x - cercle.rayon
    minposY = cercle.y - cercle.rayon

    #si le curseur est entre la position minimum x et y du cercle et la position maximum du x et y du cercle, il y a une collision
    if maxposX > x > minposX and maxposY > y > minposY:
        return True
    else:
        return False


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()

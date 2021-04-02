from paddle import Paddle # import de la classe Paddle
from ball import Ball # import de la classe Ball
from briques import Brick # import de la classe Brick

playingGame = False
bricks = [] # Création de la liste

def setup():
    global paddle, ball # on déclare les variables paddle et ball comme globale
    size(605,400)
    paddle = Paddle() # on crée l'objet paddle
    ball = Ball() # on crée l'objet ball
    for x in range(5,width - 80,75):
        addBrick(x+37.5,50,3)
        addBrick(x+37.5,70,2)
        addBrick(x+37.5,90,1)

# Fonctions créant et stockant les briques dans la liste
def addBrick(x,y,hits):
    brick = Brick(x,y,hits)
    bricks.append(brick)

def draw():
    global playingGame
    background(0,0,0)

    #appel des méthodes pour le paddle
    paddle.display()
    if playingGame:
        paddle.checkEdges()
        paddle.update()
    #appel des méthodes pour la balle
    ball.display()
    if playingGame:

        ball.checkEdges()
        ball.update()
    if (ball.meets_paddle(paddle)):
        if ball.dir.y > 0 :
            ball.dir.y *= -1
    for i in range(len(bricks)):
        bricks[i].display()
    for i in range(len(bricks)-1,-1,-1):
        if ball.meets_brick(bricks[i]):
            bricks.pop(-1) # del bricks[i]
            ball.dir.y *= -1

def mousePressed():
    global playingGame
    playingGame = True

# détection des mouvements touches a et d
def keyPressed():
    if key == "a" or key == "A":
        paddle.isMovingLeft = True
    elif key == "d" or key == "D":
        paddle.isMovingRight = True

#annulation des mouvements quand on relâche la touche
def keyReleased():
    paddle.isMovingRight = False
    paddle.isMovingLeft = False

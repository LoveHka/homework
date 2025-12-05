


import pgzrun



WIDTH = 800
HEIGHT = 600

BLACK=(0, 0, 0)
WHITE=(255,255,255)

square = Rect(400, 300, 50, 50)
speed = 5



def draw():
    screen.fill(BLACK)
    screen.draw.filled_rect(square, WHITE)



def update():
    
    
    if keyboard.left:
        square.x -= speed
    if keyboard.right:
        square.x += speed
    if keyboard.up:
        square.y -= speed
    if keyboard.down:
        square.y += speed
    
    
    
    if square.left < 0:
        square.left = 0
    if square.right > WIDTH:
        square.right = WIDTH
    if square.top < 0:
        square.top = 0
    if square.bottom > HEIGHT:
        square.bottom = HEIGHT



pgzrun.go()

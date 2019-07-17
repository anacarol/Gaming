import pgzrun

alien = Actor('alien')
# alien.pos = 100, 56
alien.topright = 0, 10

WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.clear()
    alien.draw()

def update():
    alien.left += 2
    # print(alien.left)
    if alien.left > WIDTH:
        alien.right = 0
        # alien.left += -2

def on_mouse_down(pos):
	if alien.collidepoint(pos):
		# print("eek!")
		sounds.eep.play()
		alien.image = 'alien_hurt'

	else:
		alien.image = 'alien'
		print("You missed me!")


pgzrun.go()
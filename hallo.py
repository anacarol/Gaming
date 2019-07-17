import pgzrun

WIDTH = 800
HEIGHT = 600

def draw():
  screen.clear()
  # screen.draw.text('Hallo, Raphael! Vamos jogar um jogo?', topright=(10, 10))
  screen.draw.circle((400, 300), 30, 'white')
  
pgzrun.go()

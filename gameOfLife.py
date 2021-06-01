import pygame
import numpy as np
pygame.init()

W, H = 600, 500
size = 5 
margin = 1
WIN = pygame.display.set_mode((W,H))
pygame.display.set_caption("Game of Life")
FPS = 60
rows,cols = W//size, H//size
grid = np.random.randint(0,5,(rows,cols))

def fieldCopy():
    field = grid
    return field

def neighbors(field,x,y):
    neighbor = [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),
                (x+1,y-1),(x+1,y),(x+1,y+1)]
    count = 0
    for i,j in neighbor:
        try:
            if field[i,j] == 1:
                count += 1
        except:
            pass
    return count

def rules(x,y,count):
    if count == 3:
        grid[x,y] = 1
    elif count < 2 or count > 3:
        grid[x,y] = 0

def run():
    nextGen = fieldCopy()
    count = 0
    for i in range(nextGen.shape[0]):
        for j in range(nextGen.shape[1]):
            count = neighbors(nextGen,i,j)
            rules(i,j,count)

def display():
    WIN.fill("black")
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            box = pygame.Rect(i * size, j * size,size,size)
            color = "WHITE"
            if grid[i][j] == 1:
                color = "GREEN"
                pygame.draw.rect(WIN, color, box)
            else:
                pygame.draw.rect(WIN, color, box)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display()
        run()
    pygame.quit()


if __name__ == "__main__":
    main()

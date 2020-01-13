import pygame

# Nie ma implementacji do drugiego ekrany, trzeba zrobić podzział na dwie tablice bo sie wywala inaczej




# Zdefiniowane zmienne
WINDOWHEIGHT = 555
WINDOWWIDTH = 555
ROWS = 10
COLUMNS = 10
WIDTH = 50
HEIGHT = 50
MARGIN = 5

# Kolory zdefiniowane
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


pygame.init()
# Tworzy okno statków i pola ostrzału i nazywe gry
display_ships = pygame.display.set_mode((WINDOWHEIGHT, WINDOWWIDTH))
display_fire = pygame.display.set_mode((WINDOWWIDTH * 2, WINDOWHEIGHT))
pygame.display.set_caption("Battleships")

# Tworzy tablice gridu
grid = []
for row in range(ROWS):

    grid.append([])
    for column in range(COLUMNS):
        grid[row].append(0)

# Używany żeby sprawdzać jak szybko ekran się updatuje
clock = pygame.time.Clock()


class Ship():
    def __init__(self,x,y,length,direction,grid):
        self.x = x
        self.y = y
        self.length = length
        self.direction = direction
        s_grid = grid


# Główna pętla
i = 0
while True:

    # Sprawdza eventy , zamknięcie X gry oraz klikniecie przyciskiem

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:


            pos = pygame.mouse.get_pos()
            # Zamienia koordynaty x/y na koordynaty gridu
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # ustawia w tablicy dana lokacje na 1 i wyswietla w konsoli współrzędne

            print("Click ", pos, "Grid coordinates: ", row, column)
            if grid[row][column] == 1:
                print("miejsce jest juz wykorzystane")
            elif grid[row][column] ==0:
                if i>=20:
                    print("Limit statkow wykorzystany")
                elif i<20:
                    grid[row][column] = 1
                    i=i+1
                    print(i)



    # Ustawia tło
    display_ships.fill(BLACK)


    # Rysuje siatke
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(display_ships,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])


    # Limit FPS
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
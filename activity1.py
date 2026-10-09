import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Wildlife Display")

t1 = pygame.font.Font(None, 42).render("Wildlife Spotlight: Tiger", True, "black")
t2 = pygame.font.Font(None, 28).render("Tigers are powerful wild cats.", True, "black")

timer = pygame.time.Clock()
run = True

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    # Fills the background with a solid forest green color
    win.fill((34, 139, 34))  
    
    # Draws a clean orange circle in the center as a placeholder for the tiger
    pygame.draw.circle(win, (255, 140, 0), (250, 220), 90)  

    win.blit(t1, t1.get_rect(center=(250, 45)))
    win.blit(t2, t2.get_rect(center=(250, 420)))

    pygame.display.flip()
    timer.tick(30)

pygame.quit()

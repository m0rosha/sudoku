import pygame 
import sudokum 

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((550,550))
bkgrnd_col = (255,255,255)
pygame.display.set_caption('Sudoku')

font = pygame.font.SysFont("arial", 40)

nums = [1,2,3,4,5,6,7,8,9]
board = sudokum.generate(mask_rate=0.4)


text_objects = []
for row in range(9):
    text_row = []
    for col in range(9):
        value = board[row][col]
        if value != 0:
            text = font.render(str(value), True, (0, 0, 0))
        else:
            text = font.render('', True, (0, 0, 0))
        text_row.append(text)
    text_objects.append(text_row)

win.fill((255,255,255))
 
def draw_numbers_window():
    pygame.draw.rect(win, (125, 55, 55), (150, 150, 240, 240))
    for i, number in enumerate(nums):
        text = font.render(str(number), True, (0, 0, 0))
        x = 160 + (i % 3) * 60
        y = 160 + (i // 3) * 60
        rect = pygame.Rect(x, y, 70, 70)
        if rect.collidepoint(pos):
            print("Number", number, "clicked!")
        win.blit(text, (x, y))
        

for row in range(9):
    for col in range(9):
        win.blit(text_objects[row][col], (60 + col*50, 55 + row*50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            row = (pos[1] - 50) // 50
            col = (pos[0] - 50) // 50
            if board[row][col] == 0:
                draw_numbers_window()
               
            #print(len(nums))

    for i in range(10):
        if(i%3 == 0 ):
            pygame.draw.line(win,(0,0,0),(50 + 50*i, 50), (50 + 50*i,500 ), 4)#горизонтальна жирна
            pygame.draw.line(win,(0,0,0),(50,50 + 50*i), (500,50 + 50*i ), 4)#вертикальна  жирна
        pygame.draw.line(win,(0,0,0),(50 + 50*i, 50), (50 + 50*i,500 ), 2)#горизонтальна
        pygame.draw.line(win,(0,0,0),(50,50 + 50*i), (500,50 + 50*i ), 2)#вертикальна     
    clock.tick(60)
    pygame.display.update()
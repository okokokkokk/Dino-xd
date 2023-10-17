#Khai báo thư viện:
import pygame
pygame.init()
clock = pygame.time.Clock()

#Màn hình:
screen = pygame.display.set_mode((600,300))

#Tiêu đề và icon:
pygame.display.set_caption('Game Dino')
icon = pygame.image.load(r'assets\dinosaur.png')
pygame.display.set_icon(icon)

#Thêm hình ảnh:
bg = pygame.image.load(r'assets\background.jpg')
tree = pygame.image.load(r'assets\tree.png')
dino = pygame.image.load(r'assets\dinosaur.png')

#Load sound:
sound1 = pygame.mixer.Sound(r'sound\tick.wav')
sound2 = pygame.mixer.Sound(r'sound\te.wav')

#Khởi tạo:
bg_x, bg_y = 0,0
tree_x, tree_y = 550,230
dino_x, dino_y = 20,230
x_def = 5
score = 0 
hscore = 0
#Tốc độ rơi của dino
y_def = 8   
gameplay = True
score = 0
hscore = 0
jump = False
#check va cham:
def check_vc():
    if dino_hcn.colliderect(tree_hcn):
        pygame.mixer.Sound.play(sound2)
        return False 
    return True
#Dua score vao:
game_font = pygame.font.Font('04B_19.TTF',20)
def score_view():
    if gameplay: 
        score_txt = game_font.render(f'Score: {int(score)}',True,(255,0,0))
        screen.blit(score_txt,(250,70))
        hscore_txt = game_font.render(f'High score: {int(hscore)}',True,(255,0,0))
        screen.blit(hscore_txt,(200,50))
    else:
        score_txt = game_font.render(f'Score: {int(score)}',True,(255,0,0))
        screen.blit(score_txt,(250,70))
        hscore_txt = game_font.render(f'High score: {int(hscore)}',True,(255,0,0))
        screen.blit(hscore_txt,(200,50))
        over_txt = game_font.render(f'Game Over!',True,(255,0,0))
        screen.blit(over_txt,(250,150))

#Vòng lặp xử lý:
running = True
while running:
    #Chỉnh FPS:
    clock.tick(70)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and gameplay:
                if dino_y==230:
                   jump = True
                   pygame.mixer.Sound.play(sound1)
            if event.key == pygame.K_SPACE and gameplay == False:
                gameplay = True

    if gameplay:
        #bg:
        bg_hcn = screen.blit(bg,(bg_x,bg_y))
        bg2_hcn = screen.blit(bg,(bg_x+600,bg_y))
        bg_x -= x_def
        if bg_x == -600: bg_x=0
        #tree:
        tree_hcn = screen.blit(tree,(tree_x,tree_y))
        tree_x -= x_def
        if tree_x == -20: tree_x=550
        #dino:
        dino_hcn = screen.blit(dino,(dino_x,dino_y))
        if dino_y >= 80 and jump:
            dino_y -= y_def
        else:
            jump = False 
        if dino_y < 230 and jump == False: 
            dino_y += y_def
        gameplay = check_vc()
        score += 0.01
        if hscore<score : hscore = score
        score_view()
    else:
        #resetgame:
        bg_x, bg_y = 0,0
        tree_x, tree_y = 550,230
        dino_x, dino_y = 20,230
        bg_hcn = screen.blit(bg,(bg_x,bg_y))
        tree_hcn = screen.blit(tree,(tree_x,tree_y))
        dino_hcn = screen.blit(dino,(dino_x,dino_y))
        score = 0
        score_view()
    pygame.display.update()
import pygame


def main():
    #As definicões dos objetos(variaveis)
    pygame.init()
    tela = pygame.display.set_mode([600, 450])
    pygame.display.set_caption('Jogo Iniciante')
    sair = False
    relogio = pygame.time.Clock()
    cor_branca = (255, 255, 255)
    cor_azul = (108, 194, 236)
    cor_verde = (152, 231, 114)
    cor_vermelha = (227, 57, 9)
    cor_rosa = (253, 147, 226)
    cor_preta = (0, 0, 0)
    sup = pygame.Surface((600, 450))
    sup.fill(cor_azul)

    ret = pygame.Rect(10, 10, 30, 30)
    ret2 = pygame.Rect(0, 40, 560, 20)
    ret3 = pygame.Rect(150, 100, 450, 30)
    ret4 = pygame.Rect(0, 185, 565, 40)
    ret5 = pygame.Rect(100, 275, 510, 20)
    ret6 = pygame.Rect(0, 330, 450, 30)
    ret7 = pygame.Rect(0, 370, 565, 40)

    pygame.font.init()

    font_padrao = pygame.font.get_default_font()
    fonte_perdeu = pygame.font.SysFont(font_padrao, 45)
    fonte_ganhou = pygame.font.SysFont(font_padrao, 30)

    audio_explosao = pygame.mixer.Sound('Explosão com Som - Efeito especial para filmes (online-audio-converter.com).ogg')

    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_pos(150, 150)
        relogio.tick(30)
        tela.fill(cor_branca)
        tela.blit(sup, [0, 0])

        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= ret.width/2
        ret.top -= ret.height / 2
        if ret.colliderect(ret2) or ret.colliderect(ret3) or ret.colliderect(ret4) or ret.colliderect(ret5) or ret.colliderect(ret6) or ret.colliderect(ret7):
            audio_explosao.play()
            text = fonte_perdeu.render('COLIDIU', 1, cor_branca)
            sup = pygame.Surface((600, 450))
            sup.fill(cor_azul)
            (ret.left, ret.top) = (xant, yant)
        if xant <= 0 or xant >= 580:
            print('fim de jogo')
        pygame.draw.rect(tela, cor_vermelha, ret)
        pygame.draw.rect(tela, cor_preta, ret2)
        pygame.draw.rect(tela, cor_preta, ret3)
        pygame.draw.rect(tela, cor_preta, ret4)
        pygame.draw.rect(tela, cor_preta, ret5)
        pygame.draw.rect(tela, cor_preta, ret6)
        pygame.draw.rect(tela, cor_preta, ret7)
        pygame.display.update()
    pygame.quit()

main()
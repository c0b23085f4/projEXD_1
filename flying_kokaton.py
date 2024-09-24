import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_filp_img = pg.image.load("fig/pg_bg.jpg")
    bg_filp_img = pg.transform.flip(bg_filp_img, True, False)
    # 練習2
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200


    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        mx, my = 0, 0
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            mx, my = 0, -1
        if key_lst[pg.K_DOWN]:
            mx, my= 0, +1
        if key_lst[pg.K_LEFT]:
            mx, my= -1, 0
        if key_lst[pg.K_RIGHT]:
            mx, my = +2, 0

        kk_rct.move_ip(mx, my)

        

        x = -(tmr%3200)

        screen.blit(bg_img, [x, 0])
        screen.blit(bg_filp_img,[x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg_filp_img,[x+4800, 0])
        curr_x, curr_y = kk_rct.center
        kk_rct.center = curr_x - 1, curr_y
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
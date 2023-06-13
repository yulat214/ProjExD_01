import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    fw_img = pg.image.load("fig/3.png")
    fw_img = pg.transform.flip(fw_img, True, False)
    fw_r_img = pg.transform.rotozoom(fw_img, 10, 1.0)
    
    img_lst = [fw_img, fw_r_img]
    
    tmr = 0
    x = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img, [1600-x, 0])
        
        screen.blit(img_lst[tmr%2-1], [300, 200])
        
        
        pg.display.update()
        tmr += 1   
        x += 1
        clock.tick(300)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_r_img = pg.transform.flip(bg_img, True, False)
    
    fw_img = pg.image.load("fig/3.png")
    fw_img = pg.transform.flip(fw_img, True, False)
    fw_r_img = pg.transform.rotozoom(fw_img, 10, 1.0)
    
    img_lst = [fw_img, fw_r_img]
    
    tmr = 0
    x = 0
    angle = 0
    sgn = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            
        fw_rr_img = pg.transform.rotozoom(fw_img, angle%50, 1.0)
            
        screen.blit(bg_img, [-(x%3200), 0])
        screen.blit(bg_r_img, [3200-(x%3200), 0])
        screen.blit(bg_r_img, [-(x%3200), 0])
        screen.blit(bg_img, [1600-(x%3200), 0])
        
        
        #screen.blit(img_lst[tmr%2], [300, 200])
        screen.blit(fw_rr_img, [300, 200])
        
        pg.display.update()
        
        tmr += 1   
        x += 1 
        
        if angle == 0 or x == 0:
            sgn = 1
        elif angle == 10 or x == 1600:
            sgn = -1
            
        angle += sgn
        
        clock.tick(500)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
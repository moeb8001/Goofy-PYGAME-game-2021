#IGNORE THIS-ended up not using this.*sad emoji*

import pygame

class disp_txt:

    def __init__(self,text,time,destination):
        self.text = text
        self.time = time
        self.destination = destination
        self.shfnt = pygame.font.SysFont("comicsens",30,False)
        self.shtxt = self.shfnt.render(self.text,0,(255,0,0))
    def show(self,surface):
        if self.time>0:
            surface.blit(self.shtxt,self.destination)
        self.time -= 0.0001
#hint = disp_txt("text",100,(100,400)) #example
#hint.show(screen)   #in the main loop or where you are drawing

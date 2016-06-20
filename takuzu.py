import pygame, sys
from pygame.locals import *
from drawing_grid import *
pygame.init()
BLACK = (0,0,0)
WHITE = (255,255,255)

def rules(screen): #this is graphic user documentation!
	screen.blit(pygame.image.load('documentation.jpg'),(0,0)) #loading my background
	screen.blit(pygame.image.load('game_document.png'),(10,10)) #loading my background
	screen.blit(pygame.image.load('return.png'),(15,680)) #loading my background
	screen.blit(pygame.image.load('solved_grid.png'),(15,100)) #loading my background
	font = pygame.font.Font ('freesansbold.ttf',20)
	screen.blit(font.render('Takuzu is a logic-based number placement puzzle.',1,WHITE),(140,110))
	screen.blit(font.render('The objective is to fill a grid with 1s and 0s, but ',1,WHITE),(140,135))
	screen.blit(font.render('there are rules to respect:',1,WHITE),(140,160))
	screen.blit(font.render('1.Each row and column contains an equal number of 0s and 1s.',1,WHITE),(20,220))
	screen.blit(font.render('2.There is no more than two identical numbers adjacent to each other.',1,WHITE),(20,245))
	screen.blit(font.render('3.There is no identical row or column.',1,WHITE),(20,270))
	screen.blit(pygame.image.load('hint.png'),(20,360))
	screen.blit(font.render('With this button you can ask for a hint if you are stucked',1,WHITE),(120,360))
	screen.blit(pygame.image.load('undo.png'),(20,450))
	screen.blit(font.render('With this button you can rewind your last move and retry',1,WHITE),(120,450))
	screen.blit(pygame.image.load('new.png'),(20,560))
	screen.blit(font.render('With this button you can restart a new game',1,WHITE),(170,560))
	screen.blit(font.render('Have fun and enjoy it! ;)',1,WHITE),(480,720))
	
	while 1:
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:
				x,y = event.pos			
				for lunghezza in range (15,75): #event "return" to main screen.
					for altezza in range (680,740):
						if x == lunghezza and y == altezza:
							new_game()
			if event.type == QUIT:
					pygame.quit()
					sys.exit()
		pygame.display.update()


def new_game(): #main screen, here user can choose which grid want to play, or select game manual.
	#Loading all the images 
	screen = pygame.display.set_mode((750, 750))
	pygame.display.set_caption('Takuzu')
	screen.blit(pygame.image.load('wood.jpg'),(0,0))
	screen.blit(pygame.image.load('taku.png'),(50,50))
	screen.blit(pygame.image.load('grid.png'),(330,280))
	screen.blit(pygame.image.load('rules.png'),(15,690))
	#Writing on the screen all difficult levels
	font = pygame.font.Font ('freesansbold.ttf',24)
	screen.blit(font.render('Choose difficulty:',1,BLACK),(15,435))
	screen.blit(font.render('Grid 4x4',1,BLACK),(15,485))
	screen.blit(font.render('Grid 6x6',1,BLACK),(15,535))
	screen.blit(font.render('Grid 8x8',1,BLACK),(15,585))
	screen.blit(font.render('Grid 10x10',1,BLACK),(15,635))
	
	while 1:
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:
				x,y = event.pos			
				for lunghezza in range (15,170): #event "rules" button coordinates
					for altezza in range (690,740):
						if x == lunghezza and y == altezza:
							rules(screen)
									
				for lunghezza in range (15,110): #CREATING 4X4 GRID
					for altezza in range (485,510):
						if x == lunghezza and y == altezza:
							screen.blit(pygame.image.load('brown.jpg'),(0,0)) #loading my background
							var = 0 #i need this to print coordinates on my window
							for i in range(70,221,50): #drawing coordinates 
								screen.blit(font.render(str(var),1,BLACK),(25,i))
								screen.blit(font.render(str(var),1,BLACK),(i,20))
								var = var +1	

							num = 4
							grid(screen,num)
									
				for lunghezza in range (15,110): #CREATING 6X6 GRID
					for altezza in range (535,560):
						if x == lunghezza and y == altezza:
							screen.blit(pygame.image.load('brown.jpg'),(0,0)) #loading my background
							var = 0 #i need this to print coordinates on my window
							for i in range(70,321,50): #drawing coordinates 
								screen.blit(font.render(str(var),1,BLACK),(25,i))
								screen.blit(font.render(str(var),1,BLACK),(i,20))
								var = var +1	
			
							num = 6
							grid(screen,num)
									
				for lunghezza in range (15,110): #CREATING 8X8 GRID
					for altezza in range (585,610):
						if x == lunghezza and y == altezza:
							screen.blit(pygame.image.load('brown.jpg'),(0,0)) #loading my background
							var = 0 #i need this to print coordinates on my window
							for i in range(70,421,50): #drawing coordinates 
								screen.blit(font.render(str(var),1,BLACK),(25,i))
								screen.blit(font.render(str(var),1,BLACK),(i,20))
								var = var +1

							num = 8
							grid(screen,num)
									
				for lunghezza in range (15,140): #CREATING 10X10 GRID
					for altezza in range (635,660):
						if x == lunghezza and y == altezza:
							screen.blit(pygame.image.load('brown.jpg'),(0,0)) #loading my background
							var = 0 #i need this to print coordinates on my window
							for i in range(70,521,50): #drawing coordinates 
								screen.blit(font.render(str(var),1,BLACK),(25,i))
								screen.blit(font.render(str(var),1,BLACK),(i,20))
								var = var +1

							num = 10
							grid(screen,num)
				new_game()				
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update()

new_game() #calling for the first time this function when i execute my takuzu.py sheet

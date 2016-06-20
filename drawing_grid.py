import pygame, sys
from pygame.locals import *
from create_grid import *
from hints_and_mistakes import *

WHITE = (255,255,255) #defining color constants
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0, 0, 255)

def grid(screen,num): #this function will manage all other functions and user's game.
	posY = 30 #i use this variable to print on my window results of hint function one above the other. (see HINT event click)
	last_move = [WHITE, 0, 0] #this list will be filled with last_move color square, coordinates X and Y. (see UNDO event click)
	flag_undo = False #this will be used to disable undo button! (see UNDO event click for more)
	flag_hint = True #user can ask for a hint once for every click he does! (see HINT event click for more)
	flag_mistakes = [False," "] #check if there is a mistake on the grid (see MISTAKES event click for more)
	
	win = 0 # if win == 1 user win the game!
	
	hints_grid = [[0]*num for i in range(num)] #in this multidimensional list i track all hints i gave to the user (see HINT event click for more)
	
	create_grid = [[0]*num for i in range(num)] #create a full multidimensional list with 0s. This will become my solution grid
	for x in range(0,num): 
		for y in range(0,num):
			create_grid[x][y] = random.randint(0,1) #now i randomize all numbers
	checking_rows(create_grid,num)#i'll create a grid respecting RULE 1, 2 and 3. (see create_grid.py)
	hidden_grid = hide_part_of_the_grid(num,create_grid) #This function got random position to show on the grid to help gamer to start his game(see create_grid.py)		

	positionY = 50 #from 29 to row 43 i'm drawing LINES and my grid on the screen with some squares to help user.
	for x in range (0,num):
		positionX = 50
		for y in range (0,num):
			pygame.draw.rect(screen,BLACK,(positionX,positionY,50,50),2) #drawing grid's LINES 
			if hidden_grid[x][y] == 0: #NOW I'M drawing hidden_grid to help user to start game
				pygame.draw.rect(screen,RED,(positionX + 7 ,positionY + 7,38,38)) #untouchable squares, because they are 100% correct
				hidden_grid[x][y] = 99 #99 == untouchable red squares, UNDO event or other events cannot touch this squares
			elif hidden_grid[x][y] == 1:
				pygame.draw.rect(screen,BLUE,(positionX + 7 ,positionY + 7,38,38)) #untouchable squares, because they are 100% correct
				hidden_grid[x][y] = 89 #89 == untouchable blue squares UNDO event or other events cannot touch this squares
			elif hidden_grid[x][y] == 2:
				pygame.draw.rect(screen,WHITE,(positionX + 2 ,positionY + 2,46,46))
			positionX = positionX + 50
		positionY = positionY + 50
				
				
	font = pygame.font.Font ('freesansbold.ttf',25)
	font2 = pygame.font.Font ('freesansbold.ttf',16)
	screen.blit(font.render('HINT:',1,BLACK),(610,20))
	screen.blit(pygame.image.load('new.png'),(50,700)) #drawing buttons
	screen.blit(pygame.image.load('undo.png'),(300,650))
	screen.blit(pygame.image.load('hint.png'),(500,650))
	screen.blit(pygame.image.load('frame.jpg'),(50,560)) #here i'll show error, mistakes or if the user won the game
		
	while 1:
		for event in pygame.event.get():		
			if event.type == MOUSEBUTTONDOWN:
				screen.blit(pygame.image.load('frame.jpg'),(50,560)) #this will erase error and let me print again another error on the same place
				x,y = event.pos	#i'm taking pixel coordinates of my click
				
				for coordinateX in range (50,178): #NEW_GAME() event click!
					for coordinateY in range (700,732):
						if x == coordinateX and y == coordinateY:
							return 
							
				for coordinateX in range (300,380): #UNDO event click!
					for coordinateY in range (650,730):
						if x == coordinateX and y == coordinateY: 
								if (last_move[0] == WHITE) and (flag_undo == True): #flag_undo start false, but when i click once it becomes true
									pygame.draw.rect(screen,WHITE,((last_move[1]*50)+2,(last_move[2]*50)+2,46,46))
									hidden_grid[last_move[2]-1][last_move[1]-1] = 2
									flag_undo = False 
								elif (last_move[0] == RED) and (flag_undo == True):
									pygame.draw.rect(screen,RED,((last_move[1]*50)+2,(last_move[2]*50)+2,46,46))
									hidden_grid[last_move[2]-1][last_move[1]-1] = 0
									flag_undo = False 
								elif (last_move[0] == BLUE) and (flag_undo == True):
									pygame.draw.rect(screen,BLUE,((last_move[1]*50)+2,(last_move[2]*50)+2,46,46))
									hidden_grid[last_move[2]-1][last_move[1]-1] = 1
									flag_undo = False 
									
				for coordinateX in range (500,580): #HINT event click!
					for coordinateY in range (650,730):
						if (x == coordinateX) and (y == coordinateY) and (flag_hint == True):
							draw_hint = hints(create_grid,hidden_grid,hints_grid,num) # i have solution of only one(random)square
							posY = posY + 30
							if draw_hint[0] == 0: #i'll print on the screen this hint
								screen.blit(font.render('RED',1,BLACK),(665,posY))
								screen.blit(font.render(str(draw_hint[1]),1,BLACK),(610,posY))
								screen.blit(font.render(str(draw_hint[2]),1,BLACK),(650,posY))
								screen.blit(font.render('-',1,BLACK),(630,posY))
							elif draw_hint[0] == 1: #i'll print on the screen this hint
								screen.blit(font.render('BLUE',1,BLACK),(665,posY))
								screen.blit(font.render(str(draw_hint[1]),1,BLACK),(610,posY))
								screen.blit(font.render(str(draw_hint[2]),1,BLACK),(650,posY))
								screen.blit(font.render('-',1,BLACK),(630,posY))
							elif draw_hint[0] == 3: #no hint if i return 3 from my function
								screen.blit(font.render('No Hints!',1,BLACK),(620,posY))
							flag_hint = False
								
#~ this is the manager of my grids. In fact, all this condition check if i am in a 4x4 grid, 6x6 grid and more...
#~ when i click flag_undo and flag_hint becomes true and ready to work fine.
#~ last_move save my last move before the click, then i summon function mistakes and i check, every click, if user won(create_grid == hidden_grid)
#~ My grid is draw from 50 to 500 pixels. Then,with quotient_x and y i get position on the screen.				
				quotient_x = x // 50 #these two variables simplify a lot my code, and make it more readable
				quotient_y = y // 50
				if num == 4 and (quotient_x > 0) and (quotient_x < 5) and (quotient_y > 0) and (quotient_y < 5) and (hidden_grid[quotient_y-1][quotient_x-1] != 99) and (hidden_grid[quotient_y-1][quotient_x-1] != 89): #if i click in a 4x4 grid...
					flag_undo = True 
					flag_hint = True
					last_move = switch_color(quotient_x,quotient_y, screen,hidden_grid) #i save my last move to do undo
					flag_mistakes = mistakes(hidden_grid,num)
					win = victory(screen,create_grid, hidden_grid,num)
				elif num == 6 and (quotient_x > 0) and (quotient_x < 7) and (quotient_y > 0) and (quotient_y < 7) and (hidden_grid[quotient_y-1][quotient_x-1] != 99) and (hidden_grid[quotient_y-1][quotient_x-1] != 89): #if i click in a 6x6 grid...
					flag_undo = True
					flag_hint = True
					last_move = switch_color(quotient_x,quotient_y, screen,hidden_grid) #i save my last move to do undo
					flag_mistakes = mistakes(hidden_grid,num)
					win = victory(screen,create_grid, hidden_grid,num)
				elif num == 8 and (quotient_x > 0) and (quotient_x < 9) and (quotient_y > 0) and (quotient_y < 9) and (hidden_grid[quotient_y-1][quotient_x-1] != 99) and (hidden_grid[quotient_y-1][quotient_x-1] != 89): #if i click in a 8x8 grid...
					flag_undo = True
					flag_hint = True
					last_move = switch_color(quotient_x,quotient_y, screen,hidden_grid) #i save my last move to do undo
					flag_mistakes = mistakes(hidden_grid,num)
					win = victory(screen,create_grid, hidden_grid,num)
				elif num == 10 and (quotient_x > 0) and (quotient_x < 11) and (quotient_y > 0) and (quotient_y < 11) and (hidden_grid[quotient_y-1][quotient_x-1] != 99) and (hidden_grid[quotient_y-1][quotient_x-1] != 89): #if i click in a 10x10 grid...
					flag_undo = True
					flag_hint = True
					last_move = switch_color(quotient_x,quotient_y, screen,hidden_grid) #i save my last move to do undo
					flag_mistakes = mistakes(hidden_grid,num)
					win = victory(screen,create_grid, hidden_grid,num)
				
				if win == 1: #user win game and can decide to start new game!
					return
					
				if flag_mistakes[0] == True: #MISTAKES event! flag_mistakes is a list. it is false at the beginning. (see mistakes() function)
					screen.blit(pygame.image.load('error.png'),(60,570))
					screen.blit(font2.render(str(flag_mistakes[1]),1,BLACK),(130,585))
				elif flag_mistakes[0] == False:
					screen.blit(pygame.image.load('frame.jpg'),(50,560)) #this will erase error and let me print again another error on the same place
				
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update()
		
#changing colors on my grid and updating my multidimensional list "hidden_grid" where i have 0=RED 1=BLUE 2=WHITE
def switch_color(quotient_x,quotient_y, screen, hidden_grid): 
	if hidden_grid[quotient_y-1][quotient_x-1] == 0: #IF IT IS RED:
		hidden_grid[quotient_y-1][quotient_x-1] = 1
		pygame.draw.rect(screen,BLUE,(((quotient_x)*50)+2,((quotient_y)*50)+2,46,46))
		return (RED, quotient_x, quotient_y)
	elif hidden_grid[quotient_y-1][quotient_x-1] == 1: #IF IT IS BLUE:
		hidden_grid[quotient_y-1][quotient_x-1] = 2
		pygame.draw.rect(screen,WHITE,(((quotient_x)*50)+2,((quotient_y)*50)+2,46,46))
		return (BLUE, quotient_x, quotient_y)
	elif hidden_grid[quotient_y-1][quotient_x-1] == 2: #IF IT IS WHITE:
		hidden_grid[quotient_y-1][quotient_x-1] = 0
		pygame.draw.rect(screen,RED,(((quotient_x)*50)+2,((quotient_y)*50)+2,46,46))
		return (WHITE, quotient_x, quotient_y)


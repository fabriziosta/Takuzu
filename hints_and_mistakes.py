import pygame, sys, random
from pygame.locals import *
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0, 0, 255)

#if i already gave a hint for that position, i put a "5" in the grid, so i can't give to the user twice the same hint.
def hints(create_grid,hidden_grid,hints_grid,num): #user can ask for a hint once for every click he does!
	var = 0
	while var < 1000:
		x = random.randint(0,num-1) #getting random positions
		y = random.randint(0,num-1)
		if hidden_grid[x][y] != 99 and hidden_grid[x][y] != 89 and hints_grid[x][y] != 5: 
			hints_grid[x][y] = 5
			return (create_grid[x][y],x,y)
		var = var + 1
		if var == 1000: #if i don't get any good position for 1000times, i print "No hints!" on my window
			return (3,x,y)
			
#################################################################################################################################
#~ RULE 1 = Each row and column contains an equal number of 0s and 1s.	 
#~ RULE 2 = There is no more than two identical numbers adjacent to each other.			 
#~ RULE 3 = There is no identical row or column.

#~ I need to control all my grid every single user's click, without change anything.
#~ To do this, i start checking RULE 2 for rows and cols, than RULE 1 for rows and cols and then i can check RULE 3.
#~ Building my mistakes function in this way, let me to print on screen Rule 2, Rule 1 and Rule 3 with this order.
#~ In fact, if my function finds a Rule 2 and a Rule 3 error, he will prints Rule 2.

def mistakes(hidden_grid,num):
	mistakes_grid = [[0]*num for i in range(num)]
	
	for x in range(0,num): #copying all elements of hidden_grid in this new multidimensional list "mistakes_grid"
		for y in range(0, num): #converting 99 to 0 and 89 to 1. i put 99 and 89 to let UNDO event work, but here i don't need that.
			mistakes_grid[x][y] = hidden_grid[x][y]
			if mistakes_grid[x][y] == 99:
				mistakes_grid[x][y] = 0
			elif mistakes_grid[x][y] == 89:
				mistakes_grid[x][y] = 1
	
	for x in range(0,num):  #~ RULE 2 for rows
		for y in range(1, num-1):
			if mistakes_grid[x][y] == mistakes_grid[x][y-1] and mistakes_grid[x][y] == mistakes_grid[x][y+1]:
				if mistakes_grid[x][y] == 1 or mistakes_grid[x][y] == 0: #there are a lot of "2" on my grid(white squares), so i need to specify. i need to show errors only when more 1s or 0s are adjacent.
					flag = True #with this flag i enable program to print errors
					return (flag, "There is more than two identical squares adjacent")
					
	for y in range(0,num): #~ RULE 2 for cols
		for x in range(1, num-1): 
			if mistakes_grid[x][y] == mistakes_grid[x-1][y] and mistakes_grid[x][y] == mistakes_grid[x+1][y]: 
				if mistakes_grid[x][y] == 1 or mistakes_grid[x][y] == 0: #there are a lot of "2" on my grid(white squares), so i need to specify 
					flag = True #with this flag i enable program to print errors
					return (flag, "There is more than two identical squares adjacent")
	
	for x in range(0,num): #~ RULE 1 ~ I use this to count how many 1s i have in a row
		Row1 = 0 # i need to count red and blue squares to display RULE 1 error.
		Row0 = 0
		for y in range(0,num): 
			if mistakes_grid[x][y] == 1:
				Row1 = Row1 + 1
			elif mistakes_grid[x][y] == 0:
				Row0 = Row0 + 1
		if Row1 > num/2 or Row0 > num/2:
			flag = True
			return (flag, "There is a disequal number of red and blue squares")
		
	
	for y in range(0,num): #~ RULE 1 ~ I use this to count how many 1s i have in a column
		Col1 = 0 # i  count red and blue squares to display RULE 1 error.
		Col0 = 0
		for x in range(0,num): 
			if mistakes_grid[x][y] == 1:
				Col1 = Col1 + 1
			elif mistakes_grid[x][y] == 0:
				Col0 = Col0 + 1
		if Col1 > num/2 or Col0 > num/2:
			flag = True
			return (flag, "There is a disequal number of red and blue squares")
			
			
	for x in range(0,num): #~ RULE 3 ~ checking identical rows
		for y in range(x+1,num):
			if mistakes_grid[x] == mistakes_grid[y]:
				flag = True
				return (flag, "There is an identical row")
				
	
	for x in range(0,num-1): #~ RULE 3 ~ checking identical columns
		for z in range(x+1, num):
			count_identical_col = 0 #if this var is == num, 2 columns are identical
			for y in range(0,num):	 	
				if mistakes_grid[y][x] == mistakes_grid[y][z]:
					count_identical_col = count_identical_col + 1
				if count_identical_col == num:
					flag = True	
					return (flag, "There is an identical column")


	flag = False #if all that rules are respected i can exit from this function and i don't return any error
	return (flag, "")
	
				
#################################################################################################################################
#~ this function will check every time i click on my grid if user wins or not.
#~ After converting my victory_grid, i need to compare my solution grid (create_grid) with this one. 
#~ If user wins he joins an infinite loop where he can only click on new game, or close window.

def victory(screen,create_grid, hidden_grid,num): 
	font3 = pygame.font.Font ('freesansbold.ttf',16)
	victory_grid = [[0]*num for i in range(num)]
	
	for x in range(0,num): #copying all elements of hidden_grid in this new multidimensional list "victory_grid"
		for y in range(0, num): #converting 99 to 0 and 89 to 1.
			victory_grid[x][y] = hidden_grid[x][y]
			if victory_grid[x][y] == 99:
				victory_grid[x][y] = 0
			elif victory_grid[x][y] == 89:
				victory_grid[x][y] = 1
		
	if victory_grid == create_grid:
		screen.blit(pygame.image.load('frame.jpg'),(50,560)) #this will erase error and let me print again another error on the same place
		screen.blit(font3.render('YOU WIN! Do you want to play again? Press New Game',1,BLACK),(80,585))
		while 1:
			for event in pygame.event.get():		
				if event.type == MOUSEBUTTONDOWN:
					x,y = event.pos	#i'm taking pixel coordinates of my click
					
					for coordinateX in range (50,178): #NEW_GAME() event click!
						for coordinateY in range (700,732):
							if x == coordinateX and y == coordinateY:
								return 1 #i can't recall here new_game(), so i return 1 and recall new_game from drawing_grid.py sheet
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()




import random,sys
sys.setrecursionlimit(5000)

#INSTRUCTIONS

#With "checking_cols" and "checking_rows" i'm doing the following rules:
#~ RULE 1 = Each row and column contains an equal number of 0s and 1s.	  	  				RULE 1
#~ RULE 2 = There is no more than two identical numbers adjacent to each other.				RULE 2

#Now with "identical_rows" and "identical_cols" i'm doing the following rule:
#~ RULE 3 = There is no identical row or column.											RULE 3

#~ 1) I start from checking_rows, and i modify my grid(if needed) to respect RULE1 AND RULE2 for my rows. If my rows aren't modified i 
#~ go to checking_cols,if they are modified i recall checking_rows again. 

#~ 2) Now i am in checking_cols, and i modify my grid(if needed) to respect RULE1 AND RULE2 for my cols. If my cols aren't modified i 
#~ go to identical_rows, if they are modified i recall checking_rows AGAIN. 

#~ 3) Now i am in identical_rows, and i am checking if RULE3 is respected for my rows. If my grid has same rows, i randomize that row and
#~ i call back checking_rows again. If they are not modified i call identical_cols.

#~ 4) Now i am in identical_cols, and i am checking if RULE3 is respected for my cols. If my grid has same cols, i randomize that column and
#~ i call back checking_rows (starting from the beginning again). If they are not modified i have finished and i'm ready to play!

#################################################################################################################################
def checking_cols(create_grid,num):
	flag = False #it becomes true when cols are modified. If cols are not modified i don't need to recall checking_rows
	
	for y in range(0,num): #this "for" check all cols and put 0s and 1s where it is needed
		for x in range(1, num-1): #~ RULE 2 = There is no more than two identical numbers adjacent to each other.	
			if create_grid[x][y] == create_grid[x-1][y] and create_grid[x][y] == create_grid[x+1][y] and create_grid[x][y] == 1:
				create_grid[x][y] = 0
				flag = True
			elif create_grid[x][y] == create_grid[x-1][y] and create_grid[x][y] == create_grid[x+1][y] and create_grid[x][y] == 0:
				create_grid[x][y] = 1
				flag = True
		C1 = 0 #it will count 1s in my cols
		for i in range(0,num): #i use this to count how many 1s i have in a column
			if create_grid[i][y] == 1:
				C1 = C1 + 1
		while C1 < num/2: #~ RULE 1 = Each row and column contains an equal number of 0s and 1s.
			var = random.randint(0,num-1)
			if 	create_grid[var][y] == 0:
				create_grid[var][y] = 1
				C1 = C1 + 1
				flag = True
		while C1 > num/2: #~ RULE 1 = Each row and column contains an equal number of 0s and 1s.
			var = random.randint(0,num-1)
			if 	create_grid[var][y] == 1:
				create_grid[var][y] = 0		
				C1 = C1 - 1
				flag = True
	
	try:	#sometimes, some grids create an infinite loop, so i need to use try_except to avoid run time error!
		if flag == True:
			checking_rows(create_grid,num)
		elif flag == False:
			identical_rows(create_grid,num)
	except:
		for x in range(0,num): 
			for y in range(0,num):
				create_grid[x][y] = random.randint(0,1) #i randomize again all numbers
		checking_rows(create_grid,num)

#################################################################################################################################
def checking_rows(create_grid,num): 	
	flag = False #it becomes true when rows are modified.
	
	for x in range(0,num): #this "for" check all rows and put 0s and 1s where needed
		for y in range(1, num-1):  #~ RULE 2 = There is no more than two identical numbers adjacent to each other.
			if create_grid[x][y] == create_grid[x][y-1] and create_grid[x][y] == create_grid[x][y+1] and create_grid[x][y] == 1:
				create_grid[x][y] = 0
			elif create_grid[x][y] == create_grid[x][y-1] and create_grid[x][y] == create_grid[x][y+1] and create_grid[x][y] == 0:
				create_grid[x][y] = 1
		R1 = 0 #it will count 1s in my row
		for i in range(0,num): #i use this to count how many 1s i have in a row
			if create_grid[x][i] == 1:
				R1 = R1 + 1
		while R1 < num/2: #~ RULE 1 = Each row and column contains an equal number of 0s and 1s.
			var = random.randint(0,num-1)
			if 	create_grid[x][var] == 0:
				create_grid[x][var] = 1
				R1 = R1 + 1
				flag = True
		while R1 > num/2: #~ RULE 1 = Each row and column contains an equal number of 0s and 1s.
			var = random.randint(0,num-1)
			if 	create_grid[x][var] == 1:
				create_grid[x][var] = 0		
				R1 = R1 - 1
				flag = True
	
	
	try:	#sometimes, some grids create an infinite loop, so i need to use try_except to avoid run time error!
		if flag == True:
			checking_rows(create_grid,num)
		elif flag == False:
			checking_cols(create_grid,num)
	except:
		for x in range(0,num): 
			for y in range(0,num):
				create_grid[x][y] = random.randint(0,1) #i randomize again all numbers
		checking_rows(create_grid,num)
		
#################################################################################################################################
def identical_rows(create_grid,num): #~ RULE 3 = There is no identical row or column.
	flag = False
	for x in range(0,num): #checking identical rows
		for y in range(x+1,num):
			if create_grid[x] == create_grid[y]: #if there is an identical row i randomize that row and i recall "checking_rows"
				flag = True
				for i in range(0,num):
					create_grid[x][i] = random.randint(0,1)				
	if flag == True:
		checking_rows(create_grid,num)
	elif flag == False:
		identical_cols(create_grid,num)

#################################################################################################################################
def identical_cols(create_grid,num): #~ RULE 3 = There is no identical row or column.
	flag = False

	for x in range(0,num-1):
		for z in range(x+1, num):
			count_identical_num = 0 #if this var is == num, 2 columns are identical and i need to change it.
			for y in range(0,num):	 	
				if create_grid[y][x] == create_grid[y][z]:
					count_identical_num = count_identical_num + 1
				if count_identical_num == num:
					flag = True
					for b in range(0,num):
						create_grid[b][z] = random.randint(0,1)	

	if flag == True:
		checking_rows(create_grid,num)
	elif flag == False:
		print("Tabella soluzioni takuzu ")
		for z in range(0,num):	
			print (create_grid[z]) #print final result
		return create_grid

#################################################################################################################################
#This function got random position to show on the grid to help gamer to start his game!
#I'll get with randint random position and put it on my hide_grid some values from my solution grid(create_grid) to print it on the screen. 
def hide_part_of_the_grid(num,create_grid): 
	hide_grid = [[2]*num for i in range(num)] #create a filled multidimensional list.
	cont = 0 

	if num == 4:
		help_on_the_grid = 7
	elif num == 6:
		help_on_the_grid = 11
	elif num == 8:
		help_on_the_grid = 18
	elif num == 10:
		help_on_the_grid = 30

	while cont < help_on_the_grid:
		x = random.randint(0,num-1)
		y = random.randint(0,num-1)
		if hide_grid[x][y] == 2:
			hide_grid[x][y] = create_grid[x][y]
			cont = cont +1
	
	return hide_grid
#################################################################################################################################


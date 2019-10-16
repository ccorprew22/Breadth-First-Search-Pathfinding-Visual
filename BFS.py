import pygame

def findMove(grid, sRow, sCol, eRow, eCol, movelst):
    L, R, U, D = 'L', 'R', 'U', 'D'
    a = '' #initialize move placehollder
    #Left
    lst = []
    if (sCol-1) >= 0: #Checks for end of grid
        if grid[sRow][sCol-1] == 0: #Checks for wall or already checked square
            m = []
            m.append(sRow)
            m.append(sCol-1)
            lst.append(m)
            if len(movelst) < 4: #Loop to create potential route (BFS)
                movelst.append(L)
            else:
                b = movelst[0]
                a = b + 'L'
                movelst.append(a)
                
        elif sRow == eRow and sCol-1 == eCol:
            a = movelst[0] 
            return "Done" , a
    #Right
    if (sCol+1) < len(grid[0]):
        if grid[sRow][sCol+1] == 0:
            m = []
            m.append(sRow)
            m.append(sCol+1)
            lst.append(m)
            if len(movelst) < 4:
                movelst.append(R)
            else:
                b = movelst[0]
                a = b + 'R'
                movelst.append(a)
                
            
        elif sRow == eRow and sCol+1 == eCol:
            movelst[0] = movelst[0]
            a = movelst[0] 
            return "Done", a
    #Up
    if (sRow-1) >= 0:
        if grid[sRow-1][sCol] == 0:
            m = []
            m.append(sRow-1)
            m.append(sCol)
            lst.append(m)
            if len(movelst) < 4:
                movelst.append(U)
            else:
                b = movelst[0]
                a = b + 'U'
                movelst.append(a)
                
            
        elif sRow-1 == eRow and sCol == eCol:
            a = movelst[0]
            return "Done", a
    #Down
    if (sRow+1) < len(grid[0]):
        if grid[sRow+1][sCol] == 0:
            m = []
            m.append(sRow+1)
            m.append(sCol)
            lst.append(m)
            if len(movelst) < 4:
                movelst.append(D)
            else:
                b = movelst[0]
                a = b + 'D'
                movelst.append(a)
                
            
        elif sRow+1 == eRow and sCol == eCol:
            a = movelst[0]
            return "Done", a

    if len(movelst) > 4:
        movelst.pop(0)
         
    return lst, movelst



#BFS = BFS(rows)
movelst = []

#Colors
black = (0,0,0)
white = (255,255,255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0,0,255)
yellow = (255, 255, 0)

#Screen Size
width = 20
height = 20
margin = 5
sPos = []
grid = []



rows = 18
for row in range(rows):
    columns = []
    for column in range(rows):
        columns.append(0)
    grid.append(columns)

inc = 0
sCol = 0
sRow = 0
pygame.init()
BFS = []
WINDOW_SIZE = [255,255]
screen = pygame.display.set_mode((455, 455))

pygame.display.set_caption("Click 'S' for Start, 'E' for End, 'W' for Wall', 'P' for Play")

#Loop until the user clicks the close button.
done = False
SR = 0
SC = 0
clock = pygame.time.Clock()
eRow = 0
eCol = 0
new_nodes = []
count = 0
status = None

while not done:
    #Key commands
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_s]:
        status = 'start'
    elif pressed[pygame.K_w]:
        status = 'wall'
    elif pressed[pygame.K_e]:
        status = 'end'
    elif pressed[pygame.K_p]:
        status = 'play'
        
        
        
    for event in pygame.event.get():
        PLAY = pygame.USEREVENT+1
        pygame.time.set_timer(PLAY, 400) 
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            colum = pos[0] // (width+margin)
            row = pos[1] // (height + margin)
            
            if status == 'start':
                SR = row #START ROW
                SC = colum #START COL
                if len(sPos) != 0:
                    sPos[0] = row
                    sPos[1] = colum
                    print(sPos[0])
                grid[row][colum] = 1
                sRow = row
                sCol = colum
            elif status == 'wall':
                grid[row][colum] = 2
            elif status == 'end':
                grid[row][colum] = 3
                eRow = row
                eCol = colum
        elif status == 'play':
                PLAY = pygame.USEREVENT+1
                pygame.time.set_timer(PLAY, 100)
                if event.type == PLAY:
                    if len(new_nodes) == 0: 
                        nodes = findMove(grid, sRow, sCol, eRow, eCol, movelst) #returns list of moves. CREATE FOR LOOP TO RUN THROUGH EACH SUB LIST
                        movelst = nodes[1] #updating move list
                        
                        for i in range(len(nodes[0])):
                            sRow = nodes[0][i][0]
                            sCol = nodes[0][i][1]
                            
                            moves = [] 
                            moves.append(sRow)
                            moves.append(sCol)
                            new_nodes.append(moves)
                            if grid[sRow][sCol] == 3: #if node equal target, break loop
                                status = 'start'
                                break
                            grid[sRow][sCol] = 4 #making node red after checking for target
                            count += 1

                    else: #loop to do function for each individual node
                        place_holder = []
                        for i in range(len(new_nodes)):
                            sRow = new_nodes[i][0]
                            sCol = new_nodes[i][1]
                            
                            nodes = findMove(grid, sRow, sCol, eRow, eCol, movelst)
                            movelst = nodes[1] #Updating move list
                            
                            if nodes[0] == 'Done':
                                print(movelst)
                                status = 'BFS' #Sends loop to BFS
                                break
                            for j in range(len(nodes[0])):
                                r = nodes[0][j][0]
                                c = nodes[0][j][1]
                                moves = []
                                moves.append(r)
                                moves.append(c)
                                place_holder.append(moves)
                                if grid[r][c] == 3:
                                    status = 'start'
                                    break
                                grid[r][c] = 4
                        new_nodes = place_holder
                        count += 1
        if status == 'BFS': #SR SC
            GO = pygame.USEREVENT+2
            pygame.time.set_timer(GO, 100)
            if event.type == GO:
                #print(movelst[0])
                #while inc < len(movelst):
                #print(movelst[0][inc])
                if movelst[inc] == 'L':
                    SC -= 1
                    grid[SR][SC] = 5
                elif movelst[inc] == 'R':
                    SC += 1
                    grid[SR][SC] = 5

                elif movelst[inc] == 'U':
                    SR -= 1
                    grid[SR][SC] = 5

                elif movelst[inc] == 'D':
                    SR += 1
                    grid[SR][SC] = 5
                inc += 1
                if inc == len(movelst):
                    status = 'start'
                    
    screen.fill(black)
   

    for row in range(rows):
        
        for column in range(rows):
            color = white
            if grid[row][column] == 1:
                color = blue    
            elif grid[row][column] == 2:
                color = black
            elif grid[row][column] == 3:
                color = green
            elif grid[row][column] == 4:
                color = red
            elif grid[row][column] == 5:
                color = yellow
                
            pygame.draw.rect(screen, color, [(margin + width) * column + margin, (margin + height) * row + margin, width, height])

     
    clock.tick(60)
    
    pygame.display.flip()



pygame.quit()





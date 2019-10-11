import pygame

def findMove(grid, sRow, sCol, eRow, eCol):
    #Left
    lst = []
    if (sCol-1) >= 0: #Checks for end of grid
        if grid[sRow][sCol-1] == 0: #Checks for wall or already checked square
            m = []
            m.append(sRow)
            m.append(sCol-1)
            lst.append(m)
        elif sRow == eRow and sCol-1 == eCol:
            return 'Done'
    #Right
    if (sCol+1) < len(grid[0]):
        if grid[sRow][sCol+1] == 0:
            m = []
            m.append(sRow)
            m.append(sCol+1)
            lst.append(m)
        elif sRow == eRow and sCol+1 == eCol:
            return 'Done'
    #Up
    if (sRow-1) >= 0:
        if grid[sRow-1][sCol] == 0:
            m = []
            m.append(sRow-1)
            m.append(sCol)
            lst.append(m)
        elif sRow-1 == eRow and sCol == eCol:
            return 'Done'
    #Down
    if (sRow+1) < len(grid[0]):
        if grid[sRow+1][sCol] == 0:
            m = []
            m.append(sRow+1)
            m.append(sCol)
            lst.append(m)
        elif sRow+1 == eRow and sCol == eCol:
            return 'Done'
            
    return lst

def BFS(): #GATHERS MOVES AND FINDS FASTEST ROUTE
    return 'something'


#Colors
black = (0,0,0)
white = (255,255,255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0,0,255)

#Screen Size
width = 20
height = 20
margin = 5
sPos = []
grid = []
sPos = []

rows = 18
for row in range(rows):
    columns = []
    for column in range(rows):
        columns.append(0)
    grid.append(columns)

sCol = 0
sRow = 0
pygame.init()

WINDOW_SIZE = [255,255]
screen = pygame.display.set_mode((455, 455))

pygame.display.set_caption("Click 'S' for Start, 'E' for End, 'W' for Wall', 'P' for Play")

#Loop until the user clicks the close button.
done = False

clock = pygame.time.Clock()
eRow = 0
eCol = 0
new_nodes = []
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
                if len(sPos) != 0:
                    sPos[0] = row
                    sPos[1] = colum
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
                pygame.time.set_timer(PLAY, 400)
                if event.type == PLAY:
                    print("work")
                    if len(new_nodes) == 0: 
                        nodes = findMove(grid, sRow, sCol, eRow, eCol) #returns list of moves. CREATE FOR LOOP TO RUN THROUGH EACH SUB LIST
                        for i in range(len(nodes)):
                            sRow = nodes[i][0]
                            sCol = nodes[i][1]
                            moves = [] 
                            moves.append(sRow)
                            moves.append(sCol)
                            new_nodes.append(moves)
                            if grid[sRow][sCol] == 3: #if node equal target, break loop
                                status = 'start'
                                break
                            grid[sRow][sCol] = 4 #making node red after checking for target

                    else: #loop to do function for each individual node
                        place_holder = []
                        for i in range(len(new_nodes)):
                            sRow = new_nodes[i][0]
                            sCol = new_nodes[i][1]
                            nodes = findMove(grid, sRow, sCol, eRow, eCol)
                            if nodes == 'Done':
                                done = True
                            for j in range(len(nodes)):
                                r = nodes[j][0]
                                c = nodes[j][1]
                                moves = []
                                moves.append(r)
                                moves.append(c)
                                place_holder.append(moves)
                                if grid[r][c] == 3:
                                    status = 'start'
                                    break
                                grid[r][c] = 4
                        new_nodes = place_holder
                                
                               
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
                
                
            pygame.draw.rect(screen, color, [(margin + width) * column + margin, (margin + height) * row + margin, width, height])

     
    clock.tick(60)
    
    pygame.display.flip()



pygame.quit()



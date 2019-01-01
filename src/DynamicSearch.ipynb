# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
        

goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    closed =  [[0 for col in range(len(grid[0]))] for row in range(0,len(grid))]
    x = goal[0]
    y = goal[1]
    closed[x][y] = 1

    expand = [[99 for col in range(len(grid[0]))] for row in range(0,len(grid))]
   
    g = 0
 
  
    
    rows = len(grid)
    cols = len(grid[0])
    count =0
    tOpen = [[g,x,y]]
    open =[]
    Found = False
    
    while Found is False:
        #open=[]
        open = tOpen[:]
       
        #open.reverse()
        tOpen = []
        g+=cost
        #print (g)
        if len(open)==0 :
            #print ('Fail')
            #print (closed)
            return expand
        else :
            #for i in range(0,len(open)):
            open.sort()
            
            for i in range(len(open)):
                x = open[i][1]
                y = open[i][2]
                expand[x][y]= open[i][0]
              
                for d in range(0,len(delta)) :
                    dx=x+delta[d][0]
                    dy=y+delta[d][1]
                    
                    if dx>-1 and dy>-1 and dx<rows and dy<cols:
                        
                        #print (dx,dy,open)
                        if closed[dx][dy]!=1 and grid[dx][dy]!=1:
                           
                            closed[dx][dy]=1
                            #print (count,dx,dy, count+h,f,h,f>=(count+heuristic[dx][dy]))
                            #if  f>=(count+h):
                                
                            tOpen.append([g,dx,dy])
                          
                            
                     
result = compute_value(grid,goal,cost)   
for r in range(len(result)):
    print(result[r])

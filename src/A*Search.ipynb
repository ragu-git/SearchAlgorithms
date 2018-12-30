# -----------
# User Instructions:
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
# 
# If there is no path from init to goal,
# the function should return the string 'fail'
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost,heuristic):
    # ----------------------------------------
    # modify the code below
    # ----------------------------------------
    closed =  [[0 for col in range(len(grid[0]))] for row in range(0,len(grid))]
    x = init[0]
    y = init[1]
    closed[x][y] = 1

    expand = [[-1 for col in range(len(grid[0]))] for row in range(0,len(grid))]
    action = [[-1 for col in range(len(grid[0]))] for row in range(0,len(grid))]
   # expand[x][y] = 1
   # expand[goal[0]][goal[1]] = '*' 
    g = 0
    h = heuristic[x][y]
    f =g+ h
  
    
    rows = len(grid)
    cols = len(grid[0])
    count =0
    tOpen = [[f,g,h,x,y]]
    open =[]
    found = False
    
    while found is False :
        #open=[]
        open = tOpen[:]
       
        #open.reverse()
        tOpen = []
        g+=cost
        #print (g)
        if len(open)==0 :
            print ('Fail')
            print (closed)
            return 'Fail'
        else :
            #for i in range(0,len(open)):
            open.sort()
            
           
            x = open[0][3]
            y = open[0][4]
            expand[x][y]= count
            count+=1
            for d in range(0,len(delta)) :
                dx=x+delta[d][0]
                dy=y+delta[d][1]
                
                if dx>-1 and dy>-1 and dx<rows and dy<cols:
                    
                    #print (dx,dy,open)
                    if closed[dx][dy]!=1 and grid[dx][dy]!=1:
                        h = heuristic[dx][dy]
                        f =count+ h
                        closed[dx][dy]=1
                        #print (count,dx,dy, count+h,f,h,f>=(count+heuristic[dx][dy]))
                        #if  f>=(count+h):
                            
                        tOpen.append([f,g,h,dx,dy])
                            
                        action[dx][dy]= d
                           
                            
                       # print(delta_name[d],dx,dy,goal[0],goal[1])
                        #print(goal[0]==dx and goal[1]==dy)
                        if goal[0]==dx and goal[1]==dy:
                            found = True
                            open = tOpen[:]
                            #print(closed) 
                            #open.sort()
                            expand[dx][dy]= count
                            
                            
                            return expand
                        
    
print(search(grid,init,goal,cost,heuristic))

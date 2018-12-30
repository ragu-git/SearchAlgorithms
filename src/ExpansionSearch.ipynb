# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. Note that the 'v' should be 
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']



def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    closed = [[0 for col in range(len(grid[0]))] for row in range(0,len(grid))]
    #closed[init[0]][init[1]]=1
    action = [[' ' for col in range(len(grid[0]))] for row in range(0,len(grid))]
    
    rows = len(grid)
    cols = len(grid[0])
    #print (rows , cols,closed,goal,grid)
    x= init[0]
    y= init[1]
    g=0
    tOpen = [[g,x,y]]
    open =[]
    found = False
    
    while found is False :
        #open=[]
        open = tOpen[:]
        tOpen = []
        g+=cost
        #print (g)
        if len(open)==0 :
            print ('Fail')
            return action
        else :
            for i in range(0,len(open)):

                x = open[i][1]
                y = open[i][2]
                for d in range(0,len(delta)) :
                    dx=x+delta[d][0]
                    dy=y+delta[d][1]
                    
                    if dx>-1 and dy>-1 and dx<rows and dy<cols:
                       # print (dx,dy)
                        if closed[dx][dy]!=1 and grid[dx][dy]!=1:
                            tOpen.append([g,dx,dy])
                            closed[dx][dy]=1
                            
                            action[dx][dy]= d
                           # print(delta_name[d],dx,dy,goal[0],goal[1])
                            #print(goal[0]==dx and goal[1]==dy)
                            if goal[0]==dx and goal[1]==dy:
                                found = True
                                open = tOpen[:]
                                #print(closed) 
                                #expanded.sort()
                                #print (action)
                                plan = [[' ' for col in range(len(grid[0]))] for row in range(0,len(grid))]
                                x=goal[0]
                                y=goal[1]
                                plan[x] [y]='*'
                                while x!=init[0] or y!=init[1]:
                                    
                                    x2=x - delta[action[x][y]][0]
                                    y2=y - delta[action[x][y]][1] 
                                    plan[x2][y2]=delta_name[action[x][y]]
                                    x=x2
                                    y=y2
                                return plan
                            
                
        
            

result =search(grid,init,goal,cost)

    
for i in range(len(result)):
    print(result[i])

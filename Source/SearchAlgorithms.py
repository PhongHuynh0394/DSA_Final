from Space import *
from Constants import *
import time
import math

def TraceBack(g:Graph, sc:pygame.Surface, father:list):
    ''''
    Vẽ lại đường đi ngắn nhất theo father
    '''
    goal = g.goal.value
    path = []

    while goal != g.start.value:
        path.append(goal)
        goal = father[goal]

    path.append(g.start.value)
    for i in range(len(path)+1):
        
        if path[i] == g.start.value:
            g.grid_cells[path[i]].set_color(orange)
            g.grid_cells[path[i]].draw(sc)
            pygame.display.flip()
            break

        if i == 0:
            g.grid_cells[path[i]].set_color(purple)
        else:
            g.grid_cells[path[i]].set_color(grey)

        begin = path[i]
        end = path[i+1]
        pygame.draw.line(sc,green,(g.grid_cells[begin].x,g.grid_cells[begin].y),(g.grid_cells[end].x,g.grid_cells[end].y))
        g.grid_cells[path[i]].draw(sc)
        pygame.display.flip()
        time.sleep(0.1)


def DFS(g:Graph, sc:pygame.Surface):
    print('Implement DFS algorithm')

    open_set = [g.start.value]
    closed_set = []
    father = [-1]*g.get_len()

    while open_set:
        #pop stack
        current = open_set.pop()
        current_node = g.grid_cells[current]
        current_node.set_color(yellow) #set current cell to yellow
        current_node.draw(sc)
        pygame.display.flip()
        time.sleep(0.01)

        #Check goal and trace back
        if (g.is_goal(current_node)):
            TraceBack(g, sc, father)
            break

        nei = g.get_neighbors(current_node)
        #nei.reverse()
        #Check each neighbor and change color
        for neighbor_node in g.get_neighbors(current_node):
            #Check if neighbor is totally new one
            if (neighbor_node.value not in closed_set):
                open_set.append(neighbor_node.value) #Add to open_set (stack)
                neighbor_node.set_color(red) #Change color to red
                father[neighbor_node.value] = current #Set father of neighbor
                neighbor_node.draw(sc)
                pygame.display.flip()
                time.sleep(0.01)
        
        #add current to close_set
        closed_set.append(current)
        current_node.set_color(blue) #change close_set elements to blue
        current_node.draw(sc)
        pygame.display.flip()
        time.sleep(0.01)


def BFS(g:Graph, sc:pygame.Surface):
    print('Implement BFS algorithm')

    open_set = [g.start.value]
    closed_set = []
    father = [-1]*g.get_len()
   
    while open_set:
        #pop queue
        current = open_set.pop(0)
        current_node = g.grid_cells[current]
        current_node.set_color(yellow) #set current cell to yellow
        current_node.draw(sc)
        pygame.display.flip()
        time.sleep(0.01)

        #Check goal and trace back
        if (g.is_goal(current_node)):
            TraceBack(g, sc, father)
            break

        #get list of neighbors of current
        neighbor = []
        neighbor = g.get_neighbors(current_node)

        #Check each neighbor and change color
        for value in range(len(neighbor)):
            i = neighbor[value].value
            neighbor_node = g.grid_cells[i]

            #Check if neighbor is totally new one
            if (neighbor_node.value not in open_set) and (neighbor_node.value not in closed_set):
                open_set.append(neighbor_node.value) #Add to open_set (queue)
                neighbor_node.set_color(red) #Change color to red
                father[neighbor_node.value] = current #Set father of neighbor
                neighbor_node.draw(sc)
                pygame.display.flip()
                time.sleep(0.01)
  
        #add current to close_set
        closed_set.append(current)
        current_node.set_color(blue) #change close_set elements to blue
        current_node.draw(sc)
        pygame.display.flip()
        time.sleep(0.01)
    

def UCS(g:Graph, sc:pygame.Surface):

    print('Implement UCS algorithm')
    open_set = {}
    open_set [g.start.value] = 0
    closed_set:list[int] = [] 
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len() #set infinity
    cost[g.start.value] = 0

    #Run till queue empty
    while open_set:

        #pop queue
        min_val = min(open_set.values()) #Get min cost
        open_min_val = [val for val, Cost in open_set.items() if Cost == min_val]
        #current = list(open_set.keys())[0] #Get first node value
        current = open_min_val.pop(0)
        open_set.pop(current) #pop first element from queue
        current_node = g.grid_cells[current]

        #Set color and draw
        current_node.set_color(yellow)
        current_node.draw(sc)
        pygame.display.flip()
        time.sleep(0.01)
        
        #Check goal
        if g.is_goal(current_node):
            print(f"\nCOST FROM",g.start.value,"TO",current,"IS",cost[current_node.value]) #print out cost to goal from start
            TraceBack(g, sc, father) #draw path from goal back to start
            break

        #get neighbor of current
        neighbor = {} #use to the get min way in neighbor node

        for neighbor_node in g.get_neighbors(current_node):
            #Check neighbor_node haven't been in closed_set
            if neighbor_node.value not in closed_set:
                #modify neightbor_node
                neighbor_node.set_color(red) #change color
                neighbor_node.draw(sc)
                pygame.display.flip()
                time.sleep(0.01)

                #update cost, father and add to neightbor dict when cost neighbor smaller than itself before
                if cost[neighbor_node.value] > (math.sqrt((neighbor_node.x - current_node.x)**2 + (neighbor_node.y - current_node.y)**2) + cost[current]):
                    cost[neighbor_node.value] =  math.sqrt((neighbor_node.x - current_node.x)**2 + (neighbor_node.y - current_node.y)**2) + cost[current]
                    #neighbor[neighbor_node.value] = cost[neighbor_node.value] #add to neighbor list
                    open_set[neighbor_node.value] = cost[neighbor_node.value]
                    father[neighbor_node.value] = current #set father
        
        #Add current to closed_set
        closed_set.append(current)
        current_node.set_color(blue) #change close_set elements to blue
        current_node.draw(sc)
        pygame.display.flip()
        time.sleep(0.01)

def Dijkstra(g:Graph, sc:pygame.Surface):
    '''
    Duyệt tất cả các đỉnh và trả về mảng chứ khoảng cách ngắn nhất đến mọi đỉnh
    '''
    print('Implement Dijkstra algorithm')
    open_set = {}
    open_set [g.start.value] = 0
    closed_set:list[int] = [] 
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len() #set infinity
    cost[g.start.value] = 0

    #Run till queue empty
    while open_set:

        #pop queue
        min_val = min(open_set.values()) #Get min cost
        open_min_val = [val for val, Cost in open_set.items() if Cost == min_val]
        current = open_min_val.pop(0) #
        open_set.pop(current) #pop first element from queue
        current_node = g.grid_cells[current]

        #Set color and draw
        current_node.set_color(yellow)
        current_node.draw(sc)
        pygame.display.flip()
        time.sleep(0.01)
        
        #Check goal
        if g.is_goal(current_node):
            current_node.set_color(purple)
            current_node.draw(sc)
            pygame.display.flip()
            time.sleep(0.01)

        #get neighbor of current

        for neighbor_node in g.get_neighbors(current_node):
            #Check neighbor_node haven't been in closed_set
            if neighbor_node.value not in closed_set:
                #modify neightbor_node
                neighbor_node.set_color(red) #change color
                neighbor_node.draw(sc)
                pygame.display.flip()
                time.sleep(0.01)

                #update cost, father and add to neightbor dict when cost neighbor smaller than itself before
                if cost[neighbor_node.value] > (math.sqrt((neighbor_node.x - current_node.x)**2 + (neighbor_node.y - current_node.y)**2) + cost[current]):
                    cost[neighbor_node.value] =  math.sqrt((neighbor_node.x - current_node.x)**2 + (neighbor_node.y - current_node.y)**2) + cost[current]
                    #neighbor[neighbor_node.value] = cost[neighbor_node.value] #add to neighbor list
                    open_set[neighbor_node.value] = cost[neighbor_node.value]
                    father[neighbor_node.value] = current #set father
        
        #Add current to closed_set
        closed_set.append(current)
        current_node.set_color(blue) #change close_set elements to blue
        current_node.draw(sc)
        pygame.display.flip()
        time.sleep(0.01)
    

    TraceBack(g,sc,father)
    #Show cost
    print(f"\nCOST FROM",g.start.value,"TO ALL VERTICES:")
    print(cost)

def Heuristic(point:Node, target:Node):
    '''Estimate distance of both node on screen'''
    return abs(point.x - target.x) + abs(point.y - target.y) #Taxicab distance

def AStar(g:Graph, sc:pygame.Surface):
    print('Implement A* algorithm')

    cost = [100_000]*g.get_len() #set infinity to all vertex haven't visited yet
    cost[g.start.value] = 0    
    open_set = {}
    open_set [g.start.value] = Heuristic(g.start,g.goal) + cost[g.start.value]
    closed_set = []
    father = [-1]*g.get_len()

    while open_set:
        #Get current node with minimum F (F = heuristic + cost)
        min_val = min(open_set.values()) #Get min f
        open_min_val = [val for val, f in open_set.items() if f == min_val]
        current = open_min_val.pop(0) 
        open_set.pop(current) #pop element min f
        current_node = g.grid_cells[current]
        current_node.set_color(yellow)
        current_node.draw(sc)
        pygame.display.flip()
        time.sleep(0.01)

        #Check goal
        if g.is_goal(current_node):
            TraceBack(g,sc,father)
            break

        #Get neightbor
        for neighbor_node in g.get_neighbors(current_node):
            if (neighbor_node.value not in closed_set):
                #Set color
                neighbor_node.set_color(red)
                neighbor_node.draw(sc)
                pygame.display.flip()
                time.sleep(0.01)

                #update neighbor node information
                if cost[neighbor_node.value] > (math.sqrt((neighbor_node.x - current_node.x)**2 + (neighbor_node.y - current_node.y)**2) + cost[current]):
                    cost[neighbor_node.value] =  math.sqrt((neighbor_node.x - current_node.x)**2 + (neighbor_node.y - current_node.y)**2) + cost[current]
                    open_set[neighbor_node.value] = cost[neighbor_node.value] + Heuristic(neighbor_node,g.goal) #add f = cost + h to neighbor
                    father[neighbor_node.value] = current #set father

        #Add current to closed_set
        closed_set.append(current)
        current_node.set_color(blue) #change close_set elements to blue
        current_node.draw(sc)
        pygame.display.flip()
        time.sleep(0.01)
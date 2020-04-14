# -*- coding: utf-8 -*-
from queue import PriorityQueue

import networkx as nx
import matplotlib.pyplot as plt 
import random

class PathSearch(object):
    X = nx.Graph()
    nodes_dict= {}
    search_label = 0
    Helper = 0
    START = 0
    GOAL = 0
    
    #Private methods:
    def __AddNodes(self,quantity):        
        #Grid-like with uniform spaces 
        #position varies dependent of 'height' variable
        last_node = 0
        height = 0
        for i in range(0,quantity):
            for j in range(0,quantity):
                self.nodes_dict[j+last_node] = (j,height)#(height,j) #orientation
            last_node = last_node + quantity
            height = height +1
        self.X.add_nodes_from(self.nodes_dict.keys())
        return    
    def __AddEdges(self,quantity):
        #Bilateral Edges
        for i in self.X.nodes:
            for j in range(0,3):
                #Verifie existence of node
                if self.X.has_node(i+1) and (i+1)%quantity is not 0:
                    self.X.add_edge(i,i+1, color = 'black') #from i to i+1 = right
                if self.X.has_node(i+quantity): #and (i+quantity)%quantity is not 0:
                    self.X.add_edge(i,i+quantity, color = 'black') #from i to i+quantity    = up
                if self.X.has_node(i+quantity+1) and (i+quantity+1)%quantity is not 0:
                    self.X.add_edge(i,i+quantity+1, color = 'black') #from i to i+qauntity+1  = diag_up_right
                if self.X.has_node(i-quantity+1) and (i-quantity+1)%quantity is not 0:
                    self.X.add_edge(i,i-quantity+1, color = 'black') #from i to i-quantity+1  = diag_down_right
        return
    #Public Methods
    def CreateRegularGraph(self,size):
        #Creates a mesh-like structure as regular matrix of order equal to 'size'
        self.__AddNodes(size)
        self.__AddEdges(size)
        self.Helper = size
        return
    def Display(self):
        # Show the plot in non-blocking mode
        
        
        plt.show(block=False)
        plt.figure(figsize=(10,10))
        
        nx.draw_networkx_nodes(self.X, self.nodes_dict, node_size=8, node_color='blue', alpha=0.3)        
        nx.draw_networkx_labels(self.X, self.nodes_dict, font_size=0)

        edges = self.X.edges()
        colors = [self.X[u][v]['color'] for u,v in edges]
        
        nx.draw_networkx_edges(self.X, self.nodes_dict, width = 2, edge_color=colors, alpha=0.75)
        
        if self.search_label is 1:
            plt.title('A* Search')
        elif self.search_label is 2:
            plt.title('No Heuristic Search')
        else:
            plt.title('No Search Performed')
        plt.savefig("Graph.pdf", format="PDF")
        plt.show()
        
    def DeleteRandom(self):
        #Delete between helper and ((helper*helper)/2)
        #delete nodes randomly
        max_nodes= (self.Helper*self.Helper) -1
        to_delete = random.randrange(self.Helper,int(max_nodes/2))
        #for i in range( int(max_nodes/2) ):
        for i in range(to_delete):
            rn = random.randrange(0,max_nodes)
            if self.X.has_node(rn) is False or rn is self.START or rn is self.GOAL:
                continue
            else:
                self.X.remove_node(rn)
        return
    
    def heuristic(self,a, b):
        aX = self.nodes_dict.get(a)[0]
        aY = self.nodes_dict.get(a)[1]
        bX = self.nodes_dict.get(b)[0]
        bY = self.nodes_dict.get(b)[1]
        return abs(aX - bX) + abs(aY - bY)
    
    def AStar(self,StartX,StartY, GoalX,GoalY):
        start = StartX + (self.Helper*StartY)
        goal  = GoalX  + (self.Helper*GoalY )
        self.START = start
        self.GOAL = goal
        pathSize = 0
        
        if self.X.has_node(start) is False or self.X.has_node(goal) is False:
            print("Start or goal doesn't exist")
            return 0
        #Using priority queue
        Pawn = PriorityQueue()
        Pawn.put(start, 0)
        came_from = {}
        Score = {}
        came_from[start] = None
        Score[start] = 0
        while not Pawn.empty():
            current = Pawn.get()        
            if current == goal:
                break
            for Next in self.X.neighbors(current):
                tentative_score = Score[current]
                if Next not in Score or tentative_score < Score[Next]:
                    Score[Next] = tentative_score
                    fScore = tentative_score + self.heuristic(goal, Next)
                    Pawn.put(Next, fScore)
                    came_from[Next] = current
        #print( came_from.items())
        #print( came_from.keys())        
        #Now return the path
        returnPath = {}
        returner = goal        
        while returner is not start:
            returnPath.update({returner:came_from[returner]})
            #Since adding an edge that already exists updates the edge data.
            #Change color of edges
            self.X.add_edge(returner, came_from[returner], color = 'R')
            returner = came_from[returner]
            pathSize = pathSize + 1
        print (returnPath.items())
        self.search_label = 1
        return pathSize
    def BreadthFirstSearch(self,StartX,StartY, GoalX,GoalY):
        #Coordinates
        #Start && Gaol = node labeled as: 
        #(Start)(Goal)X + quantity*(Start)(Gaol)Y
        
        #start = self.X.node[StartX + (self.Helper*StartY)]
        #goal  = self.X.node[GoalX  + (self.Helper*GoalY )]
        
        ###        
        #nodes = list(self.X.nodes)        
        #start = nodes[StartX + (self.Helper*StartY)]
        #goal  = nodes[GoalX  + (self.Helper*GoalY )]        
        #frontier = Queue()
        #frontier.put(start)        
        ###
        """
        frontier = Queue()
        frontier.put(start )
        came_from = {}
        came_from[start] = None
        
        while not frontier.empty():
           current = frontier.get()
        
           if current == goal: 
              break           
        
           for next in graph.neighbors(current):
              if next not in came_from:
                 frontier.put(next)
                 came_from[next] = current
        """
        self.search_label = 2
        return
def main():
    A= PathSearch()
    A.CreateRegularGraph(20)    
    """
    print(A.nodes_dict.get(355)[0])
    print(A.nodes_dict.get(355)[1])
    print(A.nodes_dict.items())
    """
    A.DeleteRandom()
    print("path size was ",A.AStar(0,0,15,19))
    #print("Helper was ",A.Helper)
    A.Display()        
if __name__ == '__main__':  
    main()


"""
#Direct Code for printing
    X = nx.Graph()
    nodes_dict= {}
    last_node = 0
    height = 0
    #
    for i in range(0,5):
        for j in range(0,5):
            nodes_dict[j+last_node] = (height,j)
        last_node = last_node + 5
        height = height +1
            
    X.add_nodes_from(nodes_dict.keys())
    
    #
    for i in X.nodes:
        for j in range(0,3):
            #if exist
            if X.has_node(i+1) and (i+1)%5 is not 0:
                X.add_edge(i,i+1) #from i to i+1           = right
            if X.has_node(i+5):
                X.add_edge(i,i+5) #from i to i+quantity    = up
            if X.has_node(i+5+1)and (i+1+5)%5 is not 0:
                X.add_edge(i,i+5+1) #from i to i+qauntity+1  = diag_up_right
            if X.has_node(i-5+1) and (i-5+1)%5 is not 0:
                X.add_edge(i,i-5+1) #from i to i-quantity+1  = diag_down_right
    
    #
    nx.draw(X,nodes_dict)
    
    nx.draw_networkx_labels(X,nodes_dict)
    
    plt.title('A* search')
    plt.show()
"""
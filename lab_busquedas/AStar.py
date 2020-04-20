# -*- coding: utf-8 -*-
from queue import PriorityQueue

import networkx as nx
import matplotlib.pyplot as plt
import random
import math


class PathSearch(object):
    X = nx.Graph()
    nodes_dict = {}
    search_label = 0
    Helper = 0
    START = 0
    GOAL = 0

    # Creational methods:
    def __AddNodes(self, quantity):
        # Grid-like with uniform spaces
        # position varies dependent of 'height' variable
        last_node = 0
        height = 0
        for i in range(0, quantity):
            for j in range(0, quantity):
                self.nodes_dict[j + last_node] = (j, height)  # (height,j) #orientation
            last_node = last_node + quantity
            height = height + 1
        self.X.add_nodes_from(self.nodes_dict.keys())
        return

    def __AddEdges(self, quantity):
        # Bilateral Edges
        for i in self.X.nodes:
            for j in range(0, 3):
                # Verifie existence of node
                if self.X.has_node(i + 1) and (i + 1) % quantity is not 0:
                    self.X.add_edge(i, i + 1, color='silver')  # from i to i+1 = right
                if self.X.has_node(i + quantity):  # and (i+quantity)%quantity is not 0:
                    self.X.add_edge(i, i + quantity, color='silver')  # from i to i+quantity    = up
                if self.X.has_node(i + quantity + 1) and (i + quantity + 1) % quantity is not 0:
                    self.X.add_edge(i, i + quantity + 1, color='silver')  # from i to i+qauntity+1  = diag_up_right
                if self.X.has_node(i - quantity + 1) and (i - quantity + 1) % quantity is not 0:
                    self.X.add_edge(i, i - quantity + 1, color='silver')  # from i to i-quantity+1  = diag_down_right
        return

    def CreateRegularGraph(self, size):
        # Creates a mesh-like structure similar to a regular matrix of order equal to 'size'
        self.__AddNodes(size)
        self.__AddEdges(size)
        self.Helper = size
        self.__DeleteRandom()
        return

    # Deletes nodes randomly
    def __DeleteRandom(self):
        max_nodes = (self.Helper * self.Helper)
        to_delete = (max_nodes * 20) / 100
        # to_delete = random.randrange(self.Helper, int(max_nodes / 2))

        nodes_deleted = 0
        print("Height of the graph:", self.Helper)
        i = 0
        while i < to_delete:
            rn = random.randrange(0, max_nodes)
            if self.X.has_node(rn) is False:
                continue
            elif (rn == self.START) or (rn == self.GOAL):
                continue
            else:
                self.X.remove_node(rn)
                nodes_deleted += 1
            i = i + 1

        print("Nodes deleted:", nodes_deleted)
        return

    # saves the graph in the local directory and displays the graph
    def Display(self):
        # Show the plot in non-blocking mode
        plt.show(block=False)
        plt.figure(figsize=(10, 10))

        nx.draw_networkx_nodes(self.X, self.nodes_dict, node_size=8, node_color='gray', alpha=0.3)
        nx.draw_networkx_labels(self.X, self.nodes_dict, font_size=0)

        edges = self.X.edges()
        colors = [self.X[u][v]['color'] for u, v in edges]

        nx.draw_networkx_edges(self.X, self.nodes_dict, width=2, edge_color=colors, alpha=0.75)

        if self.search_label is 1:
            plt.title('Result')
        elif self.search_label is 2:
            plt.title('Result')
        else:
            plt.title('No Search Performed')
        plt.savefig("Result.pdf", format="PDF")
        plt.show()

    # Simple heuristic, determines the distance between a pair of nodes
    def heuristic(self, a, b):
        aX = self.nodes_dict.get(a)[0]
        aY = self.nodes_dict.get(a)[1]
        bX = self.nodes_dict.get(b)[0]
        bY = self.nodes_dict.get(b)[1]
        return math.sqrt((bX - aX) ** 2 + (bY - aY) ** 2)  # Euclidean distance
        # return abs(aX - bX) + abs(aY - bY)       #Manhattan distance

    def blindSearch(self, StartX, StartY, GoalX, GoalY):
        self.START = StartX + (self.Helper * StartY)
        self.GOAL = GoalX + (self.Helper * GoalY)
        if (self.X.has_node(self.START) is False) or (self.X.has_node(self.GOAL) is False):
            print("Start or goal doesn't exist")
            return 0
        path = []
        nodossinhijos = []
        path.append(self.START)
        nodossinhijos.append(self.START)

        current = path[0]
        while current != self.GOAL:
            vecinos = []
            for i in self.X.neighbors(current):
                if i not in path and i not in nodossinhijos:
                    vecinos.append(i)
            if len(vecinos) > 0:
                current = vecinos[0]
                path.append(current)
            else:
                nodossinhijos.append(current)
                path.pop(-1)

        returnPath = path
        returnPath.reverse()
        returner = returnPath[0]
        i = 0
        while i < len(returnPath) - 1:
            if i == 0 or i == len(returnPath) - 2:
                self.X.add_edge(returner, returnPath[i + 1], color='blue')
            else:
                self.X.add_edge(returner, returnPath[i + 1], color='red')
            returner = returnPath[i + 1]
            i = i + 1
        self.search_label = 2
        return len(returnPath)

    def AStar(self, StartX, StartY, GoalX, GoalY):
        self.START = StartX + (self.Helper * StartY)
        self.GOAL = GoalX + (self.Helper * GoalY)
        pathSize = 0
        if (self.X.has_node(self.START) is False) or (self.X.has_node(self.GOAL) is False):
            print("Start or goal doesn't exist")
            return 0
        # Delete Nodes
        # self.__DeleteRandom()
        # Using priority queue
        Pawn = PriorityQueue()
        Pawn.put(self.START, 0)
        came_from = {}
        Score = {}
        came_from[self.START] = None
        Score[self.START] = 0
        while not Pawn.empty():
            current = Pawn.get()
            if current == self.GOAL:
                break
            for Next in self.X.neighbors(current):
                tentative_score = Score[current] + self.heuristic(current, self.GOAL)
                if Next not in Score or tentative_score < Score[Next]:
                    Score[Next] = tentative_score
                    fScore = tentative_score + self.heuristic(self.GOAL, Next)
                    Pawn.put(Next, fScore)
                    came_from[Next] = current
                    # Now return the path
        returnPath = {}
        returner = self.GOAL
        while returner is not self.START:
            returnPath.update({returner: came_from[returner]})
            # Since adding an edge that already exists updates the edge data.
            # Change color of edges
            self.X.add_edge(returner, came_from[returner], color='green')
            returner = came_from[returner]
            pathSize = pathSize + 1
        # print (returnPath.items())
        self.search_label = 1
        return pathSize


def main():
    A = PathSearch()
    numberNodes = 20
    A.CreateRegularGraph(numberNodes)
    Sx, Sy = 12,7
    Gx, Gy = 15,15
    print("Path size with Blind Search was: ", A.blindSearch(Sx, Sy, Gx, Gy))
    print("Path size with A* was: ", A.AStar(Sx, Sy, Gx, Gy))
    A.Display()


if __name__ == '__main__':
    main()

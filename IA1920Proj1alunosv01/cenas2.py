import math
import pickle
import time

class SearchProblem:

    def __init__(self, goal, model, auxheur = []):
        self.goal = goal
        self.model = model
        self.auxheur = auxheur
        self.awnser = []
        self.g = []
        self.h = []
        self.f = []

    def h(self, current, goal):
        return math.sqrt(pow(self.auxheur[current][0] - self.auxheur[goal][0], 2) + pow(self.auxheur[current][1] - self.auxheur[goal][0], 2))


    def search(self, init, limitexp = 2000, limitdepth = 10, tickets = [math.inf,math.inf,math.inf]):
        #set the lists values to 0
        initialize_list(self.g, 114, 0)
        initialize_list(self.h, 114, 0)
        initialize_list(self.f, 114, 0)
        return 0        
        
        
    def A_star(self, init, limitexp, limitdepth, tickets):
            
        open_list = []          #nodes visited but not expanded
        closed_list = []        #nodes visited and expanded

        open_list.append(init)

        while(len(open_list) > 0) {
            current = lowest_f(open_list)
            open_list.remove(current)
            closed_list.append(current)

            #Breaking point
            if(current = self.goal):
                return closed_list
            
            #Generate the children points
            for(child in self.model[current]):
                
                #check if child was already expanded
                if child is in closed_list:
                    continue

                #check if child was already discovered
                elif child is in open_list:
                    
                    #check if new g value is better than the old one
                    if (h(self, current, child) + g[current]) > g[child]:
                        continue
                    else
                        g[child] = g[current] + h(current, child)
                        h[child] = h(child, self.goal)
                        f[child] = g[child] + h[child]
                        continue
                
                #if not discovered, initialize it and add it to the open_list
                else:
                    g[child] = g[current] + h(current, child)
                    h[child] = h(child, self.goal)
                    f[child] = g[child] + h[child]
                    open_list.append(child)
                    continue

        }

        return []



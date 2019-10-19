import math
import pickle
import time


class SearchProblem:

    def __init__(self, goal, model, auxheur = []):
        self.goal = goal
        self.model = model
        self.auxheur = auxheur

    def search(self, init, limitexp = 2000, limitdepth = 10, tickets = [math.inf,math.inf,math.inf]):

        def func(lst, n):
            '''Receives a list of list with two integers and a integer and returns the sublist with the integer'''
            for x in lst:
                if x[1] == n:
                    return x
            return

        def A_star(self, init, limitexp, limitdepth, tickets):

            #def function_g(child, parent):
            #    coords_P = self.auxheur[parent[0] - 1]
            #    coords_C = self.auxheur[child - 1]
            #    return math.sqrt(pow(coords_P[0] - coords_C[0], 2) + pow(coords_P[1] - coords_C[1], 2)) + parent[1]

            def function_h(child):
                '''Receives a integer that represents a node and return its distance to the goal'''
                coords_C = self.auxheur[child - 1]
                coords_G = self.auxheur[self.goal[0] - 1]
                return math.sqrt(pow(coords_C[0] - coords_G[0], 2) + pow(coords_C[1] - coords_G[1], 2))

            def least_f(open_list):
                '''Receives a list and returns the element of the list with the lowest h'''
                min_i = 0
                min = open_list[0][1]
                list_lenght = len(open_list) - 1
                for i in range(1, list_lenght, 1):
                    if open_list[i][1] < min:
                        min = open_list[i][1]
                        min_i = i

                return open_list[min_i]

            def inList(i, lst):
                '''Receives a integer and a list and returns True if the integer is in the list'''
                for x in lst:
                    if x == i:
                        return True

                return False

            def tb(lst):
                '''Receives the closed_list and does traceback returning a list with the path from the initial node to the goal'''
                awnser = []
                list_lenght = len(lst) - 1
                parent = lst[list_lenght][2]
                awnser.append(lst[list_lenght][0])
                for i in range(list_lenght - 1, -1, -1):
                    if lst[i][0] == parent:
                        parent = lst[i][2]
                        awnser.insert(0, lst[i][0])
                return awnser

            ############################################################################

            open_list = []
            closed_list = []
            awnser = []
            h = function_h(init[0])
            open_list.append((init[0], h, -1))

            while len(open_list) > 0:
                current = least_f(open_list)
                open_list.pop(open_list.index(current))
                closed_list.append(current)

                if current[0] == self.goal[0]:
                    return tb(closed_list)

                for child in self.model[current[0]] :

                    if inList(child[1], closed_list):
                        continue

                    #g = function_g(child[1], current)
                    h = function_h(child[1])

                    #for x in open_list:
                    #    if x[0] == child[1] and g + h > x[1]:
                    #        print('ola')
                    #        continue

                    open_list.append((child[1], h, current[0]))

    #######################################################################################################################################################

        awnser = A_star(self = self, init = init, limitexp = limitexp, limitdepth = limitdepth, tickets = tickets)
        list_lenght = len(awnser)
        aux = awnser[0]                                 #
        awnser[0] = [[], [aux]]                         #
        for i in range(1, list_lenght, 1):              #   transforming the output into the required one
            x = func(self.model[aux], awnser[i])        #
            awnser[i] = [[x[0]], [x[1]]]                #
            aux = x[1]                                  #

        return awnser

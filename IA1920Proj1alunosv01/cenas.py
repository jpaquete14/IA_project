import math
import pickle
import time


class SearchProblem:

    def __init__(self, goal, model, auxheur = []):
        self.goal = goal
        self.model = model
        self.auxheur = auxheur
        self.awnser = []

    def search(self, init, limitexp = 2000, limitdepth = 10, tickets = [math.inf,math.inf,math.inf]):
        ###################################################################################################################################3

        def A_star(self, init, limitexp, limitdepth, tickets):
            #################################################################

            def A_star_Aux(self, init, vertice, list):
                list_aux = []
                list_vertice = self.model[vertice]
                for x in list_vertice:
                    aux = self.auxheur[x[1]]
                    h = math.sqrt(pow(aux[1] - self.auxheur[init][1], 2) + pow(aux[0] - self.auxheur[init][0], 2))
                    g = math.sqrt(pow(aux[1] - self.auxheur[self.goal[0]][1], 2) + pow(pow(aux[0] - self.auxheur[self.goal[0]][0], 2)))
                    list_aux.append((x[1], g + h))

                list.append(list_aux)
                min = list[0][0]
                aux_x = 0
                aux_i = 0
                for x in list:
                    for i in x:
                        if i[1] < min[1]:
                            min = i
                            aux_x = x

                list.pop(list.index(aux_x[aux_i]))
                self.awnser.append(min[1])

                if min[1] == goal[0]:
                    return list

                else :
                    n = list.index(aux_x)
                    n = n + 1

                    for j in range(len(self.awnser), n, -1)):
                        self.awnser.pop(j)

                    list = A_star_Aux(init = init, vertice = min[1], list = list)
                    return list

        #########################################################################
            list = []
            self.awnser.append(init[0])
            list = A_star_Aux(init = init[0], vertice = init[0], list = list)
            pass

    #######################################################################################################################################################
    A_star(init = init, limitexp = limitexp, limitdepth = limitdepth, tickets = tickets)
    return self.awnser

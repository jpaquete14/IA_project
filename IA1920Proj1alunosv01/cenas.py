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
                    h = math.sqrt(pow(aux[1] - self.auxheur[init][1], 2) + pow(aux[0] - self.auxheur[init][0], 2))                  #calculo do h atraves das coordenadas
                    g = math.sqrt(pow(aux[1] - self.auxheur[self.goal[0]][1], 2) + pow(aux[0] - self.auxheur[self.goal[0]][0], 2))  #calculo do g atraves das coordenadas
                    list_aux.append((x[1], g + h))                                                                                  #acrescenta à list_aux o tuplo (vertice adjacente, g + h)

                list.append(list_aux)                       #acrescenta a lista_aux à lista principal
                min = list[0][0]                            #  ---------------------------------------
                aux_x = 0                                   # ----------------------------------------
                aux_i = 0                                   # --------------------------------------
                print(min[1])                               # ------------------------------------
                for x in list:                              # escolhe o vertice da lista com o menor g + h
                    for i in x:                             # ------------------------------------
                        if i[1] < min[1]:                   # ------------------------------------
                            min = i                         # -------------------------------------
                            aux_x = x                       # ---------------------------------------

                print(list)
                aux_x.pop(aux_x.index(min))                 # retira da lista o vertice com menor g + h
                print(list)
                self.awnser.append(min[0])                  # acrescenta o vertice à lista com a resposta

                if min[1] == self.goal[0]:
                    return list                             # caso de paragem, caso seja o vertice que pretende atingir

                else :
                    n = list.index(aux_x)
                    n = n + 2

                    print(self.awnser)

                    for j in range(len(self.awnser), n, -1):
                        self.awnser.pop(j)                          # caso o vertice com o menor g + h não tenha acabado de ser descoberto,
                                                                    # apaga os valores que estao a mais na lista resposta

                    print("---------Nova---------")
                    list = A_star_Aux(self = self, init = init, vertice = min[0], list = list)
                    return list

        #########################################################################
            list = []
            self.awnser.append(init[0])
            list = A_star_Aux(self = self, init = init[0], vertice = init[0], list = list)
            pass

    #######################################################################################################################################################
        A_star(self = self, init = init, limitexp = limitexp, limitdepth = limitdepth, tickets = tickets)
        return self.awnser

import math
import pickle
import time


class SearchProblem:

    def __init__(self, goal, model, auxheur = []):
        self.goal = goal
        self.model = model
        self.auxheur = auxheur

    def search(self, init, limitexp = 2000, limitdepth = 10, tickets = [math.inf,math.inf,math.inf]):

        def part_of_list(element, lst):
            '''Receives a integer and a list and returns True if the integer is in the list'''
            for x in lst:
                if x == element:
                    return True

            return False

        def check(answer_i, answer_aux, j):
            #loop going through answer_i starting from the new inserted element
            answer_length = len(answer_i)
            for i in range(j, answer_length, 1):
                #checking if the elements of the new list are already occupied
                if part_of_list(answer_i[j], answer_aux[j]):
                    return False

            return True

        def fix(answer_i, answer_aux, j):
            #loop going through answer_i starting from the inserted element
            answer_length = len(answer_i)
            for i in range(j, answer_length, 1):
                # checking if the new element is marked as occupied in his previous time
                if part_of_list(answer_i[i], answer_aux[i - 1]):
                    #if so removes it from answer_aux
                    answer_aux[i-1].pop(answer_aux[i-1].index(answer_i[i]))

            return answer_aux

        def trata_pares(answer_i, diff, answer_aux):
            #basically adds to the path a adjcent node and the goal node as many times as needed until diff is 0
            answer_length = len(answer_i)
            while diff != 0:
                #loop going through the adjcent nodes of the goal node
                aux = answer_i[answer_length - 1]
                for x in self.model[aux]:
                    #TODO Improvement: only use one function, go through list one time
                    #if the adjcent node or the goal node is already occupied
                    if part_of_list(x[1], answer_aux[answer_length]) or part_of_list(aux, answer_aux[answer_length + 1]):
                        continue

                    #adding to the path a adjcent node and the goal node
                    answer_i.append(x[1])
                    answer_i.append(aux)
                    break

                diff = diff - 2

            return answer_i

        def trata_impares(answer_i, answer_aux):
            #basically goes through the path trying to add a node to it in order to make his length even
            answer_length = len(answer_i)
            for i in range(answer_length - 2, -1, -1):
                #loop going through the list of adjecent nodes of every element
                for x in self.model[answer_i[i]]:
                    #if adjcent node is already occupied
                    if part_of_list(x[1], answer_aux[i + 1]):
                        continue

                    #checking if there is any node that can be a intermediary node for two consecutive nodes of the path
                    if find_node(self.model[x[1]], answer_i[i + 1]):
                        answer_i.insert(i + 1, x[1])
                        #checking if answer_i after inserting the new element is in conflict with awnser_aux
                        if check(answer_i, answer_aux, i + 1):
                            #removing from answer_aux the changed nodes from their previous time
                            awnser_aux = fix(answer_i, answer_aux, i + 2)
                            break

                        else:
                            answer_i.pop(i + 1)

            return [answer_i, answer_aux]

        def same_time(answer, answer_aux):
            lengths = []
            max = 0
            max_i = 0

            #loop going through the answer
            answer_length = len(answer)
            for i in range(0, answer_length, 1):
                #finding the element with the highest length
                if len(answer[i]) > max:
                    max = len(answer[i])
                    max_i = i

                #adding that length to lengths
                lengths.append(len(answer[i]))

            #loop going through lengths
            lengths_length = len(lengths)
            for i in range(0, lengths_length, 1):
                #if it is the element with the highest lenght
                if lengths[i] == max:
                    continue
                #difference between the highest length and the element length
                diff = max - lengths[i]
                #if diff is even
                if (diff % 2) == 0:
                    #calling trata_pares
                    answer[i] = trata_pares(answer[i], diff, answer_aux)

                else:
                    #aux is a list with 2 elements the first is the changed path and the second is answer_aux
                    #trata_impares makes the length of the path even
                    aux = trata_impares(answer[i], answer_aux)
                    answer_i = aux[0]
                    answer_aux = aux[1]
                    #after making the length of the path even calls trata_pares
                    answer[i] = trata_pares(answer[i], diff - 1, answer_aux)

                #updates the answer_aux according to the path
                answer_aux = fix_answer_aux(answer[i], answer_aux)

            return answer

        def find_node(lst, n):
            '''Receives a list of list with two integers and a integer and returns the sublist with the integer'''
            for x in lst:
                if x[1] == n:
                    return x
            return

        def fix_answer_aux(answer_i, answer_aux):
            #loop going through answer_i
            list_length = len(answer_i)
            for i in range(0, list_length, 1):
                #if the length one of the elements is higher than answer_aux
                if i == len(answer_aux):
                    #adds the element of that position to the answer_aux
                    answer_aux.append([answer_i[i]])

                else:
                    #checking if the element its already there
                    if part_of_list(answer_i[i], answer_aux[i]):
                        continue

                    #if not adds it
                    else:
                        aux = answer_aux[i]
                        aux.append(answer_i[i])
                        answer_aux[i] = aux

            return answer_aux

        def function_h(child, i):
            '''Receives a integer that represents a node and return its distance to the goal'''
            coords_C = self.auxheur[child - 1]
            coords_G = self.auxheur[self.goal[i] - 1]
            return math.sqrt(pow(coords_C[0] - coords_G[0], 2) + pow(coords_C[1] - coords_G[1], 2))

        def least_h(open_list, answer_aux):
            '''Receives a list and returns the element of the list with the lowest h'''
            min_i = 0
            min = open_list[0][1]

            #loop going through the open_list
            list_length = len(open_list)
            answer_length = len(answer_aux) - 1
            for i in range(1, list_length, 1):

                #if the answer_aux length is higher than the expansion order of the node
                if answer_length >= open_list[i][3]:
                    #checks if the node is part of answer_aux
                    if part_of_list(open_list[i][0], answer_aux[open_list[i][3]]):
                        #if so this node cant be expanded
                        continue

                #finding the lowest h in the open_list
                if open_list[i][1] < min:
                    min = open_list[i][1]
                    min_i = i

            return open_list[min_i]

        def inList(i, lst):
            '''Receives a integer and a list and returns True if the integer is in the list'''
            for x in lst:
                if x[0] == i:
                    return True

            return False

        def tb(lst):
            '''Receives the closed_list and does traceback returning a list with the path from the initial node to the goal'''
            answer = []
            list_length = len(lst) - 1
            parent = lst[list_length][2]
            answer.append(lst[list_length][0])
            for i in range(list_length - 1, -1, -1):
                if lst[i][0] == parent:
                    parent = lst[i][2]
                    answer.insert(0, lst[i][0])
            return answer


        def A_star(self, init, tickets, i, answer_aux):

            open_list = []
            closed_list = []
            h = function_h(init[i], i)
            # 4th element of the list is the expansion order
            open_list.append([init[i], h, -1, 0])

            while len(open_list) > 0:
                current = least_h(open_list, answer_aux)
                open_list.pop(open_list.index(current))
                closed_list.append(current)

                if current[0] == self.goal[i]:
                    return tb(closed_list)

                for child in self.model[current[0]] :

                    if inList(child[1], closed_list):
                        continue

                    h = function_h(child[1], i)

                    open_list.append([child[1], h, current[0], current[3] + 1])

    #######################################################################################################################################################

        answer = []                 # list where the paths will be before function same_time
        answer_aux = []             # list that has the positions that are occupied per time
        true_answer = []            # list where the answer will be put after same_time

        #loop going through the list with the initial positions
        init_length = len(init)
        for i in range(0, init_length, 1):
            #calculating each path according to the positions in awnser_aux
            answer_i = A_star(self = self, init = init, tickets = tickets, i = i, answer_aux = answer_aux)
            #adding the path to the answer
            answer.append(answer_i)
            #updating answer_aux according to path
            answer_aux = fix_answer_aux(answer_i, answer_aux)

        #making every path finish at the same time
        answer = same_time(answer, answer_aux)


        cities = []                                                     #
        for x in answer:                                                #
            cities.append(x[0])                                         #
                                                                        #
        true_answer.append([[],cities])                                 #
                                                                        #
        list_length = len(answer[0])                                    #
        for i in range(1, list_length, 1):                              #   tranforming answer into the required output
            transp = []                                                 #
            cities = []                                                 #
            for x in answer:                                            #
                z = find_node(self.model[x[i - 1]], x[i])               #
                transp.append(z[0])                                     #
                cities.append(z[1])                                     #
                                                                        #
            true_answer.append([transp, cities])                        #

        return true_answer

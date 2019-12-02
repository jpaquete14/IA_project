import random

# LearningAgent to implement
# no knowledeg about the environment can be used
# the code should work even with another environment
class LearningAgent:

        # init
        # nS - maximum number of states
        # nA - maximum number of action per state
        # Actions - number of actions already done
        # path - sequence of state already visited
        # goal - par of states with highest reward addiction
        # N.visited - list with the states that havent been visited
        # environment - information about every visited state
        def __init__(self,nS,nA):
            self.nS = nS
            self.nA = nA
            self.k = 0
            self.f = 0
            self.Actions = 0
            self.iA = float("-inf")
            self.path = []
            self.goal = []
            self.testPath = []
            self.N_visited = []
            self.parent_R = [-1, float("-inf")]
            for i in range(1, nS):
                self.N_visited.append(i)

            self.environment = [[]]
            for i in range(1, nS + 1):
                self.environment.append([])

        # Select one action, used when learning
        # st - is the current state
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontolearn(self,st,aa):
            self.Actions = self.Actions + 1
            if self.iA == float("-inf"):
                self.iA = st

            try:
                self.N_visited.remove(st)
                self.environment[st].append(aa)
                #later used to store the reward
                self.environment[st].append([])
            except:
                pass

            self.path.append(st)


            #TODO find a better way to chose action
            a = -1
            j = -1
            if len(self.N_visited) != 0:
                for i in range(0, len(aa) - 1):
                    #if state not visited
                    try:
                        if len(self.environment[aa[i]]) == 0:
                            a = i
                            break
                    #tries to find his parent
                        elif aa[i] == self.path[-2]:
                            j = i
                    except:
                        pass

                #if all states have already been visited
                if a == -1:
                    self.path.pop(-1)
                    #chooses his parent
                    if j != -1:
                        a = j
                    #the choice is random
                    else:
                        a = random.randint(0, len(aa) - 1)

            return a

        # Select one action, used when evaluating
        # st - is the current state
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontoexecute(self,st,aa):

            def part_of_list(element, lst):
                '''Receives a integer and a list and returns True if the integer is in the list'''
                for x in lst:
                    if x == element:
                        return True
                return False

            # print("select one action to learn better")
            a = 0
            #print(st)
            #print("aa - " + str(aa))
            #print(self.testPath)
            #print(self.goal)
            #print(part_of_list(st, self.goal))
            if st == self.iA:
                self.flag = 0
                self.k = 0

            if not part_of_list(st, self.goal):
                if self.flag == 0:
                    for i in range(0, len(aa)):
                        if aa[i] == self.testPath[self.k]:
                            a = i
                            self.k = self.k + 1
                            break

            else:
                self.flag = 1
                if st == self.goal[0]:
            #        print(self.goal[0])
            #        print("i - ")
                    for i in range(0, len(aa)):
            #            print(i)
                        if aa[i] == self.goal[1]:
                            a = i

                elif st == self.goal[1]:
            #        print(self.goal[1])
            #        print("i - ")
                    for i in range(0, len(aa)):
            #            print(i)
                        if aa[i] == self.goal[0]:
                            a = i
            #    print(aa[i])
            #print("---------")
            # print("select one action to see if I learned")
            return a


        # this function is called after every action
        # st - original state
        # nst - next state
        # a - the index to the action taken
        # r - reward obtained
        def learn(self,ost,nst,a,r):

            #######################################################################################################
            def part_of_list(element, lst):
                '''Receives a integer and a list and returns True if the integer is in the list'''
                for x in lst:
                    if x == element:
                        return True
                return False

            def my_copy(lst):
                new_list = []
                for x in lst:
                    new_list.append(x.copy())
                return new_list

            def BFS(graph, num):
                closed_list = []
                open_list = []
                graph[self.goal[num]].append(0)
                open_list.append(self.goal[num])
                while (len(open_list) > 0):

                    current = open_list.pop(0)

                    for elem in graph[current][0]:

                        if len(graph[elem]) == 0:
                            continue

                        if part_of_list(elem, closed_list):
                            continue

                        if isinstance(graph[elem][-1], int):
                            if graph[current][- 1] + 1 < graph[elem][-1]:
                                graph[elem].append(graph[current][- 1] + 1)
                        else:
                            graph[elem].append(graph[current][- 1] + 1)

                        open_list.append(elem)

                    closed_list.append(current)

                return
            #########################################################################################################

            #adds reward
            if len(self.environment[ost][1]) == 0:
                self.environment[ost][1].append(r)

            changedGoal = False

            #stores the goal after taking action
            if len(self.goal) < 2:
                self.goal.append(ost)

            else:
                try:
                    if (self.environment[self.goal[0]][1][0] + self.environment[self.goal[1]][1][0]) < (r + self.parent_R[1]):
                        self.goal[0] = self.parent_R[0]
                        self.goal[1] = ost
                        changedGoal = True
                except:
                    #if (self.environment[self.goal[0]][1][0] + self.environment[self.goal[1]][1][0]) < (r + self.parent_R[1]):
                    #    self.goal[0] = self.parent_R[0]
                    #    self.goal[1] = ost
                    #    changedGoal = True

                    pass

            if changedGoal:
                self.k = 0
                self.flag = 0
                #TODO encontrar a razao pela qual a BFS n chega aos estados todos
                self.testPath.clear()

                #for i in range(0, len(self.environment) - 1):
                #    print(str(i) + " - " + str(self.environment[i]))

                copy1 = my_copy(self.environment)
                copy2 = my_copy(self.environment)

                BFS(copy1, 0)
                BFS(copy2, 1)


                min = float("inf")
                if (copy1[1][2] < min):
                    min = self.goal[0]
                    graph = my_copy(copy1)


                if (copy2[1][2] < min):
                    min = self.goal[1]
                    graph = my_copy(copy2)

                #for i in range(0, len(self.environment) - 1):
                #    print(str(i) + " - " + str(self.environment[i]))


                #for i in range(0, len(graph) - 1):
                #    print(str(i) + " - " + str(graph[i]))

                self.testPath.append(self.iA)

                state = self.testPath[-1]
                print(state)
                k = float("inf")
                k_state = float("-inf")
                while state != min:
                    #TODO em caso de empate escolhe o que tem o maior reward
                    for elem in graph[state][0]:

                        if len(graph[elem]) < 3:
                            continue

                        if graph[elem][2] < k:
                            k = graph[elem][2]
                            k_state = elem


                    self.testPath.append(k_state)
                    state = self.testPath[-1]

                self.testPath.pop(0)

            #if limit of actions achieved clears path
            if self.Actions == self.nA :
                self.Actions = 0
                self.path.clear()
                self.parent_R = [-1, float("-inf")]

            else:
                self.parent_R = [ost, r]

            return


        def printGraph(self):
            print(self.iA)
            print(self.N_visited)

            for i in range(0, len(self.environment) - 1):
                print(str(i) + " - " + str(self.environment[i]))

            print("goal - "  + str(self.goal))

            print(self.testPath)

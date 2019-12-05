#Joao Paquete - 89477 || Tomas Inacio - 89553 || Grupo 16

import random

def index_max(self, lst, st):
    max = float("-inf")
    index_max = 0
    for el in self.q_table[st]:
        #check highest q value
        for i in range (0, len(lst)):
            if self.q_table[st][i][0] > max:
                max = self.q_table[st][i][0]
                index_max = i
    return index_max

def index_min(self, lst, st):
    min = float("+inf")
    index_min = 0
    for el in self.q_table[st]:
        #check highest q value
        for i in range (0, len(lst)):
            if self.q_table[st][i][1] < min:
                min = self.q_table[st][i][1]
                index_min = i
    return index_min

class LearningAgent:

        def __init__(self,nS,nA):
            self.nS = nS
            self.nA = nA
            self.alpha = 0.5
            self.gamma = 0.9
            self.epsilon = 0.5
            #Q_TABLE inicialization
            self.q_table = []
            for i in range (0, nS + 1):
                #list for each state that contains the possible actions
                self.q_table.append([])

        def selectactiontolearn(self,st,aa):
            #action list initialization
            if not self.q_table[st]:
                for i in range (0, len(aa)):
                    self.q_table[st].append([0, 0])

            if random.uniform(0, 1) < self.epsilon:      # Exploration
                try:
                    a = index_min(self, aa, st)
                except:
                    a = random.randint(0, len(aa) - 1)  #just to avoid an unexpected stoppage of the program

                self.q_table[st][a][1] += 1
            else:                                   # Exploitation
                try:
                    a = index_max(self, aa, st)
                except:
                    a = random.randint(0, len(aa) - 1)  #just to avoid an unexpected stoppage of the program

            return a


        def selectactiontoexecute(self,st,aa):
            #action list initialization
            if not self.q_table[st]:
                for i in range (0, len(aa)):
                    self.q_table[st].append(0)
            try:
                a = index_max(self, aa, st)
            except:
                a = random.randint(0, len(aa) - 1) #just to avoid an unexpected stoppage of the program

            return a


        def learn(self,ost,nst,a,r):

            old_q = self.q_table[ost][a][0]
            next_max = max(self.q_table[nst] or [0]) #Prevents empty list case

            if next_max == 0:
                next_max = [next_max]

            new_q = (1 - self.alpha) * old_q + self.alpha * (r + self.gamma * next_max[0])
            self.q_table[ost][a][0] = new_q

            return

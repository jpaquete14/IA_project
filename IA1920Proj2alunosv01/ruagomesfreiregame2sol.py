import random

def index_max(self, lst, st):
    max = float("-inf")
    index_max = 0
    for el in self.q_table[st]:
        #check highest q value
        for i in range (0, len(lst)):
            if self.q_table[st][i] > max:
                max = self.q_table[st][i]
                index_max = i
    return index_max

class LearningAgent:

        def __init__(self,nS,nA):
            self.nS = nS
            self.nA = nA
            self.alpha = 0.5
            self.gamma = 0.9
            self.epsilon = 0.3
            #Q_TABLE inicialization
            self.q_table = []
            for i in range (0, nS):
                #list for each state that contains the possible actions
                self.q_table.append([])

        def selectactiontolearn(self,st,aa):
            #action list initialization
            if not self.q_table[st]:
                for i in range (0, len(aa)):
                    self.q_table[st].append(0)

            a = 0
            if random.uniform(0, 1) < self.epsilon:      # Exploration
                a = random.randint(0, len(aa) - 1)
            else:                                   # Exploitation
                a = index_max(self, aa, st)

            return a


        def selectactiontoexecute(self,st,aa):
            #action list initialization
            if not self.q_table[st]:
                for i in range (0, len(aa)):
                    self.q_table[st].append(0)

            a = index_max(self, aa, st)

            return a


        def learn(self,ost,nst,a,r):

            old_q = self.q_table[ost][a]
            next_max = max(self.q_table[nst] or [0]) #Prevents empty list case

            new_q = (1 - self.alpha) * old_q + self.alpha * (r + self.gamma * next_max)
            self.q_table[ost][a] = new_q

            return

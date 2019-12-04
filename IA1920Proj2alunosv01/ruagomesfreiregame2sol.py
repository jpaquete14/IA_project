import random
import numpy as np

#Globa Variables for Q table calculation
alpha = 0.1
gamma = 0.5
epsilon = 0.5

# LearningAgent to implement
# no knowledeg about the environment can be used
# the code should work even with another environment
class LearningAgent:

        # init
        # nS maximum number of states
        # nA maximum number of action per state
        def __init__(self,nS,nA):

                self.nS = nS
                self.nA = nA
                
                #Q_TABLE inicialization
                self.q_table = []
                for i in range (0, nS):
                        #list for each state that contains the possible actions
                        self.q_table.append([]) 
                #######################
        

        # Select one action, used when learning  
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontolearn(self,st,aa):
                # print("select one action to learn better")

                def index_max(lst):
                        max = float("-inf")
                        index_max = 0
                        for el in self.q_table[st]:
                                #check highest q value
                                for i in range (0, len(aa)):
                                        if self.q_table[st][i] > max:
                                                max = self.q_table[st][i]
                                                index_max = i
                        return index_max

                #action list initialization
                if not self.q_table[st]:       
                        for i in range (0, len(aa)):
                                self.q_table[st].append(0)


                a = 0
                if random.uniform(0, 1) < epsilon:      # Exploration
                        a = random.randint(0, len(aa) - 1) 

                else:   # Exploitation
                        a = index_max(aa)

                return a

        # Select one action, used when evaluating
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontoexecute(self,st,aa):

                def index_max(lst):
                        max = float("-inf")
                        index_max = 0
                        for i in range (0, len(lst)):
                                if self.q_table[st][i] > max:
                                        max = self.q_table[st][i]
                                        index_max = i
                        return index_max

                 #action list initialization (Dont know if needed)
                if not self.q_table[st]:       
                        for i in range (0, len(aa)):
                                q_table[st].append(0)

                a = index_max(aa)

                # print("select one action to see if I learned")
                return a


        # this function is called after every action
        # ost - original state
        # nst - next state
        # a - the index to the action taken
        # r - reward obtained
        def learn(self,ost,nst,a,r):
                #print("learn something from this data")

                old_q = self.q_table[ost][a]
                next_max = max(self.q_table[nst] or [0]) #Prevents empty list case
        
                new_q = (1 - alpha) * old_q + alpha * (r + gamma * next_max)
                self.q_table[ost][a] = new_q
                
                return

        
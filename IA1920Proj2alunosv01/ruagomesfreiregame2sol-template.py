import random
import numpy

#Globa Variables for Q table calculation
alpha = 0,1
gamma = 0,7
epsilon = 0,7

# LearningAgent to implement
# no knowledeg about the environment can be used
# the code should work even with another environment
class LearningAgent:

        # init
        # nS maximum number of states
        # nA maximum number of action per state
        def __init__(self,nS,nA):

                # define this function
                self.nS = nS
                self.nA = nA
                self.q_table = np.zeros([nS, nA])


                # define this function
              
        
        # Select one action, used when learning  
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontolearn(self,st,aa):
                # define this function
                # print("select one action to learn better")
                
                a = 0
                if random.uniform(0, 1) < epsilon:
                        a = random.randint(0, len(aa) - 1) # Exploration
                else:
                        a = index_max(st, aa) # Exploitation

                # define this function
                return a

        # Select one action, used when evaluating
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontoexecute(self,st,aa):

                # define this function
                a = index_max(st, aa)

                # print("select one action to see if I learned")
                return a


        # this function is called after every action
        # ost - original state
        # nst - next state
        # a - the index to the action taken
        # r - reward obtained
        def learn(self,ost,nst,a,r):
                # define this function
                #print("learn something from this data")

                old_q = self.q_table[ost, a]
                next_max = np.max(self.q_table[nst])
        
                new_q = (1 - alpha) * old_q + alpha * (r + gamma * next_max)
                self.q_table[ost, a] = new_q
                
                return

        def index_max(self, lst):
                max = float("-inf")
                index_max = 0
                for i in range (0, len(lst)):
                        if self.q_table[st][i - 1] > max:
                                max = self.q_table[st][i]
                                index_max = i
        
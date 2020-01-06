import random

#Set up a class.
class Agent():
    def __init__ ( self, x, y, environment, agents, neighbourhood):
        self.environment = environment
        self.store = 0
        self.agents = agents
        self.neighbourhood = neighbourhood
        
#Adjust x and y in the agent.           
        if x == None:
            self.x = random.randint(0,300)
        else:
            self.x = x   
        if y == None:
            self.y = random.randint(0,300)
        else:
            self.y = y
            
#This function makes sure that points move in the range between 0 and 300.            
    def move(self):
         if random.random() < 0.5:
            self.x = (self.x + 1) % 300
         else:
            self.x = (self.x - 1) % 300

         if random.random() < 0.5:
            self.y = (self.y + 1) % 300
         else:
            self.y = (self.y - 1) % 300
#This function shows the process of eating.           
    def eat(self): 
         if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10

#This funcation caluclates the distance between self and a parameter:    
    def distance_between(self, agent):
        """ This funcation caluclated the distance beteen self and a
        Parameters:
            a is an agent
        Returns:
            a numerical distance
        """
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 

#This function makes neighbours interact with each other.    
    def share_with_neighbours(self):
        
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= self.neighbourhood:
               sum = self.store + agent.store
               ave = sum /2
               self.store = ave
               agent.store = ave
               
               print("sharing " + str(dist) + " " + str(ave))  
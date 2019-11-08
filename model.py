import random
import operator
import matplotlib.pyplot
import agentframework

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

#f = open("in.txt", 'r')
#data = []
#for line in f:
    #parsed_line = str.split(line,",")
    #data_line = []
    #for word in parsed_line:
        #data_line.append(float(word))
    #data.append(data_line)
#print(data)


f = open("in.txt", 'r')
environment = []
for row in f:
    parsed_row = str.split(row,",")
    rowlist = []
    for value in parsed_row:
        rowlist.append(float(value))
    environment.append(rowlist)
print(environment)


num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        agents[i].move()
        agents[i].eat()
        
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

distances = []
for agents_row_a in agents:
    distance = []
    for agents_row_b in agents:
        distance.append(distance_between(agents_row_a, agents_row_b))
    distances.append(distance)
    
    
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()    

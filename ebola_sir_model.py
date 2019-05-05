import numpy as np
import json
import os
from random import randint
import matplotlib.pyplot as plt

def loadData(path):
    """Load the simulation conditions from .json file"""
    #Check file being exists and that it is a JSON file
    assert path[-5:] == ".json" and os.path.isfile(path), "File not found or incorrect file type"
    #Attempt to load file and parse the JSON content
    data = json.loads(open(path, 'r').read())
    return data

def runSimulation(conditions):
    """Run simulation with given conditions and return tuple of S, I, and R"""
    duration = conditions['ending_day'] - conditions['starting_day']
    #Initialize numpy arrays
    s = np.zeros(shape=(duration, 2))
    i = np.zeros(shape=(duration, 2))
    r = np.zeros(shape=(duration, 2))
    #Make plot points with randomized death counts
    totalRemoved = conditions['starting_deaths']
    totalSusceptible = conditions['starting_healthy']
    totalInfected = conditions['starting_infected']

    for day in range(0, duration):
        s[day] = [day+1, totalSusceptible]
        i[day] = [day+1, totalInfected]
        r[day] = [day+1, totalRemoved]

    return s, i, r

def plotSim(simResults, simConfig):
    #(simResults)
    """Create plot of simulation given the results of a simulation"""
    #Configure plot labels
    plt.title("Estimated effect of ebola outbreak on {}".format(simConfig["city"]))
    plt.xlabel("Day")
    plt.ylabel("Number of deaths")
    #Suceptible data
    sx,sy = simResults[0].T
    plt.plot(sx, sy, label="Susceptible")
    #Infected data
    ix, iy = simResults[1].T
    plt.plot(ix, iy, label="Infected")
    #Removed data
    rx, ry = simResults[2].T
    plt.plot(rx, ry, label="Removed")
    #Show plot
    plt.legend()
    plt.show()

def main():
    simData = loadData('conditions.json')
    simVals = runSimulation(simData)
    plotSim(simVals, simData)

if __name__ == '__main__':
    main()
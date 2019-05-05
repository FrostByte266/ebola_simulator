import numpy as np
import json
import os
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

    susceptibleStart = conditions['starting_healthy']
    infected = conditions['starting_infected']
    removed = conditions['starting_deaths']

    susceptible = susceptibleStart

    infectionRate = 100 * (infected / susceptible)
    # infectionRate = 0.8
    deathRate =  0.5


    for day in range(0, duration):
        #Run SIR model
        dailySusceptible = susceptible-((susceptible/susceptibleStart)*(infectionRate*infected))
        dailyInfected = infected+(susceptible/susceptibleStart)*(infectionRate*infected)-(infected*deathRate)
        dailyRemoved = removed+(infected*deathRate)

        susceptible = dailySusceptible
        infected = dailyInfected
        removed = dailyRemoved

        s[day] = [day+1, susceptible]
        i[day] = [day+1, infected]
        r[day] = [day+1, removed]

    return s, i, r

def plotSim(simResults, simConfig):
    """Create plot of simulation given the results of a simulation"""
    #Configure plot labels
    plt.title("Estimated effect of ebola outbreak on {}".format(simConfig["city"]))
    plt.xlabel("Day")
    plt.ylabel("People")
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
    # np.savetxt('results.csv', simResults[0], delimiter=',', fmt='%.0f')
    plt.legend()
    plt.show()

def main():
    np.set_printoptions(suppress=True)
    simData = loadData('conditions.json')
    simResults = runSimulation(simData)
    plotSim(simResults, simData)

if __name__ == '__main__':
    main()
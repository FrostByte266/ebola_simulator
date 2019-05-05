import json
import os
from sys import exit

import numpy as np
import matplotlib.pyplot as plt

def load_data(path):
    """Load the simulation conditions from .json file"""
    #Check file being exists and that it is a JSON file
    if path[-5:] != ".json" or not os.path.isfile(path):
        print("File not found or incorrect file type")
        exit(1)
    #Attempt to load file and parse the JSON content
    data = json.loads(open(path, 'r').read())
    return data

def run_simulation(conditions):
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

    infection_rate = 100 * (infected / susceptible)
    # infectionRate = 0.8
    death_rate =  0.5


    for day in range(0, duration):
        #Run SIR model
        susceptible_x_infection = susceptible/susceptibleStart * (infection_rate*infected)
        infected_x_death = infected*death_rate

        daily_susceptible = susceptible-susceptible_x_infection
        daily_infected = infected + susceptible_x_infection - infected_x_death
        removed = removed + infected_x_death

        susceptible = daily_susceptible
        infected = daily_infected

        s[day] = [day+1, susceptible]
        i[day] = [day+1, infected]
        r[day] = [day+1, removed]

    return s, i, r

def plot_sim(sim_results, sim_config):
    """Create plot of simulation given the results of a simulation"""
    #Configure plot labels
    plt.title("Estimated effect of ebola outbreak on {}".format(sim_config["city"]))
    plt.xlabel("Day")
    plt.ylabel("People")
    #Suceptible data
    sx,sy = sim_results[0].T
    plt.plot(sx, sy, label="Susceptible")
    #Infected data
    ix, iy = sim_results[1].T
    plt.plot(ix, iy, label="Infected")
    #Removed data
    rx, ry = sim_results[2].T
    plt.plot(rx, ry, label="Removed")
    #Show plot
    # np.savetxt('results.csv', simResults[0], delimiter=',', fmt='%.0f')
    plt.legend()
    plt.show()

def main():
    np.set_printoptions(suppress=True)
    sim_data = load_data('conditions.json')
    simResults = run_simulation(sim_data)
    plot_sim(simResults, sim_data)

if __name__ == '__main__':
    main()
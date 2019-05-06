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

    susceptible_start = conditions.get('starting_healthy', 0)
    infected = conditions.get('starting_infected', 0)
    removed = conditions.get('starting_dead', 0)
    susceptible = susceptible_start
    infection_rate = 100 * (infected / susceptible)
    death_rate =  0.5
    reduced_rate = 0.3

    for day in range(0, duration):
        #Run SIR model
        next_day = day+1
        susceptible_x_infection = (susceptible/susceptible_start) * (infection_rate*infected)
        infected_x_death = infected*death_rate
        susceptible_x_dead = susceptible / susceptible_start * (infection_rate * reduced_rate * removed)

        daily_susceptible = susceptible-susceptible_x_infection
        daily_infected = infected + susceptible_x_infection + susceptible_x_dead - infected_x_death
        removed = removed + infected_x_death

        susceptible = daily_susceptible
        infected = daily_infected

        s[day] = [next_day, susceptible]
        i[day] = [next_day, infected]
        r[day] = [next_day, removed]

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
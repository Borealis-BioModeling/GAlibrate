'''
Generated by nestedsample_it
Gleipnir NS run script for dimerization_model.py
'''
from dimerization_model_gaoit import model, gao_it
import numpy as np

from galibrate.pysb_utils import GAlibrateIt

if __name__ == '__main__':
    # Initialize PySB solver object for running simulations.
    # Simulation timespan should match experimental data.
    tspan = np.linspace(0,1, num=51)

    # USER must add commands to import/load any experimental
    # data for use in the likelihood function!
    experiments_avg = np.load('dimerization_model_dimer_data.npy')
    experiments_sd = np.load('dimerization_model_dimer_sd.npy')

    # Setup the Nested Sampling run
    population_size = 100
    observable_data = dict()
    time_idxs = list(range(len(tspan)))
    observable_data['A_dimer'] = tuple((experiments_avg, experiments_sd, time_idxs))
    # Initialize the GAlibrateIt instance with the model details.
    galibrate_it = GAlibrateIt(model, observable_data, tspan, gao_it=gao_it)
    # Now build the GAO object. -- All inputs are
    # optional keyword arguments.
    gao = galibrate_it(gao_population_size=population_size,
                       gao_kwargs=dict({'generations':100, 'mutation_rate':0.05}),
                       fitness_type='norm_logpdf')

    # run it
    best_theta, best_theta_fitness = gao.run()
    print("best_theta: ",best_theta)
    print("best_theta_fitness: ", best_theta_fitness)
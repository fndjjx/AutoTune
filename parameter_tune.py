
from deap import creator, base, tools, algorithms
import random
import pandas as pd
from sklearn.cross_validation import cross_val_score
import numpy as np
from hyperparameter import Hyperparameter
from parameter_config import *
from sklearn.metrics import f1_score, make_scorer, accuracy_score


class ParameterTune():

    def __init__(self, algo, parameter_space, x, y):
        self.h = Hyperparameter(parameter_space)
        map_length = self.h.parse_config()

        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMax)
        toolbox = base.Toolbox()
        toolbox.register("attr_bool", random.randint, 0, 1)
        toolbox.register("individual", tools.initRepeat, creator.Individual, 
                           toolbox.attr_bool, map_length)
        toolbox.register("population", tools.initRepeat, list, toolbox.individual)

        toolbox.register("mate", tools.cxTwoPoint)
        toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
        toolbox.register("select", tools.selTournament, tournsize=3)

        self.toolbox = toolbox
        self.x = x
        self.y = y
        self.algo = algo
        self.pop = None
        self.count = 0

    def eval_performance(self, individual):
        configuration = self.h.generate_parameter(individual)
        self.count += 1
        print(self.count)
        print(configuration)
        scorer = make_scorer(f1_score)
        scorer = make_scorer(accuracy_score)
        if configuration:
            try:
                clf = self.algo(**configuration)
                score = np.mean(cross_val_score(clf, self.x, self.y, scoring=scorer))
                print(score)
                return score,
            except Exception as err:
                print(err)
                return 0,
        else:
            return 0,

    def run(self, pop_num, cxpb, mutpb, gen_num):
        self.toolbox.register("evaluate", self.eval_performance)
        pop = self.toolbox.population(n=pop_num)
        self.pop, log = algorithms.eaSimple(pop, self.toolbox, cxpb=cxpb, mutpb=mutpb, ngen=gen_num, verbose=True)

    def get_best(self, k):
        fits = [(ind.fitness.values[0],ind) for ind in self.pop]
        fits.sort(key=lambda x:x[0])
        
        best_inds = fits[-k:]
        configurations = []
        for ind in best_inds:
            configurations.append([ind[0], self.h.generate_parameter(ind[1])])

        return configurations
        


if __name__ == "__main__":
    df = pd.read_csv("/tmp/train.csv")
    y = df["Survived"].values
    df = df.drop("Survived",axis=1)
    x = df.values

    hs = gradient_boost_config
    pt = ParameterTune(GradientBoostingClassifier,hs,x,y) 
    pt.run(10, 0.5, 0.3, 10)
    print(pt.get_best(3))

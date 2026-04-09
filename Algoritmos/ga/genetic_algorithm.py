
from random import Random
import copy
from ga.population import Population
from ga.genetic_operators.mutation import Mutation
from ga.selection_methods.selection_method import SelectionMethod
from ga.ga_event import GAEvent


class GeneticAlgorithm:

    rand = None

    def __init__(self,
                 seed: int,
                 population_size: int,
                 max_generations: int,
                 selection_method: SelectionMethod,
                 recombination: "Recombination",
                 mutation: Mutation):
        GeneticAlgorithm.rand = Random(seed)
        self.population_size = population_size
        self.max_generations = max_generations
        self.selection_method = selection_method
        self.recombination_method = recombination
        self.mutation_method = mutation
        self.population = None
        self.generation = 0
        self.stopped = False
        self.best_in_run = None
        self.problem = None
        self.listeners = []

    def stop(self) -> None:
        self.stopped = True

    # TODO
    def run(self) -> None:
        pass

    def __str__(self):
        return "GA: \n" + str(self.population)

    # Listeners

    def add_listener(self, listener):
        self.listeners.append(listener)

    def fire_generation_ended(self) -> None:
        for listener in self.listeners:
            listener.generation_ended(GAEvent(copy.deepcopy(self.best_in_run), self.population.average_fitness))

    def fire_run_ended(self) -> None:
        for listener in self.listeners:
            listener.run_ended(GAEvent(copy.deepcopy(self.best_in_run), self.population.average_fitness, True))


from ga.individual_bit_vector import BitVectorIndividual
from ga.genetic_operators.mutation import Mutation
from ga.genetic_algorithm import GeneticAlgorithm


class MutationBinary(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    # TODO
    def mutate(self, individual: BitVectorIndividual) -> None:
        pass

    def __str__(self):
        return "Binary mutation (" + f'{self.probability}' + ")"


from ga.individual_bit_vector import BitVectorIndividual
from ga.genetic_operators.mutation import Mutation
from ga.genetic_algorithm import GeneticAlgorithm


class MutationBinary(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    # TODO
    def mutate(self, individual: BitVectorIndividual) -> None:
        # Para cada gene com determinada probabilidade, fazer o "flip" do gene (e.g., 0.01)
        #GeneticalALgoritm.rand.rondom()
        for i in range(individual.num_genes):
            if GeneticAlgorithm.rand.random() < self.probability:
                individual.genome[i] = not individual.genome[i]
        

    def __str__(self):
        return "Binary mutation (" + f'{self.probability}' + ")"

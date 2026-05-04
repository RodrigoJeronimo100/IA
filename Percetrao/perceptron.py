import numpy as np

class Perceptron:
    '''Write the Perceptron class, which represents a Perceptron neuron. The class should have an array
of weights'''
    def __init__(self):
        self.weights = None
        self.bias = None

    def fit(self, xx: np.ndarray, yy: np.ndarray, learning_rate: float = 0.1, seed: int = 1) -> None:
        rng = np.random.default_rng(seed)
        self.weights = rng.random(2)
        self.bias = rng.random()
        change = True
        while change:
            change = False
            for i, x in enumerate(xx):
                a = self.predict(x)
                if a != yy[i]:
                    change = True

                    self.weights[0] += learning_rate * (yy[i] - a) * x[0]
                    self.weights[1] += learning_rate * (yy[i] - a) * x[1]
                    self.bias += learning_rate * (yy[i] - a)  * 1     
        '''Given the learning data xx, the learning labels yy, the learning rate and random number generator’s
            seed, this method implements the learning algorithm above.'''

    def predict(self, x: np.ndarray) -> int:
        #weighted_sum = x[0]*self.weights[0] + x[1]*self.weights[1] + 1*self.bias
        weighted_sum = np.dot(x, self.weights) + self.bias
        return self.__signal(weighted_sum)
    '''Given a sample x, this method computes the output of the network'''

    def __signal(self, z) -> int:
       if z >= 0:
           return 1
       else:
           return -1

def main():
    # Test AND
    xx_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    yy_and = np.array([0, 0, 0, 1])
    p_and = Perceptron()
    p_and.fit(xx_and, yy_and)
    print("AND predictions:")
    for x in xx_and:
        print(f"{x} -> {p_and.predict(x)}")

    # Test OR
    xx_or = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    yy_or = np.array([0, 1, 1, 1])
    p_or = Perceptron()
    p_or.fit(xx_or, yy_or)
    print("OR predictions:")
    for x in xx_or:
        print(f"{x} -> {p_or.predict(x)}")

if __name__ == "__main__":
    
    training_data = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]])
    training_labels = np.array([-1, -1, -1, 1])  

    perceptron = Perceptron()
    perceptron.fit(training_data, training_labels)
    print("Predictions:")
    for x in training_data:
        print(f"{x} -> {perceptron.predict(x)}")
    
#TPC ANALISAR SLIDES DE 42 a 51
#Executar codigo passo a passo, ver se bate certo com o oq esta nos slides
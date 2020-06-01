import unittest
from random import random
from knapSackProblem import knapSackProblem
from solution import Solution


class Test(unittest.TestCase):
    def test_compute_total_weights(self):
        inputs_array = ['test1.in']
        print("Compute total weights test ---> ")
        for instance_index in range(len(inputs_array)):
            print(f"Test #{instance_index+1}")
            file_name = 'testFiles/' + inputs_array[instance_index]
            # Reading the problem from the test file
            instance = knapSackProblem(file_name)
            sol = Solution(instance)
            # Creating a solution randomly
            for i in range(instance.nb_items):
                sol.x[i] = 0 if random() < 0.5 else 1
            w = 0
            for i in range(instance.nb_items):
                w += instance.weights[i] * sol.x[i]
            self.assertEqual(sol.computeTotalWeight(), w)


if __name__ == '__main__':
    unittest.main()
import unittest
from random import random
from knapSackProblem import knapSackProblem
from solution import Solution
from solver import Solver
from math import floor

class Test(unittest.TestCase):

    def generate_input_file_names(self):
      inputs_array = []
      for i in range(1,10):
        inputs_array.append(f"test{i}.in")
      inputs_array.append("testBig.in")
      return inputs_array
    
    def test_solve_fractional_KP(self):
        inputs_array = self.generate_input_file_names()
        outputs_array = [39, 312, 1035, 37, 54, 107, 10000, 137, 1036, 9279]
        print("\n\nCompute fractional knapSack solution test ---> ")
        for instance_index in range(len(inputs_array)):
            print(f"Test #{instance_index+1}")
            file_name = 'testFiles/' + inputs_array[instance_index]
            # Reading the problem from the test file
            instance = knapSackProblem(file_name)
            solver = Solver(instance)
            sol = solver.fractionalKP()
            self.assertLessEqual(sol.computeTotalWeight(), instance.capacity)
            self.assertEqual(floor(sol.computeTotalValue()), outputs_array[instance_index])

    def test_compute_total_weights(self):
        inputs_array = self.generate_input_file_names()
        print("\n\nCompute total weights test ---> ")
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

    def test_compute_total_values(self):
        inputs_array = self.generate_input_file_names()
        print("\n\nCompute total values test ---> ")
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
                w += instance.values[i] * sol.x[i]
            self.assertEqual(sol.computeTotalValue(), w)

    def test_print_instances(self):
      inputs_array = self.generate_input_file_names()
      for instance_index in range(len(inputs_array)):
            print(f"Test #{instance_index+1}")
            file_name = 'testFiles/' + inputs_array[instance_index]
            # Reading the problem from the test file
            instance = knapSackProblem(file_name)
            print(instance.to_string())

if __name__ == '__main__':
    unittest.main()

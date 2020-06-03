from solution import Solution

class Solver:
    def __init__(self, instance):
        self.instance = instance

    def fractionalKP(self):
      ratios = []
      indices = []
      for i in range(self.instance.nb_items):
        ratios.append(self.instance.weights[i]/self.instance.values[i])
        indices.append(i)
      indices = sorted(indices, key=lambda item: ratios[item])
      solution = Solution(self.instance)
      print(indices)
      print(ratios)
      current_capacity = self.instance.capacity
      current_item_index = 0
      while current_capacity > 0:
        chosen_index = indices[current_item_index]
        quantity = self.instance.weights[chosen_index]
        proportion = 1
        if quantity > current_capacity:
          proportion = current_capacity/quantity
          quantity = current_capacity
        solution.x[chosen_index] = proportion
        current_capacity -= quantity
        current_item_index += 1
      print(solution.to_string())
      return solution
    
    def zeroOneKP(self):
      pass

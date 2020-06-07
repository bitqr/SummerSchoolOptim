class Solution:
    def __init__(self, instance):
        self.instance = instance
        # Initial solution where nothing is taken in the bag
        self.x = []
        for i in range(instance.nb_items):
            self.x.append(0)

    def to_string(self) -> str:
        s = "The solution is:\n\n"
        for i in range(self.instance.nb_items):
            s += f"x{i} = {str(self.x[i])}\n"
        s += "\n"
        return s

    def computeTotalWeight(self):
        # TODO: Write the function
        pass

    def computeTotalValue(self):
        # TODO: Write the function
        pass

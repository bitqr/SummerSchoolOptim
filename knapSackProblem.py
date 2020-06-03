class knapSackProblem:
    def __init__(self, file_name: str):
        with open(file_name, 'r') as file:
            x = file.read()
            file_split = x.splitlines()
            first_line = file_split[0].split(' ')
            self.nb_items = int(first_line[0])
            self.capacity = int(first_line[1])
            self.weights = []
            self.values = []
            for i in range(1, self.nb_items+1):
                line = file_split[i].split(' ')
                self.values.append(int(line[0]))
                self.weights.append(int(line[1]))

    def to_string(self) -> str:
        s = f"\nNb items: {self.nb_items}\n"
        s += f"Total capacity: {self.capacity}"
        s += "\nWeights and values:\n"
        for i in range(self.nb_items):
            s += f"v{i} = {str(self.values[i])} / w{i} = {str(self.weights[i])}\n"
        s += "\n"
        return s

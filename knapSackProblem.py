class knapSackProblem:
    def __init__(self, file_name: str):
        with open(file_name, 'r') as file:
            x = file.read()
            file_split = x.splitlines()
            self.nb_items = int(file_split[0])
            self.weights = []
            self.values = []
            w = file_split[1].split(' ')
            v = file_split[2].split(' ')
            for i in range(0, self.nb_items):
                self.weights.append(int(w[i]))
                self.values.append(int(v[i]))

    def to_string(self) -> str:
        s = "KnapSack Problem:\n\n"
        s += f"Nb items: {self.nb_items}\n"
        s += "\nWeights and values:\n"
        for i in range(self.nb_items):
            s += f"w{i} = {str(self.weights[i])} / v{i} = {str(self.values[i])}\n"
        s += "\n"
        return s

import numpy as np

class ManageArray:
    @staticmethod
    def create(dna):
        row = []
        for i in range(len(dna) - 1):
            row.append(list(map(str,dna[i])))
        new_array = np.array(row)
        return new_array

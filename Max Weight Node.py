class Solution():
    def maxWeightCell(self, N, Edge):
        weights = [0] * N
        for i in range(N):
            if Edge[i] != -1:
                weights[Edge[i]] += i
        max_weight = float('-0')
        max_weight_cell = -1
        
        for i in range(N):
            if weights[i] > max_weight or (weights[i] == max_weight and i > max_weight_cell):
                max_weight = weights[i]
                max_weight_cell = i
        
        return max_weight_cell

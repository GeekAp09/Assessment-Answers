
class Solution():
    def largestSumCycle(self, N, Edge):
        maxval = -1
        visited = [0 for _ in Edge]
        
        for i in range(len(Edge)):
            if visited[i]:
                continue
            
            curr_path = dict()
            curr = i
            tot = 0
            err = 0
            
            while not visited[curr]:
                if curr == -1:
                    err = 1
                    visited[curr] = 1
                    break
                
                visited[curr] = 1
                curr_path[curr] = tot
                tot += Edge[curr]
                curr = Edge[curr]
                
            try:
                if not err:
                    maxval = max(maxval, tot - curr_path[curr])
            except:
                pass
        return maxval

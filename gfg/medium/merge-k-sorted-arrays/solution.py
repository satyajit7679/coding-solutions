class Solution:
    def mergeArrays(self, mat):
        # code here
        res = []
        n = len(mat)
        heap = []
        
        for i in range(n):
            if mat[i]:
                heapq.heappush(heap,(mat[i][0],i,0))
                
        
        while heap:
            value, row, col = heapq.heappop(heap)
            res.append(value)
            
            if col + 1 < len(mat[row]):
                heapq.heappush(heap,(mat[row][col+1],row,col + 1))
                
        return res
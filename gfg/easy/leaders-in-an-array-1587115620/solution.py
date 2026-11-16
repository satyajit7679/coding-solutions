class Solution:
    def leaders(self, arr):
        # code here
        i = len(arr) - 2
		id = len(arr) - 1
		res = []
		res.append(arr[id])
		while i >= 0:
			if arr[i] >= arr[id]:
				res.append(arr[i])
				id = i
				i -= 1
			else:
			    i -= 1
		res.reverse()
		
		return res
        
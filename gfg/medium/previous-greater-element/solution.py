class Solution:
	def preGreaterEle(self, arr):
		# code here
		st = []
		ans = [-1] * len(arr)
		
		st.append(arr[0])
		for i in range(1,len(arr)):
		    while st and st[-1] <= arr[i]:
		        st.pop()
		    if st:
		        ans[i] = st[-1]
		    st.append(arr[i])
	    return ans
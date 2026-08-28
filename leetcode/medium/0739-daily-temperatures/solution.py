class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = []
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            while st and temperatures[st[-1]] <= temperatures[i]:
                st.pop()

            if st:
                ans[i] = st[-1] - i
                
            st.append(i)

        return ans
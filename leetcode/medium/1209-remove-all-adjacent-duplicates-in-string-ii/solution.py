class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        for c in s:
            if not st or st[-1][0] != c:
                st.append([c,1])
            else:
                st[-1][1] += 1
                if st[-1][1] == k:
                    st.pop()
        res = ""
        for char,count in st:
            res += char * count
        return res
        
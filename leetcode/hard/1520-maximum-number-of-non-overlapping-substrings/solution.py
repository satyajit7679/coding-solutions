class Solution:
    def maxNumOfSubstrings(self, s: str):
        n = len(s)

        # First and last occurrence of every character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        intervals = []

        # Try to create a valid substring for every character
        for c in range(26):

            if first[c] == n:
                continue

            left = first[c]
            right = last[c]

            i = left
            valid = True

            while i <= right:

                x = ord(s[i]) - ord('a')

                # This character occurs before our starting point
                if first[x] < left:
                    valid = False
                    break

                # Need to include all occurrences of this character
                right = max(right, last[x])

                i += 1

            if valid:
                intervals.append((left, right))

        # Sort by ending position
        intervals.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1

        for left, right in intervals:

            if left > prev_end:
                ans.append(s[left:right + 1])
                prev_end = right

        return ans
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        freq = Counter(words)
        ans = []

        for start in range(word_len):
            left = start
            right = start
            count = 0
            curr = {}

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in freq:
                    curr[word] = curr.get(word, 0) + 1
                    count += 1

                    while curr[word] > freq[word]:
                        left_word = s[left:left + word_len]
                        curr[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == word_count:
                        ans.append(left)

                        left_word = s[left:left + word_len]
                        curr[left_word] -= 1
                        left += word_len
                        count -= 1

                else:
                    curr.clear()
                    count = 0
                    left = right

        return ans
        
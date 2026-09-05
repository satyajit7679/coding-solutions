# Substring with Concatenation of All Words

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given a string `s` and an array of strings `words`. All the strings of `words` are of  **the same length**.

A  **concatenated string**  is a string that exactly contains all the strings of any permutation of `words` concatenated.

- For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.

Return an array of  *the starting indices*  of all the concatenated substrings in `s`. You can return the answer in  **any order**.

 

 **Example 1:** 

 **Input:**  s = "barfoothefoobarman", words = ["foo","bar"]

 **Output:**  [0,9]

 **Explanation:** 

The substring starting at 0 is `"barfoo"`. It is the concatenation of `["bar","foo"]` which is a permutation of `words`.
The substring starting at 9 is `"foobar"`. It is the concatenation of `["foo","bar"]` which is a permutation of `words`.

 **Example 2:** 

 **Input:**  s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

 **Output:**  []

 **Explanation:** 

There is no concatenated substring.

 **Example 3:** 

 **Input:**  s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

 **Output:**  [6,9,12]

 **Explanation:** 

The substring starting at 6 is `"foobarthe"`. It is the concatenation of `["foo","bar","the"]`.
The substring starting at 9 is `"barthefoo"`. It is the concatenation of `["bar","the","foo"]`.
The substring starting at 12 is `"thefoobar"`. It is the concatenation of `["the","foo","bar"]`.

 

 **Constraints:** 

- 1 <= s.length <= 104
- 1 <= words.length <= 5000
- 1 <= words[i].length <= 30
- s and words[i] consist of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 22 ms (beats 79.12%)  
**Memory:** 19.8 MB (beats 69.84%)  
**Submitted:** 2026-09-05T15:06:03.795Z  

```py
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
        
```

---

[View on LeetCode](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        have = {}
        need = {}

        for i in range(len(ransomNote)):
            need[ransomNote[i]] = need.get(ransomNote[i], 0) + 1

        for i in range(len(magazine)):
            have[magazine[i]] = have.get(magazine[i], 0) + 1

        for key, value in need.items():
            if key not in have or value > have[key]:
                return False

        return True
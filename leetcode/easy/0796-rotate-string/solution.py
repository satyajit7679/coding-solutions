class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if len(s) == 1:
            return True

        if s == goal:
            return False
        
        return goal in (s + s)

        
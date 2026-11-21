class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        size = [1] * n
        last_seen = [-1] * 26

        def dfs(u: int) -> None:
            char_idx = ord(s[u]) - ord('a')
            prev_ancestor = last_seen[char_idx]
            
            # Update closest ancestor for this character before visiting children
            last_seen[char_idx] = u
            
            for v in children[u]:
                dfs(v)
            
            # Restore state (backtrack)
            last_seen[char_idx] = prev_ancestor
            
            # Propagate u's final subtree size to its new parent
            if u != 0:
                new_parent = prev_ancestor if prev_ancestor != -1 else parent[u]
                size[new_parent] += size[u]

        dfs(0)
        return size
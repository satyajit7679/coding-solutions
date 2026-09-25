class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        def multiply(set1, set2):
            res = set()

            for a in set1:
                for b in set2:
                    res.add(a + b)

            return res

        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == '{':
                    inside, i = parse(i + 1)
                    current = multiply(current, inside)

                elif expression[i] == ',':
                    result.update(current)
                    current = {""}
                    i += 1

                else:
                    current = multiply(current, {expression[i]})
                    i += 1

            result.update(current)

            return result, i + 1

        ans, _ = parse(0)

        return sorted(ans)
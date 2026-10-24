
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,
                         arriveBob: str, leaveBob: str) -> int:

        months = [31, 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]

        def convert(date):
            month, day = map(int, date.split("-"))

            total = sum(months[:month - 1]) + day

            return total

        a_start = convert(arriveAlice)
        a_end = convert(leaveAlice)

        b_start = convert(arriveBob)
        b_end = convert(leaveBob)

        start = max(a_start, b_start)
        end = min(a_end, b_end)

        if start > end:
            return 0

        return end - start + 1

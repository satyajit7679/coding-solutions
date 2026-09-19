import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1

         # Check if rearrangement is impossible
        if max(freq.values()) > (len(s) + 1) // 2:
            return ""

        heap = []
        
        for ch,count in freq.items():
            heapq.heappush(heap,(-count,ch))

        ans = []
        prev_count = 0
        prev_ch = ""

        while heap:
            count,ch = heapq.heappop(heap)
            if ch == prev_ch:
                if not heap:
                    return ""
                count2,ch2 = heapq.heappop(heap)
                ans.append(ch2)
                count2 += 1
                heapq.heappush(heap,(count,ch))
                prev_ch = ch2
                prev_count = count2
            else:
                ans.append(ch)
                count += 1
                if prev_count < 0:
                    heapq.heappush(heap,(prev_count,prev_ch))
                prev_ch = ch
                prev_count = count

        return "".join(ans)

        
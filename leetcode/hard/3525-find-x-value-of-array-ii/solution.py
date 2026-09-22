class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:

        n = len(nums)

        # tree[node] = [product of whole segment, count of prefix remainders]
        tree = [[0, [0] * k] for _ in range(4 * n)]

        def merge(left, right):
            left_prod, left_cnt = left
            right_prod, right_cnt = right

            # Product of the complete merged segment
            prod = (left_prod * right_prod) % k

            # Prefixes completely inside left
            cnt = left_cnt[:]

            # Prefixes that go into right
            for r in range(k):
                new_rem = (left_prod * r) % k
                cnt[new_rem] += right_cnt[r]

            return [prod, cnt]

        def build(node, l, r):
            if l == r:
                rem = nums[l] % k

                tree[node][0] = rem
                tree[node][1][rem] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, idx, value):
            if l == r:
                rem = value % k

                tree[node][0] = rem
                tree[node][1] = [0] * k
                tree[node][1][rem] = 1
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, value)
            else:
                update(node * 2 + 1, mid + 1, r, idx, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            if r < ql or l > qr:
                return None

            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            if left is None:
                return right

            if right is None:
                return left

            return merge(left, right)

        # Build the segment tree
        build(1, 0, n - 1)

        answer = []

        for index, value, start, x in queries:

            # Update persists for future queries
            nums[index] = value

            update(
                1, 0, n - 1,
                index,
                value
            )

            # Get information for nums[start:]
            result = query(
                1, 0, n - 1,
                start, n - 1
            )

            # Number of prefixes having remainder x
            answer.append(result[1][x])

        return answer
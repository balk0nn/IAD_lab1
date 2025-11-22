import heapq
from collections import defaultdict


def medianSlidingWindowHeaps(nums, k):
    # max-heap (values stored as negative), contains smaller half
    lo = []
    # min-heap (larger half)
    hi = []
    # delayed deletions
    delayed = defaultdict(int)

    # Effective sizes (since heaps may contain "deleted" items)
    lo_size = 0
    hi_size = 0

    def prune(heap):
        # Remove elements that are marked deleted
        while heap:
            num = heap[0]
            if heap is lo:
                num = -num
            if delayed[num]:
                delayed[num] -= 1
                heapq.heappop(heap)
            else:
                break

    def make_balance():
        nonlocal lo_size, hi_size

        # rebalance heaps so that:
        # lo_size == hi_size (+1 if k is odd)
        if lo_size > hi_size + 1:
            # move top from lo → hi
            val = -heapq.heappop(lo)
            lo_size -= 1
            heapq.heappush(hi, val)
            hi_size += 1
            prune(lo)
        elif lo_size < hi_size:
            # move top from hi → lo
            val = heapq.heappop(hi)
            hi_size -= 1
            heapq.heappush(lo, -val)
            lo_size += 1
            prune(hi)

    out = []
    odd = (k % 2 == 1)

    push_lo = lambda x: heapq.heappush(lo, -x)
    push_hi = lambda x: heapq.heappush(hi, x)

    for i, x in enumerate(nums):
        # Insert
        if not lo or x <= -lo[0]:
            push_lo(x)
            lo_size += 1
        else:
            push_hi(x)
            hi_size += 1

        make_balance()

        # Remove old element when window slides
        if i >= k:
            old = nums[i - k]
            delayed[old] += 1
            # Decrement logical size
            if old <= -lo[0]:
                lo_size -= 1
                if old == -lo[0]:
                    prune(lo)
            else:
                hi_size -= 1
                if hi and old == hi[0]:
                    prune(hi)

            make_balance()

        # Emit median
        if i >= k - 1:
            if odd:
                out.append(-lo[0])
            else:
                out.append((-lo[0] + hi[0]) / 2)

    return out
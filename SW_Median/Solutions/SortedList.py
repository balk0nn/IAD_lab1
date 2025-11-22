from sortedcontainers import SortedList


def medianSlidingWindow(nums: list[int], k: int) -> list[float]:
    sl = SortedList()
    for i in range(len(nums)):
        if i >= k:
            sl.remove(nums[i - k])
        sl.add(nums[i])
        if i >= k - 1:
            yield sl[k // 2] if k % 2 == 1 else (sl[k // 2 - 1] + sl[k // 2]) / 2

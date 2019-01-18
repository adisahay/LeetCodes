class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        if l is 0:
            return [-1, -1]

        pos = bsearch(nums, 0, l, target)

        if nums[pos] is not target:
            return [-1, -1]

        start = bsearch(nums, 0, l, target - 0.5)
        end = bsearch(nums, 0, l, target + 0.5)

        if nums[start] != target:
            start += 1

        return [start, end]

def bsearch(arr, start, end, val):
    while start < end - 1:
        mid = (start + end) // 2

        if arr[mid] < val:
            start = mid
        elif arr[mid] > val:
            end = mid
        else:
            return mid
    return start

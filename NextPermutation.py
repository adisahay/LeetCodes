class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(l - 1, -1, -1):
            if nums[i] > nums[i - 1]:
                break

        if i is 0:
            final = sorted(nums)

        j = i
        i -= 1
        diff = float("inf")
        gt = 0
        while j < l:
            if nums[j] > nums[i] and nums[j] - nums[i] < diff:
                diff = nums[j] - nums[i]
                gt = j
            j += 1

        tmp = nums[i]
        nums[i] = nums[gt]
        nums[gt] = tmp

        final = nums[: i + 1] + sorted(nums[i + 1 :])

        for i in range(l):
            nums[i] = final[i]

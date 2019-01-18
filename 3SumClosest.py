class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        nums = sorted(nums)
        msum = None
        mdiff = float("inf")

        for i in range(l - 2):
            j = i + 1
            k = l - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                diff = abs(total - target)

                if diff < mdiff:
                    msum = total
                    mdiff = diff

                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    return target

        return msum

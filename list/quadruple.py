class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 枚举四元组, 暴力解法
        # 时间复杂度: O(n^4)， TLE
        # n = len(nums)
        # res = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             for l in range(k + 1, n):
        #                 if nums[i] + nums[j] + nums[k] == nums[l]:
        #                     res += 1
        # return res
        n = len(nums)
        res = 0
        pre = [0] * (n + 1)
        for j in range(n):
            suf = 0
            for k in range(n - 1, j, -1):
                if nums[k] < nums[j]:
                    res += pre[nums[k]] * suf
                else:
                    suf += 1
            for x in range (nums[j] + 1, n + 1):
                pre[x] += 1
        return res
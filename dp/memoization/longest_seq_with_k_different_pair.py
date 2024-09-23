# 给你一个整数数组 nums 和一个 非负 整数 k 。如果一个整数序列 seq 满足在下标范围 [0, seq.length - 2] 中 最多只有 k 个
# 下标 i 满足 seq[i] != seq[i + 1] ，那么我们称这个整数序列为 好 序列。
#
#  请你返回 nums 中 好 子序列 的最长长度。
#
#
#
#  示例 1：
#
#
#  输入：nums = [1,2,1,1,3], k = 2
#
#
#  输出：4
#
#  解释：
#
#  最长好子序列为 [1,2,1,1,3] 。
#
#  示例 2：
#
#
#  输入：nums = [1,2,3,4,5,1], k = 0
#
#
#  输出：2
#
#  解释：
#
#  最长好子序列为 [1,2,3,4,5,1] 。
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 500
#  1 <= nums[i] <= 10⁹
#  0 <= k <= min(nums.length, 25)

class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        @cache
        # dfs(i, j) 表示以 nums[i] 结尾，且至多有j对不同元素的最长好子序列长度
        def dfs(i, j):
            if j < 0:
                return 0
            if i == n - 1:
                return 1
            res = 0
            for x in range(i + 1, n):
                if nums[x] == nums[i]:
                    res = max(res, dfs(x, j) + 1)
                else:
                    res = max(res, dfs(x, j - 1) + 1)
            return res

        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i, k))
        return ans
# 给你一个下标从 0 开始的整数数组 nums 。
#
#  一开始，所有下标都没有被标记。你可以执行以下操作任意次：
#
#
#  选择两个 互不相同且未标记 的下标 i 和 j ，满足 2 * nums[i] <= nums[j] ，标记下标 i 和 j 。
#
#
#  请你执行上述操作任意次，返回 nums 中最多可以标记的下标数目。
#
#
#
#  示例 1：
#
#
# 输入：nums = [3,5,2,4]
# 输出：2
# 解释：第一次操作中，选择 i = 2 和 j = 1 ，操作可以执行的原因是 2 * nums[2] <= nums[1] ，标记下标 2 和 1 。
# 没有其他更多可执行的操作，所以答案为 2 。
#
#
#  示例 2：
#
#
# 输入：nums = [9,2,5,4]
# 输出：4
# 解释：第一次操作中，选择 i = 3 和 j = 0 ，操作可以执行的原因是 2 * nums[3] <= nums[0] ，标记下标 3 和 0 。
# 第二次操作中，选择 i = 1 和 j = 2 ，操作可以执行的原因是 2 * nums[1] <= nums[2] ，标记下标 1 和 2 。
# 没有其他更多可执行的操作，所以答案为 4 。
#
#
#  示例 3：
#
#
# 输入：nums = [7,6,8]
# 输出：0
# 解释：没有任何可以执行的操作，所以答案为 0 。
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10⁵
#  1 <= nums[i] <= 10⁹
#
#
#  Related Topics 贪心 数组 双指针 二分查找 排序 👍 68 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxNumOfMarkedIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self.binarySearch(nums)
        n = len(nums)
        nums.sort()
        l, r = 0, n // 2
        res = 0
        while l < n // 2:
            while r < n and 2 * nums[l] > nums[r]:
                r += 1
            if r < n:
                res += 2
                r += 1
            l += 1

        return res


    def binarySearch(self, nums):
        nums.sort()
        n = len(nums)
        l, r = 0, n // 2
        def check(m):
            for i in range(m):
                if 2 * nums[i] > nums[n - m + i]:
                    return False
            return True

        while l < r:
            m = (l + r + 1) // 2
            if check(m):
                l = m
            else:
                r = m - 1

        return l * 2

# leetcode submit region end(Prohibit modification and deletion)

# 给你一个整数数组 rewardValues，长度为 n，代表奖励的值。
#
#  最初，你的总奖励 x 为 0，所有下标都是 未标记 的。你可以执行以下操作 任意次 ：
#
#
#  从区间 [0, n - 1] 中选择一个 未标记 的下标 i。
#  如果 rewardValues[i] 大于 你当前的总奖励 x，则将 rewardValues[i] 加到 x 上（即 x = x +
# rewardValues[i]），并 标记 下标 i。
#
#
#  以整数形式返回执行最优操作能够获得的 最大 总奖励。
#
#
#
#  示例 1：
#
#
#  输入：rewardValues = [1,1,3,3]
#
#
#  输出：4
#
#  解释：
#
#  依次标记下标 0 和 2，总奖励为 4，这是可获得的最大值。
#
#  示例 2：
#
#
#  输入：rewardValues = [1,6,4,3,2]
#
#
#  输出：11
#
#  解释：
#
#  依次标记下标 0、2 和 1。总奖励为 11，这是可获得的最大值。
#
#
#
#  提示：
#
#
#  1 <= rewardValues.length <= 2000
#  1 <= rewardValues[i] <= 2000
#
#
#  Related Topics 数组 动态规划 👍 29 👎 0
from audioop import reverse
from linecache import cache


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        dp = [0] * (rewardValues[-1] * 2)
        dp[0] = 1

        for v in rewardValues:
            for vv in range(v, 2*v, 1):
                if dp[vv - v] == 1:
                    dp[vv] = 1

        res = 0
        for i in range(2 * rewardValues[-1]):
            if dp[i] == 1:
                res = i
        return res

        # with sort
        # rewardValues.sort()
        #
        # @cache
        # def dp(i, x):
        #     if i == len(rewardValues):
        #         return x
        #     if x < rewardValues[i]:
        #         return dp(i + 1, x)
        #     return max(dp(i + 1, x), dp(i + 1, x + rewardValues[i]))
        #
        # return dp(0, 0)

        # if not sort, we need to enumerate all possible values


        @cache
        # def dp(x, set_tuple):
        #     set_ = set(set_tuple)
        #     if len(set_) == len(rewardValues):
        #         return x
        #     max_value = x
        #     for i in range(len(rewardValues)):
        #         if i not in set_:
        #             set_.add(i)
        #             if x < rewardValues[i]:
        #                 max_value = max(max_value, dp(x, tuple(set_)))
        #             else:
        #                 max_value = max(max_value, dp(x + rewardValues[i], tuple(set_)))
        #             set_.remove(i)
        #     return max_value
        #
        #
        # return dp(0, ())
        # leetcode submit region end(Prohibit modification and deletion)

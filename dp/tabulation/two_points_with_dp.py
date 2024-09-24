# 在 X轴 上有一些奖品。给你一个整数数组 prizePositions ，它按照 非递减 顺序排列，其中 prizePositions[i] 是第 i 件奖
# 品的位置。数轴上一个位置可能会有多件奖品。再给你一个整数 k 。
#
#  你可以同时选择两个端点为整数的线段。每个线段的长度都必须是 k 。你可以获得位置在任一线段上的所有奖品（包括线段的两个端点）。注意，两个线段可能会有相交。
#
#
#
#  比方说 k = 2 ，你可以选择线段 [1, 3] 和 [2, 4] ，你可以获得满足 1 <= prizePositions[i] <= 3 或者 2
# <= prizePositions[i] <= 4 的所有奖品 i 。
#
#
#  请你返回在选择两个最优线段的前提下，可以获得的 最多 奖品数目。
#
#
#
#  示例 1：
#
#
# 输入：prizePositions = [1,1,2,2,3,3,5], k = 2
# 输出：7
# 解释：这个例子中，你可以选择线段 [1, 3] 和 [3, 5] ，获得 7 个奖品。
#
#
#  示例 2：
#
#
# 输入：prizePositions = [1,2,3,4], k = 0
# 输出：2
# 解释：这个例子中，一个选择是选择线段 [3, 3] 和 [4, 4] ，获得 2 个奖品。
#
#
#
#
#  提示：
#
#
#  1 <= prizePositions.length <= 10⁵
#  1 <= prizePositions[i] <= 10⁹
#  0 <= k <= 10⁹
#  prizePositions 有序非递减。
#
#
#  Related Topics 数组 二分查找 滑动窗口 👍 65 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximizeWin(self, prizePositions, k):
        """
        :type prizePositions: List[int]
        :type k: int
        :rtype: int
        """
        n = len(prizePositions)
        left, right = 0, 0
        res = 0
        dp = [0] * (n + 1)
        while right < n:
            while prizePositions[right] - prizePositions[left] > k:
                left += 1
            res = max(res, right - left + 1 + dp[left])
            dp[right + 1] = max(dp[right], right - left + 1)
            right += 1

        # binary search style
        # for i in range (n):
        #     x = bisect.bisect_left(prizePositions, prizePositions[i] - k)
        #     res = max(res, i - x + 1 + dp[x])
        #     dp[i + 1] = max(dp[i], i - x + 1)
        return res
# leetcode submit region end(Prohibit modification and deletion)

# 有 n 位乘客即将登机，飞机正好有 n 个座位。第一位乘客的票丢了，他随便选了一个座位坐下。
#
#  剩下的乘客将会：
#
#
#  如果他们自己的座位还空着，就坐到自己的座位上，
#  当他们自己的座位被占用时，随机选择其他座位
#
#
#  第 n 位乘客坐在自己的座位上的概率是多少？
#
#
#
#  示例 1：
#
#
# 输入：n = 1
# 输出：1.00000
# 解释：第一个人只会坐在自己的位置上。
#
#  示例 2：
#
#
# 输入: n = 2
# 输出: 0.50000
# 解释：在第一个人选好座位坐下后，第二个人坐在自己的座位上的概率是 0.5。
#
#
#
#
#  提示：
#
#
#  1 <= n <= 10^5
#
#
#  Related Topics 脑筋急转弯 数学 动态规划 概率与统计 👍 146 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1 if n == 1 else 0.5

    # dp solution，该dp的递推公式是错的，用了谷歌的gemini, 但是他也不看不出问题
    # openai 的copilot也是错的
    def dpSolution(self, n: int) -> float:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = 1 / i + (i - 2) / i * dp[i - 1]
        return dp[n]
    def mathSolution(self, n: int) -> float:
        return 1 if n == 1 else 0.5
# leetcode submit region end(Prohibit modification and deletion)

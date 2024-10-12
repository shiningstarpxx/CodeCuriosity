# 给你两个整数数组 nums1 和 nums2，长度分别为 n 和 m。同时给你一个正整数 k。
#
#  如果 nums1[i] 可以被 nums2[j] * k 整除，则称数对 (i, j) 为 优质数对（0 <= i <= n - 1, 0 <= j <=
#  m - 1）。
#
#  返回 优质数对 的总数。
#
#
#
#  示例 1：
#
#
#  输入：nums1 = [1,3,4], nums2 = [1,3,4], k = 1
#
#
#  输出：5
#
#  解释：
#
#  5个优质数对分别是 (0, 0), (1, 0), (1, 1), (2, 0), 和 (2, 2)。
#
#  示例 2：
#
#
#  输入：nums1 = [1,2,4,12], nums2 = [2,4], k = 3
#
#
#  输出：2
#
#  解释：
#
#  2个优质数对分别是 (3, 0) 和 (3, 1)。
#
#
#
#  提示：
#
#
#  1 <= n, m <= 50
#  1 <= nums1[i], nums2[j] <= 50
#  1 <= k <= 50
#
#
#  Related Topics 数组 哈希表 👍 11 👎 0
from collections import Counter


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        #return sum(a % (b*k) == 0 for a in nums1 for b in nums2)
        count = Counter(nums1)
        max1 = max(count)
        res = 0
        for a, cnt in Counter(nums2).items():
            for b in range(a * k, max1 + 1, a * k):
                if b in count:
                    res += count[b] * cnt
        return res
# leetcode submit region end(Prohibit modification and deletion)

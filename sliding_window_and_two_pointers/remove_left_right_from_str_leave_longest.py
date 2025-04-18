# 给你一个由字符 'a'、'b'、'c' 组成的字符串 s 和一个非负整数 k 。每分钟，你可以选择取走 s 最左侧 还是 最右侧 的那个字符。
#
#  你必须取走每种字符 至少 k 个，返回需要的 最少 分钟数；如果无法取到，则返回 -1 。
#
#
#
#  示例 1：
#
#
# 输入：s = "aabaaaacaabc", k = 2
# 输出：8
# 解释：
# 从 s 的左侧取三个字符，现在共取到两个字符 'a' 、一个字符 'b' 。
# 从 s 的右侧取五个字符，现在共取到四个字符 'a' 、两个字符 'b' 和两个字符 'c' 。
# 共需要 3 + 5 = 8 分钟。
# 可以证明需要的最少分钟数是 8 。
#
#
#  示例 2：
#
#
# 输入：s = "a", k = 1
# 输出：-1
# 解释：无法取到一个字符 'b' 或者 'c'，所以返回 -1 。
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 10⁵
#  s 仅由字母 'a'、'b'、'c' 组成
#  0 <= k <= s.length
#
#
#  Related Topics 哈希表 字符串 滑动窗口 👍 66 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Time: O(n)
        # Space: O(1)
        n = len(s)
        cnt = [0] * 3
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        if any(c < k for c in cnt):
            return -1

        res = n
        l, r = 0, 0
        local_cnt = [0] * 3
        while r < n:
            local_cnt[ord(s[r]) - ord('a')] += 1
            while any(cnt[i] - local_cnt[i] < k for i in range(3)):
                res = min(res, n - (r - l))
                local_cnt[ord(s[l]) - ord('a')] -= 1
                l += 1
            r += 1
        return min(res, n - (r - l))
# leetcode submit region end(Prohibit modification and deletion)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_length = len(s)
        t_length = len(t)
        lesser_length = s_length if s_length < t_length else t_length
        i, j = 0, 0
        count = 0
        while i < s_length and j < t_length:
            if s[i] == t[j]:
                count += 1
                i += 1
                j += 1
            else:
                i += 1
        if count == lesser_length:
            return True
        else:
            return False

solution = Solution()
solution.isSubsequence("abc", "ahbgdc")
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_length = len(s)
        t_length = len(t)
        i, j, count = 0, 0, 0

        while i < s_length and j < t_length:
            if s[i] == t[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1

        if count == s_length:
            return True
        else:
            return False
solution = Solution()
print(solution.isSubsequence("abc", "ahbgdc"))
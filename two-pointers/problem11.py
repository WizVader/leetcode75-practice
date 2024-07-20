class Solution:
    def maxArea(self, height: list[int]) -> int:
        array_length = len(height)
        i = 0
        j = array_length - 1
        amount = 0
        while i < j:
            current_amount = min((height[i], height[j])) * (j - i)
            if current_amount > amount:
                amount = current_amount
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return amount


solution = Solution()
print(solution.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))

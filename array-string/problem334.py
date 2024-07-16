# i, j, k such that nums at i, j, k < each other
# i, j, k are continuous indices, if pattern exists return true else return false
# Implement O(n) time complexity

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num_i = num_j = float('inf')
        for number in nums:
            if number < num_i:
                num_i = number
            elif num_i < number < num_j:
                num_j = number
            elif number > num_j:
                return True
        return False


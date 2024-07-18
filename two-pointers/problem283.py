class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] == 0:
                if nums[j] != 0:
                    nums.pop(i)
                    nums.insert(j, 0)
                    j -= 1
                else:
                    j -= 1
            else:
                i += 1

"""
How the two pointer works:
    * In the case of finding the two elements that add up to a given sum
    * One pointer to the beginning, one pointer to the end
    * Traverse through the array while the left pointer is less than that of the right
    * Conditional statements according to given target (handle edge cases)
    
    inputs: arr = [2, 3, 5, 8, 9, 10, 11], val = 17

    i = 0
    j = len(arr) - 1

    while i < j:
        if arr[i] + arr[j] == val:
            print(arr[i], arr[j])
            break
        elif arr[i] + arr[j] > val:
            j -= 1
        else:
            i += 1
"""

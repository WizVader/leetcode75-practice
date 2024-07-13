class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        flowerbed_length = len(flowerbed)
        for i in range(flowerbed_length):
            if i < flowerbed_length - 1:
                if i == 0:
                    if flowerbed[i+1] == 0 and flowerbed[i] == 0:
                        count += 1
                        flowerbed[i] = 1
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                        print(flowerbed[i-1], flowerbed[i], flowerbed[i+1], i)
                        count += 1
                        flowerbed[i] = 1
            else:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                    count += 1
                    flowerbed[i] = 1
        if count >= n:
            return True
        else:
            return False

solution = Solution()
print(solution.canPlaceFlowers([0,0,1,0,0], 1))



class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        x, y = len(str1), len(str2)
        lesser = str2
        greater = str1
        length_lesser = y
        length_greater = x
        if y > x:
            lesser = str1
            greater = str2
            length_lesser = x
            length_greater = y

        i = length_lesser
        while i > 0:
            divisor = lesser[:i]
            divisor_length = len(divisor)
            count_1 = greater.count(divisor)
            count_2 = lesser.count(divisor)

            if count_1 * divisor_length == length_greater and count_2 * divisor_length == length_lesser:
                return divisor
            i -= 1
        return ""

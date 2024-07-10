class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        x, y = len(word1), len(word2)
        limit = max([len(word1), len(word2)])
        for i in range(0, limit):
            if i >= x:
                output += word2[i]
            elif i >= y:
                output += word1[i]
            else:
                output += word1[i] + word2[i]
        return output
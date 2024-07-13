class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words.reverse()
        output = [word for word in words if word != '']

        return ' '.join(output)
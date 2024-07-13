class Solution:
    def reverseVowels(self, s: str) -> str:
        output = list(s)
        index = []
        vowels = []

        for i in range(len(s)):
            if s[i].lower() in "aeiou":
                vowels.append(s[i])
                index.append(i)

        vowels.reverse()

        for i in range(len(vowels)):
            output[index[i]] = vowels[i]

        return ''.join(output)
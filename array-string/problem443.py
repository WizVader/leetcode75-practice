class Solution:
    def compress(self, chars: list[str]) -> int:
        s = ""
        array_length = len(chars)
        if array_length == 1:
            return 1
        else:
            prev_character = chars[0]
            count = 1

            for i in range(1, array_length):
                if i == array_length - 1:
                    if chars[i] == prev_character:
                        count += 1
                        s += chars[i] + str(count)
                        count = 1
                    else:
                        if count > 1:
                            s += prev_character + str(count) + chars[i]
                        else:
                            s += prev_character + chars[i]
                else:
                    if chars[i] == prev_character:
                        count += 1
                    else:
                        if count == 1:
                            s += prev_character
                        else:
                            s += prev_character + str(count)
                            count = 1
                    prev_character = chars[i]

            chars[:] = list(s)
            return len(chars)

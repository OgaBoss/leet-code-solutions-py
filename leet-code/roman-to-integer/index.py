class Solution:
    @staticmethod
    def roman_to_int(s: str) -> int:
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        value = 0
        count = 0

        while count < len(s):
            if count < len(s) - 1 and (symbols[s[count + 1]] > symbols[s[count]]):
                value += (symbols[s[count + 1]] - symbols[s[count]])
                count += 2
            else:
                value += symbols[s[count]]
                count += 1

        return value

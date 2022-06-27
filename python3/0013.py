class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
            }

        prev = 0
        result = 0
        for n in reversed(s):
            if roman[n] < prev:
                result = result - roman[n]
            else:
                result = result + roman[n]
            prev = roman[n]

        return results

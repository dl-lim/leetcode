class Solution:
    def intToRoman(self, num: int) -> str:
        romstr = ''
        while num != 0:
            if num >= 1000:
                romstr += 'M'
                num -= 1000

            elif num >= 900:
                romstr += 'CM'
                num -= 900

            elif num >= 500:
                romstr += 'D'
                num -= 500

            elif num >= 400:
                romstr += 'CD'
                num -= 400

            elif num >= 100:
                romstr += 'C'
                num -= 100

            elif num >= 90:
                romstr += 'XC'
                num -= 90

            elif num >= 50:
                romstr += 'L'
                num -= 50

            elif num >= 40:
                romstr += 'XL'
                num -= 40

            elif num >= 10:
                romstr += 'X'
                num -= 10

            elif num >= 9:
                romstr += 'IX'
                num -= 9

            elif num >= 5:
                romstr += 'V'
                num -= 5

            elif num >= 4:
                romstr += 'IV'
                num -= 4
            else:
                romstr += 'I'
                num -= 1

        return romstr
            s

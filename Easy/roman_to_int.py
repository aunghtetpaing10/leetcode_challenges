class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        n = len(s)
        for i in range(0, n - 1):
            val_current = roman_map[s[i]]
            val_next = roman_map[s[i + 1]]

            if val_current >= val_next:
                total += val_current
            else:
                total -= val_current

        if n > 0:
            total += roman_map[s[n - 1]]

        return total

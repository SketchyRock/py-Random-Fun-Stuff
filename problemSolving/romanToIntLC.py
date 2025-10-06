class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
                            'I': 1,'V': 5, 'X': 10,
                            'L': 50, 'C': 100, 'D': 500,
                            'M': 1000
                        }

        n = len(s)
        total = 0

        for i in range(n):
        	value = roman_numerals[s[i]]
        	if (i + 1 < n) and (value < roman_numerals[s[i + 1]]):
        		total -= value
        	else:
        		total += value

        return total

"""initially tried a solution using two dicts checking the string
backwards and i made it over complicated.

I need to learn to accept basic facts about these problems, such as
whenever a complicated numeral appears such as IV being = 4 the I is 
always less than the procceeding number

"""
        
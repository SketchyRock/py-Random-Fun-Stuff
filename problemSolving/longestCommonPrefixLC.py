# this is the solution i had help and hints with
# I found out that min(strs, key=len) uses C to iterate through a list so it is
# much more efficient than your own for loop
# I need to stop thinking like im programming in java and go to nested
# for loops immediately
# this is not the most efficient solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        shortest_string = min(strs, key=len)
        prefix = ''

        for i in range(len(shortest_string)):
            if all(word[i] == shortest_string[i] for word in strs):
                prefix += shortest_string[i]
            else:
                break

        return prefix

""" iterates through the letters in the shortest word in the list
if any letters from the words in the list do not match whichever 
letter is currently being tested from the shortest word, then it
returns all previous letters which would be the prefix
MOST EFFICIENT

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        shortest = min(strs, key=len)

        for i, char in enumerate(shortest):
            if any(word[i] != char for word in strs):
                return shortest[:i]

        return shortest
"""









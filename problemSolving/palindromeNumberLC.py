class Solution:
    def isPalindrome(self, x: int) -> bool:
        check = str(x)

        for i in range(len(check)):
        	if not (check[i] == check[len(check) - (1 + i)]):
        		return False
        return True

"""efficient solution:

#checks if x is negative or if x ends in a 0 and is not equal to 0
#because an int cannot start and end with a 0 without being 0
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

#initialized reversed_half
#while loop is essentially taking the end of x and putting it in reversed_half
#until reversed_half becomes bigger
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

#returns whether the num is a palindrome,
#middle num is ignored if num is odd
    return x == reversed_half or x == reversed_half // 10

"""
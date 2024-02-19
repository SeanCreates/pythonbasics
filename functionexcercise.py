# function which return reverse of a string
def ispalindrome(s):
    return s == s[::-1]
# Driver code
s = "Wasitacatoradogisaw?"
ans = ispalindrome(s)
if ans:
    print("Yes")

else:
    print("No")


def ispalindrome(n):
    return n == n[::-1]

n = "sitonapotatopanotis"
ans = ispalindrome(n)

if ans:
    print("True")

else:
    print("False")






def checkPalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

myStr = [1,2,1.1]

print(checkPalindrome(myStr))
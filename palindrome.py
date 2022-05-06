name=input("Enter any name : ")
l=len(name)
print(l)
def isPalindrome(str):
    for i in range(0,round(l/2)):
        if(name[i]!=name[l-i-1]):
            return False
    return True
result=isPalindrome(name)
if result:
    print("Palindrome")
else:
    print("not a Palindrome")
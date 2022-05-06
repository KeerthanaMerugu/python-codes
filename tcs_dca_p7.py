print(ord('a'))
print(ord('z'))
print(ord('A'))
print(ord('Z'))
s='name@1234password'

print(s)
s=s.lower()
s1=s;s2=''
for i in range(len(s)):
    if(ord(s[i])>=97 and ord(s[i])<=122):
        continue
    elif((ord(s[i])>=32 and ord(s[i])<=47) or (ord(s[i])>=58 and ord(s[i])<=64) or (ord(s[i])>=91 and ord(s[i])<=96) or (ord(s[i])>=123 and ord(s[i])<=126)):
        s2=s2+s[i]
        s1=s1.replace(s[i],'')
    else:
        s1=s1.replace(s[i],'')
print(s1+s2)

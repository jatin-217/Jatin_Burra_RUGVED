def is_hill_number(num):
    s=str(num)
    i=1
    while i<len(s) and s[i]>s[i-1]:
        i +=1
    if i==1 or i==len(s):
        return False
    while i<len(s) and s[i]<s[i-1]:
        i+=1
    return i==len(s)
num=int(input("Enter a number:"))
if is_hill_number(num):
    print("Hill number")
else:
    print("Not a hill number")
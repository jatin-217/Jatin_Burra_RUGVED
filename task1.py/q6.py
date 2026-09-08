def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

s1 = input("Enter first string:")
s2 = input("Enter second string:")

if are_anagrams(s1, s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
 

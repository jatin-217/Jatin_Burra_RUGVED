s = input("Enter a string: ")
s = s.replace(" ", "").lower()
sorted_str=''.join(sorted(s))
print("Sorted string:",sorted_str)
for ch in sorted(set(sorted_str)):
    print(f"{ch}:{sorted_str.count(ch)}")
print("Total letters:",len(sorted_str))
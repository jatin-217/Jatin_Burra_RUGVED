def first_repeating(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return None 
arr=list(map(int,input("Enter array elements separated by space:").split()))
result = first_repeating(arr)
if result is not None:
    print("First repeating element is:",result)
else:
    print("No repeating element found.")

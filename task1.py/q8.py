def divide_string(s:str, n:int):
    if len(s) % n != 0:
        print("Error: String length is not divisible by",n)
        return
    parts = [s[i:i+n] for i in range(0, len(s),n)]
    if all(part == parts[0] for part in parts):
        print("Output:", ", ".join(parts))
    else:
        print("Error: Parts are not identical")
string = "abcdabcdabcdabcd"
n = int(input("Enter number of characters per part:"))
divide_string(string,n)

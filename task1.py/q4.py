def selection_sort_string(s):
    chars = list(s)
    n = len(chars)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if chars[j] < chars[min_index]:
                min_index = j
        chars[i], chars[min_index] = chars[min_index], chars[i]
    return ''.join(chars)
text = input("Enter a string: ")
sorted_text = selection_sort_string(text)
print("Sorted string:", sorted_text)

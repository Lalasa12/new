def find_maximum(arr):
    if not arr:
        return None
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element
# Example usage:
arr = [3, 5, 7, 2, 8]
print(find_maximum(arr))  # Output: 8

def quick_sort(numbers):
    if not len(numbers):
        return []
    n = numbers[0]
    half1 = [i for i in numbers if n > i]
    half2 = [i for i in numbers if n == i]
    half3 = [i for i in numbers if n < i] 
    half1 = quick_sort(half1)
    half3 = quick_sort(half3)
    result = half1 + half2 + half3
    return result

print(quick_sort([5, 2, 8, 1, 9, 3]))
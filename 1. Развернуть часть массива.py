def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def rotate(arr, k):
    n = len(arr)
    if n == 0:
        return arr
        
    k = k % n 
    
    if k == 0:
        return arr

    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    
    return arr

'''
1) Сложность составляет O(n) + O(k) + O(n-k) = O(2n), что в нотации Big O составляет O(n)
2) Не используем новых списков, для обмена используем временные переменные left и right, 
количество памяти не зависит от размера входного массива, поэтому дополнительная память составляет O(1) 
'''
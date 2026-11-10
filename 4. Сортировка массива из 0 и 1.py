def sort_binary_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == 1:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
        else:
            left += 1

    return arr

'''
Решение имеет линейную сложность, потому что указатели left и right движутся навстречу друг другу. 
На каждой итерации цикла мы либо увеличиваем left, либо уменьшаем right, поэтому цикл выполнится не более n раз. 
Каждая операция внутри цикла занимает O(1), что в сумме дает O(n).
'''
def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums

'''
Границы поддерживаются тремя указателями:[0, low-1] - нули, [low, mid-1] - единицы, [mid, high] - необработанные элементы, [high+1, n-1] - двойки.
Указатель mid двигается вперед только при встрече 0 или 1, а high сдвигается влево, когда встречается 2.
'''